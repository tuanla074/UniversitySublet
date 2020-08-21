from django.urls import path
from . import views

app_name = 'UniversitySublet'

urlpatterns = [

    path('', views.index, name="index"),
    path('<int:listing_id>/', views.details, name="details"),
]