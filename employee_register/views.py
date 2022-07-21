from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .models import Employee
from employee_register.form import EmployeeForm
from django.contrib import messages

# Create your views here.

def employee_list(request):
    return render(request,'employee_register/employee_list.html',{
        'employee_list':Employee.objects.all().order_by('fullname'),
        'count_items':Employee.objects.count()})
    

def employee_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            employee.save()
            return redirect('/')
    else:
        form = EmployeeForm()
    return render(request,'employee_register/employee_form.html',{'form':form})


def employee_update(request,id):
    obj = get_object_or_404(Employee, id = id)
    form = EmployeeForm(request.POST or None, instance= obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'employee_register/employee_form.html',{'form':form})


def employee_delete(request,id):
    obj = get_object_or_404(Employee, id= id)
    obj.delete()
    return redirect('/')

def search_employee(request):
    search_user = request.GET.get('username')
    #print(search_user)
    if search_user:
        user = Employee.objects.filter(Q(fullname__icontains = search_user))
        messages.add_message(request, messages.INFO,f'Usuário {search_user} encontrado.')
    else:
        messages.add_message(request, messages.INFO,f'Usuário {search_user} não cadastrado.')
        user = Employee.objects.all()
    return render(request,'employee_register/employee_list.html',{'employee_list':user})
