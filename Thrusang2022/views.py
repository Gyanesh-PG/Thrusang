from django.shortcuts import render,redirect
from .models import profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from instamojo_wrapper import Instamojo
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# api = Instamojo(api_key='test_a0ea97bffacc77a18394a713038',auth_token='test_57850829a42be8360521ac63509',endpoint='https://test.instamojo.com/api/1.1/')
api = Instamojo(api_key='8a970ccd0f7c91c021f14e5e6cf00bf8',auth_token='79a868b1a57640a7abe4a4f4d74d7d36')
def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')
def events(request):
    return render(request,'events.html')
def gallery(request):
    return render(request,'gallery.html')
def sponsers(request):
    return render(request,'sponsers.html')
def team(request):
    return render(request,'team.html')
def contact(request):
    return render(request,'contact.html')
def user_profile(request):
    return render(request, 'profile.html')
def register(request):
    return render(request,'signup.html')
def register_user(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        id_no = str(request.POST.get('idno'))
        college = request.POST.get('college')
        college_name = ''
        branch = request.POST.get('branch')
        year_of_study = request.POST.get('year_of_study')
        gender = request.POST.get('gender')
        phn_no = request.POST.get('phno')
        email = request.POST.get('email')
        passw = request.POST.get('psw')
        passw2 = request.POST.get('cpsw')
        coll = None
        if college == "Other":
            coll = request.POST.get('college_name')
        else:
            coll = college

        if passw != passw2:
            messages.info(request, 'Password and Confirm Password does not match.')
            return render(request, 'signup.html')
        if User.objects.filter(username=email).exists():
            messages.info(request, "Email already exists")
            return render(request, 'signup.html')
        elif profile.objects.filter(id_no=id_no).exists():
            messages.info(request, "ID number already exists")
            return render(request, 'signup.html')

        user = User.objects.create_user(username=email, first_name=name, email=email, password=passw)
        prof = profile(id_no=id_no, college_name=coll, branch=branch, year_of_study=year_of_study,gender=gender, mobile=phn_no,payment='No',pay_id='', user=user)
        prof.save()
        messages.error(request, 'Account created successfully.', extra_tags='signup')
        return render(request, 'login.html')
    else:
        return render(request, 'signup.html')
def log(request):
    return render(request,'login.html')
def login_user(request):
    if request.method == 'POST':
        uname = request.POST.get('email')
        passw = request.POST.get('psw')
        user = authenticate(username=uname, password=passw)
        if user is not None:
            login(request, user)
            return render(request,'index.html')
        else:
            messages.error(request, 'username or password wrong.', extra_tags='login')
            return render(request, 'login.html')

def pay_initiate(request):
    if request.user.is_authenticated and request.user.profile.payment=="No":

        response = api.payment_request_create(buyer_name=request.user.first_name,email=request.user.email,phone=request.user.profile.mobile,amount='10', purpose='Test', send_email=False,redirect_url="http://127.0.0.1:8000/success")
        pro = profile.objects.get(id_no=request.user.profile.id_no)
        pro.pay_id=response['payment_request']['id']
        pro.save()
        return redirect(response['payment_request']['longurl'])
    else:
        return render(request, 'index.html')

def success(request):
            pay_id= request.GET.get('payment_request_id')
            response = api.payment_request_status(pay_id)
            if response['payment_request']['status'] =="Completed":
                pro=profile.objects.get(pay_id=pay_id)
                pro.payment = "Yes"
                pro.save()
                messages.error(request, 'Payment Successfully Completed.', extra_tags='paid')
                return render(request, 'profile.html')
            messages.error(request, 'Payment Failed.', extra_tags='fail')
            return  render(request,'profile.html')
def logout_user(request):
    logout(request)
    return render(request, 'index.html')




