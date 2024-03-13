from django.urls import path
from . import views

urlpatterns = [
    path('', views.fees,name="Fees"),
    path('feesRecord/',views.showRecords,name='showRecords'),
    path('delete/<int:id>/', views.Feesdelete, name='Feesdelete'),
    path('edit/<int:id>', views.FeesEdit, name="FeesEdit")
]