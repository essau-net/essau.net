"""User admin classes """

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#Local
from users.models import User


admin.site.register(User, UserAdmin)