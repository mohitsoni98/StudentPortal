from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html',{'title':"Dashboard | Student Portal"})

def login(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        if(User.objects.filter(username=username).exists()):
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                print("User Authenticated!")
                return redirect("/")
            else:
                messages.info(request,"Invalid Password!")
        else:
            messages.info(request,"Username does\'nt exist!")
    return render(request,'login.html',{"title":"Login | Student Portal"})
    
def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method=='POST':
        isValid=True
        data = request.POST
        msgs=[]
        fname = data['fname']
        lname = data['lname']
        email = data['email']
        contact = data['contact']
        password1 = data['password1']
        password2 = data['password2']
        username = data['username']
        if(User.objects.filter(username=username).exists()):
            msgs+=["Username Exists"]
            isValid=False
        if (User.objects.filter(email=email).exists()):
            msgs+=["Email Exist"]
            isValid=False
        # if(User.objects.filter(contact=contact).exists()):
        #     messages.info(request,"Contact Exist")
        #     isValid=False
        if password1!=password2:
            msgs+=["Password Mismatched!"]
            isValid=False
        if isValid:
            user = User.objects.create_user(username=username,email=email,password=password1,first_name=fname,last_name=lname)
            user.save()
            msgs+=["Successfully Registered"]
            return JsonResponse({"response":"SUCCESS","messages":msgs},status=200)
        else:
            return JsonResponse({"response":"FALIURE","messages":msgs},status=200)
    return render(request,'register.html',{"title":"Register | Student Portal"})

def logout(request):
    auth.logout(request)
    return redirect("/")
def exists(request):
    if request.method=="POST":
        data = request.POST
        print(data)
    return redirect("/")