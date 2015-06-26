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
            student_vivek=Query.addStudent("Ankit_Bhatia",ankit_user, school.key,'password')




            class_VA=Query.addClass(name="Class_V",school_key= school.key,section_details="A",year_session="2013-2014")  #to be changed
            class_VIB=Query.addClass(name="Class_VI",school_key= school.key,section_details="B",year_session="2013-2014")  #to be changed
            Query.assign_students_to_class(class_VA.key, [student_vivek.key])
            Query.assign_students_to_class(class_VA.key, [student_demo1.key,student_demo2.key,student_demo3.key,student_demo4.key,student_demo5.key,student_demo6.key,student_demo7.key,student_demo8.key,student_demo9.key,student_demo10.key,student_demo11.key,student_demo12.key,student_demo13.key,student_demo14.key,student_demo15.key,student_demo16.key,student_demo17.key,student_demo18.key,student_demo19.key,student_demo20.key,student_demo21.key,student_demo22.key,student_demo23.key,student_demo24.key,student_demo25.key,student_demo26.key,student_demo27.key,student_demo28.key,student_demo29.key,student_demo30.key])


            SUB_maths=Query.addSubject(Constant.Subject_Name.TYPE_CLASS, Constant.Subject_Name.SUB_MATHS,school.key,class_VA.key)
            a=Query.assign_subjects_to_class(class_VA.key, [SUB_maths.key])

            topic_fac_multiples=Query.addTopic(school_key=school.key,name="Factors and Multiples", prerequisite_topics=[],subject_key=SUB_maths.key,types=["6_3_FNM1","6_3_FNM2","6_3_FNM3"])
            #topic_prima_composite=Query.addTopic(school_key=school.key,name="Prime and Composite Number", prerequisite_topics=[],subject_key=SUB_maths.key,types=["6_3_PNC1","6_3_PNC2","6_3_PNC3","6_3_PNC4","6_3_PNC5","6_3_PNC6"])
            #topic_divisibility=Query.addTopic(school_key=school.key,name="Test for divisibility", prerequisite_topics=[topic_prima_composite.key],subject_key=SUB_maths.key,types=["6_3_CDN1","6_3_CDN2","6_3_CDN3","6_3_CDN4","6_3_CDN5","6_3_CDN6","6_3_CDN7","6_3_CDN8","6_3_CDN9"])
            #topic_common_factors=Query.addTopic(school_key=school.key,name="Common Factors and Multiples", prerequisite_topics=[],subject_key=SUB_maths.key,types=["6_3_CFCM1","6_3_CFCM2","6_3_CFCM3","6_3_CFCM4","6_3_CFCM5"])
            topic_prime_factor=Query.addTopic(school_key=school.key,name="Prime Factorization", prerequisite_topics=[topic_fac_multiples.key],subject_key=SUB_maths.key,types=["6_3_PF1","6_3_PF2"])
            topic_hcf=Query.addTopic(school_key=school.key,name="Highest Common Factor", prerequisite_topics=[topic_fac_multiples.key,topic_fac_multiples.key],subject_key=SUB_maths.key,types=["6_3_HCF1","6_3_HCF2","6_3_HCF3","6_3_HCF4"])
            topic_lcm=Query.addTopic(school_key=school.key,name="Lowest Common Factor", prerequisite_topics=[topic_fac_multiples.key,topic_fac_multiples.key],subject_key=SUB_maths.key,types=["6_3_LCM1","6_3_LCM2","6_3_LCM3","6_3_LCM4"])







            questioninstance_FNM11=Query.addQuestionInstance(problem_statement="Find the possible factors of 54 ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["1","2","3","4","6","9","27","54"],school_key=school.key,url="")

            question_FNM11=Query.addQuestion(questioninstance_FNM11,school.key)

            questioninstance_FNM12=Query.addQuestionInstance(problem_statement="Find the possible factors of 48 ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["1","2","3","4","6","8","12","24","48"],school_key=school.key,url="")
            question_FNM12=Query.addQuestion(questioninstance_FNM12,school.key)
            questioninstance_FNM21=Query.addQuestionInstance(problem_statement="Find all the multiples of 9 upto 100?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["9","18","27","36","45","54","63","72","81","90","99"],school_key=school.key,url="")
            question_FNM21=Query.addQuestion(questioninstance_FNM21,school.key)


            questioninstance_FNM22=Query.addQuestionInstance(problem_statement="Find all the multiples of 8 upto 100?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["8","16","24","32","40","48","56","64","72","80","88","96"],school_key=school.key,url="")

            questioninstance_FNM31=Query.addQuestionInstance(problem_statement="Is the statement True or False : Number of factors of a given number are finite?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["true"],school_key=school.key,url="")

            question_FNM31=Query.addQuestion(questioninstance_FNM31,school.key)

            questioninstance_PNC11=Query.addQuestionInstance(problem_statement="Find whether 11  is Prime or not?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["yes"],school_key=school.key,url="")
            question_PNC11=Query.addQuestion(questioninstance_PNC11,school.key)

            questioninstance_PNC21=Query.addQuestionInstance(problem_statement="Find whether 8 is Composite or not?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["yes"],school_key=school.key,url="")
            question_PNC21=Query.addQuestion(questioninstance_PNC21,school.key)


            questioninstance_PNC31=Query.addQuestionInstance(problem_statement="Write Prime numbers less than 32.", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["1","2","3","5","7","11","13","17","23","29","31"],school_key=school.key,url="")
            question_PNC31=Query.addQuestion(questioninstance_PNC31,school.key)

            questioninstance_PNC41=Query.addQuestionInstance(problem_statement="Find whether 1226 is Even or not?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["yes"],school_key=school.key,url="")
            question_PNC41=Query.addQuestion(questioninstance_PNC41,school.key)

            questioninstance_PNC51=Query.addQuestionInstance(problem_statement="Find whether 1229 is Odd or not?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["yes"],school_key=school.key,url="")
            question_PNC51=Query.addQuestion(questioninstance_PNC51,school.key)

            questioninstance_PNC61=Query.addQuestionInstance(problem_statement="Express the following as the sum of two odd primes: 44.", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["13","31"],school_key=school.key,url="")
            question_PNC61=Query.addQuestion(questioninstance_PNC61,school.key)

            questioninstance_CDN11=Query.addQuestionInstance(problem_statement="Using divisibility tests, determine  which of the following numbers are divisible by 10:15,20,25,30", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["30"],school_key=school.key)
            question_CDN11=Query.addQuestion(questioninstance_CDN11,school.key)

            questioninstance_CDN21=Query.addQuestionInstance(problem_statement="Using divisibility tests, determine  which of the following numbers are divisible by 5: 36,12,16,25,13", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["25"],school_key=school.key)
            question_CDN21=Query.addQuestion(questioninstance_CDN21,school.key)

            questioninstance_CDN31=Query.addQuestionInstance(problem_statement="Using divisibility tests, determine  which of the following numbers are divisible by 2 : 100001, 99985, 9994,10876", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["9994"],school_key=school.key)
            question_CDN31=Query.addQuestion(questioninstance_CDN31,school.key)

            questioninstance_CDN41=Query.addQuestionInstance(problem_statement="Using divisibility tests, determine  which of the following  numbers are divisible by 3 : 224,2198,219,342,389", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["219","342"],school_key=school.key)
            question_CDN41=Query.addQuestion(questioninstance_CDN41,school.key)

            questioninstance_CDN51=Query.addQuestionInstance(problem_statement="Using divisibility tests, determine  which of the following numbers are divisible by 6: 3861,1278,4352,5531", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["1278"],school_key=school.key)
            question_CDN51=Query.addQuestion(questioninstance_CDN51,school.key)

            questioninstance_CDN61=Query.addQuestionInstance(problem_statement="Using divisibility tests, determine  which of the following numbers are divisible by 4 : 1724,1434,56734,8764", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["1724","8764"],school_key=school.key)
            question_CDN61=Query.addQuestion(questioninstance_CDN61,school.key)

            questioninstance_CDN71=Query.addQuestionInstance(problem_statement="Using divisibility tests, determine  which of the following numbers are divisible by 8 : 17528, 3446, 32654,3448", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["17528","3448"],school_key=school.key)
            question_CDN71=Query.addQuestion(questioninstance_CDN71,school.key)

            questioninstance_CDN81=Query.addQuestionInstance(problem_statement="Using divisibility tests, determine  which of the following numbers are divisible by 9 : 100001, 99985, 9994,10876", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["9994"],school_key=school.key)
            question_CDN81=Query.addQuestion(questioninstance_CDN81,school.key)

            questioninstance_CDN91=Query.addQuestionInstance(problem_statement="Using divisibility tests, determine  which of the following numbers are divisible by 11 : 5445, 10824, 7138965", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["5445","7138965"],school_key=school.key)
            question_CDN91=Query.addQuestion(questioninstance_CDN91,school.key)

            questioninstance_CFCM11=Query.addQuestionInstance(problem_statement=" Find the common factors of  20 and 28.", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["1","2","4"],school_key=school.key)
            question_CFCM11=Query.addQuestion(questioninstance_CFCM11,school.key)

            questioninstance_CFCM21=Query.addQuestionInstance(problem_statement="Find the common factors of  35 ,50 and 55", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["1","5"],school_key=school.key)
            question_CFCM21=Query.addQuestion(questioninstance_CFCM21,school.key)

            questioninstance_CFCM31=Query.addQuestionInstance(problem_statement="Find the Common factors of 12 and 13.", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["1"],school_key=school.key)
            question_CFCM31=Query.addQuestion(questioninstance_CFCM31,school.key)

            questioninstance_CFCM41=Query.addQuestionInstance(problem_statement="Find atleast 3 common multiples of  4 and 6", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["12","24","36"],school_key=school.key)
            question_CFCM41=Query.addQuestion(questioninstance_CFCM41,school.key)

            questioninstance_CFCM51=Query.addQuestionInstance(problem_statement="Find atleast 2 common multiples of 3,5 and 6", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["30","60"],school_key=school.key)
            question_CFCM51=Query.addQuestion(questioninstance_CFCM51,school.key)

            questioninstance_PF11=Query.addQuestionInstance(problem_statement="Find the prime factorisation of 980", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["2","2","5","7","7"],school_key=school.key)
            question_PF11=Query.addQuestion(questioninstance_PF11,school.key)

            questioninstance_PF21=Query.addQuestionInstance(problem_statement="Complete the factor tree of 36 :2*2*_*3", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["3"],school_key=school.key)
            question_PF21=Query.addQuestion(questioninstance_PF21,school.key)

            questioninstance_HCF11=Query.addQuestionInstance(problem_statement="Find the HCF of  12 and 36", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["12"],school_key=school.key)
            question_HCF11=Query.addQuestion(questioninstance_HCF11,school.key)

            questioninstance_HCF21=Query.addQuestionInstance(problem_statement="Find the HCF of  15,25 and 30", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["5"],school_key=school.key)
            question_HCF21=Query.addQuestion(questioninstance_HCF21,school.key)

            questioninstance_HCF31=Query.addQuestionInstance(problem_statement="Find the HCF of  20,28 and 36", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["4"],school_key=school.key)
            question_HCF31=Query.addQuestion(questioninstance_HCF31,school.key)

            questioninstance_HCF41=Query.addQuestionInstance(problem_statement="Find the HCF of  12 and 36", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["2","2","5","7","7"],school_key=school.key)
            question_HCF41=Query.addQuestion(questioninstance_HCF41,school.key)


            questioninstance_LCM11=Query.addQuestionInstance(problem_statement="Find the LCM of  12 and 18", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["36"],school_key=school.key,url="")
            question_LCM11=Query.addQuestion(questioninstance_LCM11,school.key)

            questioninstance_LCM21=Query.addQuestionInstance(problem_statement="Find the LCM of  40,48 and 45", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["720"],school_key=school.key,url="")
            question_LCM21=Query.addQuestion(questioninstance_LCM21,school.key)

            questioninstance_LCM31=Query.addQuestionInstance(problem_statement="Find the LCM of  12,16,24 and 36", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["144"],school_key=school.key,url="")
            question_LCM31=Query.addQuestion(questioninstance_LCM31,school.key)

            questioninstance_LCM41=Query.addQuestionInstance(problem_statement="Find the prime factorisation of 980", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["2","2","5","7","7"],school_key=school.key,url="")
            question_LCM41=Query.addQuestion(questioninstance_LCM41,school.key)






            Query.assign_questions_to_topic(topic_fac_multiples.key,[question_FNM11.key],school.key,"6_3_FNM1")
            Query.assign_questions_to_topic(topic_fac_multiples.key,[question_FNM21.key],school.key,"6_3_FNM2")
            Query.assign_questions_to_topic(topic_fac_multiples.key,[question_FNM31.key],school.key,"6_3_FNM3")
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
            Query.assign_questions_to_topic(topic_common_factors.key,[question_CFCM51.key],school.key,"6_3_CFCM5")
            '''
            Query.assign_questions_to_topic(topic_prime_factor.key,[question_PF11.key],school.key,"6_3_PF1")
            Query.assign_questions_to_topic(topic_prime_factor.key,[question_PF21.key],school.key,"6_3_PF2")
            Query.assign_questions_to_topic(topic_hcf.key,[question_HCF11.key],school.key,"6_3_HCF1")
            Query.assign_questions_to_topic(topic_hcf.key,[question_HCF21.key],school.key,"6_3_HCF2")
            Query.assign_questions_to_topic(topic_hcf.key,[question_HCF31.key],school.key,"6_3_HCF3")
            Query.assign_questions_to_topic(topic_hcf.key,[question_HCF41.key],school.key,"6_3_HCF4")
            Query.assign_questions_to_topic(topic_lcm.key,[question_LCM11.key],school.key,"6_3_LCM1")
            Query.assign_questions_to_topic(topic_lcm.key,[question_LCM21.key],school.key,"6_3_LCM2")
            Query.assign_questions_to_topic(topic_lcm.key,[question_LCM31.key],school.key,"6_3_LCM3")
            Query.assign_questions_to_topic(topic_lcm.key,[question_LCM41.key],school.key,"6_3_LCM4")


            Query.map_state_to_topic_type(topic_fac_multiples.key, {1:["6_3_FNM1"],2:["6_3_FNM2"],3:["6_3_FNM3"],4:["6_3_FNM1","6_3_FNM2"],5:["6_3_FNM1","6_3_FNM3"],6:["6_3_FNM2","6_3_FNM3"],7:["6_3_FNM1","6_3_FNM2","6_3_FNM3"]},school.key)
            Query.map_state_to_topic_type(topic_prime_factor.key, {1:["6_3_PF1"],2:["6_3_PF1","6_3_PF2"],},school.key)
            Query.map_state_to_topic_type(topic_hcf.key, {1:["6_3_HCF1"],2:["6_3_HCF1","6_3_HCF2"],3:["6_3_HCF1","6_3_HCF2","6_3_HCF3"],4:["6_3_HCF1","6_3_HCF2","6_3_HCF3","6_3_HCF4"]},school.key)
            Query.map_state_to_topic_type(topic_lcm.key, {1:["6_3_LCM1"],2:["6_3_LCM1","6_3_LCM2"],3:["6_3_LCM1","6_3_LCM2","6_3_LCM3"],4:["6_3_LCM1","6_3_LCM2","6_3_LCM3","6_3_LCM4"]},school.key)

            #Query.assign_states_to_topic(topic_chap_one.key,[state_chapone_one.key,state_chapone_two.key,state_chapone_six.key,state_chapone_eight.key],school.key)
            assessment3=Query.addAssessment(name="Maths :1",list_topic_key=[topic_fac_multiples.key,topic_prime_factor.key,topic_hcf.key,topic_lcm.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime(int(2014),int(11),int(12),int(23),int(12),int(8)),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            assessment4=Query.addAssessment(name="Maths :2",list_topic_key=[topic_prime_factor.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime(int(2014),int(11),int(12),int(23),int(12),int(8)),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            assessment5=Query.addAssessment(name="Maths :3",list_topic_key=[topic_prime_factor.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime(int(2014),int(11),int(12),int(23),int(12),int(8)),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            assessment6=Query.addAssessment(name="Maths :4",list_topic_key=[topic_hcf.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime(int(2014),int(11),int(12),int(23),int(12),int(8)),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)

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
    ndb.delete
    _multi(Student_Assessments.query().fetch(keys_only=True))
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
