from django.urls import path
from . import views


urlpatterns = [
    path('contract_main_index/', views.contract_main_index, name='contract_main_index'),
    path('contract_user_index/', views.contract_user_index, name='contract_user_index'),
    path('add_new_contract/', views.add_new_contract, name='add_new_contract'),
]