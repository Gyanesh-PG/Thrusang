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
    path('pay_initiate', views.pay_initiate, name="pay_initiate"),
    path('success', views.success, name="success"),
    path('ttsuccess', views.ttsuccess, name="ttsuccess"),
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
    path('ld', views.ld, name="ld"),
    path('wb', views.wb, name="wb"),
    path('sg', views.sg, name="sg"),
    path('rd', views.rd, name="rd"),
    path('ai', views.ai, name="ai"),
    path('aisuccess', views.aisuccess, name="aisuccess"),
    path('bgmi', views.bgmi, name="bgmi"),
    path('ttdetails', views.ttdetails, name="ttdetails"),
    path('tank_det', views.tank_det, name="tank_det"),
    path('slg_det', views.slg_det, name="slg_det"),
    path('ssb_det', views.ssb_det, name="ssb_det"),
    path('techtalk_det', views.techtalk_det, name="techtalk_det"),
    path('tricky_det', views.tricky_det, name="tricky_det"),
    path('debug_det', views.debug_det, name="debug_det"),
    path('saw_det', views.saw_det, name="saw_det"),
    path('codegolf_det', views.codegolf_det, name="codegolf_det"),
    path('ipl_det', views.ipl_det, name="ipl_det"),
    path('bgmi_det', views.bgmi_det, name="bgmi_det"),
    path('squid_det', views.squid_det, name="squid_det"),
    path('ludo_det', views.ludo_det, name="ludo_det"),
    path('roadies_det', views.roadies_det, name="roadies_det"),
    path('mock_det', views.mock_det, name="mock_det"),
    path('quiz_det', views.quiz_det, name="quiz_det"),
    path('wirebuzz_det', views.wirebuzz_det, name="wirebuzz_det"),
    path('iot_det', views.iot_det, name="iot_det"),
    path('cs_det', views.cs_det, name="cs_det"),
    path('arduino_det', views.arduino_det, name="arduino_det"),
    path('blockchain_det', views.blockchain_det, name="blockchain_det"),
    path('printing_det', views.printing_det, name="printing_det"),
    path('ai_det', views.ai_det, name="ai_det"),
    path('eventexplore', views.eventexplore, name="eventexplore"),
    path('thanks', views.thanks, name="thanks"),
]
