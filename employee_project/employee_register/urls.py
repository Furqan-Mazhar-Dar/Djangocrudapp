from django.urls import path,include
from . import views

urlpatterns = [
    path('employee',views.employee_form),
    path('list/',views.employee_list),
]