import smtplib
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth
from validate_email import validate_email
from email.message import EmailMessage


# Create your views here.
def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(req,user)
            return redirect('/')
        else:
            messages.info(req,'Invalid Credentials!...')
            return redirect('/login')
    else:
        return render(req,'login.html')

def register(req):

    if req.method == 'POST' :
        if req.POST['first_name'] and req.POST['last_name'] and req.POST['username'] and req.POST['email'] and req.POST['password'] and req.POST['confirm_password']:
            first_name = req.POST['first_name']
            last_name = req.POST['last_name']
            username = req.POST['username']
            email = req.POST['email']
            password = req.POST['password']
            confirm_password = req.POST['confirm_password']
            # print(first_name,last_name,username,email,password,confirm_password)
            
            if User.objects.filter(username = username).exists():
                messages.info(req,'User Name had already taken!. Please try another one...')
            elif User.objects.filter(email = email).exists():
                messages.info(req,'Email has already taken!, Please try another one...')
            elif password != confirm_password:
                messages.info(req,'Please conform Password correctly. Both Passwords are not same! ...')
            else:
                valid_email = validate_email(email_address = email,check_smtp = True)
                user = User.objects.create_user(first_name = first_name,last_name = last_name, username = username , email = email, password = password)
                user.save()
                return redirect('/login')
            return redirect('/accounts/register')
        else:
            messages.info(req,'Please fill all forms...')
    return render(req,'register.html')

def logout(req):
    auth.logout(req)
    return redirect('/')

def subscribe(req):
    if User.is_authenticated:
        # send_email()
        sender = 'mfpvcode@gmail.com'
        password = 'frmnhzjocwibfyik'
        reciever = ['fayispvchelari@gmail.com','finutyping@gmail.com']
        msg = EmailMessage()
        msg['Subject']= 'Hope you are fine'
        msg['From'] = sender
        msg['To'] = reciever
        msg.set_content = 'How are You, There are many days between us'
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)

        server.login(sender,password) 
        server.send_message(msg)
        print('email send')
    else:
        redirect('/login')
    return redirect('/') 

def send_email():
    # sender = 'mfpvcode@gmail.com'
    # password = 'frmnhzjocwibfyik'
    # # reciever = 'fayispvchelari@gmail.com'
    # smtp = smtplib.SMTP('smtp.gmail.com',587)
    # smtp.starttls()
    # smtp.login(sender,password) 
    # smtp.sendmail(sender,['fayispvchelari@gmail.com','finutyping@gmail.com'],'Thanks',)
    # print('email send')
    pass  