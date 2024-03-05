from django.shortcuts import render

def home(request):
    # name = "Rohit Bajpayee"
    # city = "Delhi"
    # email = "rohit@gmail.com"
    # context = {
    #     'name': name,
    #     'city' : city,
    #     'email' : email
    # }
    return render(request,'index.html')


