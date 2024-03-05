from django.shortcuts import render,HttpResponse

# Create your views here.
def setsession(request):
    request.session['name']= 'Ajay Kumar'
    return HttpResponse('<h1>Session set</h1>')

def getsession(request):
    item = request.session['name']
    context ={
        'name':item
    }
    return render(request,'getsession.html',context)

def deletesession(request):
    request.session.flush()
    return HttpResponse('<h1> Session deleted </h1>')