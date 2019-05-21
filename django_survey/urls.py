from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('results/', login_required(views.ResultSentimental.as_view()), name='dashboard'),
    path('', login_required(views.RegisterSentimental.as_view()), name='register-sentimental')
]
