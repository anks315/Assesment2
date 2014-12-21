# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from gaesessions import get_current_session
from engine import nextquestion,Question,update,maxstate,setcount,getcount,usersdict,UserBuffer,maxstatesize,getnumquestions,readytolearn,completedtopics,currentstatelist,scorelist,nextstatelist,readytolearnquestionkey
from django.template import RequestContext
from google.appengine.api import users
from dummydata import fill,flush
from Query import login
import logging
import inferenceengine
from google.appengine.ext import ndb
import  Query
import datetime
import Constant
from django.core.context_processors import csrf


# askquestion function call assessment engine to update states probabilty and choose next \
# probable question to ask and redirect to question page.
# If no effective next question to ask it redirect to report page

def asknextquestion(request):


    session = get_current_session()
    assessmentkey=''

    c=session.get('studentname',-1)
    if c != -1:
        if request.method != 'POST':
            usersdict.pop(c, None)
            assessmentkey = request.GET['id']
            session['assessmentkey']=assessmentkey
            key = ndb.Key(urlsafe=assessmentkey)
            session['assessmentkey']=key
            logging.error(assessmentkey)
            assessment = key.get()
            listoftopics=assessment.topics_in_assessment_key
            session['listoftopics']=listoftopics
            session['topicnumber'] = 0
            completedtopics[session['studentname']] ={}
            scorelist[session['studentname']] = []
            readytolearn[session['studentname']]=[]
            readytolearnquestionkey[session['studentname']]=[]
            currentstatelist[session['studentname']]=[]
            nextstatelist[session['studentname']]=[]
            session['score']=0
            usersdict[c]= UserBuffer(listoftopics[0])
    else:
        return render_to_response('Home/homepage.html',{'loginurl': users.create_login_url('/'),},context_instance = RequestContext(request))


    if request.method == 'POST':

        setcount(session['studentname'])
        answer =request.POST['answer']

        if answer == usersdict[session['studentname']].questions[nextquestion(session['studentname'])].answer[0] :
             update(session['studentname'], True)
        else:
            update(session['studentname'], False)
    logging.error(maxstatesize(session['studentname']))
    logging.error(maxstate(session['studentname']))
    logging.error(usersdict[session['studentname']].states[maxstatesize(session['studentname'])][maxstate(session['studentname'])].questionstuple)
    val=0
    if  session.get('studentname',-1)!=-1 and (usersdict[session['studentname']].states[maxstatesize(session['studentname'])][maxstate(session['studentname'])].prob > 0.40 or getcount(session['studentname'])==getnumquestions(session['studentname']) ):
        #global val
        #global readytolearn
        strknow = "You know :"
        for quest in usersdict[session['studentname']].states[maxstatesize(session['studentname'])][maxstate(session['studentname'])].questionstuple:
            if quest==-1:
                val=0
            else:
                strknow+=usersdict[session['studentname']].questions[quest].questionstring
                strknow+=",,"
                val+=1
        maxsta =maxstate(session['studentname'])
        logging.error(val)
        logging.error(getnumquestions(session['studentname']))

        if val==getnumquestions(session['studentname']):
            nextstatelist[session['studentname']].append(None)
            currentstatelist[session['studentname']].append(usersdict[session['studentname']].states[maxstatesize(session['studentname'])][maxstate(session['studentname'])].key)
            scorelist[session['studentname']].append(100)
            completedtopics[session['studentname']][listoftopics[session['topicnumber']]]=1
            logging.error("hii")
            #readytolearn[session['studentname']]=["Congratulations!!you have completed maths donut"]
        else:
            logging.error(maxstate(session['studentname']))

            states = usersdict[session['studentname']].states[maxstatesize(session['studentname']) + 1]
            logging.error(states)
            if(maxstatesize(session['studentname'])!=0):
                currentstate= usersdict[session['studentname']].states[maxstatesize(session['studentname'])][maxstate(session['studentname'])]
                for state in states:
                    stateset = set(state.questionstuple)
                    logging.error(stateset)
                    currentstateset = set(currentstate.questionstuple)
                    if stateset.issuperset(currentstateset):
                        quetionkey = stateset.difference(currentstateset)
                        logging.error(next(iter(quetionkey)))
                        logging.error(currentstate.key)
                        score =(val/(float)(getnumquestions(session['studentname'])))*100
                        scorelist[session['studentname']].append(int(score))
                        currentstatelist[session['studentname']].append(currentstate.key)
                        nextstatelist[session['studentname']].append(state.key)

                        session['score']+=score
                        #studentkey= session.get('studentkey',-1)
                        #schoolkey= session.get('schoolkey',-1)
                        #a=Query.update_assessment_detail_of_student(student_key=studentkey, assessment_key=ndb.Key(urlsafe=session['assessmentkey']),current_state_key= currentstate.key, next_state_key=currentstate.key,next_question_key=next(iter(quetionkey)),score=int(score),school_key=schoolkey,completion_date=datetime.datetime.now())
                        #logging.error(a)
                        readytolearn[session['studentname']].append(usersdict[session['studentname']].questions[next(iter(quetionkey))].questionstring)
                        readytolearnquestionkey[session['studentname']].append(usersdict[session['studentname']].questions[next(iter(quetionkey))].key)
                        break
            else:
                 scorelist[session['studentname']].append(0)
                 currentstatelist[session['studentname']].append(None)
                 nextstatelist[session['studentname']].append(None);
                 for state in states:
                     questiontuple = state.questionstuple
                     readytolearn[session['studentname']].append(usersdict[session['studentname']].questions[questiontuple[0]].questionstring)
                     readytolearnquestionkey[session['studentname']].append(usersdict[session['studentname']].questions[questiontuple[0]].key)


        if(session['topicnumber']==len(session['listoftopics'])-1):
            Query.update_assessment_detail_of_student(int(session['score']/(len(session['listoftopics']))) ,scorelist[session['studentname']], session['studentkey'], session['assessmentkey'], currentstatelist[session['studentname']], nextstatelist[session['studentname']], readytolearnquestionkey[session['studentname']], session['schoolkey'], datetime.datetime.now())
            del usersdict[session['studentname']]
            return render_to_response('AssessingPie_toBeremoved/pie.html',{'readytolearn':readytolearn[session['studentname']],'num_known': session['score']/(len(session['listoftopics'])) ,'st': maxsta,'state' : 'completed','know':strknow,},context_instance = RequestContext(request))

        else:
            del usersdict[session['studentname']]
            checknext=1;
            nexttopickey=0;
            while checknext==1:
                session['topicnumber']+=1
                if(session['topicnumber']==len(session['listoftopics'])):
                   logging.error("ankur")
                   logging.error(int(session['score']/(len(session['listoftopics']))))
                   Query.update_assessment_detail_of_student(int(session['score']/(len(session['listoftopics']))) ,scorelist[session['studentname']], session['studentkey'], session['assessmentkey'], currentstatelist[session['studentname']], nextstatelist[session['studentname']], readytolearnquestionkey[session['studentname']], session['schoolkey'], datetime.datetime.now())
                   return render_to_response('AssessingPie_toBeremoved/pie.html',{'readytolearn':readytolearn[session['studentname']],'num_known': session['score']/(len(session['listoftopics'])) ,'st': maxsta,'state' : 'completed','know':strknow,},context_instance = RequestContext(request))
                else:
                    nexttopickey =session['listoftopics'][session['topicnumber']]
                    prerequisitetopiclist = Query.get_prerequisite_topics_of_topic(nexttopickey)
                    checknext=0;
                    for topic in prerequisitetopiclist:
                        if completedtopics[session['studentname']].get(topic,-1)==-1 :
                            checknext=1;
                    if checknext==1:
                        currentstatelist[session['studentname']].append(None)
                        scorelist[session['studentname']].append(0)
                        nextstatelist[session['studentname']].append(None);



            usersdict[session['studentname']]=UserBuffer(nexttopickey)

            return render_to_response('AssessingPie/question.html',{'logouturl':users.create_logout_url('/') ,'logger' : users.get_current_user() ,'nextquestion' : usersdict[session['studentname']].questions[nextquestion(session['studentname'])].questionstring,},context_instance = RequestContext(request))


    else:
        return render_to_response('AssessingPie/question.html',{'logouturl':users.create_logout_url('/') ,'logger' : users.get_current_user() ,'nextquestion' : usersdict[session['studentname']].questions[nextquestion(session['studentname'])].questionstring,},context_instance = RequestContext(request))


# redirect to home page
# html : homepage.html
def home(request):

     return render_to_response('Home/homepage.html',{'loginurl': users.create_login_url('/'),},context_instance = RequestContext(request))


blocknumber = -1
numofpossibleantecedent=-1
currentblocknumber = -1
currentantecedentnumber=0
implication=-1
antecedent=[]
numalreadyinferred=0


#Contact Us page
def contactus(request):
        flush()
        fill()
        return render_to_response('AssessingPie/contact.html',{},context_instance = RequestContext(request))


def topicnames(request):
        return render_to_response('AssessingPie/topicname.html',{},context_instance = RequestContext(request))


def infer(request):
        return render_to_response('AssessingPie/testpage.html',{},context_instance = RequestContext(request))

def assesstopicname(request):
        return render_to_response('AssessingPie/assesstopicname.html',{},context_instance = RequestContext(request))



def  inferquestion(request):

    global currentantecedentnumber
    global currentblocknumber
    global  numofpossibleantecedent
    global  blocknumber
    global  numalreadyinferred
    global antecedent
    global implication
    session = get_current_session()
    if request.method == 'GET':
          key = request.GET['topickey']
          session['topickey']  = ndb.Key(urlsafe=key)
          key = request.GET['schoolkey']
          session['inferschoolkey'] = ndb.Key(urlsafe=key)


    c=session.get('infer',-1)
    if c==-1:
        session['infer']=users.get_current_user()

        usersdict[session['infer']]= inferenceengine.InferenceBuffer(session['topickey'])
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
            session['infer']=users.get_current_user()
            usersdict[session['infer']]= inferenceengine.InferenceBuffer(session['topickey'])
            blocknumber = usersdict[session['infer']].typeCache.getlength()

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

                    question = "&nbsp;&nbsp<b>If student do not know:</b> &nbsp;&nbsp"
                    for x in antecedent:
                        question +=usersdict[session['infer']].typeCache.gettype(x)
                    question = question+ "<br> &nbsp;&nbsp<b>He will not be able to answer: </b>&nbsp;&nbsp" +   usersdict[session['infer']].typeCache.gettype(implication)
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
                inferenceengine.generatestates(usersdict[session['infer']],session['topickey'], session['inferschoolkey'])
                return render_to_response('Home/homepage.html',{'loginurl': users.create_login_url('/'),},context_instance = RequestContext(request))
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
                inferenceengine.generatestates(usersdict[session['infer']],session['topickey'], session['inferschoolkey'])
                return render_to_response('Home/homepage.html',{'loginurl': users.create_login_url('/'),},context_instance = RequestContext(request))

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

def signout(request):
    session = get_current_session()
    if session['type'] == Constant.Constant.STUDENT:
        del session['studentkey']
        del session['schoolkey']
        del session['studentname']
        del session['email']
        del session['studentaddress']
        del session['contactnumber']
        del session['dateofbirth ']
        del session['sex']
        del session['lastlogin']

    if session['type'] == Constant.Constant.TEACHER:
            del session['teacherkey']
            del session['schoolkey']
            del session['teachername']
            del session['email']
            del session['teacheraddress']
            del session['contactnumber']
            del session['dateofbirth ']
            del session['sex']
            del session['lastlogin']

    return render_to_response('Home/homepage.html',{'loginurl': users.create_login_url('/'),},context_instance = RequestContext(request))


# dashboard gets called when username and password
def dashboard(request):


    session = get_current_session()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user_information= Query.login(username,password)
        session['type'] = user_information[0]
        if session['type'] == Constant.Constant.STUDENT:
            student = user_information[1]
            session['studentkey']= student.key
            session['schoolkey']=student.school
            session['studentname']=student.basic_info.firstname + student.basic_info.lastname
            session['email'] = student.basic_info.email
            session['studentaddress']= student.basic_info.address
            session['contactnumber'] = student.basic_info.contact_no
            session['dateofbirth '] =student.basic_info.date_of_birth
            session['sex']=student.basic_info.sex
            session['lastlogin']=user_information[2]

            return render_to_response('Dashboard/dashboard.html',{ },context_instance = RequestContext(request))
        if session['type'] == Constant.Constant.TEACHER:
            teacher = user_information[1]
            session['teacherkey']=teacher.key
            session['schoolkey']=teacher.school
            session['teachername']=teacher.basic_info.firstname + teacher.basic_info.lastname
            session['email'] = teacher.basic_info.email
            session['teacheraddress']= teacher.basic_info.address
            session['contactnumber'] = teacher.basic_info.contact_no
            session['dateofbirth '] = teacher.basic_info.date_of_birth
            session['sex']=teacher.basic_info.sex
            session['lastlogin']=user_information[2]
            return render_to_response('Dashboard/teacherdashboard.html',{},context_instance = RequestContext(request))
        return render_to_response('Home/homepage.html',{'loginurl': users.create_login_url('/'),},context_instance = RequestContext(request))
    else:
        if session['type'] == Constant.Constant.TEACHER:
            return render_to_response('Dashboard/teacherdashboard.html',{},context_instance = RequestContext(request))
        if session['type'] == Constant.Constant.STUDENT:
            return render_to_response('Dashboard/dashboard.html',{},context_instance = RequestContext(request))


def ques(request):
    return render_to_response('Home/Questions.html',{},context_instance = RequestContext(request))

def whatisscan(request):
    return render_to_response('Home/Home_scan.html',{},context_instance = RequestContext(request))

def login(request):
    return render_to_response('Home/login.html',{},context_instance = RequestContext(request))

def meetExperts(request):
    return render_to_response('Home/Meet_experts.html',{},context_instance = RequestContext(request))

def vedicMaths(request):
    return render_to_response('Home/vedicmaths.html',{},context_instance = RequestContext(request))

def xyz(request):
    return render_to_response('Dashboard/dashboardaleks.html',{},context_instance = RequestContext(request))
