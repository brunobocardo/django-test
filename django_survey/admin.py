from django.contrib import admin
from .models import UserProfile, Group, HappinessLevel

admin.site.register(UserProfile)
admin.site.register(Group)
admin.site.register(HappinessLevel)