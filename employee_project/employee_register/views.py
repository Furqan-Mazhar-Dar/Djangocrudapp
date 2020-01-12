from django.shortcuts import render,redirect
from .forms import employeeform
from .models import employee

# Create your views here.
def employee_list(request):
    return render(request,"employee_register/employee_list.html")

def employee_form(request):
    if request.method == "GET":
        if id == 0:
            form = employeeform()
        else:
            employee = employee.objects.get(pk=id)
            form = employeeform(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = employeeform(request.POST)
        else:
            employee = employee.objects.get(pk=id)
            form = employeeform(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employee_delete(request):
    employee = employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')