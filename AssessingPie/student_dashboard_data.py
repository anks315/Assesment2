from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext,loader,Context
import Query
import Constant
from gaesessions import get_current_session
import logging
from google.appengine.ext import ndb

def userdetails(request):
    session = get_current_session()
    type =session.get('type',-1)
    if type == Constant.Constant.STUDENT:
        t = loader.get_template('Dashboard/user_information.xml')
        c = Context({'user_name':session.get('studentname',-1),'last_login':session.get('lastlogin',-1),'email':session.get('email',-1),'contactnumber':session.get('contactnumber',-1)})
        return HttpResponse(t.render(c),
        content_type="text/xml")
    if  type == Constant.Constant.TEACHER :
        t = loader.get_template('Dashboard/user_information.xml')
        c = Context({'user_name':session.get('teachername',-1),'last_login':session.get('lastlogin',-1),'email':session.get('email',-1),'contactnumber':session.get('contactnumber',-1)})
        return HttpResponse(t.render(c),
        content_type="text/xml")

        #return render_to_response('Dashboard/user_information.xml',{'user_name':user_name,'last_login':last_login},context_instance = RequestContext(request),content_type="text/xml;")
def subjectdetailsofstudent(request):
    session = get_current_session()
    type =session.get('type',-1)
    if type == Constant.Constant.STUDENT:
         subjectdetails = Query.get_subject_details_by_student(session['studentkey'])
         t = loader.get_template('Dashboard/subjectdetailsofstudent')
         c = Context({'subjectdetails':subjectdetails,})
         return HttpResponse(t.render(c),content_type="text/xml")


def getmasterybysubject(request):
    session = get_current_session()
    studentkey = session.get('studentkey',-1)
    mastery = Query.get_mastery_for_all_subjects(studentkey)
    t = loader.get_template('Dashboard/mastery_by_subject.xml')
    c = Context({'masterdict':mastery,})
    return HttpResponse(t.render(c),
    content_type="text/xml")

    #return render_to_response('Dashboard/mastery_by_subject.xml',{'masterdict':mastery,},context_instance = RequestContext(request),content_type="text/xml")

def getpendingassessment(request):

    session = get_current_session()
    studentkey = session.get('studentkey',-1)
    subjectlist = Query.get_subjects_by_student(studentkey)
    pendingassessmentbysubject = {}
    for subject in subjectlist:
        pendingassessments = Query.get_pending_assessments_by_subject(studentkey,subject.key)
        logging.error(pendingassessments)
        pendingassessmentbysubject[subject.name]= pendingassessments
    t = loader.get_template('Dashboard/pending_assessmentbysubject.xml')
    c = Context({'assessmentdict':pendingassessmentbysubject,})
    return HttpResponse(t.render(c),
    content_type="text/xml")
    #return render_to_response('Dashboard/pending_assessmentbysubject.xml',{'assessmentdict':pendingassessmentbysubject,},context_instance = RequestContext(request),content_type="text/xml")

def getgrowthforallsubject(request):

    session = get_current_session()
    studentkey = session.get('studentkey',-1)
    growthdict = Query.get_growth_for_all_subject(studentkey)
    t = loader.get_template('Dashboard/growth_by_subject.xml')
    c = Context({'growthdict':growthdict,})
    return HttpResponse(t.render(c),
    content_type="text/xml")
    #return render_to_response('Dashboard/growth_by_subject.xml',{'growthdict':growthdict,},context_instance = RequestContext(request),content_type="text/xml")


def getreadytolearnbysubject(request):

    session = get_current_session()
    studentkey = session.get('studentkey',-1)
    readytolearndict =  Query.get_ready_to_learn_of_all_topic_dummy(studentkey)
    t = loader.get_template('Dashboard/readytolearn_by_subject')
    c = Context({'readytolearndict':readytolearndict,})
    return HttpResponse(t.render(c),
    content_type="text/xml")
    #return render_to_response('Dashboard/readytolearn_by_subject',{'readytolearndict':readytolearndict,},context_instance = RequestContext(request),content_type="text/xml")


def getlearningprogressdatewise(request):

    session = get_current_session()
    studentkey = session.get('studentkey',-1)
    key = request.GET['id']
    subjectkey = ndb.Key(urlsafe=key)
    learningprogressdict = Query.get_learning_progress_date_wise_dummy(studentkey,subjectkey)
    t = loader.get_template('Dashboard/learningprogress_by_date')
    c = Context({'learningprogressdict':learningprogressdict,})
    return HttpResponse(t.render(c),
    content_type="text/xml")
    #return render_to_response('Dashboard/learningprogress_by_date',{'learningprogressdict':learningprogressdict,},context_instance = RequestContext(request))


def getspecialcourses(request):
    session = get_current_session()
    schoolkey=session.get('schoolkey',-1)
    specialcourseslist=Query.get_global_subjects(schoolkey)
    t = loader.get_template('Dashboard/globalcourseslist.xml')
    c = Context({'specialcourses':specialcourseslist,})
    return HttpResponse(t.render(c),
    content_type="text/xml")



def gettopicwisescoreofsubject(request):
    session = get_current_session()
    studentkey = session.get('studentkey',-1)
    key = request.GET['id']
    subjectkey = ndb.Key(urlsafe=key)
    topicwisescore=Query.get_recent_assessment_topic_scores_of_student(studentkey,subjectkey)
    t = loader.get_template('Dashboard/topicwisescoreofsubject.xml')
    c = Context({'topicwisescore':topicwisescore,})
    return HttpResponse(t.render(c),
    content_type="text/xml")

def getreadytolearnofsubject(request):
    session = get_current_session()
    studentkey = session.get('studentkey',-1)
    key = request.GET['id']
    subjectkey = ndb.Key(urlsafe=key)
    readytolearnofsubject=Query.get_recent_assessment_next_questions_of_student(studentkey,subjectkey)
    t = loader.get_template('Dashboard/readytolearn_ofsubject')
    c = Context({'readytolearnofsubject':readytolearnofsubject,})
    return HttpResponse(t.render(c),
    content_type="text/xml")

def getmasteryofsubject(request):
    session = get_current_session()
    studentkey = session.get('studentkey',-1)
    logging.error("ank")
    logging.error(studentkey)
    key = request.GET['id']
    subjectkey = ndb.Key(urlsafe=key)
    mastery=Query.get_recent_assessment_score_of_student(studentkey,subjectkey)
    t = loader.get_template('Dashboard/masteryofsubject.xml')
    c = Context({'mastery':mastery,})
    return HttpResponse(t.render(c),
    content_type="text/xml")

def getgrowthofsubject(request):
    session = get_current_session()
    studentkey = session.get('studentkey',-1)
    logging.error("ank")
    logging.error(studentkey)
    key = request.GET['id']
    subjectkey = ndb.Key(urlsafe=key)
    growthdict=Query.get_learning_progress(studentkey,subjectkey)
    t = loader.get_template('Dashboard/growthofsubject.xml')
    c = Context({'growth':growthdict,})
    return HttpResponse(t.render(c),
    content_type="text/xml")

def getcourseinformation(request):
    key = request.GET['id']
    subjectkey = ndb.Key(urlsafe=key)
    courseinformation=Query.get_course_detail_by_subject(subjectkey)
    t = loader.get_template('Dashboard/getcourseinformation.xml')
    c = Context({'total_students':courseinformation['Total_Students'],'number_completed':courseinformation['100_Score_Students'],'average_score':courseinformation['Average_Score']})
    return HttpResponse(t.render(c),
    content_type="text/xml")