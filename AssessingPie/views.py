# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from gaesessions import get_current_session
from engine import nextquestion,Question,update,maxstate,setcount,getcount,usersdict,UserBuffer
from django.template import RequestContext
from google.appengine.api import  users


counters=0
counter =0
val=0
def asknextquestion(request):

    global counters
    counters+=1
    session = get_current_session()

    c=session.get('index',-1)
    if c== -1:
        session['index']=counters
        usersdict[session['index']]= UserBuffer()



    if request.method == 'POST':

        setcount(session['index'])
        answer =request.POST['answer']

        if int(answer) == usersdict[session['index']].questions[nextquestion(session['index'])].answer :
             update(session['index'], True)
        else:
            update(session['index'], False)

    if  session.get('index',-1)!=-1 and (usersdict[session['index']].states[maxstate(session['index'])].prob > 0.70 or getcount(session['index'])==3 ):
        global counter
        counter=0
        global val
        strknow = "You know :"
        val =0;
        while(counter<3):
            if counter in usersdict[session['index']].states[maxstate(session['index'])].questionstuple:
                val+=1

                strknow+=usersdict[session['index']].questions[counter].questionstring
                strknow+=",,"
            counter+=1
        maxsta =maxstate(session['index'])
        if val!=3:
            readytolearn = usersdict[session['index']].questions[val].questionstring
        else:
            readytolearn = 'Congratulation You have completed the course'
        del usersdict[session['index']]
        del session['index']
        return render_to_response('AssessingPie/pie.html',{'num_known': val ,'num_dontknow':3-val,'st': maxsta,'state' : 'completed','know':strknow,'ready_to_learn':readytolearn},context_instance = RequestContext(request))
    else:

        return render_to_response('AssessingPie/question.html',{'logouturl':users.create_logout_url('/') ,'logger' : users.get_current_user() ,'nextquestion' : usersdict[session['index']].questions[nextquestion(session['index'])].questionstring,},context_instance = RequestContext(request))

def home(request):
     session = get_current_session()
     if session.get('index',-1) != -1:
        del session['index']

     return render_to_response('AssessingPie/home.html',{'loginurl': users.create_login_url('/'),},context_instance = RequestContext(request))