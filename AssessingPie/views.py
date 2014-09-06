# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from gaesessions import get_current_session
from engine import nextquestion,Question,update,maxstate,setcount,getcount,usersdict,UserBuffer,maxstatesize,getnumquestions
from django.template import RequestContext
from google.appengine.api import  users
from dummydata import fill
from Query import login
import logging
import inferenceengine


counters=0
counter =0
val=0
readytolearn=""
def asknextquestion(request):

    global counters
    counters+=1
    session = get_current_session()

    c=session.get('index',-1)
    if c== -1:
        session['index']=users.get_current_user()
        usersdict[session['index']]= UserBuffer()
    else:
        if request.method != 'POST':
            del usersdict[session['index']]
            session['index']=-1




    if request.method == 'POST':

        setcount(session['index'])
        answer =request.POST['answer']

        if answer == usersdict[session['index']].questions[nextquestion(session['index'])].answer[0] :
             update(session['index'], True)
        else:
            update(session['index'], False)
    logging.error(maxstatesize(session['index']))
    logging.error(maxstate(session['index']))
    logging.error(usersdict[session['index']].states[maxstatesize(session['index'])][maxstate(session['index'])].questionstuple)
    val=0
    if  session.get('index',-1)!=-1 and (usersdict[session['index']].states[maxstatesize(session['index'])][maxstate(session['index'])].prob > 0.40 or getcount(session['index'])==getnumquestions(session['index']) ):
        global val
        global readytolearn
        strknow = "You know :"
        for quest in usersdict[session['index']].states[maxstatesize(session['index'])][maxstate(session['index'])].questionstuple:
            if quest==-1:
                val=0
            else:
                strknow+=usersdict[session['index']].questions[quest].questionstring
                strknow+=",,"
                val+=1
        maxsta =maxstate(session['index'])
        if val==getnumquestions(session['index']):

            readytolearn="Congratulations!!you have completed maths donut"
        else:
            logging.error(maxstate(session['index']))
            states = usersdict[session['index']].states[maxstatesize(session['index']) + 1]
            currentstate= usersdict[session['index']].states[maxstatesize(session['index'])][maxstate(session['index'])]
            for state in states:
                stateset = set(state.questionstuple)
                currentstateset = set(currentstate.questionstuple)
                if stateset.issuperset(currentstateset):
                    quetionkey = stateset.difference(currentstateset)
                    readytolearn+=usersdict[session['index']].questions[next(iter(quetionkey))].questionstring




        del usersdict[session['index']]
        del session['index']
        return render_to_response('AssessingPie/pie.html',{'readytolearn':readytolearn,'num_known': val ,'num_dontknow':3-val,'st': maxsta,'state' : 'completed','know':strknow,},context_instance = RequestContext(request))

    else:
        return render_to_response('AssessingPie/question.html',{'logouturl':users.create_logout_url('/') ,'logger' : users.get_current_user() ,'nextquestion' : usersdict[session['index']].questions[nextquestion(session['index'])].questionstring,},context_instance = RequestContext(request))

def home(request):


     session = get_current_session()
     if session.get('index',-1) != -1:
        del session['index']

     return render_to_response('Home/homepage.html',{'loginurl': users.create_login_url('/'),},context_instance = RequestContext(request))


blocknumber = -1
numofpossibleantecedent=-1
currentblocknumber = -1
currentantecedentnumber=0
implication=-1
antecedent=[]
numalreadyinferred=0

def contactus(request):
        fill()
        return render_to_response('AssessingPie/contact.html',{},context_instance = RequestContext(request))

def topicnames(request):
        return render_to_response('AssessingPie/topicname.html',{},context_instance = RequestContext(request))

def assesstopicname(request):
        return render_to_response('AssessingPie/assesstopicname.html',{},context_instance = RequestContext(request))


topicname = ''
def  inferquestion(request):

    global currentantecedentnumber
    global currentblocknumber
    global  numofpossibleantecedent
    global  blocknumber
    global  numalreadyinferred
    global antecedent
    global implication
    global topicname
    session = get_current_session()
    if request.method == 'GET':
         topicname = request.GET['topic']
    c=session.get('infer',-1)
    if c==-1:
        session['infer']=users.get_current_user()
        usersdict[session['infer']]= inferenceengine.InferenceBuffer()
        blocknumber = usersdict[session['infer']].typeCache.getlength()
    else:
        if request.method!='POST':
            del session['infer']
            session['infer'] = -1
            blocknumber = -1
            numofpossibleantecedent=-1
            currentblocknumber = -1
            currentantecedentnumber=0
            implication=-1
            antecedent=[]
            numalreadyinferred=0
            return render_to_response('AssessingPie/abc.html',{'loginurl': users.create_login_url('/'),},context_instance = RequestContext(request))

    if request.method=='POST':
        if request.POST['answer']=='yes':
             if currentblocknumber>0 and inferenceengine.passedhstest(usersdict[session['infer']],currentblocknumber,antecedent,implication):
                 inferenceengine.updatesurmise(usersdict[session['infer']],antecedent,implication)
             usersdict[session['infer']].blockCache.setimplicationtrue(currentblocknumber,currentantecedentnumber-1)
             inferenceengine.infertrue(usersdict[session['infer']],currentblocknumber,currentantecedentnumber-1,antecedent)
        else:
             usersdict[session['infer']].blockCache.setimplicationfalse(currentblocknumber,currentantecedentnumber-1)

    if currentblocknumber==-1:

        blocknumber = usersdict[session['infer']].typeCache.getlength()
        currentblocknumber=0
        usersdict[session['infer']].blockCache.initializeblock(currentblocknumber)


    while True:
        if numofpossibleantecedent==-1:
            numofpossibleantecedent=blocknumber**(currentblocknumber+2)
        if currentantecedentnumber<numofpossibleantecedent:
            if usersdict[session['infer']].blockCache.getimplication(currentblocknumber,currentantecedentnumber) ==-1:

                alreadyinffered=askquestion(currentblocknumber,currentantecedentnumber)
                currentantecedentnumber+=1
                if len(alreadyinffered)!=0:

                    question = "If student donot know: \n"
                    for x in antecedent:
                        question +=usersdict[session['infer']].typeCache.gettype(x)
                    question = question+ "He will not be able to answer: " +   usersdict[session['infer']].typeCache.gettype(implication)
                    return render_to_response('AssessingPie/inference.html',{'logouturl':users.create_logout_url('/') ,'logger' : users.get_current_user() ,'nextquestion' : question},context_instance = RequestContext(request))
                else:
                     numalreadyinferred+=1
            else:
                numalreadyinferred+=1
                currentantecedentnumber+=1
        else:
            logging.error("entered else")
            currentantecedentnumber=0
            if currentblocknumber==0:

                inferenceengine.createsurmise(usersdict[session['infer']])
            logging.error(numalreadyinferred)
            logging.error(numofpossibleantecedent)
            if(numalreadyinferred==numofpossibleantecedent):
                blocknumber = -1
                numofpossibleantecedent=-1
                currentblocknumber = -1
                currentantecedentnumber=0
                implication=-1
                antecedent=[]
                numalreadyinferred=0
                inferenceengine.generatestates(usersdict[session['infer']],topicname)
                return render_to_response('AssessingPie/abc.html',{'loginurl': users.create_login_url('/'),},context_instance = RequestContext(request))
            currentblocknumber+=1
            numalreadyinferred=0
            logging.error(currentblocknumber)
            inferenceengine.prepareblock(usersdict[session['infer']],currentblocknumber)
            if currentblocknumber<blocknumber:

                numofpossibleantecedent=blocknumber**(currentblocknumber+2)
            else:
                logging.error(usersdict[session['infer']].surmiseRelation.getstates(0))
                logging.error(usersdict[session['infer']].surmiseRelation.getstates(1))
                logging.error(usersdict[session['infer']].surmiseRelation.getstates(2))
                blocknumber = -1
                numofpossibleantecedent=-1
                currentblocknumber = -1
                currentantecedentnumber=0
                implication=-1
                antecedent=[]
                numalreadyinferred=0
                inferenceengine.generatestates(usersdict[session['infer']],topicname)
                return render_to_response('AssessingPie/abc.html',{'loginurl': users.create_login_url('/'),},context_instance = RequestContext(request))

            if usersdict[session['infer']].blockCache.getimplication(currentblocknumber,currentantecedentnumber) ==-1:
                logging.error("asking question")
                alreadyinffered=askquestion(currentblocknumber,currentantecedentnumber)
                currentantecedentnumber+=1
                if len(alreadyinffered)!=0:
                    question = "If student do not know: \n"
                    for x in antecedent:
                        question+= usersdict[session['infer']].typeCache.gettype(x)
                    question += "He will not  be able to answer: " +   usersdict[session['infer']].typeCache.gettype(implication)
                    return render_to_response('AssessingPie/inference.html',{'logouturl':users.create_logout_url('/') ,'logger' : users.get_current_user() ,'nextquestion' : question,},context_instance = RequestContext(request))
                else:
                     numalreadyinferred+=1
            else:
                numalreadyinferred+=1
                currentantecedentnumber+=1

def askquestion(block,antecedentid):
    session = get_current_session()
    global  blocknumber
    global antecedent
    global  implication
    antecedentqueryid = antecedentid
    antecedent =[]
    isvalid =1
    implication = antecedentqueryid % blocknumber
    for k in range(0,block+1):
        divisor = blocknumber**(block-k+1)
        if antecedentqueryid/divisor in antecedent:
            isvalid=0

        antecedent.append(antecedentqueryid/divisor)
        antecedentqueryid=antecedentqueryid%divisor
    if isvalid==1:
        inferred =0
        if block>0:
            for questiontype in antecedent:
                if questiontype == implication:
                    usersdict[session['infer']].blockCache.setimplicationtrue(block,antecedentid)
                    inferred=1
                    inferenceengine.infertrue(usersdict[session['infer']],block,antecedentid,antecedent)
                    return list()
                if usersdict[session['infer']].blockCache.getimplication(0,(blocknumber*questiontype)+implication)==1:
                    usersdict[session['infer']].blockCache.setimplicationtrue(block,antecedentid)
                    inferred=1
                    inferenceengine.infertrue(usersdict[session['infer']],block,antecedentid,antecedent)
                    return list()
                if usersdict[session['infer']].blockCache.getimplication(0,(blocknumber*questiontype)+implication)==2:
                    inferred=1
                    usersdict[session['infer']].blockCache.setimplicationfalse(block,antecedentid)
                    return  list()
        else:
            if antecedent[0]==implication:
                usersdict[session['infer']].blockCache.setimplicationtrue(block,antecedentid)
                inferred=1
                inferenceengine.infertrue(usersdict[session['infer']],block,antecedentid,antecedent)
                return list()
            return antecedent

    return list()


def dashboard(request):
    subjectsenrolled=['Maths','Science','English']
    return render_to_response('Dashboard/dashboard.html',{'logger' : 'kapeelbhandari' },context_instance = RequestContext(request))