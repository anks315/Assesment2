from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext,loader,Context
import Query
import Constant
from gaesessions import get_current_session


def get_not_recently_loggedin(request):
    session = get_current_session()
    teacher_information = Query.login('Vijay_Mehta','jkjk')
    teacher = teacher_information[1]
    session['teacher']= teacher
    notrecentlydict =Query.get_students_not_logged_in_by_class(session['teacher'].key)
    t = loader.get_template('Dashboard/not_recently_logged_in_byclass')
    c = Context({'notrecentlylogin':notrecentlydict,})
    return HttpResponse(t.render(c),content_type="text/xml")


def mastery_by_student_by_class(request):
    session = get_current_session()
    teacher_information = Query.login('Vijay_Mehta','jkjk')
    teacher = teacher_information[1]
    session['teacher']= teacher
    mastery_by_student = Query.get_mastery_by_student_of_class(session['teacher'].key)
    t = loader.get_template('Dashboard/teacher_mastery_by_student')
    c = Context({'mastery_by_student':mastery_by_student ,})
    return HttpResponse(t.render(c),content_type="text/xml")

