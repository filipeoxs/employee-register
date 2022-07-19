from django.http import HttpResponse
from django.shortcuts import render

from employee_register.form import EmployeeForm

# Create your views here.
def employee_list(request):
    return render(request,'employee_register/employee_list.html')

def employee_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            employee.save()
    else:
        form = EmployeeForm()
    return render(request,'employee_register/employee_form.html',{'form':form})

def employee_delete(request):
    return render(request,'employee_register/employee_delete.html')