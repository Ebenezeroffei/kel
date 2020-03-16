from django.shortcuts import render
from django.views import View,generic


# Create your views here.

class HomeView(View):
    template_name = 'landing/index.html'
    
    def dispatch(self,request,*args,**kwargs):
        return render(request,self.template_name)
    
