from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Assesment.views.home', name='home'),
    # url(r'^Assesment/', include('Assesment.foo.urls')),
    (r'^getcourseinformation$', 'AssessingPie.student_dashboard_data.getcourseinformation'),
    (r'^testreport$', 'AssessingPie.views.testreport'),
    (r'^signout/$', 'AssessingPie.views.signout'),
    (r'^subjectdetailsofstudent$', 'AssessingPie.student_dashboard_data.subjectdetailsofstudent'),
    (r'^getspecialcourselist$', 'AssessingPie.student_dashboard_data.getspecialcourses'),
    (r'^gettopicwisescoreofsubject$', 'AssessingPie.student_dashboard_data.gettopicwisescoreofsubject'),
    (r'^getreadytolearn_ofsubject$', 'AssessingPie.student_dashboard_data.getreadytolearnofsubject'),
    (r'^getmasteryofsubject$', 'AssessingPie.student_dashboard_data.getmasteryofsubject'),
     (r'^getgrowthofsubject$', 'AssessingPie.student_dashboard_data.getgrowthofsubject'),
    (r'^numberline/$', 'AssessingPie.views.numberline'),
    (r'^graph/$', 'AssessingPie.views.graph'),
    (r'^assessment$', 'AssessingPie.views.asknextquestion'),
    (r'^infer$', 'AssessingPie.views.infer'),
    (r'^getallschools$', 'AssessingPie.inferencelogin.getallschools'),
    (r'^getclassesofschool', 'AssessingPie.inferencelogin.getclassesofschool'),
    (r'^getsubjectsofclass', 'AssessingPie.inferencelogin.getsubjectsofclass'),
    (r'^gettopicsofsubject', 'AssessingPie.inferencelogin.gettopicsofsubject'),
    (r'^inference$', 'AssessingPie.views.inferquestion'),
    (r'^contact_us/$', 'AssessingPie.views.contactus'),
    (r'^topicnames/$', 'AssessingPie.views.topicnames'),
    (r'^assesstopicname/$', 'AssessingPie.views.assesstopicname'),
    (r'^dashboard/$', 'AssessingPie.views.dashboard'),
    url(r'^$', 'AssessingPie.views.home'),
    (r'^userdetails/$', 'AssessingPie.student_dashboard_data.userdetails'),
    (r'^masterybysubject/$', 'AssessingPie.student_dashboard_data.getmasterybysubject'),
    (r'^pendingassessmentbysubject/$', 'AssessingPie.student_dashboard_data.getpendingassessment'),
    (r'^growthbysubject/$', 'AssessingPie.student_dashboard_data.getgrowthforallsubject'),
     (r'^readytolearnbysubject/$', 'AssessingPie.student_dashboard_data.getreadytolearnbysubject'),
     (r'^learningprogress_by_date/$', 'AssessingPie.student_dashboard_data.getlearningprogressdatewise'),
     (r'^notrecentlyloggedin_by_class/$', 'AssessingPie.teacher_dashboard_data.get_not_recently_loggedin'),
     (r'^mastery_by_student_by_class/$', 'AssessingPie.teacher_dashboard_data.mastery_by_student_by_class'),
     (r'^notrecentlyloggedinall_by_teacher/$', 'AssessingPie.teacher_dashboard_data.get_not_recently_loggedin_all'),
     (r'^averagemasterybysubjectallclass/$', 'AssessingPie.teacher_dashboard_data.getaveragemasterybysubjectallclass'),
      (r'^getclassdetailsbyteacher/$', 'AssessingPie.teacher_dashboard_data.get_classes_of_teacher'),
        (r'^notloggedinbyclass$', 'AssessingPie.teacher_dashboard_data.get_students_not_logged_in_by_class'),
          (r'^averagemasterybysubjectbyclass$', 'AssessingPie.teacher_dashboard_data.getaveragemasterybysubjectallsubject'),
           (r'^assessmentcoveragebyclass$', 'AssessingPie.teacher_dashboard_data.get_assessment_coverage_of_class'),
            (r'^subjectsofclass$', 'AssessingPie.teacher_dashboard_data.get_subject_of_class'),
            (r'^readytolearnofsubject$', 'AssessingPie.teacher_dashboard_data.get_readytolearn_of_subject'),
            (r'^assessmentcoverageofsubject$', 'AssessingPie.teacher_dashboard_data.get_assessment_coverage_of_subject'),
            (r'^averagemasteryofsubject_topicwise$', 'AssessingPie.teacher_dashboard_data.get_averagemastery_of_subject_topicwise'),
            (r'^ques/$', 'AssessingPie.views.ques'),
            (r'^home_scan/$', 'AssessingPie.views.whatisscan'),
            (r'^login/$', 'AssessingPie.views.login'),
            (r'^meetexperts/$', 'AssessingPie.views.meetExperts'),
            (r'^vedicMaths/$', 'AssessingPie.views.vedicMaths'),
            (r'^xyz/$', 'AssessingPie.views.xyz'),







    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^test', include('gaeunit.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

