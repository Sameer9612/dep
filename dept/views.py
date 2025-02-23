from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Department
from .forms import DepartmentForm

def is_admin(user):
    return user.is_authenticated and user.is_superuser

@user_passes_test(is_admin)
def department_list(request):
    departments = Department.objects.all()  # Fetch data from the database
    return render(request, 'department_list.html', {'departments': departments})

@user_passes_test(is_admin)
def add_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'add_department.html', {'form': form})

@user_passes_test(is_admin)
def update_department(request, dept_id):  # Updated parameter
    department = get_object_or_404(Department, dept_id=dept_id)  # Fetch by dept_id
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'update_department.html', {'form': form})

@user_passes_test(is_admin)
def delete_department(request, dept_id):  # Updated parameter
    department = get_object_or_404(Department, dept_id=dept_id)  # Fetch by dept_id
    department.delete()
    return redirect('department_list')



def department_list(request):
    departments = Department.objects.all()  # Fetch data from the database
    return render(request, 'department_list.html', {'departments': departments})
