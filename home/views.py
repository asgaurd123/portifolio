from django.shortcuts import render
from .models import Client

# Create your views here.
def index(request):
   return render(request,'index.html')
def contact(request):
   if request.method=="POST":
      email=request.POST.get('email')
      name=request.POST.get('name')
      phone=request.POST.get('phone')
      client=Client(name=name,email=email, phone=phone)
      client.save()

   return render(request,'contact.html')
def about(request):
   return render(request,'about.html')