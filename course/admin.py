from django.contrib import admin
from .models import Courses,Signup
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','courseName','courseFee','courseDuration')

    
class SignupAdmin(admin.ModelAdmin):
    list_display = ('id','firstName','lastName','email')

admin.site.register(Signup,SignupAdmin)
admin.site.register(Courses,CourseAdmin)