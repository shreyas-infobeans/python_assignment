from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Employee
from .forms import EmployeeForm
from django.views.generic import ListView
from .models import Contract
# Create your views here.

def index(request):
    emp1 = Employee.objects.all()
    context = {"emp1":emp1}
    return render(request,'index.html',context=context )

def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index1.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})
def edit(request, id):  
    employee = Employee.objects.get(id=id) 
    form = EmployeeForm(instance=employee)   
    return render(request,'edit.html', {'form': form,'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    print(form)
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'form': form,'employee': employee})
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")

class ContractListView(ListView):
    model = Contract
    template_name = 'contracts/contract_list.html'  # Specify your template
    context_object_name = 'contracts'  # Default is 'object_list', this renames it
# views.py
from django.views.generic import ListView
from .models import Contract

class ContractListView(ListView):
    model = Contract
    template_name = 'contract_list.html'  # Specify your template
    context_object_name = 'contracts'  # Default is 'object_list', this renames it