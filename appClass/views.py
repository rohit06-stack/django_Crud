from django.shortcuts import render,HttpResponse
from django.views import View
from django.views.generic import TemplateView

# Create your views here.

class MyView(View):
    def get(self,request):
        return render(request,'appclass/app.html')
        # return HttpResponse("<h1>Hi, I am class based views</h1>")
    

class ContactView(TemplateView):
    template_name = 'appclass/contact.html'