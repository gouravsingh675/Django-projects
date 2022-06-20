from django.contrib import messages 
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['user_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'user name already taken')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')
    else:  
        return render(request,'register.html')