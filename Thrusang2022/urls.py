"""Thrusang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('index.html', views.index,name="index"),
    path('aboutus', views.aboutus,name="aboutus"),
    path('team', views.team,name="team"),
    path('gallery', views.gallery,name="gallery"),
    path('events', views.events,name="events"),
    path('sponsers', views.sponsers,name="sponsers"),
    path('contact', views.contact,name="contact"),
    path('register', views.register,name="register"),
    path('register_user', views.register_user, name="register_user"),
    path('login_user', views.login_user, name="login_user"),
    path('log', views.log, name="log"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('user_profile', views.user_profile, name="user_profile"),
    path('ttpay_initiate', views.ttpay_initiate, name="ttpay_initiate"),
    path('iplpay_initiate', views.iplpay_initiate, name="iplpay_initiate"),
    path('pay_initiate', views.pay_initiate, name="pay_initiate"),
    path('success', views.success, name="success"),
    path('ttsuccess', views.ttsuccess, name="ttsuccess"),
    path('iplsuccess', views.iplsuccess, name="iplsuccess"),
    path('cwssuccess', views.cwssuccess, name="cwssuccess"),
    path('cws', views.cws, name="cws"),
    path('iotsuccess', views.iotsuccess, name="iotsuccess"),
    path('iot', views.iot, name="iot"),
    path('afssuccess', views.afssuccess, name="afssuccess"),
    path('afs', views.afs, name="afs"),
    path('bcmsuccess', views.bcmsuccess, name="bcmsuccess"),
    path('bcm', views.bcm, name="bcm"),
    path('prtsuccess', views.prtsuccess, name="prtsuccess"),
    path('prt', views.prt, name="prt"),
    path('tt', views.tt, name="tt"),
    path('sl', views.sl, name="sl"),
    path('sb', views.sb, name="sb"),
    path('tet', views.tet, name="tet"),
    path('tc', views.tc, name="tc"),
    path('deb', views.deb, name="deb"),
    path('saw', views.saw, name="saw"),
    path('cg', views.cg, name="cg"),
    path('ipl', views.ipl, name="ipl"),
    path('quiz', views.quiz, name="quiz"),
    path('mp', views.mp, name="mp"),
    path('ps', views.ps, name="ps"),
    path('mmt', views.mmt, name="mmt"),
    path('sg', views.sg, name="sg"),
    path('rd', views.rd, name="rd"),
    path('bgmi', views.bgmi, name="bgmi"),
    path('ttdetails', views.ttdetails, name="ttdetails"),
]
