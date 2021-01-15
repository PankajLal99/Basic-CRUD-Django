from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('view/',views.view,name="view"),
    path('delete/<int:pk>/',views.delete,name="delete"),
    path('edit/<int:pk>/',views.edit,name="edit"),
]
