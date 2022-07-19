from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee_list, name='employee_list'),
    path('create/',views.employee_form, name='employee_form'),
    path('delete/',views.employee_delete, name='delete'),
]