from .models import UserProfile, Group, HappinessLevel
from django.views.generic import FormView
from .forms import HappinessLevelForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from django.core.serializers.json import DjangoJSONEncoder
import json
import pandas as pd


#@method_decorator(login_required, name='login')
class RegisterSentimental(FormView):

    template_name_register = 'home.html'
    template_name_results = 'dashboard.html'
    form_class = HappinessLevelForm
    model = HappinessLevel
    success_url = reverse_lazy('dashboard')

    def get(self, request, *args, **kwargs):
        today = datetime.today().date()
        already_answered = HappinessLevel.objects.filter(user_id=request.user.id, date=today).last()
        if already_answered:
            user = UserProfile.objects.get(group_id=request.user.group_id)
            answers_query = HappinessLevel.objects.filter(user_id=request.user.id).values()
            answers_json = json.dumps(list(answers_query), cls=DjangoJSONEncoder)

            responses = {'user': user.user,
                         'group': user.group_id,
                         'answers': answers_json}
            return render(request, self.template_name_results, {'responses': responses})
        else:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name_register, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            try:
                user_profile_id = UserProfile.objects.get(user=self.request.user.id)
                today = datetime.today().date()

                if HappinessLevel.objects.filter(user_id=user_profile_id, date=today):
                    print("User already answered")

                happy = form.save(commit=False)
                happy.user_id = user_profile_id
                happy.save()

                return HttpResponseRedirect(self.success_url)

            except Exception as e:
                raise e

        return render(request, self.template_name, {'form': form})

    # @login_required(login_url='/accounts/login/')
    '''def register(request):
        #print(HappinessLevel.objects.get(user_id=request.user.id))
        form = super(HappinessLevelForm)
        print(form)
        # response = UserProfile.objects.get(user=request.user.username)
        return render(request, 'home.html', {'form': form})'''
