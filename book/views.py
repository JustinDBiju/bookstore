from django.shortcuts import render,redirect,HttpResponse
from.models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Q


def home(request):
    results=""
    b="home"
    book= Book.objects.all()
    if request.method == 'POST':
        search =request.POST.get('search')
        b="search"
        results = Book.objects.filter(Q(name__icontains=search) )


    context = {
        'result':results,
        'book':book,
        'b':b

    }
    return render(request,'home.html',context)




    # context = {
    #     'book':book,

    # }
    # return render(request,'home.html',context)

def login(request):
    if request.method == "POST":
        mobile = request.POST.get("mobile")
        password = request.POST.get("password")
        userdata = userModel.objects.get(phonenumber=mobile)
        if password== userdata.password:
            request.session['user']=userdata.id
            return redirect('/')
        else:
            return render(request,'login.html',{'error':'username or password is incorrect'})
    return render(request,'login.html')

def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        # Check if passwords match
        if request.POST.get('password1') == request.POST.get('password2'):
            phone = request.POST.get("mobile")
            # Check if mobile number already exists
            mobile = userModel.objects.filter(phonenumber=phone)
            if mobile:
                # Mobile number already taken, render signup page with error message
                return render(request, 'signup.html', {'error': 'Mobile number is already taken'})
            else:
                # Create new user
                name = request.POST.get('name')
                mobile = request.POST.get('mobile')
                password = request.POST.get('password1')
                # Save user data
                userdata = userModel.objects.create(name=name, phonenumber=mobile, password=password)
                # Redirect to login page
                return redirect('login')  # Assuming 'login' is the name of the login URL pattern
        else:
            # Passwords don't match, render signup page with error message
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
    # Render signup page for GET requests
    return render(request, 'signup.html')
