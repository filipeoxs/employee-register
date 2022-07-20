from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee_list, name='employee_list'), #List
    path('create/',views.employee_form, name='employee_form'), #Create
    path('<int:id>/',views.employee_update, name='employee_edit'), #Update
    path('delete/<int:id>/',views.employee_delete, name='employee_delete'), #Delete
]