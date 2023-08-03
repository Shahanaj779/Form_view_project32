from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,FormView
from django.http import HttpResponse
from app.forms import *

class TempDataRender(TemplateView):
    template_name='TempDataRender.html'

    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='Harshadh'
        return ECDO


class TempDatainsert(TemplateView):
    template_name='TempDatainsert.html'

    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        SFO=StudentForm()
        ECDO['SFO']=SFO
        return ECDO

    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
           SFD.save()
        return HttpResponse('Data inserted')

class StudentFormViewInsert(FormView):
    template_name='StudetFormViewInsert.html'
    form_class=StudentForm
    def form_valid(self,form):
        form.save()
        return HttpResponse('StudetFormViewInserted')

       


