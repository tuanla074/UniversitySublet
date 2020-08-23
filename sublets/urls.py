from django.urls import path
from . import views

app_name = 'UniversitySublet'

urlpatterns = [

    path('', views.index, name="index"),
    path('<int:listing_id>/', views.details, name="details"),
    path('<int:listing_id>/subtenantInfo/', views.subtenantInfo, name="subtenantInfo"),
    path('int:listing_id/subtenantInfo/Generic_Sublet_Agreement_11th.pdf', views.pdf_view,
         name="Generic_Sublet_Agreement_11th.pdf"),

]