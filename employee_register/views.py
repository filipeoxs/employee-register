from django.shortcuts import redirect, render
from .models import Employee
from employee_register.form import EmployeeForm

# Create your views here.
def employee_list(request):
    return render(request,'employee_register/employee_list.html',{'employee_list':Employee.objects.all()})

def employee_form(request,id=0):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            employee.save()
            return redirect('/')
    else:
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk = id)
            form = EmployeeForm(instance=employee)
    return render(request,'employee_register/employee_form.html',{'form':form})

def employee_delete(request):
    return render(request,'employee_register/employee_delete.html')