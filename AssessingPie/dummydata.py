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
            ankit_user=Query.addUserInfo("Ankit","Bhatia",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            kavya_user=Query.addUserInfo("Kavya","Singh",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "kavya@gmail.com", 7667654766)
            prajjwal_user=Query.addUserInfo("Prajjwal","Ojha",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "prajjwal@gmail.com", 87654766)
            shiv_user=Query.addUserInfo("Shiv","Sahay",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            
            
            sarthaj_user=Query.addUserInfo("Sarthak","Tiwari",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            mishika_user=Query.addUserInfo("Mishika","Singh",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "kavya@gmail.com", 7667654766)
            prasoon_user=Query.addUserInfo("Prasoon","Garg",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "prajjwal@gmail.com", 87654766)
            pravesh_user=Query.addUserInfo("Pravesh","Sahay",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
   
            
            
            vijay_user=Query.addUserInfo("Vijay","Mehta",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            sulabh_user=Query.addUserInfo("Sulabj","Jain",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            #userinfo7=Query.addUserInfo("Smriti","Arora",datetime.datetime.now(),Constant.SEX_FEMALE, address1, "8778", 654766)
            #userinfo8=Query.addUserInfo("Samarath","Tiwari",datetime.datetime.now(),Constant.SEX_FEMALE, address1, "8778", 654766)
            
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
            student_kavya=Query.addStudent("Kavya_Singh",kavya_user, school.key,'pwd')
            student_prajjwal=Query.addStudent("Prajjwal_Ojha",prajjwal_user, school.key,'pwd')
            student_shiv=Query.addStudent("Shiv_Sahay",shiv_user, school.key,'pwd')
            
            
            student_sarthak=Query.addStudent("Sarthak_Tiwari",sarthaj_user, school.key,'pwd')
            student_mishika=Query.addStudent("Mishika_Singh",mishika_user, school.key,'pwd')
            student_prasoon=Query.addStudent("Prasoon_Garg", prasoon_user,school.key,'pwd')
            student_pravesh=Query.addStudent("Pravesh_Sahay",pravesh_user, school.key,'pwd')
            #teacher1=Query.addTeacher("teacher1", userinfo1, school.key)
            
            
            
            class_VA=Query.addClass(name="Class_V",school_key= school.key,section_details="A",year_session="2013-2014")  #to be changed
            class_VIB=Query.addClass(name="Class_VI",school_key= school.key,section_details="B",year_session="2013-2014")  #to be changed
            
            
            
            
            Query.assign_students_to_class(class_VA.key, [student_vivek.key])
            Query.assign_students_to_class(class_VA.key, [student_demo1.key,student_demo2.key,student_demo3.key,student_demo4.key,student_demo5.key,student_demo6.key,student_demo7.key,student_demo8.key,student_demo9.key,student_demo10.key,student_demo11.key,student_demo12.key,student_demo13.key,student_demo14.key,student_demo15.key,student_demo16.key,student_demo17.key,student_demo18.key,student_demo19.key,student_demo20.key,student_demo21.key,student_demo22.key,student_demo23.key,student_demo24.key,student_demo25.key,student_demo26.key,student_demo27.key,student_demo28.key,student_demo29.key,student_demo30.key])
            Query.assign_students_to_class(class_VA.key, [student_sarthak.key,student_mishika.key,student_prasoon.key,student_pravesh.key])

            
            
            
            
            
            
            teacher_vijay=Query.addTeacher("Vijay_Mehta",vijay_user, school.key,"password")
            teacher_sulabh=Query.addTeacher("Sulabj_Jain" ,sulabh_user, school.key,"")
            
          
            
            
            a=Query.assign_classes_to_teacher(teacher_vijay.key,[class_VA.key])
            Query.assign_classes_to_teacher(teacher_vijay.key,[class_VA.key])
            
            
            
            SUB_maths=Query.addSubject(Constant.Subject_Name.TYPE_CLASS, Constant.Subject_Name.SUB_MATHS,school.key,class_VA.key)
            #subject2=Query.addSubject(Subject.TYPE_CLASS, Subject.SUB_SCIENCE,school.key,class1.key)
            SUB_english=Query.addSubject(Constant.Subject_Name.TYPE_CLASS, Constant.Subject_Name.SUB_ENGLISH,school.key,class_VA.key)
            SUB_vedic = Query.addSubject(Constant.Subject_Name.TYPE_GLOBAL, Constant.Subject_Name.SUB_VEDIC,school.key,class_VA.key)
            #subject4=Query.addSubject(Subject.TYPE_CLASS, Subject.SUB_GEOLOGY,school.key,class1.key)

            a=Query.assign_subjects_to_class(class_VA.key, [SUB_maths.key])
            a=Query.assign_subjects_to_class(class_VA.key, [SUB_english.key])
            a=Query.assign_subjects_to_class(class_VA.key, [SUB_vedic.key])
            
            
            Query.assign_subjects_to_teacher(teacher_vijay.key,[SUB_maths.key])
            a=Query.assign_subjects_to_teacher(teacher_vijay.key,[SUB_english.key])
            a=Query.assign_subjects_to_teacher(teacher_vijay.key,[SUB_vedic.key])

           
            ##Query.login("Suraj_Singh", "pwd")
            
            
            
            
            topic_fac_multiples=Query.addTopic(school_key=school.key,name="Factors and Multiples", prerequisite_topics=[],subject_key=SUB_maths.key,types=["6_3_FNM1","6_3_FNM2","6_3_FNM3"])
            topic_prima_composite=Query.addTopic(school_key=school.key,name="Prime and Composite Number", prerequisite_topics=[],subject_key=SUB_maths.key,types=["6_3_PNC1","6_3_PNC2","6_3_PNC3","6_3_PNC4","6_3_PNC5","6_3_PNC6"])
            topic_divisibility=Query.addTopic(school_key=school.key,name="Test for divisibility", prerequisite_topics=[topic_prima_composite.key],subject_key=SUB_maths.key,types=["6_3_CDN1","6_3_CDN2","6_3_CDN3","6_3_CDN4","6_3_CDN5","6_3_CDN6","6_3_CDN7","6_3_CDN8","6_3_CDN9"])
            topic_common_factors=Query.addTopic(school_key=school.key,name="Common Factors and Multiples", prerequisite_topics=[],subject_key=SUB_maths.key,types=["6_3_CFCM1","6_3_CFCM2","6_3_CFCM3","6_3_CFCM4","6_3_CFCM5"])
            topic_prime_factor=Query.addTopic(school_key=school.key,name="Prime Factorization", prerequisite_topics=[topic_fac_multiples.key],subject_key=SUB_maths.key,types=["6_3_PF1","6_3_PF2"])
            topic_hcf=Query.addTopic(school_key=school.key,name="Highest Common Factor", prerequisite_topics=[topic_fac_multiples.key,topic_common_factors.key],subject_key=SUB_maths.key,types=["6_3_HCF1","6_3_HCF2","6_3_HCF3","6_3_HCF4"])
            topic_lcm=Query.addTopic(school_key=school.key,name="Lowest Common Factor", prerequisite_topics=[topic_fac_multiples.key,topic_common_factors.key],subject_key=SUB_maths.key,types=["6_3_LCM1","6_3_LCM2","6_3_LCM3","6_3_LCM4"])

            
            
            
            topic_part=Query.addTopic(school_key=school.key,name="Part of Speech", prerequisite_topics=[],subject_key=SUB_english.key,types=["type1","type2","type3"])
            topic_tenses=Query.addTopic(school_key=school.key,name="Tenses", prerequisite_topics=[],subject_key=SUB_english.key,types=["type1","type2","type3"])
            topic_sentences=Query.addTopic(school_key=school.key,name="Sentences", prerequisite_topics=[topic_part.key],subject_key=SUB_english.key,types=["type1","type2","type3"])
            topic_voices=Query.addTopic(school_key=school.key,name="Voices", prerequisite_topics=[topic_sentences.key,topic_part.key],subject_key=SUB_english.key,types=["type1","type2","type3"])
            #topic5=Query.addTopic(school_key=school.key,name="Ellipse ", prerequisite_topics=[topic.key],subject_key=subject1.key)
            
            
            topic_chap_one=Query.addTopic(school_key=school.key,name="Basic Concept of Vedic Maths", prerequisite_topics=[],subject_key=SUB_vedic.key,types=["Base of A Number","Complement with zero in between","Complement with zero at end","Complement with decimal in between"])
            topic_chap_two=Query.addTopic(school_key=school.key,name="Subtraction at a Look", prerequisite_topics=[topic_chap_one.key],subject_key=SUB_vedic.key,types=["Subtraction from base","Subtraction from bigger base","Subtraction from multiple of base","Subtraction with same number of digit","General Subtraction"])
            topic_chap_three=Query.addTopic(school_key=school.key,name="Multiplication with 99999...", prerequisite_topics=[topic_chap_one.key],subject_key=SUB_vedic.key,types=["Multiplication of 999.. with same number of digit","Multiplication of 999.. with less number of digit","Multiplication of 999.. with greater number of digit"])
            topic_chap_four=Query.addTopic(school_key=school.key,name="Magic with 11", prerequisite_topics=[topic_chap_one.key],subject_key=SUB_vedic.key,types=["Multipyling with 11","Multiplying with 1111.."])
            topic_chap_five=Query.addTopic(school_key=school.key,name="Multiplying with 12(without using 12)", prerequisite_topics=[topic_chap_one.key],subject_key=SUB_vedic.key,types=["Multiply with 12","Multiply with 112","Multiply with 1112"])
            


            questioninstance_FNM11=Query.addQuestionInstance(problem_statement="Find the possible factors of 54 ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["1,2,3,4,6,9,27,54"],school_key=school.key,url="")
            question_FNM11=Query.addQuestion(questioninstance_FNM11,school.key)

            questioninstance_FNM12=Query.addQuestionInstance(problem_statement="Find the possible factors of 48 ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["1,2,3,4,6,8,12,24,48"],school_key=school.key,url="")
            questioninstance_FNM21=Query.addQuestionInstance(problem_statement="Find all the multiples of 9 upto 100?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["9,18,27,36,45,54,63,72,81,90,99"],school_key=school.key,url="")
            question_FNM21=Query.addQuestion(questioninstance_FNM21,school.key)


            questioninstance_FNM22=Query.addQuestionInstance(problem_statement="Find all the multiples of 8 upto 100?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["8,16,24,32,40,48,56,64,72,80,88,96"],school_key=school.key,url="")

            questioninstance_FNM31=Query.addQuestionInstance(problem_statement="Is the statement True or False : Number of factors of a given number are finite?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["true"],school_key=school.key,url="")

            question_FNM31=Query.addQuestion(questioninstance_FNM31,school.key)

            questioninstance_PNC11=Query.addQuestionInstance(problem_statement="Find whether 11  is Prime or not?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["yes"],school_key=school.key,url="")
            question_PNC11=Query.addQuestion(questioninstance_PNC11,school.key)

            questioninstance_PNC21=Query.addQuestionInstance(problem_statement="Find whether 8 is Composite or not?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["yes"],school_key=school.key,url="")
            question_PNC21=Query.addQuestion(questioninstance_PNC21,school.key)


            questioninstance_PNC31=Query.addQuestionInstance(problem_statement="Write Prime numbers less than 32.", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["1,2,3,5,7,11,13,17,23,29,31"],school_key=school.key,url="")
            question_PNC31=Query.addQuestion(questioninstance_PNC31,school.key)

            questioninstance_PNC41=Query.addQuestionInstance(problem_statement="Find whether 1226 is Even or not?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["yes"],school_key=school.key,url="")
            question_PNC41=Query.addQuestion(questioninstance_PNC41,school.key)

            questioninstance_PNC51=Query.addQuestionInstance(problem_statement="Find whether 1229 is Odd or not?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["yes"],school_key=school.key,url="")
            question_PNC51=Query.addQuestion(questioninstance_PNC51,school.key)

            questioninstance_PNC61=Query.addQuestionInstance(problem_statement="Express the following as the sum of two odd primes: 44.", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["13,31"],school_key=school.key,url="")
            question_PNC61=Query.addQuestion(questioninstance_PNC61,school.key)

            questioninstance_CDN11=Query.addQuestionInstance(problem_statement="Using divisibility tests, determine  which of the following numbers are divisible by 10:15,20,25,30", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["30"],school_key=school.key)
            question_CDN11=Query.addQuestion(questioninstance_CDN11,school.key)

            questioninstance_CDN21=Query.addQuestionInstance(problem_statement="Using divisibility tests, determine  which of the following numbers are divisible by 5: 36,12,16,25,13", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["25"],school_key=school.key)
            question_CDN21=Query.addQuestion(questioninstance_CDN21,school.key)

            questioninstance_CDN31=Query.addQuestionInstance(problem_statement="Using divisibility tests, determine  which of the following numbers are divisible by 2 : 100001, 99985, 9994,10876", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["9994"],school_key=school.key)
            question_CDN31=Query.addQuestion(questioninstance_CDN31,school.key)

            questioninstance_CDN41=Query.addQuestionInstance(problem_statement="Using divisibility tests, determine  which of the following  numbers are divisible by 3 : 224,2198,219,342,389", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["219,342"],school_key=school.key)
            question_CDN41=Query.addQuestion(questioninstance_CDN41,school.key)

            questioninstance_CDN51=Query.addQuestionInstance(problem_statement="Using divisibility tests, determine  which of the following numbers are divisible by 6: 3861,1278,4352,5531", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["1278"],school_key=school.key)
            question_CDN51=Query.addQuestion(questioninstance_CDN51,school.key)

            questioninstance_CDN61=Query.addQuestionInstance(problem_statement="Using divisibility tests, determine  which of the following numbers are divisible by 4 : 1724,1434,56734,8764", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["1724,8764"],school_key=school.key)
            question_CDN61=Query.addQuestion(questioninstance_CDN61,school.key)

            questioninstance_CDN71=Query.addQuestionInstance(problem_statement="Using divisibility tests, determine  which of the following numbers are divisible by 8 : 17528, 3446, 32654,3448", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["17528,3448"],school_key=school.key)
            question_CDN71=Query.addQuestion(questioninstance_CDN71,school.key)

            questioninstance_CDN81=Query.addQuestionInstance(problem_statement="Using divisibility tests, determine  which of the following numbers are divisible by 9 : 100001, 99985, 9994,10876", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["9994"],school_key=school.key)
            question_CDN81=Query.addQuestion(questioninstance_CDN81,school.key)

            questioninstance_CDN91=Query.addQuestionInstance(problem_statement="Using divisibility tests, determine  which of the following numbers are divisible by 11 : 5445, 10824, 7138965", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["5445,7138965"],school_key=school.key)
            question_CDN91=Query.addQuestion(questioninstance_CDN91,school.key)

            questioninstance_CFCM11=Query.addQuestionInstance(problem_statement=" Find the common factors of  20 and 28.", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["1,2,4"],school_key=school.key)
            question_CFCM11=Query.addQuestion(questioninstance_CFCM11,school.key)

            questioninstance_CFCM21=Query.addQuestionInstance(problem_statement="Find the common factors of  35 ,50 and 55", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["1,5"],school_key=school.key)
            question_CFCM21=Query.addQuestion(questioninstance_CFCM21,school.key)

            questioninstance_CFCM31=Query.addQuestionInstance(problem_statement="Find the Common factors of 12 and 13.", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["1"],school_key=school.key)
            question_CFCM31=Query.addQuestion(questioninstance_CFCM31,school.key)

            questioninstance_CFCM41=Query.addQuestionInstance(problem_statement="Find atleast 3 common multiples of  4 and 6", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["12,24,36"],school_key=school.key)
            question_CFCM41=Query.addQuestion(questioninstance_CFCM41,school.key)

            questioninstance_CFCM51=Query.addQuestionInstance(problem_statement="Find atleast 2 common multiples of 3,5 and 6", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["30,60"],school_key=school.key)
            question_CFCM51=Query.addQuestion(questioninstance_CFCM51,school.key)

            questioninstance_PF11=Query.addQuestionInstance(problem_statement="Find the prime factorisation of 980", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["2,2,5,7,7"],school_key=school.key)
            question_PF11=Query.addQuestion(questioninstance_PF11,school.key)

            questioninstance_PF21=Query.addQuestionInstance(problem_statement="Complete the factor tree of 36 :2*2*_*3", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["3"],school_key=school.key)
            question_PF21=Query.addQuestion(questioninstance_PF21,school.key)

            questioninstance_HCF11=Query.addQuestionInstance(problem_statement="Find the HCF of  12 and 36", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["12"],school_key=school.key)
            question_HCF11=Query.addQuestion(questioninstance_HCF11,school.key)

            questioninstance_HCF21=Query.addQuestionInstance(problem_statement="Find the HCF of  15,25 and 30", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["5"],school_key=school.key)
            question_HCF21=Query.addQuestion(questioninstance_HCF21,school.key)

            questioninstance_HCF31=Query.addQuestionInstance(problem_statement="Find the HCF of  20,28 and 36", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["4"],school_key=school.key)
            question_HCF31=Query.addQuestion(questioninstance_HCF31,school.key)

            questioninstance_HCF41=Query.addQuestionInstance(problem_statement="Find the HCF of  12 and 36", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["2,2,5,7,7"],school_key=school.key)
            question_HCF41=Query.addQuestion(questioninstance_HCF41,school.key)


            questioninstance_LCM11=Query.addQuestionInstance(problem_statement="Find the LCM of  12 and 18", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["36"],school_key=school.key,url="")
            question_LCM11=Query.addQuestion(questioninstance_LCM11,school.key)

            questioninstance_LCM21=Query.addQuestionInstance(problem_statement="Find the LCM of  40,48 and 45", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["720"],school_key=school.key,url="")
            question_LCM21=Query.addQuestion(questioninstance_LCM21,school.key)

            questioninstance_LCM31=Query.addQuestionInstance(problem_statement="Find the LCM of  12,16,24 and 36", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["144"],school_key=school.key,url="")
            question_LCM31=Query.addQuestion(questioninstance_LCM31,school.key)

            questioninstance_LCM41=Query.addQuestionInstance(problem_statement="Find the prime factorisation of 980", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["2,2,5,7,7"],school_key=school.key,url="")
            question_LCM41=Query.addQuestion(questioninstance_LCM41,school.key)



            questioninstance_number1=Query.addQuestionInstance(problem_statement="Sum of of 2 and 3 ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["5"],school_key=school.key)
            
            questioninstance_number2=Query.addQuestionInstance(problem_statement="Sum of 222+30  ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["252"],school_key=school.key)
            #questioninstance_number3=Query.addQuestionInstance(problem_statement="Which one is greatest ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["1902","1920","9201","9021","9210"], answers=["9210"],school_key=school.key)

            #questioninstance_number4=Query.addQuestionInstance(problem_statement="Which one is smallest ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["1902","1920","9201","9021","9210"], answers=["9210"],school_key=school.key)

            questioninstance_number3=Query.addQuestionInstance(problem_statement="quotient of 58 by 9", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["6"],school_key=school.key)


            questioninstance_base_one=Query.addQuestionInstance(problem_statement="Whether 2900 is base or not? y or n ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["n"],school_key=school.key,url="")
            questioninstance_complement_zeroinbetween = Query.addQuestionInstance(problem_statement="Find Complement of 3049 ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["6941"],school_key=school.key,url="")
            questioninstance_complement_zeroatend = Query.addQuestionInstance(problem_statement="Find Complement of 3420", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["6580"],school_key=school.key,url="")
            questioninstance_complement_decimalinbetween = Query.addQuestionInstance(problem_statement="Find Complement of 437.26", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["437.26"],school_key=school.key,url="")

            question_base_one=Query.addQuestion(questioninstance_base_one,school.key)
            question_complement_zeroinbetween=Query.addQuestion(questioninstance_complement_zeroinbetween,school.key)
            question_complement_zeroatend=Query.addQuestion(questioninstance_complement_zeroatend,school.key)
            question_complement_decimalinbetween=Query.addQuestion(questioninstance_complement_decimalinbetween,school.key)


            Query.assign_questions_to_topic(topic_fac_multiples.key,[question_FNM11.key],school.key,"6_3_FNM1")
            Query.assign_questions_to_topic(topic_fac_multiples.key,[question_FNM21.key],school.key,"6_3_FNM2")
            Query.assign_questions_to_topic(topic_fac_multiples.key,[question_FNM31.key],school.key,"6_3_FNM3")
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





            Query.assign_questions_to_topic(topic_chap_one.key,[question_complement_zeroinbetween.key],school.key,"Complement with zero in between")
            Query.assign_questions_to_topic(topic_chap_one.key,[question_complement_zeroatend.key],school.key,"Complement with zero at end")
            Query.assign_questions_to_topic(topic_chap_one.key,[question_complement_decimalinbetween.key],school.key,"Complement with decimal in between")
            '''
            state_chapone_one=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapone_two=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapone_three = Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapone_four = Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapone_five=  Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapone_six = Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapone_seven = Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapone_eight = Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            '''
         #   Query.assign_questions_to_state(state_chapone_one.key, [question_base_one.key],school.key)
          #  Query.assign_questions_to_state(state_chapone_two.key, [question_base_one.key,question_complement_zeroinbetween.key],school.key)
           # Query.assign_questions_to_state(state_chapone_three.key, [question_base_one.key,question_complement_decimalinbetween.key],school.key)
           # Query.assign_questions_to_state(state_chapone_four.key, [question_base_one.key,question_complement_zeroatend.key],school.key)
           # Query.assign_questions_to_state(state_chapone_five.key, [question_base_one.key,question_complement_zeroinbetween.key,question_complement_decimalinbetween.key],school.key)
           # Query.assign_questions_to_state(state_chapone_six.key, [question_base_one.key,question_complement_zeroinbetween.key,question_complement_zeroatend.key],school.key)
           # Query.assign_questions_to_state(state_chapone_seven.key, [question_base_one.key,question_complement_zeroatend.key,question_complement_decimalinbetween.key],school.key)
            #Query.assign_questions_to_state(state_chapone_eight.key, [question_base_one.key,question_complement_zeroatend.key,question_complement_decimalinbetween.key,question_complement_zeroinbetween.key],school.key)

            Query.map_state_to_topic_type(topic_chap_one.key, {1:["Base of A Number"],2:["Base of A Number","Complement with zero in between"],3:["Base of A Number","Complement with zero in between","Complement with zero at end"],4:["Base of A Number","Complement with zero in between","Complement with zero at end","Complement with decimal in between"]},school.key)


            Query.map_state_to_topic_type(topic_fac_multiples.key, {1:["6_3_FNM1"],2:["6_3_FNM2"],3:["6_3_FNM3"],4:["6_3_FNM1","6_3_FNM2"],5:["6_3_FNM1","6_3_FNM3"],6:["6_3_FNM2","6_3_FNM3"],7:["6_3_FNM1","6_3_FNM2","6_3_FNM3"]},school.key)
            Query.map_state_to_topic_type(topic_prime_factor.key, {1:["6_3_PF1"],2:["6_3_PF1","6_3_PF2"],},school.key)
            Query.map_state_to_topic_type(topic_hcf.key, {1:["6_3_HCF1"],2:["6_3_HCF1","6_3_HCF2"],3:["6_3_HCF1","6_3_HCF2","6_3_HCF3"],4:["6_3_HCF1","6_3_HCF2","6_3_HCF3","6_3_HCF4"]},school.key)
            Query.map_state_to_topic_type(topic_lcm.key, {1:["6_3_LCM1"],2:["6_3_LCM1","6_3_LCM2"],3:["6_3_LCM1","6_3_LCM2","6_3_LCM3"],4:["6_3_LCM1","6_3_LCM2","6_3_LCM3","6_3_LCM4"]},school.key)

            #Query.assign_states_to_topic(topic_chap_one.key,[state_chapone_one.key,state_chapone_two.key,state_chapone_six.key,state_chapone_eight.key],school.key)



            '''
            questioninstance_subtractionfrombase=Query.addQuestionInstance(problem_statement="10000-3246=? ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["6754"],school_key=school.key,url="")
            questioninstance_subtractionfrombiggerbase=Query.addQuestionInstance(problem_statement="10000-23=? ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["9977"],school_key=school.key,url="")
            questioninstance_subtractionfrommultipleofbase=Query.addQuestionInstance(problem_statement="5000-248=? ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["752"],school_key=school.key,url="")
            questioninstance_subtractionsamenumberofdigit=Query.addQuestionInstance(problem_statement="9000-5246=? ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["3754"],school_key=school.key,url="")
            questioninstance_general_subtraction=Query.addQuestionInstance(problem_statement="96247-28519=? ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["67728"],school_key=school.key,url="")

            question_subtractionfrombase=Query.addQuestion(questioninstance_subtractionfrombase,school.key)
            question_subtractionfrombiggerbase=Query.addQuestion(questioninstance_subtractionfrombiggerbase,school.key)
            question_subtractionfrommultipleofbase=Query.addQuestion(questioninstance_subtractionfrommultipleofbase,school.key)
            question_subtractionsamenumberofdigit=Query.addQuestion(questioninstance_subtractionsamenumberofdigit,school.key)
            question_general_subtraction=Query.addQuestion(questioninstance_general_subtraction,school.key)


            Query.assign_questions_to_topic(topic_chap_two.key,[question_subtractionfrombase.key,question_subtractionfrombiggerbase.key,question_subtractionfrommultipleofbase.key,question_subtractionsamenumberofdigit.key,question_general_subtraction.key],school.key,"type1")

            state_chaptwo_one=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chaptwo_two=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chaptwo_three=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chaptwo_four=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chaptwo_five=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chaptwo_six=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chaptwo_seven=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chaptwo_eight=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chaptwo_nine=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)



            Query.assign_questions_to_state(state_chaptwo_one.key, [question_subtractionfrombase.key],school.key)
            Query.assign_questions_to_state(state_chaptwo_two.key, [question_general_subtraction.key],school.key)
            Query.assign_questions_to_state(state_chaptwo_three.key, [question_subtractionfrombase.key,question_general_subtraction.key],school.key)
            Query.assign_questions_to_state(state_chaptwo_four.key, [question_subtractionfrombase.key,question_subtractionfrombiggerbase.key],school.key)
            Query.assign_questions_to_state(state_chaptwo_five.key, [question_subtractionfrombase.key,question_subtractionfrombiggerbase.key,question_subtractionfrommultipleofbase.key],school.key)
            Query.assign_questions_to_state(state_chaptwo_six.key, [question_subtractionfrombase.key,question_subtractionfrombiggerbase.key,question_subtractionfrommultipleofbase.key,question_subtractionsamenumberofdigit.key],school.key)
            Query.assign_questions_to_state(state_
            chaptwo_seven.key, [question_subtractionfrombase.key,question_general_subtraction.key,question_subtractionfrombiggerbase.key],school.key)
            Query.assign_questions_to_state(state_chaptwo_eight.key, [question_subtractionfrombase.key,question_general_subtraction.key,question_subtractionfrombiggerbase.key,question_subtractionfrommultipleofbase.key],school.key)
            Query.assign_questions_to_state(state_chaptwo_nine.key, [question_subtractionfrombase.key,question_general_subtraction.key,question_subtractionfrombiggerbase.key,question_subtractionsamenumberofdigit.key,question_subtractionfrommultipleofbase.key],school.key)


            Query.assign_states_to_topic(topic_chap_two.key, [state_chaptwo_one.key,state_chaptwo_two.key,state_chaptwo_three.key,state_chaptwo_four.key,state_chaptwo_five.key,state_chaptwo_six.key,state_chaptwo_seven.key,state_chaptwo_eight.key,state_chaptwo_nine.key],school.key)




            questioninstance_multiplication999=Query.addQuestionInstance(problem_statement="389 * 999=?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["388611"],school_key=school.key,url="")
            questioninstance_multiplication999less=Query.addQuestionInstance(problem_statement="243 * 9999=?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["2429757"],school_key=school.key,url="")
            questioninstance_multiplication999greater=Query.addQuestionInstance(problem_statement="7428 * 99=?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["735372"],school_key=school.key,url="")

            question_multiplication999=Query.addQuestion(questioninstance_multiplication999,school.key)
            question_multiplication999less=Query.addQuestion(questioninstance_multiplication999less,school.key)
            question_multiplication999greater=Query.addQuestion(questioninstance_multiplication999greater,school.key)

            Query.assign_questions_to_topic(topic_chap_three.key,[question_multiplication999.key,question_multiplication999less.key,question_multiplication999greater.key],school.key,"type1")

            state_chapthree_one=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapthree_two=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapthree_three=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)


            Query.assign_questions_to_state(state_chapthree_one.key, [question_multiplication999.key],school.key)
            Query.assign_questions_to_state(state_chapthree_two.key, [question_multiplication999.key,question_multiplication999less.key],school.key)
            Query.assign_questions_to_state(state_chapthree_three.key, [question_multiplication999.key,question_multiplication999less.key,question_multiplication999greater.key],school.key)

            Query.assign_states_to_topic(topic_chap_three.key, [state_chapthree_one.key,state_chapthree_two.key,state_chapthree_three.key],school.key)



            questioninstance_magicwith11=Query.addQuestionInstance(problem_statement="4573 * 11=?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["50303"],school_key=school.key,url="")
            questioninstance_magicwith1111=Query.addQuestionInstance(problem_statement="2473 * 1111=?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["2747503"],school_key=school.key,url="")

            question_magicwith11=Query.addQuestion(questioninstance_magicwith11,school.key)
            question_magicwith1111=Query.addQuestion(questioninstance_magicwith1111,school.key)


            Query.assign_questions_to_topic(topic_chap_four.key,[question_magicwith11.key,question_magicwith1111.key],school.key,"type1")

            state_chapfour_one=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapfour_two=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)

            Query.assign_questions_to_state(state_chapfour_one.key, [question_magicwith11.key],school.key)
            Query.assign_questions_to_state(state_chapfour_two.key, [question_magicwith11.key,question_magicwith1111.key],school.key)

            Query.assign_states_to_topic(topic_chap_four.key, [state_chapfour_one.key,state_chapfour_two.key],school.key)



            questioninstance_multiplywith12=Query.addQuestionInstance(problem_statement="3785 * 12=?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["45420"],school_key=school.key,url="")
            questioninstance_multiplywith112=Query.addQuestionInstance(problem_statement="432 * 112=?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["48384"],school_key=school.key,url="")
            questioninstance_multiplywith1112=Query.addQuestionInstance(problem_statement="5321 * 1112=?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["5916952"],school_key=school.key,url="")


            question_multiplywith12=Query.addQuestion(questioninstance_multiplywith12,school.key)
            question_multiplywith112=Query.addQuestion(questioninstance_multiplywith112,school.key)
            question_multiplywith1112=Query.addQuestion(questioninstance_multiplywith1112,school.key)

            Query.assign_questions_to_topic(topic_chap_five.key,[question_multiplywith12.key,question_multiplywith112.key,question_multiplywith1112.key],school.key,"type1")

            state_chapfive_one=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapfive_two=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapfive_three=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)


            Query.assign_questions_to_state(state_chapfive_one.key, [question_multiplywith12.key],school.key)
            Query.assign_questions_to_state(state_chapfive_two.key, [question_multiplywith12.key,question_multiplywith112.key],school.key)
            Query.assign_questions_to_state(state_chapfive_three.key, [question_multiplywith12.key,question_multiplywith112.key,question_multiplywith1112.key],school.key)

            Query.assign_states_to_topic(topic_chap_five.key, [state_chapfive_one.key,state_chapfive_two.key,state_chapfive_three.key],school.key)


            '''
            assessment1=Query.addAssessment(name="Vedic Maths :1",list_topic_key=[topic_chap_one.key,topic_chap_two.key,topic_chap_three.key,topic_chap_four.key,topic_chap_five.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime(int(2014),int(11),int(12),int(23),int(12),int(8)),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)

            assessment2=Query.addAssessment(name="Vedic Maths :2",list_topic_key=[topic_chap_one.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime(int(2014),int(11),int(12),int(23),int(12),int(8)),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            assessment3=Query.addAssessment(name="Maths :1",list_topic_key=[topic_fac_multiples.key,topic_prime_factor.key,topic_hcf.key,topic_lcm.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime(int(2014),int(11),int(12),int(23),int(12),int(8)),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            assessment4=Query.addAssessment(name="Maths :2",list_topic_key=[topic_prime_factor.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime(int(2014),int(11),int(12),int(23),int(12),int(8)),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)

            
            
            a=Query.get_global_subjects(school.key)
            a=Query.get_subject_details_by_student(student_vivek.key);

            #a=Query.update_assessment_detail_of_student(total_score=50,topic_scores=[20,40,20,21,56],student_key= student_vivek.key,assessment_key= assessment1.key, current_state_key=[state_chapfive_one.key,state_chapfive_two.key,state_chapfive_three.key,state_chapfive_three.key,state_chapfive_three.key], next_state_key=[state_chapfive_one.key,state_chapfive_two.key,state_chapfive_three.key,state_chapfive_three.key,state_chapfive_three.key] \
            #                                          , next_question_key=[question_multiplywith12.key,question_general_subtraction.key,question_multiplywith12.key,question_multiplywith12.key,question_multiplywith12.key], school_key=school.key, completion_date=datetime.datetime(int(2014),int(8),int(8),int(8),int(8),int(8)))
            
            
            
            a=Query.get_mastery_by_subject_sc(SUB_vedic.key, student_vivek.key)
            b=Query.get_assessment_score_of_student(student_vivek.key,assessment1.key)
            a=Query.get_assessment_next_states_of_student(student_vivek.key,assessment1.key)
            a=Query.get_assessment_next_questions_of_student(student_vivek.key,assessment1.key)
            a=Query.get_assessment_scores_of_student(student_vivek.key,assessment1.key)
            a=Query.get_pending_assessments_by_subject(student_vivek.key,SUB_vedic.key)
            a=Query.get_learning_progress(student_vivek.key,SUB_vedic.key)
            b=Query.get_recent_assessment_score_of_student(student_vivek.key,SUB_vedic.key)
            a=Query.get_recent_assessment_next_states_of_student(student_vivek.key,SUB_vedic.key)
            a=Query.get_recent_assessment_topic_scores_of_student(student_vivek.key,SUB_vedic.key)
            a=Query.get_recent_assessment_next_questions_of_student(student_vivek.key,SUB_vedic.key)
            return str(a)+str(b)


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
    