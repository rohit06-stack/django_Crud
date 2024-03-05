from django.shortcuts import render,redirect,HttpResponse
from . models import Signup
from . forms import StudentForm
# Create your views here.
def course(request):
  res = HttpResponse("<h1>Cookie Set</h1>")
  res.set_cookie("name","pooja",max_age=None)
  val = request.COOKIES.get('name')
  context ={
     'cookie': val
  }
  if res:
   return res
   # return render(request,'index.html',context)
  else:
   print("cookies not set")
   return render(request,'index.html')



def create(request):
   if request.method =='POST':
      fm = StudentForm(request.POST)
      if fm.is_valid():
         fm.save()
         return redirect('login')
   else:
      fm = StudentForm()
   return render(request,'signup.html',{'signupForm':fm})

def read(request):
   data = Signup.objects.all()
   return render(request,'allData.html',{'records':data})

def edit(request,id):
   dataget = Signup.objects.get(id=id)
   fm = StudentForm(instance=dataget)
   if request.method == 'POST':
      fm = StudentForm(request.POST,instance=dataget)
      if fm.is_valid():
         fm.save()
         return redirect('create')
   return render(request,'edit.html',{'editForm':fm})


def delete(request,id):
   dataget = Signup.objects.get(id=id)
   dataget.delete()
   return redirect('read')

def about(request):
   return render(request,"about.html")

def login(request):
   if request.method == 'POST':
      email= request.POST['email']
      password = request.POST['password']
      userobj = Signup.objects.filter(email=email)
      print(userobj)

      if userobj:
         password = Signup.objects.filter(password=password)
         if password:
            return HttpResponse("dashboard")
         else:
            return redirect('login')
      else:
         return redirect('login')
      
   else:
      pass
   return render(request, 'login.html')

def dtl(request):
   name = "Rohit vajpayee"
   city = "Delhi"
   email = "rohitvajpayee2001@gmail.com"
   message = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
   context ={
      'name': name,
      'message': message,
      'email': email,
      'city' : city
   }
   return render(request,'course/dtl.html',context)
