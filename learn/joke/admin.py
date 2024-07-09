from django.contrib import admin
from .models import Stureg

@admin.register(Stureg)
class StuAdmin(admin.ModelAdmin):
    list_display= ('id', 'name', 'email')