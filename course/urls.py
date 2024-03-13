from django.urls import path
from . import views

urlpatterns = [
    path('', views.course,name="course"),
    path('create/',views.create,name='create'),
    path('read/',views.read, name='read'),
    path('update/<int:id>/', views.edit, name="update"),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('about/',views.about,name='about'),
    path('login/',views.login,name='login'),
    # path('dtl/',views.dtl,name='dtl')
]