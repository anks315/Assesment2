from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext,loader,Context
import Query
import Constant
from gaesessions import get_current_session

def demoresponse(request):
    data = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<note>Ankur</note>"


    return render_to_response('AssessingPie/login_data.xml',{'loginname':"ankurl"},context_instance = RequestContext(request),content_type="text/xml")

def userdetails(request):
    session = get_current_session()

    user_information= Query.login("Ankit_Bhatia","ankit")
    teacher_information = Query.login('Vijay_Mehta','jkjk')
    if user_information[0] == Constant.Constant.TEACHER :
        student = user_information[1]
        session['student']= student
        user_name =  student.basic_info.firstname + ' ' + student.basic_info.lastname
        last_login = user_information[2]
        t = loader.get_template('Dashboard/user_information.xml')
        c = Context({'user_name':user_name,'last_login':last_login})
        return HttpResponse(t.render(c),
        content_type="text/xml")
    if teacher_information[0] == Constant.Constant.TEACHER :
        teacher = teacher_information[1]
        session['teacher']= teacher
        user_name =  teacher.basic_info.firstname + ' ' + teacher.basic_info.lastname
        last_login = teacher_information[2]
        t = loader.get_template('Dashboard/user_information.xml')
        c = Context({'user_name':user_name,'last_login':last_login})
        return HttpResponse(t.render(c),
        content_type="text/xml")

        #return render_to_response('Dashboard/user_information.xml',{'user_name':user_name,'last_login':last_login},context_instance = RequestContext(request),content_type="text/xml;")

def getmasterybysubject(request):
    user_information= Query.login("Ankit_Bhatia","ankit")
    session = get_current_session()
    student = user_information[1]
    session['student']= student
    mastery = Query.get_mastery_for_all_subjects(session['student'].key)
    t = loader.get_template('Dashboard/mastery_by_subject.xml')
    c = Context({'masterdict':mastery,})
    return HttpResponse(t.render(c),
    content_type="text/xml")

    #return render_to_response('Dashboard/mastery_by_subject.xml',{'masterdict':mastery,},context_instance = RequestContext(request),content_type="text/xml")

def getpendingassessment(request):
    user_information= Query.login("Ankit_Bhatia","ankit")
    session = get_current_session()
    student = user_information[1]
    session['student']= student
    subjectlist = Query.get_subjects_by_student(session['student'].key)
    pendingassessmentbysubject = {}
    for subject in subjectlist:
        pendingassessments = Query.get_pending_assessment_subject(subject.key,session['student'].key)
        pendingassessmentbysubject[subject.name]= pendingassessments
    t = loader.get_template('Dashboard/pending_assessmentbysubject.xml')
    c = Context({'assessmentdict':pendingassessmentbysubject,})
    return HttpResponse(t.render(c),
    content_type="text/xml")
    #return render_to_response('Dashboard/pending_assessmentbysubject.xml',{'assessmentdict':pendingassessmentbysubject,},context_instance = RequestContext(request),content_type="text/xml")

def getgrowthforallsubject(request):
    user_information= Query.login("Ankit_Bhatia","ankit")
    session = get_current_session()
    student = user_information[1]
    session['student']= student
    growthdict = Query.get_growth_for_all_subject(session['student'].key)
    t = loader.get_template('Dashboard/growth_by_subject.xml')
    c = Context({'growthdict':growthdict,})
    return HttpResponse(t.render(c),
    content_type="text/xml")
    #return render_to_response('Dashboard/growth_by_subject.xml',{'growthdict':growthdict,},context_instance = RequestContext(request),content_type="text/xml")


def getreadytolearnbysubject(request):
    user_information= Query.login("Ankit_Bhatia","ankit")
    session = get_current_session()
    student = user_information[1]
    session['student']= student
    readytolearndict =  Query.get_ready_to_learn_of_all_topic_dummy(session['student'].key)
    t = loader.get_template('Dashboard/readytolearn_by_subject')
    c = Context({'readytolearndict':readytolearndict,})
    return HttpResponse(t.render(c),
    content_type="text/xml")
    #return render_to_response('Dashboard/readytolearn_by_subject',{'readytolearndict':readytolearndict,},context_instance = RequestContext(request),content_type="text/xml")


def getlearningprogressdatewise(request):
    user_information= Query.login("Ankit_Bhatia","ankit")
    session = get_current_session()
    student = user_information[1]
    session['student']= student
    learningprogressdict = Query.get_learning_progress_date_wise_dummy(session['student'].key)
    t = loader.get_template('Dashboard/learningprogress_by_date')
    c = Context({'learningprogressdict':learningprogressdict,})
    return HttpResponse(t.render(c),
    content_type="text/xml")
    #return render_to_response('Dashboard/learningprogress_by_date',{'learningprogressdict':learningprogressdict,},context_instance = RequestContext(request))