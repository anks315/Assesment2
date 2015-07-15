__author__ = 'ankur'
from google.appengine.ext import ndb
import Query
import logging
import datetime
import time

from Constant import Constant,UserType,Subject_Name
import Constant
from Query import addSubject, addTopic
from models import QuestionInstance,State_Questions,Topic_States,Question,State,Address,Teacher,Class,\
    Assessment_Record
from models import School,Student,UserInfo,Subject,Assessment,Student_Assessments
from  models import Topic_Questions,State_Questions,Topic_States,Subject_Topics,State_Types
from models import Topic,User,Subject

def fill():
    try:
            flush()
            address1=Query.addAddress(type=Constant.Constant.ADDRESS_TYPE_HOME,state="UP",city="Meerut",street="12")
            school=Query.addSchool("CVSchool", address1)
            time.sleep(15)
            vijay_user=Query.addUserInfo("Vijay","Mehta",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            teacher_vijay=Query.addTeacher("Vijay_Mehta",vijay_user, school.key,"password")

            ankit_user=Query.addUserInfo("Ankit","Bhatia",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user1=Query.addUserInfo("Demo","1",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user2=Query.addUserInfo("Demo","2",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user3=Query.addUserInfo("Demo","3",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user4=Query.addUserInfo("Demo","4",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user5=Query.addUserInfo("Demo","5",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user6=Query.addUserInfo("Demo","6",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user7=Query.addUserInfo("Demo","7",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user8=Query.addUserInfo("Demo","8",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user9=Query.addUserInfo("Demo","9",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user10=Query.addUserInfo("Demo","10",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user11=Query.addUserInfo("Demo","11",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user12=Query.addUserInfo("Demo","12",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user13=Query.addUserInfo("Demo","13",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user14=Query.addUserInfo("Demo","14",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user15=Query.addUserInfo("Demo","15",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user16=Query.addUserInfo("Demo","16",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user17=Query.addUserInfo("Demo","17",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user18=Query.addUserInfo("Demo","18",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user19=Query.addUserInfo("Demo","19",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user20=Query.addUserInfo("Demo","20",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user21=Query.addUserInfo("Demo","21",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user22=Query.addUserInfo("Demo","22",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user23=Query.addUserInfo("Demo","23",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user24=Query.addUserInfo("Demo","24",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user25=Query.addUserInfo("Demo","25",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user26=Query.addUserInfo("Demo","26",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user27=Query.addUserInfo("Demo","27",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user28=Query.addUserInfo("Demo","28",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user29=Query.addUserInfo("Demo","29",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user30=Query.addUserInfo("Demo","30",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user31=Query.addUserInfo("Demo","31",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user32=Query.addUserInfo("Demo","32",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user33=Query.addUserInfo("Demo","33",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user34=Query.addUserInfo("Demo","34",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user35=Query.addUserInfo("Demo","35",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user36=Query.addUserInfo("Demo","36",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user37=Query.addUserInfo("Demo","37",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user38=Query.addUserInfo("Demo","38",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user39=Query.addUserInfo("Demo","39",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user40=Query.addUserInfo("Demo","40",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user41=Query.addUserInfo("Demo","41",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user42=Query.addUserInfo("Demo","42",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user43=Query.addUserInfo("Demo","43",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user44=Query.addUserInfo("Demo","44",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user45=Query.addUserInfo("Demo","45",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user46=Query.addUserInfo("Demo","46",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user47=Query.addUserInfo("Demo","47",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user48=Query.addUserInfo("Demo","48",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user49=Query.addUserInfo("Demo","49",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user50=Query.addUserInfo("Demo","50",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user51=Query.addUserInfo("Demo","51",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user52=Query.addUserInfo("Demo","52",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user53=Query.addUserInfo("Demo","53",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user54=Query.addUserInfo("Demo","54",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user55=Query.addUserInfo("Demo","55",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user56=Query.addUserInfo("Demo","56",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user57=Query.addUserInfo("Demo","57",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user58=Query.addUserInfo("Demo","58",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user59=Query.addUserInfo("Demo","59",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user60=Query.addUserInfo("Demo","60",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user61=Query.addUserInfo("Demo","61",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user62=Query.addUserInfo("Demo","62",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user63=Query.addUserInfo("Demo","63",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user64=Query.addUserInfo("Demo","64",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user65=Query.addUserInfo("Demo","65",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user66=Query.addUserInfo("Demo","66",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user67=Query.addUserInfo("Demo","67",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user68=Query.addUserInfo("Demo","68",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user69=Query.addUserInfo("Demo","69",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user70=Query.addUserInfo("Demo","70",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user71=Query.addUserInfo("Demo","71",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user72=Query.addUserInfo("Demo","72",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user73=Query.addUserInfo("Demo","73",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user74=Query.addUserInfo("Demo","74",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user75=Query.addUserInfo("Demo","75",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user76=Query.addUserInfo("Demo","76",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user77=Query.addUserInfo("Demo","77",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user78=Query.addUserInfo("Demo","78",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user79=Query.addUserInfo("Demo","79",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user80=Query.addUserInfo("Demo","80",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user81=Query.addUserInfo("Demo","81",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user82=Query.addUserInfo("Demo","82",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user83=Query.addUserInfo("Demo","83",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user84=Query.addUserInfo("Demo","84",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user85=Query.addUserInfo("Demo","85",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user86=Query.addUserInfo("Demo","86",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user87=Query.addUserInfo("Demo","87",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user88=Query.addUserInfo("Demo","88",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user89=Query.addUserInfo("Demo","89",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user90=Query.addUserInfo("Demo","90",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user91=Query.addUserInfo("Demo","91",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user92=Query.addUserInfo("Demo","92",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user93=Query.addUserInfo("Demo","93",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user94=Query.addUserInfo("Demo","94",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user95=Query.addUserInfo("Demo","95",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user96=Query.addUserInfo("Demo","96",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user97=Query.addUserInfo("Demo","97",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user98=Query.addUserInfo("Demo","98",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user99=Query.addUserInfo("Demo","99",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            demo_user100=Query.addUserInfo("Demo","100",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)

            student_demo1=Query.addStudent("Demo_1",demo_user1, school.key,'demo_1')
            student_demo2=Query.addStudent("Demo_2",demo_user2, school.key,'demo_2')
            student_demo3=Query.addStudent("Demo_3",demo_user3, school.key,'demo_3')
            student_demo4=Query.addStudent("Demo_4",demo_user4, school.key,'demo_4')
            student_demo5=Query.addStudent("Demo_5",demo_user5, school.key,'demo_5')
            student_demo6=Query.addStudent("Demo_6",demo_user6, school.key,'demo_6')
            student_demo7=Query.addStudent("Demo_7",demo_user7, school.key,'demo_7')
            student_demo8=Query.addStudent("Demo_8",demo_user8, school.key,'demo_8')
            student_demo9=Query.addStudent("Demo_9",demo_user9, school.key,'demo_9')
            student_demo10=Query.addStudent("Demo_10",demo_user10, school.key,'demo_10')
            student_demo11=Query.addStudent("Demo_11",demo_user11, school.key,'demo_11')
            student_demo12=Query.addStudent("Demo_12",demo_user12, school.key,'demo_12')
            student_demo13=Query.addStudent("Demo_13",demo_user13, school.key,'demo_13')
            student_demo14=Query.addStudent("Demo_14",demo_user14, school.key,'demo_14')
            student_demo15=Query.addStudent("Demo_15",demo_user15, school.key,'demo_15')
            student_demo16=Query.addStudent("Demo_16",demo_user16, school.key,'demo_16')
            student_demo17=Query.addStudent("Demo_17",demo_user17, school.key,'demo_17')
            student_demo18=Query.addStudent("Demo_18",demo_user18, school.key,'demo_18')
            student_demo19=Query.addStudent("Demo_19",demo_user19, school.key,'demo_19')
            student_demo20=Query.addStudent("Demo_20",demo_user20, school.key,'demo_20')
            student_demo21=Query.addStudent("Demo_21",demo_user21, school.key,'demo_21')
            student_demo22=Query.addStudent("Demo_22",demo_user22, school.key,'demo_22')
            student_demo23=Query.addStudent("Demo_23",demo_user23, school.key,'demo_23')
            student_demo24=Query.addStudent("Demo_24",demo_user24, school.key,'demo_24')
            student_demo25=Query.addStudent("Demo_25",demo_user25, school.key,'demo_25')
            student_demo26=Query.addStudent("Demo_26",demo_user26, school.key,'demo_26')
            student_demo27=Query.addStudent("Demo_27",demo_user27, school.key,'demo_27')
            student_demo28=Query.addStudent("Demo_28",demo_user28, school.key,'demo_28')
            student_demo29=Query.addStudent("Demo_29",demo_user29, school.key,'demo_29')
            student_demo30=Query.addStudent("Demo_30",demo_user30, school.key,'demo_30')
            student_demo31=Query.addStudent("Demo_31",demo_user31, school.key,'demo_31')
            student_demo32=Query.addStudent("Demo_32",demo_user32, school.key,'demo_32')
            student_demo33=Query.addStudent("Demo_33",demo_user33, school.key,'demo_33')
            student_demo34=Query.addStudent("Demo_34",demo_user34, school.key,'demo_34')
            student_demo35=Query.addStudent("Demo_35",demo_user35, school.key,'demo_35')
            student_demo36=Query.addStudent("Demo_36",demo_user36, school.key,'demo_36')
            student_demo37=Query.addStudent("Demo_37",demo_user37, school.key,'demo_37')
            student_demo38=Query.addStudent("Demo_38",demo_user38, school.key,'demo_38')
            student_demo39=Query.addStudent("Demo_39",demo_user39, school.key,'demo_39')
            student_demo40=Query.addStudent("Demo_40",demo_user40, school.key,'demo_40')
            student_demo41=Query.addStudent("Demo_41",demo_user41, school.key,'demo_41')
            student_demo42=Query.addStudent("Demo_42",demo_user42, school.key,'demo_42')
            student_demo43=Query.addStudent("Demo_43",demo_user43, school.key,'demo_43')
            student_demo44=Query.addStudent("Demo_44",demo_user44, school.key,'demo_44')
            student_demo45=Query.addStudent("Demo_45",demo_user45, school.key,'demo_45')
            student_demo46=Query.addStudent("Demo_46",demo_user46, school.key,'demo_46')
            student_demo47=Query.addStudent("Demo_47",demo_user47, school.key,'demo_47')
            student_demo48=Query.addStudent("Demo_48",demo_user48, school.key,'demo_48')
            student_demo49=Query.addStudent("Demo_49",demo_user49, school.key,'demo_49')
            student_demo50=Query.addStudent("Demo_50",demo_user50, school.key,'demo_50')
            student_demo51=Query.addStudent("Demo_51",demo_user51, school.key,'demo_51')
            student_demo52=Query.addStudent("Demo_52",demo_user52, school.key,'demo_52')
            student_demo53=Query.addStudent("Demo_53",demo_user53, school.key,'demo_53')
            student_demo54=Query.addStudent("Demo_54",demo_user54, school.key,'demo_54')
            student_demo55=Query.addStudent("Demo_55",demo_user55, school.key,'demo_55')
            student_demo56=Query.addStudent("Demo_56",demo_user56, school.key,'demo_56')
            student_demo57=Query.addStudent("Demo_57",demo_user57, school.key,'demo_57')
            student_demo58=Query.addStudent("Demo_58",demo_user58, school.key,'demo_58')
            student_demo59=Query.addStudent("Demo_59",demo_user59, school.key,'demo_59')
            student_demo60=Query.addStudent("Demo_60",demo_user60, school.key,'demo_60')
            student_demo61=Query.addStudent("Demo_61",demo_user61, school.key,'demo_61')
            student_demo62=Query.addStudent("Demo_62",demo_user62, school.key,'demo_62')
            student_demo63=Query.addStudent("Demo_63",demo_user63, school.key,'demo_63')
            student_demo64=Query.addStudent("Demo_64",demo_user64, school.key,'demo_64')
            student_demo65=Query.addStudent("Demo_65",demo_user65, school.key,'demo_65')
            student_demo66=Query.addStudent("Demo_66",demo_user66, school.key,'demo_66')
            student_demo67=Query.addStudent("Demo_67",demo_user67, school.key,'demo_67')
            student_demo68=Query.addStudent("Demo_68",demo_user68, school.key,'demo_68')
            student_demo69=Query.addStudent("Demo_69",demo_user69, school.key,'demo_69')
            student_demo70=Query.addStudent("Demo_70",demo_user70, school.key,'demo_70')
            student_demo71=Query.addStudent("Demo_71",demo_user71, school.key,'demo_71')
            student_demo72=Query.addStudent("Demo_72",demo_user72, school.key,'demo_72')
            student_demo73=Query.addStudent("Demo_73",demo_user73, school.key,'demo_73')
            student_demo74=Query.addStudent("Demo_74",demo_user74, school.key,'demo_74')
            student_demo75=Query.addStudent("Demo_75",demo_user75, school.key,'demo_75')
            student_demo76=Query.addStudent("Demo_76",demo_user76, school.key,'demo_76')
            student_demo77=Query.addStudent("Demo_77",demo_user77, school.key,'demo_77')
            student_demo78=Query.addStudent("Demo_78",demo_user78, school.key,'demo_78')
            student_demo79=Query.addStudent("Demo_79",demo_user79, school.key,'demo_79')
            student_demo80=Query.addStudent("Demo_80",demo_user80, school.key,'demo_80')
            student_demo81=Query.addStudent("Demo_81",demo_user81, school.key,'demo_81')
            student_demo82=Query.addStudent("Demo_82",demo_user82, school.key,'demo_82')
            student_demo83=Query.addStudent("Demo_83",demo_user83, school.key,'demo_83')
            student_demo84=Query.addStudent("Demo_84",demo_user84, school.key,'demo_84')
            student_demo85=Query.addStudent("Demo_85",demo_user85, school.key,'demo_85')
            student_demo86=Query.addStudent("Demo_86",demo_user86, school.key,'demo_86')
            student_demo87=Query.addStudent("Demo_87",demo_user87, school.key,'demo_87')
            student_demo88=Query.addStudent("Demo_88",demo_user88, school.key,'demo_88')
            student_demo89=Query.addStudent("Demo_89",demo_user89, school.key,'demo_89')
            student_demo90=Query.addStudent("Demo_90",demo_user90, school.key,'demo_90')
            student_demo91=Query.addStudent("Demo_91",demo_user91, school.key,'demo_91')
            student_demo92=Query.addStudent("Demo_92",demo_user92, school.key,'demo_92')
            student_demo93=Query.addStudent("Demo_93",demo_user93, school.key,'demo_93')
            student_demo94=Query.addStudent("Demo_94",demo_user94, school.key,'demo_94')
            student_demo95=Query.addStudent("Demo_95",demo_user95, school.key,'demo_95')
            student_demo96=Query.addStudent("Demo_96",demo_user96, school.key,'demo_96')
            student_demo97=Query.addStudent("Demo_97",demo_user97, school.key,'demo_97')
            student_demo98=Query.addStudent("Demo_98",demo_user98, school.key,'demo_98')
            student_demo99=Query.addStudent("Demo_99",demo_user99, school.key,'demo_99')
            student_demo100=Query.addStudent("Demo_100",demo_user100, school.key,'demo_100')
            student_vivek=Query.addStudent("Ankit_Bhatia",ankit_user, school.key,'password')




            class_VA=Query.addClass(name="Class_V",school_key= school.key,section_details="A",year_session="2013-2014")  #to be changed
            class_VIB=Query.addClass(name="Class_VI",school_key= school.key,section_details="B",year_session="2013-2014")  #to be changed
            Query.assign_students_to_class(class_VA.key, [student_vivek.key])
            Query.assign_students_to_class(class_VA.key, [student_demo1.key,student_demo2.key,student_demo3.key,student_demo4.key,student_demo5.key,student_demo6.key,student_demo7.key,student_demo8.key,student_demo9.key,student_demo10.key,student_demo11.key,student_demo12.key,student_demo13.key,student_demo14.key,student_demo15.key,student_demo16.key,student_demo17.key,student_demo18.key,student_demo19.key,student_demo20.key,student_demo21.key,student_demo22.key,student_demo23.key,student_demo24.key,student_demo25.key,student_demo26.key,student_demo27.key,student_demo28.key,student_demo29.key,student_demo30.key,student_demo31.key,student_demo32.key,student_demo33.key,student_demo34.key,student_demo35.key,student_demo36.key,student_demo37.key,student_demo38.key,student_demo39.key,student_demo40.key,student_demo41.key,student_demo42.key,student_demo43.key,student_demo44.key,student_demo45.key,student_demo46.key,student_demo47.key,student_demo48.key,student_demo49.key,student_demo50.key,student_demo51.key,student_demo52.key,student_demo53.key,student_demo54.key,student_demo55.key,student_demo56.key,student_demo57.key,student_demo58.key,student_demo59.key,student_demo60.key,student_demo61.key,student_demo62.key,student_demo63.key,student_demo64.key,student_demo65.key,student_demo66.key,student_demo67.key,student_demo68.key,student_demo69.key,student_demo70.key,student_demo71.key,student_demo72.key,student_demo73.key,student_demo74.key,student_demo75.key,student_demo76.key,student_demo77.key,student_demo78.key,student_demo79.key,student_demo80.key,student_demo81.key,student_demo82.key,student_demo83.key,student_demo84.key,student_demo85.key,student_demo86.key,student_demo87.key,student_demo88.key,student_demo89.key,student_demo90.key,student_demo91.key,student_demo92.key,student_demo93.key,student_demo94.key,student_demo95.key,student_demo96.key,student_demo97.key,student_demo98.key,student_demo99.key,student_demo100.key])


            SUB_maths=Query.addSubject(Constant.Subject_Name.TYPE_CLASS, Constant.Subject_Name.SUB_MATHS,school.key,class_VA.key)
            a=Query.assign_subjects_to_class(class_VA.key, [SUB_maths.key])

            topic_addition=Query.addTopic(school_key=school.key,name="Addition", prerequisite_topics=[],subject_key=SUB_maths.key,types=["One digit addition with carry","Addition Without Carry","Addition with Carry","Addtion with Large numbers"])
            #topic_prima_composite=Query.addTopic(school_key=school.key,name="Prime and Composite Number", prerequisite_topics=[],subject_key=SUB_maths.key,types=["6_3_PNC1","6_3_PNC2","6_3_PNC3","6_3_PNC4","6_3_PNC5","6_3_PNC6"])
            #topic_divisibility=Query.addTopic(school_key=school.key,name="Test for divisibility", prerequisite_topics=[topic_prima_composite.key],subject_key=SUB_maths.key,types=["6_3_CDN1","6_3_CDN2","6_3_CDN3","6_3_CDN4","6_3_CDN5","6_3_CDN6","6_3_CDN7","6_3_CDN8","6_3_CDN9"])
            #topic_common_factors=Query.addTopic(school_key=school.key,name="Common Factors and Multiples", prerequisite_topics=[],subject_key=SUB_maths.key,types=["6_3_CFCM1","6_3_CFCM2","6_3_CFCM3","6_3_CFCM4","6_3_CFCM5"])
            topic_substaction=Query.addTopic(school_key=school.key,name="Substraction", prerequisite_topics=[],subject_key=SUB_maths.key,types=["Substraction of one digit number from two digit","Substraction without borrow","Substraction with borrow"])
            topic_multiplication=Query.addTopic(school_key=school.key,name="Multiplication", prerequisite_topics=[topic_addition.key,topic_substaction.key],subject_key=SUB_maths.key,types=["Multiplication of one digit number","Multiplication with 10,100","Multiplication without carry","Multiplication with carry"])
            topic_division=Query.addTopic(school_key=school.key,name="Division", prerequisite_topics=[topic_addition.key,topic_substaction.key,topic_multiplication.key],subject_key=SUB_maths.key,types=["Division without carry","Division with carry","Quotient and remainder","Word problem on quotient and remainder"])







            questioninstance_add11=Query.addQuestionInstance(problem_statement="Add 5 and 7.", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["12"],school_key=school.key,url="")

            question_add11=Query.addQuestion(questioninstance_add11,school.key)

            questioninstance_add12=Query.addQuestionInstance(problem_statement="Add 345 and 544.", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["889"],school_key=school.key,url="")
            question_add12=Query.addQuestion(questioninstance_add12,school.key)
            questioninstance_add13=Query.addQuestionInstance(problem_statement="Add 78 and 37", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["115"],school_key=school.key,url="")
            question_add13=Query.addQuestion(questioninstance_add13,school.key)
            questioninstance_add14=Query.addQuestionInstance(problem_statement="Add 7832 and 8937.", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["16769"],school_key=school.key,url="")
            question_add14=Query.addQuestion(questioninstance_add14,school.key)


            questioninstance_sub11=Query.addQuestionInstance(problem_statement="Subtract 6 from 19.", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["13"],school_key=school.key,url="")

            question_sub11=Query.addQuestion(questioninstance_sub11,school.key)

            questioninstance_sub12=Query.addQuestionInstance(problem_statement="Subtract 15 from 26", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["11"],school_key=school.key,url="")
            question_sub12=Query.addQuestion(questioninstance_sub12,school.key)
            questioninstance_sub13=Query.addQuestionInstance(problem_statement="Subtract 45 and 73", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["28"],school_key=school.key,url="")
            question_sub13=Query.addQuestion(questioninstance_sub13,school.key)




            questioninstance_mul11=Query.addQuestionInstance(problem_statement="Multiply 4 and 7.", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["28"],school_key=school.key,url="")

            question_mul11=Query.addQuestion(questioninstance_mul11,school.key)

            questioninstance_mul12=Query.addQuestionInstance(problem_statement="Multiply 6 by 1000", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["6000"],school_key=school.key,url="")
            question_mul12=Query.addQuestion(questioninstance_mul12,school.key)
            questioninstance_mul13=Query.addQuestionInstance(problem_statement="Multiply 132 by 3", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["396"],school_key=school.key,url="")
            question_mul13=Query.addQuestion(questioninstance_mul13,school.key)

            questioninstance_mul14=Query.addQuestionInstance(problem_statement="Multiply 45 by 38", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["1710"],school_key=school.key,url="")
            question_mul14=Query.addQuestion(questioninstance_mul14,school.key)


            questioninstance_div11=Query.addQuestionInstance(problem_statement="Divide 428 by 2.", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["214"],school_key=school.key,url="")

            question_div11=Query.addQuestion(questioninstance_div11,school.key)

            questioninstance_div12=Query.addQuestionInstance(problem_statement="Divide 476 by 4", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["119"],school_key=school.key,url="")
            question_div12=Query.addQuestion(questioninstance_div12,school.key)
            questioninstance_div13=Query.addQuestionInstance(problem_statement="Remainder when 341 is divided by 9", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["8"],school_key=school.key,url="")
            question_div13=Query.addQuestion(questioninstance_div13,school.key)

            questioninstance_div14=Query.addQuestionInstance(problem_statement="The cost of 23 icecreams is 276. Find the cost of 1 icecream.", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["12"],school_key=school.key,url="")
            question_div14=Query.addQuestion(questioninstance_div14,school.key)





            Query.assign_questions_to_topic(topic_addition.key,[question_add11.key],school.key,"One digit addition with carry")
            Query.assign_questions_to_topic(topic_addition.key,[question_add12.key],school.key,"Addition Without Carry")
            Query.assign_questions_to_topic(topic_addition.key,[question_add13.key],school.key,"Addition with Carry")
            Query.assign_questions_to_topic(topic_addition.key,[question_add14.key],school.key,"Addtion with Large numbers")

            Query.assign_questions_to_topic(topic_substaction.key,[question_sub11.key],school.key,"Substraction of one digit number from two digit")
            Query.assign_questions_to_topic(topic_substaction.key,[question_sub12.key],school.key,"Substraction without borrow")
            Query.assign_questions_to_topic(topic_substaction.key,[question_sub13.key],school.key,"Substraction with borrow")

            Query.assign_questions_to_topic(topic_multiplication.key,[question_mul11.key],school.key,"Multiplication of one digit number")
            Query.assign_questions_to_topic(topic_multiplication.key,[question_mul12.key],school.key,"Multiplication with 10,100")
            Query.assign_questions_to_topic(topic_multiplication.key,[question_mul13.key],school.key,"Multiplication without carry")

            Query.assign_questions_to_topic(topic_multiplication.key,[question_mul14.key],school.key,"Multiplication with carry")

            Query.assign_questions_to_topic(topic_division.key,[question_div11.key],school.key,"Division without carry")
            Query.assign_questions_to_topic(topic_division.key,[question_div12.key],school.key,"Division with carry")
            Query.assign_questions_to_topic(topic_division.key,[question_div13.key],school.key,"Quotient and remainder")
            Query.assign_questions_to_topic(topic_division.key,[question_div14.key],school.key,"Word problem on quotient and remainder")








            '''
            Query.assign_questions_to_topic(topic_prima_composite.key,[question_PNC11.key],school.key,"6_3_PNC1")
            Query.assign_questions_to_topic(topic_prima_composite.key,[question_PNC21.key],school.key,"6_3_PNC2")
            Query.assign_questions_to_topic(topic_prima_composite.key,[question_PNC31.key],school.key,"6_3_PNC3")
            Query.assign_questions_to_topic(topic_prima_composite.key,[question_PNC41.key],school.key,"6_3_PNC4")
            Query.assign_questions_to_topic(topic_prima_composite.key,[question_PNC51.key],school.key,"6_3_PNC5")
            Query.assign_questions_to_topic(topic_prima_composite.key,[question_PNC61.key],school.key,"6_3_PNC6")
            Query.assign_questions_to_topic(topic_divisibility.key,[question_CDN11.key],school.key,"6_3_CDN1")
            Query.assign_questions_to_topic(topic_divisibility.key,[question_CDN21.key],school.key,"6_3_CDN2")
            Query.assign_questions_to_topic(topic_divisibility.key,[question_CDN31.key],school.key,"6_3_CDN3")
            Query.assign_questions_to_topic(topic_divisibility.key,[question_CDN41.key],school.key,"6_3_CDN4")
            Query.assign_questions_to_topic(topic_divisibility.key,[question_CDN51.key],school.key,"6_3_CDN5")
            Query.assign_questions_to_topic(topic_divisibility.key,[question_CDN61.key],school.key,"6_3_CDN6")
            Query.assign_questions_to_topic(topic_divisibility.key,[question_CDN71.key],school.key,"6_3_CDN7")
            Query.assign_questions_to_topic(topic_divisibility.key,[question_CDN81.key],school.key,"6_3_CDN8")
            Query.assign_questions_to_topic(topic_divisibility.key,[question_CDN91.key],school.key,"6_3_CDN9")
            Query.assign_questions_to_topic(topic_common_factors.key,[question_CFCM11.key],school.key,"6_3_CFCM1")
            Query.assign_questions_to_topic(topic_common_factors.key,[question_CFCM21.key],school.key,"6_3_CFCM2")
            Query.assign_questions_to_topic(topic_common_factors.key,[question_CFCM31.key],school.key,"6_3_CFCM3")
            Query.assign_questions_to_topic(topic_common_factors.key,[question_CFCM41.key],school.key,"6_3_CFCM4")
            Query.(assign_questions_to_topictopic_common_factors.key,[question_CFCM51.key],school.key,"6_3_CFCM5")
            '''


            Query.map_state_to_topic_type(topic_addition.key, {1:["One digit addition with carry"],2:["One digit addition with carry","Addition Without Carry"],3:["One digit addition with carry","Addition Without Carry","Addition with Carry"],4:["One digit addition with carry","Addition Without Carry","Addition with Carry","Addtion with Large numbers"],},school.key)
            Query.map_state_to_topic_type(topic_substaction.key, {1:["Substraction without borrow"],2:["Substraction without borrow","Substraction of one digit number from two digit"],3:["Substraction without borrow","Substraction of one digit number from two digit","Substraction with borrow"]},school.key)
            Query.map_state_to_topic_type(topic_multiplication.key, {1:["Multiplication of one digit number"],2:["Multiplication of one digit number","Multiplication with 10,100"],3:["Multiplication of one digit number","Multiplication with 10,100","Multiplication without carry"],4:["Multiplication of one digit number","Multiplication with 10,100","Multiplication without carry","Multiplication with carry"]},school.key)
            Query.map_state_to_topic_type(topic_division.key, {1:["Division without carry"],2:["Division without carry","Division with carry"],3:["Division without carry","Division with carry","Quotient and remainder"],4:["Division without carry","Division with carry","Quotient and remainder","Word problem on quotient and remainder"]},school.key)

            #Query.assign_states_to_topic(topic_chap_one.key,[state_chapone_one.key,state_chapone_two.key,state_chapone_six.key,state_chapone_eight.key],school.key)
            assessment3=Query.addAssessment(name="Maths :1",list_topic_key=[topic_addition.key,topic_substaction.key,topic_multiplication.key,topic_division.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime(int(2014),int(11),int(12),int(23),int(12),int(8)),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)

            a=Query.get_global_subjects(school.key);
            a=Query.get_subject_details_by_student(student_vivek.key);
            return str(a)+str(a)


    except Exception :
            logging.exception("")
            return Constant.Constant.ERROR_OPERATION_FAIL



def flush():
    ndb.delete_multi(School.query().fetch(keys_only=True))
    ndb.delete_multi(QuestionInstance.query().fetch(keys_only=True))
    ndb.delete_multi(State_Questions.query().fetch(keys_only=True))
    ndb.delete_multi(Topic_States.query().fetch(keys_only=True))
    ndb.delete_multi(Question.query().fetch(keys_only=True))
    ndb.delete_multi(State.query().fetch(keys_only=True))
    ndb.delete_multi(Address.query().fetch(keys_only=True))
    ndb.delete_multi(Teacher.query().fetch(keys_only=True))
    ndb.delete_multi(Class.query().fetch(keys_only=True))
    ndb.delete_multi(Assessment_Record.query().fetch(keys_only=True))
    ndb.delete_multi(Student.query().fetch(keys_only=True))
    ndb.delete_multi(UserInfo.query().fetch(keys_only=True))
    ndb.delete_multi(Student_Assessments.query().fetch(keys_only=True))
    ndb.delete_multi(Assessment.query().fetch(keys_only=True))
    ndb.delete_multi(Subject.query().fetch(keys_only=True))
    ndb.delete_multi(Topic_Questions.query().fetch(keys_only=True))
    ndb.delete_multi(State_Questions.query().fetch(keys_only=True))
    ndb.delete_multi(Topic_States.query().fetch(keys_only=True))
    ndb.delete_multi(Subject_Topics.query().fetch(keys_only=True))
    ndb.delete_multi(Student_Assessments.query().fetch(keys_only=True))
    ndb.delete_multi(Topic.query().fetch(keys_only=True))
    ndb.delete_multi(User.query().fetch(keys_only=True))
    ndb.delete_multi(Assessment_Record.query().fetch(keys_only=True))
    ndb.delete_multi(State_Types.query().fetch(keys_only=True))
