import random
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Contact,Products

# Create your views here.

def index(req):
    latest_reviews = Contact.objects.order_by('-message_time')[:3]
    products_list = list(Products.objects.all())
    products_list = random.sample(products_list,6)
    context={'last_reviews' :  latest_reviews,'first_review' : latest_reviews[0], 'product_list' : products_list ,}
    if req.method == 'POST':
        contact_name= req.POST['Name']
        contact_email= req.POST['Email']
        contact_number = req.POST['Phone_Number']
        contact_message= req.POST['Message']
        post=Contact(contact_name=contact_name,contact_email= contact_email, contact_number = contact_number,contact_message = contact_message)
        post.save()  
        messages.info(req,'Thank You for Message...')
        return render(req, 'index.html', context)  
    else:
        return render(req, 'index.html',context)

def about(req):
    return render(req,'about.html')

def computer(req):
    return render(req,'computer.html')

def laptop(req):
    return render(req,'laptop.html')

def product(req):
    products_list = list(Products.objects.all())
    products_list = random.sample(products_list,9)
    return render(req,'product.html',{'product_list': products_list})

def contact(req):
    return render(req,'contact.html')

def login(req):
    return render(req,'login.html')

def signUp(req):
    return render(req,'signup.html')