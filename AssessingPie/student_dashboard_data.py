from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import Query
import Constant
from gaesessions import get_current_session

def demoresponse(request):
    data = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<note>Ankur</note>"


    return render_to_response('AssessingPie/login_data.xml',{'loginname':"ankurl"},context_instance = RequestContext(request),content_type="text/xml")

def userdetails(request):
    session = get_current_session()

    user_information= Query.login("Ankit_Bhatia","ankit")

    if user_information[0] == Constant.Constant.STUDENT :
        student = user_information[1]
        session['student']= student
        user_name =  student.basic_info.firstname + ' ' + student.basic_info.lastname
        last_login = user_information[2]
        return render_to_response('Dashboard/user_information.xml',{'user_name':user_name,'last_login':last_login},context_instance = RequestContext(request),content_type="text/xml;")

def getmasterybysubject(request):
    user_information= Query.login("Ankit_Bhatia","ankit")
    session = get_current_session()
    student = user_information[1]
    session['student']= student
    mastery = Query.get_mastery_for_all_subjects(session['student'].key)
    return render_to_response('Dashboard/mastery_by_subject.xml',{'masterdict':mastery,},context_instance = RequestContext(request),content_type="text/xml")

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
        return render_to_response('Dashboard/pending_assessmentbysubject.xml',{'assessmentdict':pendingassessmentbysubject,},context_instance = RequestContext(request),content_type="text/xml")
