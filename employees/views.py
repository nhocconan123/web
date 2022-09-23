from django.shortcuts import render
from .models import employees as employees_model
from home.models import department as department_model
# Create your views here.
def get_employees(request,id):
    employee_list=employees_model.objects.filter(department_id = id) #select * from employee where department_id=gia tri cua id
    department=department_model.objects.get(department_id = id)
    return render(request,'employees.html',{'employee_list':employee_list,'department':department})
   