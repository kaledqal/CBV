from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from basic_app.models import School,Student
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                  ListView,DetailView,
                                  UpdateView,DeleteView,
                                  CreateView)

# Create your views here.
class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'BASIC INJECTION'
        return context


class SchoolList(ListView):
    """Logic responsible for returning a list of books in the library """
    model = School
    school_list = School.objects.all()

class SchoolDetailView(DetailView):
    model = School


class CreateSchoolView(CreateView):
    model = School
    fields = '__all__'

class SchoolUpdateView(UpdateView):
    
    model = School
    fields = ('principal','name')
