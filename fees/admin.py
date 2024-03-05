from django.contrib import admin
from .models import Fees

# Register your models here.
# class FeesAdmin(admin.ModelAdmin):
    # list_display = ('id','name','course','duration','fees')

admin.site.register(Fees)