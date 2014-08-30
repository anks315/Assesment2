from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext,loader,Context
import Query
import Constant
import dummydata
from gaesessions import get_current_session
import logging

def get_not_recently_loggedin(request):
    session = get_current_session()
    teacherkey = session.get('teacherkey',-1)
    notrecentlydict =Query.get_students_not_logged_in_by_class(teacherkey)
    logging.error('sbxjks' )
    logging.error(notrecentlydict)
    t = loader.get_template('Dashboard/not_recently_logged_in_byclass')
    c = Context({'notrecentlylogin': notrecentlydict,})
    return HttpResponse(t.render(c),content_type="text/xml")


def mastery_by_student_by_class(request):
    session = get_current_session()
    teacherkey = session.get('teacherkey',-1)
    mastery_by_student = Query.get_mastery_by_student_of_class(teacherkey)

    t = loader.get_template('Dashboard/teacher_mastery_by_student')
    c = Context({'mastery_by_student':mastery_by_student ,})
    return HttpResponse(t.render(c),content_type="text/xml")

def get_not_recently_loggedin_all(request):
    session = get_current_session()
    teacherkey = session.get('teacherkey',-1)
    notrecentlyloggedin = Query.get_students_not_logged_in_of_all_class(teacherkey)
    logging.error(notrecentlyloggedin)
    t = loader.get_template('Dashboard/not_recently_logged_in_byclass')
    c = Context({'notrecentlyloginall': notrecentlyloggedin,})
    return HttpResponse(t.render(c),content_type="text/xml")

def getaveragemasterybysubjectallclass(request):
    session = get_current_session()
    teacherkey = session.get('teacherkey',-1)
    averagemasterybysubject = Query.get_average_mastery_by_subject_of_all_class(teacherkey)
    logging.error(averagemasterybysubject)
    t = loader.get_template('Dashboard/not_recently_logged_in_byclass')
    c = Context({'averagemasterydict': averagemasterybysubject,})
    return HttpResponse(t.render(c),content_type="text/xml")
