from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Assesment.views.home', name='home'),
    # url(r'^Assesment/', include('Assesment.foo.urls')),
    (r'^assessment$', 'AssessingPie.views.asknextquestion'),
    (r'^inference/$', 'AssessingPie.views.inferquestion'),
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
     (r'^averagemasterybysubjectallclass/$', 'AssessingPie.teacher_dashboard_data.getaveragemasterybysujectallclass'),



    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

