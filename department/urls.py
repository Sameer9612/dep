from django.contrib import admin
from django.urls import path
from dept.views import department_list, add_department, update_department, delete_department 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', department_list, name='department_list'),
    path('departments/add/', add_department, name='add_department'),
    path('departments/update/<int:dept_id>/', update_department, name='update_department'),
    path('departments/delete/<int:dept_id>/', delete_department, name='delete_department'),
]
