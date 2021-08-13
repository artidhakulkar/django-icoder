from django.shortcuts import render
from.models import Contact

# Create your views here.

def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    if request.method == "POST":
        email = request.POST.get("email", ""),
        name = request.POST.get("name", ""),
        phone = request.POST.get("phone", ""),
        address = request.POST.get("address", "")
        # print(email, name, phone, address)
        contact = Contact(email=email, name=name, phone=phone, address=address)
        contact.save()
    return render(request, "home/contact.html")