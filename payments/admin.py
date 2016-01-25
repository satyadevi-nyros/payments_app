from django.contrib import admin

# Register your models here.
from .models import mobile_details
from django.contrib.auth.models import User


admin.site.register(mobile_details)
