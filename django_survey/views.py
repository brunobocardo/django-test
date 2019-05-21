from .models import UserProfile, Group, HappinessLevel
from django.views.generic import FormView
from .forms import HappinessLevelForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic.base import TemplateView
from django.core.exceptions import ObjectDoesNotExist
import json
import pandas as pd


class ResultSentimental(FormView):
    template_name_results = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        users_query = UserProfile.objects.filter(user=request.user.id).values()
        users_json = json.dumps(list(users_query), cls=DjangoJSONEncoder)
        group_id = json.loads(users_json)[0]['group_id_id']
        users_group_query = UserProfile.objects.filter(group_id=group_id).values()
        users_ids = [uid['user_id'] for uid in users_group_query]
        answers_query = HappinessLevel.objects.filter(user_id__in=users_ids).values()
        answers_json = json.dumps(list(answers_query), cls=DjangoJSONEncoder)

        df = pd.read_json(answers_json)
        df_stats = (df.groupby(['level'], as_index=False).agg('count')).to_dict('response')
        happiness_level_dict = {1: 'Unhappy', 2: 'Not Happy', 3: 'Neutral', 4: 'Happy', 5: 'Very Happy'}

        happiness_avg = happiness_level_dict[round(df['level'].mean(), 0)]

        stats = []
        for stts in df_stats:
            dict_stats = {'happiness_level': happiness_level_dict[stts['level']],
                          'count_people': stts['user_id_id']}
            stats.append(dict_stats)

        responses = {'answers': stats,
                     'happiness_avg': happiness_avg,
                     'report': True}
        return render(request, self.template_name_results, responses)


class RegisterSentimental(FormView):

    template_name_register = 'register_sentimental.html'
    template_name_results = 'dashboard.html'
    form_class = HappinessLevelForm
    model = HappinessLevel
    success_url = reverse_lazy('dashboard')

    def get(self, request, *args, **kwargs):
        today = datetime.today().date()
        already_answered = HappinessLevel.objects.filter(user_id=request.user.id, date=today).last()
        if already_answered:
            return HttpResponseRedirect(self.success_url)
        else:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name_register, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            try:
                happy = form.save(commit=False)
                happy.user_id = UserProfile.objects.get(user=request.user.id)
                happy.save()
                return HttpResponseRedirect(self.success_url)
            except ObjectDoesNotExist:
                if self.request.user.is_superuser:
                    html_error = """
                            This user is not registered to submit the happiness level. <br />
                            You need to be registered in UserProfile using
                            Django Admin to be able to submit your happiness level. <br /><br />
                            You can register the user using the link: <a href='/admin'>Admin Page</a>
                    """
                else:
                    html_error = """
                            Your user is not registered to submit the happiness level. <br />
                            Request access to submit your happiness level.
                    """
                return HttpResponse(html_error)

            except Exception as e:
                raise e
