
from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    #anc register urls
    path('anc_register_create/', views.anc_register_create, name='anc_register_create'),
    path('anc_register_list/', views.anc_register_list, name='anc_register_list'),
    path('anc_register/<int:id>/', views.anc_register_view, name='anc_register_view'),
   
    #labour register urls
    path('labour_register_create/', views.labour_register_create, name='labour_register_create'),
    path('labour_register_list/', views.labour_register_list, name='labour_register_list'),
    path('labour_delivery/<int:id>/', views.labour_register_view, name='labour_delivery_view'),
    
    path('child_immunization_create/', views.child_immunization_create, name='child_immunization_create'),
    path('child_immunization_list/', views.child_immunization_list, name='child_immunization_list'),
    path('child_immunization/<int:id>/', views.child_immunization_view, name='child_immunization_view'),
    
    path('child_immunization_tally_list/', views.child_immunization_tally_list, name='child_immunization_tally_list'),
     path('child_immunization_tally_create/', views.child_immunization_tally_create, name='child_immunization_tally_create'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
]

