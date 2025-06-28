from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('multirotor/', views.Page_two, name='multirotor'),
    path('fixed-wing/', views.Page_three, name='fixed-wing'),
    path('helicopter/', views.Page_four, name='helicopter'),
]
