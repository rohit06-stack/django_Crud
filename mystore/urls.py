from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('',include('course.urls')),
    path('fees/',include('fees.urls')),
    path('appsession/',include('appsession.urls')),
    path('appclass/',include('appClass.urls'))
]
