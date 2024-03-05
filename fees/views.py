from django.shortcuts import render,redirect
from .models import Fees

# Create your views here.
def fees(request):
    if request.method =="POST":
        name = request.POST['nm']
        course = request.POST['course']
        duration = request.POST['duration']
        fees = request.POST['fees']
        # print('Name :',name)
        # print('course :',course)
        # print('duration :',duration)
        # print('fees :',fees)
        data = Fees(name=name,course=course,duration=duration,fees=fees)
        data.save()
        return redirect('feesRecord/') 
    else:
        pass
    return render(request,'fees/index.html')

def showRecords(request):
    records =Fees.objects.all()
    context = {
        'records': records
    }
    return render(request,'fees/feesRecord.html',context)