from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import nozzel_master
# Create your views here.
class NewNozzelView(CreateView):
    model = nozzel_master
    fields = '__all__'
#model_form.html

class ListNozzelView(ListView):
    model = nozzel_master
    context_object_name = 'nozzel'
    template_name = 'nozzel/nozzel_master_list.html'
#model_list.html
class UpdateNozzelView(UpdateView):
    model = nozzel_master
    fields = '__all__'

class DeleteNozzelView(DeleteView):
    model = nozzel_master
    success_url = '/nozzel/view'

#model_confirm_delete.html
class DetailNozzelView(DetailView):
    model = nozzel_master

