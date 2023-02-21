from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import profile, thrusangtank
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
import datetime
def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def events(request):
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
    return render(request, 'index.html')

def gyasundil(request):
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
        regtype = request.POST.get('regtype')
        ethpay='No'
        ardpay='No'
        if regtype == 'ETHICAL HACKING':
            ethpay = 'Yes'
        elif regtype == 'ARDUINO FOR SCHOOLS':
            ardpay = 'Yes'
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
        dat = str(datetime.datetime.now())
        t_id=""
        c = 0
        s = "TRG-WEB-0000"
        pr = profile.objects.all();
        for k in pr:
            if k.th_id != "0":
                c += 1
        if c < 9:
            ss = s[0:11] + str(c + 1)
            t_id = ss
        elif c >= 9 and c <= 98:
            ss = s[0:10] + str(c + 1)
            t_id = ss
        elif c >= 99 and c <= 999:
            ss = s[0:9] + str(c + 1)
            t_id = ss
        else:
            ss = s[0:8] + str(c + 1)
            t_id = ss
        prof = profile(id_no=id_no, college_name=coll, branch=branch, year_of_study=year_of_study,
                       gender=gender, mobile=phn_no, payment='Yes', pay_id='', th_id=t_id
                       ,evpay="Yes",reg_time=dat,ethical= ethpay,aurdino= ardpay,crtdrsk= 'No',repair= 'No',knowit= 'No',cyber="No",
                       thrsngtnk= 'No',selectstr= 'No',techt= 'No',tricky= 'No',spinweb= 'No',ithon= 'No',dreams= 'No',
                       droneai= 'No',wordwiz= 'No',sanklp= 'No',prodigai= 'No',woedblk= 'No',mathbz= 'No',jam= 'No',
                       quiz= 'No',webdes= 'No',postdes= 'No',codewar= 'No',dpquer= 'No',innovatr= 'No',techsi= 'No',iplauc= 'No',bgmi= 'No',
                       squid= 'No',ludo= 'No',quizcomb= 'No',onemorepls= 'No',handsup= 'No',chunk= 'No',myclay= 'No',rushup= 'No',
                       spellb= 'No',phtophon= 'No',suduko= 'No',smashkrts= 'No',dhumcrds= 'No',thugof= 'No',lemonspn= 'No',
                       esports= 'No',badmnton= 'No',volleybl= 'No',crckt= 'No',foodchlng= 'No',evcount=0, user=user)

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


def logout_user(request):
    logout(request)
    return render(request, 'index.html')


def ethical(request):

    messages.error(request, 'You have already registered for events.To register to this workshop please contact the management team.', extra_tags = 'fail')
    return render(request, 'events.html')

def aurdino(request):

    messages.error(request, 'You have already registered for events.To register to this workshop please contact the management team.', extra_tags = 'fail')
    return render(request, 'events.html')

def tank_detpay(request):
    return render(request, 'Thrusang_Tank_det.html')

def tank_success(request):
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
        pro = profile.objects.get(id_no=request.user.profile.id_no)
        pro.thrsngtnk = "Yes"
        pro.save()
        return render(request,'thankyou.html')
    else:
        return render(request, 'login.html')

def crtdrsk(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.crtdrsk="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def repair(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.repair="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def cyber(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.cyber="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def knowit(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.knowit="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def selectstr(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.selectstr="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def techt(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.techt="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def tricky(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.tricky="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def spinweb(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.spinweb="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def ithon(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.ithon="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def dreams(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.dreams="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def droneai(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.droneai="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def wordwiz(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.wordwiz="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def sanklp(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.sanklp="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def prodigai(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.prodigai="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def woedblk(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.woedblk="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def mathbz(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.mathbz="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def jam(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.jam="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def quiz(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.quiz="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def webdes(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.webdes="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def postdes(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.postdes="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def codewar(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.codewar="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def dpquer(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.dpquer="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def innovatr(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.innovatr="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def techsi(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.techsi="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def iplauc(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.iplauc="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def bgmi(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.bgmi="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def squid(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.squid="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def ludo(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.ludo="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def quizcomb(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.quizcomb="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def onemorepls(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.onemorepls="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def handsup(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.handsup="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def chunk(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.chunk="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def myclay(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.myclay="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def rushup(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.rushup="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def spellb(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.spellb="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def phtophon(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.phtophon="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def suduko(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.suduko="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def smashkrts(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.smashkrts="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def dhumcrds(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.dhumcrds="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def thugof(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.thugof="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def lemonspn(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.lemonspn="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def esports(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.esports="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def badmnton(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.badmnton="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def volleybl(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.volleybl="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def crckt(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.crckt="Yes"
        pro.evcount += 1
        pro.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'login.html')

def foodchlng(request):
    if request.user.is_authenticated and request.user.profile.payment=="Yes" :
        pro=profile.objects.get(user=request.user)
        pro.foodchlng="Yes"
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

def ttdetails(request):
    return render(request,'Thrusang_Tank.html')

# descriptions


def tank_det(request):
    return render(request, 'Thrusangtank.html')


def ssb_det(request):
    return render(request, 'SELECTfrombrain.html')


def techtalk_det(request):
    return render(request, 'Techtalk.html')


def tricky_det(request):
    return render(request, 'TRICKYCRICUITS.html')

def saw_det(request):
    return render(request, 'SPIN-A-WEB.html')


def ipl_det(request):
    return render(request, 'IPL AUCTION.html')


def bgmi_det(request):
    return render(request, 'BGMI.html')


def squid_det(request):
    return render(request, 'SQUID GAME.html')


def ludo_det(request):
    return render(request, 'LUDO KING.html')

def quiz_det(request):
    return render(request, 'QUIZ COMBAT.html')


def cs_det(request):
    return redirect("https://drive.google.com/file/d/15b70Z1qaAZJmp-HsSS9_P2WRZywYc82q/view?usp=sharing")

def aids_det(request):
    return redirect("https://drive.google.com/file/d/13uDUiVbA4Qh2ugL3Z3FZ3kwNGuaNLcsW/view?usp=sharing")


def eventexplore(request):
    return render(request, 'events.html')

def thanks(request):
    return render(request, 'events.html')

def quizophile_det(request):
    return render(request, 'Quizophile_event.html')

def dbqueries_det(request):
    return render(request, 'DBQueries_event.html')
def posterdesign_det(request):
    return render(request, 'posterDesign_event.html')

def technicalessay_det(request):
    return render(request, 'technicalEssay_event.html')
def innovator_det(request):
    return render(request, 'innovator_event.html')

def webdesign_det(request):
    return render(request, 'webDesign_event.html')

def codewar_det(request):
    return render(request, 'codeWar_event.html')

def regform(request):
    return redirect("https://forms.gle/UeygUBGBcz8HjFp16")

