from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import creditor_master
# Create your views here.
class NewCreditorView(CreateView):
    model = creditor_master
    fields = '__all__'

#model_form.html

class ListCreditorView(ListView):
    model = creditor_master
    context_object_name = 'creditors'
#model_list.html
class UpdateCreditorView(UpdateView):
    model = creditor_master
    fields = '__all__'

class DeleteCreditorView(DeleteView):
    model = creditor_master
    success_url = '/vehicle/view'

#model_confirm_delete.html
class DetailCreditorView(DetailView):
    model = creditor_master