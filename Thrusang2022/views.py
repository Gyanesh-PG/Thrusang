from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import profile, workshop,iplcount,thrusangtank,transactions
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from instamojo_wrapper import Instamojo
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
import datetime
def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def events(request):
    iplcc = iplcount.objects.all()
    ipl_count = iplcc.count()
    return render(request, 'events.html')


def gallery(request):
    return render(request, 'gallery.html')


def sponsers(request):
    return render(request, 'sponsers.html')


def team(request):
    return render(request, 'team.html')


def contact(request):
    return render(request, 'contact.html')

def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return render(request, 'login.html')


def register(request):
    return render(request, 'signup.html')


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
        iplcc = iplcount.objects.all()
        ipl_count = iplcc.count()
        dat = str(datetime.datetime.now())
        prof = profile(id_no=id_no, college_name=coll, branch=branch, year_of_study=year_of_study,
                       gender=gender, mobile=phn_no, payment='No', pay_id='', tt='No', sl='No', sb="No", tet="No"
                       , tc="No",deb="No", ipl="No", quiz="No", mp="No", ld="No", wb="No", sg="No", rd="No",th_id="0"
                       ,evpay="No",reg_time=dat,ipcount=ipl_count, evpay_id='', bgmi="No",ttpay="No", ttpay_id='',iplpay="No", iplpay_id='',cg="No",saw="No",evcount=0, user=user)
        work = workshop(name='', payment='No', pay_id='', tg='x', user=user)
        work.save()
        prof.save()
        messages.error(request, 'Account created successfully.', extra_tags='signup')
        return render(request, 'login.html')
    else:
        return render(request, 'signup.html')


def log(request):
    return render(request, 'login.html')


def login_user(request):
    if request.method == 'POST':
        uname = request.POST.get('email')
        passw = request.POST.get('psw')
        user = authenticate(username=uname, password=passw)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            messages.error(request, 'username or password wrong.', extra_tags='login')
            return render(request, 'login.html')


def pay_initiate(request):
    if request.user.is_authenticated :
        return render(request,'payment300.html')
    else:
        return render(request, 'login.html')

@csrf_exempt
def success(request):
    # only accept POST request.
    if request.method == "POST":
        trans_id=request.POST.get('trans')
        if transactions.objects.filter(tans_id=trans_id).exists():
            messages.error(request, "The transaction ID you have enetered is already used.", extra_tags='trans')
            return render(request,'payment300.html')
        dat = str(datetime.datetime.now())
        tra=transactions(tans_id=trans_id,email=request.user.username,trans_time=dat,reason="Events")
        tra.save()
        pro=profile.objects.get(id_no=request.user.profile.id_no)
        pro.pay_id = trans_id
        pro.evpay_id = trans_id
        pro.evpay = "Yes"
        pro.payment = "Yes"
        if request.user.profile.th_id == "0":
            c = 0
            s = "TRG-WEB-0000"
            pr = profile.objects.all();
            for k in pr:
                if k.th_id != "0":
                    c += 1
            if c < 9:
                ss=s[0:11]+str(c+1)
                pro.th_id=ss
            elif c>=9 and c<=98:
                ss = s[0:10] + str(c+1)
                pro.th_id = ss
            elif c>=99 and c<=999:
                ss = s[0:9] + str(c+1)
                pro.th_id = ss
            else:
                ss = s[0:8] + str(c+1)
                pro.th_id = ss
        pro.save()
        messages.error(request, 'Payment Successfully Completed.Now you can register to the events.', extra_tags='paid')
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return render(request, 'index.html')


def cws(request):
    if request.user.is_authenticated:

        return render(request, 'cyberpay.html')
    else:
        return render(request, 'login.html')

@csrf_exempt
def cwssuccess(request):
    if request.method == "POST":
        trans_id=request.POST.get('trans')
        if transactions.objects.filter(tans_id=trans_id).exists():
            messages.error(request, "The transaction ID you have enetered is already used.", extra_tags='trans')
            return render(request,'cyberpay.html')
        dat = str(datetime.datetime.now())
        tra=transactions(tans_id=trans_id,email=request.user.username,trans_time=dat,reason="Cyber")
        tra.save()
        pro=profile.objects.get(id_no=request.user.profile.id_no)
        ws = workshop.objects.get(user=request.user)
        pro.payment = "Yes"
        pro.evpay = "Yes"
        pro.pay_id = trans_id
        pro.evcount += 1
        ws.payment = "Yes"
        ws.tg = "cs"
        ws.pay_id=trans_id
        if request.user.profile.th_id == "0":
            c = 0
            s = "TRG-WEB-0000"
            pr = profile.objects.all();
            for k in pr:
                if k.th_id != "0":
                    c += 1
            if c < 9:
                ss = s[0:11] + str(c + 1)
                pro.th_id = ss
            elif c >= 9 and c <= 98:
                ss = s[0:10] + str(c + 1)
                pro.th_id = ss
            elif c >= 99 and c <= 999:
                ss = s[0:9] + str(c + 1)
                pro.th_id = ss
            else:
                ss = s[0:8] + str(c + 1)
                pro.th_id = ss
        ws.save()
        pro.save()
        messages.error(request, 'Payment Successfully Completed.Yor have registered for Cyber Security Workshop', extra_tags='paid')
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')


def iot(request):
    if request.user.is_authenticated:
        return render(request, 'iotpay.html')
    else:
        return render(request, 'login.html')

@csrf_exempt
def iotsuccess(request):
    if request.method == "POST":
        trans_id=request.POST.get('trans')
        if transactions.objects.filter(tans_id=trans_id).exists():
            messages.error(request, "The transaction ID you have enetered is already used.", extra_tags='trans')
            return render(request,'iotpay.html')
        dat = str(datetime.datetime.now())
        tra=transactions(tans_id=trans_id,email=request.user.username,trans_time=dat,reason="IOT")
        tra.save()
        pro=profile.objects.get(id_no=request.user.profile.id_no)
        ws = workshop.objects.get(user=request.user)
        pro.payment = "Yes"
        pro.evpay = "Yes"
        pro.pay_id = trans_id
        pro.evcount += 1
        ws.payment = "Yes"
        ws.tg = "iot"
        ws.pay_id=trans_id
        if request.user.profile.th_id == "0":
            c = 0
            s = "TRG-WEB-0000"
            pr = profile.objects.all();
            for k in pr:
                if k.th_id != "0":
                    c += 1
            if c < 9:
                ss = s[0:11] + str(c + 1)
                pro.th_id = ss
            elif c >= 9 and c <= 98:
                ss = s[0:10] + str(c + 1)
                pro.th_id = ss
            elif c >= 99 and c <= 999:
                ss = s[0:9] + str(c + 1)
                pro.th_id = ss
            else:
                ss = s[0:8] + str(c + 1)
                pro.th_id = ss
        ws.save()
        pro.save()
        messages.error(request, 'Payment Successfully Completed.Yor have registered for IOT Workshop', extra_tags='paid')
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')


def afs(request):
    if request.user.is_authenticated:
        return render(request, 'afspay.html')
    else:
        return render(request, 'login.html')

@csrf_exempt
def afssuccess(request):
    if request.method == "POST":
        trans_id=request.POST.get('trans')
        if transactions.objects.filter(tans_id=trans_id).exists():
            messages.error(request, "The transaction ID you have enetered is already used.", extra_tags='trans')
            return render(request,'afspay.html')
        dat = str(datetime.datetime.now())
        tra=transactions(tans_id=trans_id,email=request.user.username,trans_time=dat,reason="AFS")
        tra.save()
        pro=profile.objects.get(id_no=request.user.profile.id_no)
        ws = workshop.objects.get(user=request.user)
        pro.payment = "Yes"
        pro.evpay = "Yes"
        pro.pay_id = trans_id
        pro.evcount += 1
        ws.payment = "Yes"
        ws.tg = "afs"
        ws.pay_id=trans_id
        if request.user.profile.th_id == "0":
            c = 0
            s = "TRG-WEB-0000"
            pr = profile.objects.all();
            for k in pr:
                if k.th_id != "0":
                    c += 1
            if c < 9:
                ss = s[0:11] + str(c + 1)
                pro.th_id = ss
            elif c >= 9 and c <= 98:
                ss = s[0:10] + str(c + 1)
                pro.th_id = ss
            elif c >= 99 and c <= 999:
                ss = s[0:9] + str(c + 1)
                pro.th_id = ss
            else:
                ss = s[0:8] + str(c + 1)
                pro.th_id = ss
        ws.save()
        pro.save()
        messages.error(request, 'Payment Successfully Completed.Yor have registered for Arduino For Schools Workshop', extra_tags='paid')
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')


def bcm(request):
    if request.user.is_authenticated:
        return render(request, 'bcmpay.html')
    else:
        return render(request, 'login.html')

@csrf_exempt
def bcmsuccess(request):
    if request.method == "POST":
        trans_id=request.POST.get('trans')
        if transactions.objects.filter(tans_id=trans_id).exists():
            messages.error(request, "The transaction ID you have enetered is already used.", extra_tags='trans')
            return render(request,'bcmpay.html')
        dat = str(datetime.datetime.now())
        tra=transactions(tans_id=trans_id,email=request.user.username,trans_time=dat,reason="BCM")
        tra.save()
        pro=profile.objects.get(id_no=request.user.profile.id_no)
        ws = workshop.objects.get(user=request.user)
        pro.payment = "Yes"
        pro.evpay = "Yes"
        pro.pay_id = trans_id
        pro.evcount += 1
        ws.payment = "Yes"
        ws.tg = "bcm"
        ws.pay_id=trans_id
        if request.user.profile.th_id == "0":
            c = 0
            s = "TRG-WEB-0000"
            pr = profile.objects.all();
            for k in pr:
                if k.th_id != "0":
                    c += 1
            if c < 9:
                ss = s[0:11] + str(c + 1)
                pro.th_id = ss
            elif c >= 9 and c <= 98:
                ss = s[0:10] + str(c + 1)
                pro.th_id = ss
            elif c >= 99 and c <= 999:
                ss = s[0:9] + str(c + 1)
                pro.th_id = ss
            else:
                ss = s[0:8] + str(c + 1)
                pro.th_id = ss
        ws.save()
        pro.save()
        messages.error(request, 'Payment Successfully Completed.Yor have registered for BlockChain  Workshop', extra_tags='paid')
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')


def prt(request):
    if request.user.is_authenticated:
        return render(request, 'prtpay.html')
    else:
        return render(request, 'login.html')

@csrf_exempt
def prtsuccess(request):
    if request.method == "POST":
        trans_id=request.POST.get('trans')
        if transactions.objects.filter(tans_id=trans_id).exists():
            messages.error(request, "The transaction ID you have enetered is already used.", extra_tags='trans')
            return render(request,'prtpay.html')
        dat = str(datetime.datetime.now())
        tra=transactions(tans_id=trans_id,email=request.user.username,trans_time=dat,reason="3Dprt")
        tra.save()
        pro=profile.objects.get(id_no=request.user.profile.id_no)
        ws = workshop.objects.get(user=request.user)
        pro.payment = "Yes"
        pro.pay_id = trans_id
        pro.evpay = "Yes"
        pro.evcount += 1
        ws.payment = "Yes"
        ws.tg = "prt"
        ws.pay_id=trans_id
        if request.user.profile.th_id == "0":
            c = 0
            s = "TRG-WEB-0000"
            pr = profile.objects.all();
            for k in pr:
                if k.th_id != "0":
                    c += 1
            if c < 9:
                ss = s[0:11] + str(c + 1)
                pro.th_id = ss
            elif c >= 9 and c <= 98:
                ss = s[0:10] + str(c + 1)
                pro.th_id = ss
            elif c >= 99 and c <= 999:
                ss = s[0:9] + str(c + 1)
                pro.th_id = ss
            else:
                ss = s[0:8] + str(c + 1)
                pro.th_id = ss
        ws.save()
        pro.save()
        messages.error(request, 'Payment Successfully Completed.Yor have registered for 3D Printing Workshop', extra_tags='paid')
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def ai(request):
    if request.user.is_authenticated:
        return render(request, 'aipay.html')
    else:
        return render(request, 'index.html')

@csrf_exempt
def aisuccess(request):
    if request.method == "POST":
        trans_id=request.POST.get('trans')
        if transactions.objects.filter(tans_id=trans_id).exists():
            messages.error(request, "The transaction ID you have enetered is already used.", extra_tags='trans')
            return render(request,'aipay.html')
        dat = str(datetime.datetime.now())
        tra=transactions(tans_id=trans_id,email=request.user.username,trans_time=dat,reason="AI & ML")
        tra.save()
        pro=profile.objects.get(id_no=request.user.profile.id_no)
        ws = workshop.objects.get(user=request.user)
        pro.payment = "Yes"
        pro.evpay = "Yes"
        pro.pay_id = trans_id
        pro.evcount += 1
        ws.payment = "Yes"
        ws.pay_id=trans_id
        ws.tg = "ai"
        if request.user.profile.th_id == "0":
            c = 0
            s = "TRG-WEB-0000"
            pr = profile.objects.all();
            for k in pr:
                if k.th_id != "0":
                    c += 1
            if c < 9:
                ss = s[0:11] + str(c + 1)
                pro.th_id = ss
            elif c >= 9 and c <= 98:
                ss = s[0:10] + str(c + 1)
                pro.th_id = ss
            elif c >= 99 and c <= 999:
                ss = s[0:9] + str(c + 1)
                pro.th_id = ss
            else:
                ss = s[0:8] + str(c + 1)
                pro.th_id = ss
        ws.save()
        pro.save()
        messages.error(request, 'Payment Successfully Completed.Yor have registered for AI & ML Workshop', extra_tags='paid')
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def tt(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.tt="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')
def sl(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes":
        pro=profile.objects.get(user=request.user)
        pro.sl="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')
def sb(request):
    if request.user.is_authenticated  and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.sb="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def tet(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes":
        pro=profile.objects.get(user=request.user)
        pro.tet="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def tc(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes":
        pro=profile.objects.get(user=request.user)
        pro.tc="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def deb(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes":
        pro=profile.objects.get(user=request.user)
        pro.deb="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def saw(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes":
        pro=profile.objects.get(user=request.user)
        pro.saw="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def cg(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes":
        pro=profile.objects.get(user=request.user)
        pro.cg="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def ipl(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes":
        pro=profile.objects.get(user=request.user)
        pro.ipl="Yes"
        pro.evcount += 1
        iplc=iplcount(name=pro.id_no,count=1)
        iplc.save()
        iplcc=iplcount.objects.all()
        ipl_count=iplcc.count()
        prof=profile.objects.all()
        for k in prof:
            k.ipcount = ipl_count
            k.save()
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def quiz(request):
    if request.user.is_authenticated  and request.user.profile.payment=="Yes":
        pro=profile.objects.get(user=request.user)
        pro.quiz="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def mp(request):
    if request.user.is_authenticated  and request.user.profile.payment=="Yes":
        pro=profile.objects.get(user=request.user)
        pro.mp="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def ld(request):
    if request.user.is_authenticated  and request.user.profile.payment=="Yes":
        pro=profile.objects.get(user=request.user)
        pro.ld="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def wb(request):
    if request.user.is_authenticated  and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.wb="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def sg(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes":
        pro=profile.objects.get(user=request.user)
        pro.sg="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def rd(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes":
        pro=profile.objects.get(user=request.user)
        pro.rd="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def bgmi(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes":
        pro=profile.objects.get(user=request.user)
        pro.bgmi="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')
def ttpay_initiate(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST.get('name')
            mob = request.POST.get('mobile')
            user = User.objects.get(username=request.user.username)
            if user is not None:
                tr1 = thrusangtank.objects.filter(user=user)
                if not tr1:
                    tr = thrusangtank(name=name, mobile=mob, user=user)
                    tr.save()
                else:
                    tr = thrusangtank.objects.get(user=user)
                    tr.name = name
                    tr.mobile = mob
                    tr.save()
            else:
                messages.error(request, 'Something went wrong.', extra_tags='login')
                return render(request, 'login.html')
        return render(request,'payment500.html')
    else:
        return render(request, 'login.html')

@csrf_exempt
def ttsuccess(request):
    if request.method == "POST":
        trans_id=request.POST.get('trans')
        if transactions.objects.filter(tans_id=trans_id).exists():
            messages.error(request, "The transaction ID you have enetered is already used.", extra_tags='trans')
            return render(request,'payment500.html')
        dat = str(datetime.datetime.now())
        tra=transactions(tans_id=trans_id,email=request.user.username,trans_time=dat,reason="Thrusang Tank")
        tra.save()
        pro=profile.objects.get(id_no=request.user.profile.id_no)
        pro.pay_id = trans_id
        pro.ttpay_id = trans_id
        pro.ttpay = "Yes"
        pro.payment = "Yes"
        pro.tt = "Yes"
        pro.evcount += 1
        if request.user.profile.th_id == "0":
            c = 0
            s = "TRG-WEB-0000"
            pr = profile.objects.all();
            for k in pr:
                if k.th_id != "0":
                    c += 1
            if c < 9:
                ss = s[0:11] + str(c + 1)
                pro.th_id = ss
            elif c >= 9 and c <= 98:
                ss = s[0:10] + str(c + 1)
                pro.th_id = ss
            elif c >= 99 and c <= 999:
                ss = s[0:9] + str(c + 1)
                pro.th_id = ss
            else:
                ss = s[0:8] + str(c + 1)
                pro.th_id = ss
        pro.save()
        messages.error(request, 'Payment Successfully Completed.', extra_tags='paid')
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')


def ttdetails(request):
    return render(request,'Thrusang_Tank.html')

# descriptions


def tank_det(request):
    return render(request, 'Thrusangtank.html')


def slg_det(request):
    return render(request, 'SNAKE & LADDER.html')


def ssb_det(request):
    return render(request, 'SELECTfrombrain.html')


def techtalk_det(request):
    return render(request, 'Techtalk.html')


def tricky_det(request):
    return render(request, 'TRICKYCRICUITS.html')


def debug_det(request):
    return render(request, 'DE-BUGGING.html')


def saw_det(request):
    return render(request, 'SPIN-A-WEB.html')


def codegolf_det(request):
    return render(request, 'CODE GOLF.html')


def ipl_det(request):
    return render(request, 'IPL AUCTION.html')


def bgmi_det(request):
    return render(request, 'BGMI.html')


def squid_det(request):
    return render(request, 'SQUID GAME.html')


def ludo_det(request):
    return render(request, 'LUDO KING.html')


def roadies_det(request):
    return render(request, 'ROADIES.html')


def mock_det(request):
    return render(request, 'MOCK PARLIAMENT.html')


def quiz_det(request):
    return render(request, 'QUIZ COMBAT.html')


def wirebuzz_det(request):
    return render(request, 'WIRE BUZZ.html')


def iot_det(request):
    return render(request, 'index.html')


def cs_det(request):
    return redirect("https://drive.google.com/file/d/15b70Z1qaAZJmp-HsSS9_P2WRZywYc82q/view?usp=sharing")


def arduino_det(request):
    return render(request, 'index.html')


def blockchain_det(request):
    return redirect("https://drive.google.com/file/d/1_ULxTeaUMp1816uHC1bUjRsJyAAt5VyV/view?usp=sharing")


def printing_det(request):
    return redirect("https://drive.google.com/file/d/16o4TeolOOf8k_j_7otZuNj6mk7d0BYRf/view?usp=sharing")


def ai_det(request):
    return redirect("https://drive.google.com/file/d/10geB4duBQyNcTo38pFUtlZM9IV_UNCZr/view?usp=sharing")


def eventexplore(request):
    return render(request, 'events.html')

def thanks(request):
    return render(request, 'events.html')





