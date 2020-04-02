from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.views import View
from django.http import HttpResponseRedirect
from .models import Location
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import NewUser,ClientLocation

# Create your views here.

class NewUserView(View):
    template_name = 'user/signup.html'
    form_class = NewUser
    form_class2 = ClientLocation
    
    def get(self,request,*args,**kwargs):
        form = self.form_class()
        loc = self.form_class2()
        context = {
            'form':form,
            'loc':loc,
        }
        return render(request,self.template_name,context)
    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        loc = self.form_class2(request.POST)
        context = {
            'form':form,
            'loc':loc,
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if loc.is_valid():
                location = Location(client = user,**loc.cleaned_data)
                location.save()
            messages.success(request,f'You have been successfully registered, you can now sign in.')
            return HttpResponseRedirect(reverse('user:signin'))
        return render(request,self.template_name,context)

    
class UserProfileView(View):
    """ This class displays the profile of the user """
    template_name = 'user/user_profile.html'
    
    @method_decorator(login_required)
    def dispatch(self,request,*args,**kwargs):
        return render(request,self.template_name)