# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from gaesessions import get_current_session
from engine import nextquestion,Question,update,maxstate,setcount,getcount,usersdict,UserBuffer
from django.template import RequestContext
from google.appengine.api import  users
from dummydata import fill
from Query import login
import logging


counters=0
counter =0
val=0
def asknextquestion(request):

    global counters
    counters+=1
    session = get_current_session()

    c=session.get('index',-1)
    if c== -1:
        session['index']=users.get_current_user()
        usersdict[session['index']]= UserBuffer()



    if request.method == 'POST':

        setcount(session['index'])
        answer =request.POST['answer']

        if answer == usersdict[session['index']].questions[nextquestion(session['index'])].answer[0] :
             update(session['index'], True)
        else:
            update(session['index'], False)

    logging.error(usersdict[session['index']].states[maxstate(session['index'])].questionstuple)
    val=0
    if  session.get('index',-1)!=-1 and (usersdict[session['index']].states[maxstate(session['index'])].prob > 0.40 or getcount(session['index'])==3 ):
        global val
        strknow = "You know :"
        for quest in usersdict[session['index']].states[maxstate(session['index'])].questionstuple:
            if quest==-1:
                val=0
            else:
                strknow+=usersdict[session['index']].questions[quest].questionstring
                strknow+=",,"
                val+=1
        maxsta =maxstate(session['index'])
        if val==3:

            readytolearn="Congratulations!!you have completed maths donut"
        else:
            logging.error(maxstate(session['index']))
            readytolearn=usersdict[session['index']].questions[usersdict[session['index']].states[maxstate(session['index'])+1].questionstuple[maxstate(session['index'])]].questionstring
        del usersdict[session['index']]
        del session['index']
        return render_to_response('AssessingPie/pie.html',{'readytolearn':readytolearn,'num_known': val ,'num_dontknow':3-val,'st': maxsta,'state' : 'completed','know':strknow,},context_instance = RequestContext(request))

    else:
        return render_to_response('AssessingPie/question.html',{'logouturl':users.create_logout_url('/') ,'logger' : users.get_current_user() ,'nextquestion' : usersdict[session['index']].questions[nextquestion(session['index'])].questionstring,},context_instance = RequestContext(request))

def home(request):


     session = get_current_session()
     if session.get('index',-1) != -1:
        del session['index']

     return render_to_response('AssessingPie/abc.html',{'loginurl': users.create_login_url('/'),},context_instance = RequestContext(request))


def contactus(request):

        return render_to_response('AssessingPie/contact.html',{},context_instance = RequestContext(request))