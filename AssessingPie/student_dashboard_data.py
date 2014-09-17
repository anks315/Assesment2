from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext,loader,Context
import Query
import Constant
from gaesessions import get_current_session
import logging

def userdetails(request):
    session = get_current_session()
    type =session.get('type',-1)
    if type == Constant.Constant.STUDENT:
        t = loader.get_template('Dashboard/user_information.xml')
        c = Context({'user_name':session.get('studentname',-1),'last_login':session.get('lastlogin',-1)})
        return HttpResponse(t.render(c),
        content_type="text/xml")
    if  type == Constant.Constant.TEACHER :
        t = loader.get_template('Dashboard/user_information.xml')
        c = Context({'user_name':session.get('teachername',-1),'last_login':session.get('lastlogin',-1)})
        return HttpResponse(t.render(c),
        content_type="text/xml")

        #return render_to_response('Dashboard/user_information.xml',{'user_name':user_name,'last_login':last_login},context_instance = RequestContext(request),content_type="text/xml;")

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
        pendingassessments = Query.get_pending_assessment_subject(subject.key,studentkey)
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
    learningprogressdict = Query.get_learning_progress_date_wise_dummy(studentkey)
    t = loader.get_template('Dashboard/learningprogress_by_date')
    c = Context({'learningprogressdict':learningprogressdict,})
    return HttpResponse(t.render(c),
    content_type="text/xml")
    #return render_to_response('Dashboard/learningprogress_by_date',{'learningprogressdict':learningprogressdict,},context_instance = RequestContext(request))