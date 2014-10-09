from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext,loader,Context
import Query
import Constant
from gaesessions import get_current_session
import logging
from google.appengine.ext import ndb

def getallschools(request):

        schooldict = Query.get_all_schools()
        t = loader.get_template('Dashboard/getallschools.xml')
        c = Context({'schooldict': schooldict})
        return HttpResponse(t.render(c),
        content_type="text/xml")


def getclassesofschool(request):

        key = request.GET['schoolkey']
        schoolkey = ndb.Key(urlsafe=key)
        classdict = Query.get_class_of_school(schoolkey)
        t = loader.get_template('Dashboard/getclassesofschool.xml')
        c = Context({'classdict': classdict})
        return HttpResponse(t.render(c),
        content_type="text/xml")

def getsubjectsofclass(request):

        key = request.GET['classkey']
        classkey = ndb.Key(urlsafe=key)
        subjectdict = Query.get_subject_details_of_class(classkey)
        t = loader.get_template('Dashboard/getsubjectsofclass.xml')
        c = Context({'subjectdict': subjectdict})
        return HttpResponse(t.render(c),
        content_type="text/xml")

def gettopicsofsubject(request):

        key = request.GET['subjectkey']
        subjectkey = ndb.Key(urlsafe=key)
        topicdict = Query.get_topic_details_by_subject(subjectkey)
        t = loader.get_template('Dashboard/gettopicsofsubject.xml')
        c = Context({'topicdict': topicdict})
        return HttpResponse(t.render(c),
        content_type="text/xml")
