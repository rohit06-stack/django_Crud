from django.urls import path
from . import views

urlpatterns = [
    path('', views.fees,name="Fees"),
    path('feesRecord/',views.showRecords,name='showRecords')
]