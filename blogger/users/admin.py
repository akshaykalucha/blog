from django.contrib import admin

# Register your models here.
from . models import UserProfileInfo, Profile
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Profile)