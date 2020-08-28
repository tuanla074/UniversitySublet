from django.urls import path
from . import views

app_name = 'UniversitySublet'

urlpatterns = [

    path('', views.index, name="index"),
    path('<int:listing_id>/', views.details, name="details"),
    path('<int:listing_id>/subtenantInfo/', views.subtenantInfo, name="subtenantInfo"),
    path('<int:listing_id>/subtenantInfo/legalFee', views.legalFee, name="legalFee"),
    path('<int:listing_id>/subtenantInfo/Generic_Sublet_Agreement_11th.pdf', views.pdf_view,
         name="Generic_Sublet_Agreement_11th.pdf"),
    path('<int:listing_id>/contract/', views.contract, name="contract"),
    path('<int:listing_id>/charge/', views.charge, name="charge"),
    path('success/<int:args>/', views.successMsg, name="success"),
    path('About/', views.About, name="About"),
    path('FAQ/', views.FAQ, name="FAQ"),


]
