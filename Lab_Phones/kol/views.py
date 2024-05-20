from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from kol.models import Phone, Manufacturer
from kol.forms import PhoneForm


def phones(request):
    phones = Phone.objects.all()

    return render(request, "phones.html", {"phones": phones})

def phone_detail(request, phone_id):
    try:
        phone = Phone.objects.get(pk=phone_id)
    except Phone.DoesNotExist:
        raise Http404("Phone does not exist")
    return render(request,"phone_detail.html", {"phone": phone})

def add_phone(request):
    if request.method == "POST":
        phone=PhoneForm(request.POST, request.FILES)
        if phone.is_valid():
            phone.save()
            return redirect("phones")
    else:
        phone=PhoneForm()
    return render(request,"add_phone.html",{'form':phone})





# Create your views here.
