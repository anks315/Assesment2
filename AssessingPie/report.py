__author__ = 'ankur'

import Query
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext,loader,Context
import logging

def get_reports_of_students(request):
    assessmentreport = Query.get_assessment_report()
    logging.error(assessmentreport)
    return render_to_response('AssessingPie_toBeremoved/reort_newera.html',{'rows':assessmentreport,},context_instance = RequestContext(request))


