import email
from email.headerregistry import Address
from tokenize import Name
from django.shortcuts import redirect, render,HttpResponse
from datetime import datetime 
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable":"LOL"
    }
    return render(request,'index.html',context)

def about(request):
   return render(request,'about.html')    

def dropdown(request):
   return render(request,'drop.html')  

def contact(request):
   if request.method == "POST":
      Name=request.POST.get('Name')
      Email=request.POST.get('Email')
      PhoneNo=request.POST.get('PhoneNo')
      City=request.POST.get('City')
      Address=request.POST.get('Address')
      Zip=request.POST.get('Zip')
     # ch=request.POST.get('ch')
      contact= Contact(Name=Name, Email=Email,PhoneNo=PhoneNo,City=City,Address=Address,Zip=Zip,date=datetime.today())
      contact.save()
      messages.success(request, 'Profile details sent!')
   


   return render(request,'contact.html')

def view(request):
   students = Contact.objects.all()
   return render(request,"view.html",{'students':students})   

def delete(request,id):
   students = Contact.objects.get(id=id)
   students.delete()
   return redirect("/view") 

def edit(request,id):
  students = Contact.objects.get(id=id)
#   if request.method == 'POST':
#       pi= Contact.objects.get(pk=id)
#       fm= Contact(request.POST, instance =pi)
#       if fm.is_valid():
#          fm.save()
#       else:
#             pi= Contact.objects.get(pk=id)
#             fm= Contact(request.POST, instance =pi)
  return render(request,'edit.html',{'students':students})     