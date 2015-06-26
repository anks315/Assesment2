from django.shortcuts import render_to_response
from oauth2client.appengine import AppAssertionCredentials
import httplib2
from django.template import RequestContext
from apiclient.discovery import build
import logging


API_KEY  = 'AIzaSyCpB2q4SwpockE1E94Pd0Eg_gN2G1P_m0s';

PROJECT_NUMBER = '607173849540'






def index(request):

   credentials = AppAssertionCredentials(
              scope='https://www.googleapis.com/auth/bigquery')
   http = credentials.authorize(httplib2.Http())
   bigquery_service = build('bigquery', 'v2', http=http)
   query_request = bigquery_service.jobs()
   query_data = {'query':'SELECT *  FROM [maveriks_assessment_sprint_1.test_new]'}
   query_response = query_request.query(projectId=PROJECT_NUMBER,
                                         body=query_data).execute()
   return render_to_response('AssessingPie_toBeremoved/testmeveriks.html',{'result':query_response['rows']},context_instance = RequestContext(request))




"""

"""


def bmispeedrelationships(request):
    credentials = AppAssertionCredentials(
              scope='https://www.googleapis.com/auth/bigquery')
    http = credentials.authorize(httplib2.Http())

    bigquery_service = build('bigquery', 'v2', http=http,developerKey=API_KEY)
    query_request = bigquery_service.jobs()
    query_data = {'query':'SELECT bmi, sprint_speed FROM [maveriks_assessment_sprint_1.test_new] ORDER BY bmi'}

    query_response = query_request.query(projectId=PROJECT_NUMBER,

                                         body=query_data).execute()





    return render_to_response('AssessingPie_toBeremoved/testmeveriks_bmi_sprint_speed.html',{'result':query_response['rows']},context_instance = RequestContext(request))



