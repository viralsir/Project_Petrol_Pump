from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import employee
# Create your views here.
class NewemployeeView(CreateView):
    model = employee
    fields = '__all__'

#model_form.html

class ListemployeeView(ListView):
    model = employee
    context_object_name = 'employees'
#model_list.html
class UpdateemployeeView(UpdateView):
    model = employee
    fields = '__all__'

class DeleteemployeeView(DeleteView):
    model = employee
    success_url = '/employee/view'
    template_name = "employee/employee_confirm_delete.html"
#model_confirm_delete.html
class DetailemployeeView(DetailView):
    model = employee

