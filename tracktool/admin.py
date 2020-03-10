from django.contrib import admin

# Register your models here.
from .models  import Bugs


@admin.register(Bugs)
class BugsAdmin(admin.ModelAdmin):
    list_display = ['name', 'issue', 'status','priority']
    list_filter = ['priority']
    list_per_page = 10
