
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
    
    path('add_state_budget/', views.add_state_budget, name='add_state_budget'),
    path('list_state_budget/', views.list_state_budget, name='list_state_budget'),
    
    path('add_state_costed_implementation_plan/', views.add_state_costed_implementation_plan, name='add_state_costed_implementation_plan'),
    path('list_state_costed_implementation_plan/', views.list_state_costed_implementation_plan, name='list_state_costed_implementation_plan'),
    
    path('add_state_implementation_partner/', views.add_state_implementation_partner, name='add_state_implementation_partner'),
    path('list_state_implementation_partner/', views.list_state_implementation_partner, name='list_state_implementation_partner'),
    
    path('add_fp_commodity/', views.add_fp_commodity, name='add_fp_commodity'),
    path('list_fp_commodity/', views.list_fp_commodity, name='list_fp_commodity'),
    
    path('add_state_commodity_mix/', views.add_state_commodity_mix, name='add_state_commodity_mix'),
    path('list_state_commodity_mix/', views.list_state_commodity_mix, name='list_state_commodity_mix'), 
    
     path('add_contraceptive_statistics/', views.add_contraceptive_statistics, name='add_contraceptive_statistics'),
    path('list_contraceptive_statistics/', views.list_contraceptive_statistics, name='list_contraceptive_statistics'), 
    
    path('dashboard/', views.dashboard, name='dashboard'),
]

