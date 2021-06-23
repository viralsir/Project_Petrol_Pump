from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import tank_master
# Create your views here.
class NewTankView(CreateView):
    model = tank_master
    fields = '__all__'

#model_form.html

class ListTankView(ListView):
    model = tank_master
    context_object_name = 'tank_masters'
#model_list.html
class UpdateTankView(UpdateView):
    model = tank_master
    fields = '__all__'

class DeleteTankView(DeleteView):
    model = tank_master
    success_url = '/tank_masters/view'
#model_confirm_delete.html
class DetailTankView(DetailView):
    model = tank_master

