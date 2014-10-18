
from google.appengine.ext import ndb
import Query
import logging
import datetime
import time

#from Constant import Constant,UserType,Subject
import Constant
from Query import addSubject, addTopic   
from models import QuestionInstance,State_Questions,Topic_States,Question,State,Address,Teacher,Class,\
    Assessment_Record
from models import School,Student,UserInfo,Subject,Assessment,Student_Assessments
from  models import Topic_Questions,State_Questions,Topic_States,Subject_Topics
from models import Topic,User  

def fill():
      try: 
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
            
            
            
            
            Query.assign_students_to_class(class_VA.key, [student_vivek.key,student_kavya.key,student_prajjwal.key,student_shiv.key])
            Query.assign_students_to_class(class_VA.key, [student_sarthak.key,student_mishika.key,student_prasoon.key,student_pravesh.key])

            
            
            
            
            
            
            teacher_vijay=Query.addTeacher("Vijay_Mehta",vijay_user, school.key,"password")
            teacher_sulabh=Query.addTeacher("Sulabj_Jain" ,sulabh_user, school.key,"")
            
          
            
            
            a=Query.assign_classes_to_teacher(teacher_vijay.key,[class_VA.key])
            Query.assign_classes_to_teacher(teacher_vijay.key,[class_VA.key])
            
            
            
            subject_maths=Query.addSubject(Constant.Subject.TYPE_CLASS, Constant.Subject.SUBJECT_MATHS,school.key,class_VA.key)
            #subject2=Query.addSubject(Subject.TYPE_CLASS, Subject.SUBJECT_SCIENCE,school.key,class1.key)
            subject_english=Query.addSubject(Constant.Subject.TYPE_CLASS, Constant.Subject.SUBJECT_ENGLISH,school.key,class_VA.key)
            #subject4=Query.addSubject(Subject.TYPE_CLASS, Subject.SUBJECT_GEOLOGY,school.key,class1.key)
            
            a=Query.assign_subjects_to_class(class_VA.key, [subject_maths.key])
            a=Query.assign_subjects_to_class(class_VA.key, [subject_english.key])
            
            
            Query.assign_subjects_to_teacher(teacher_vijay.key,[subject_maths.key])
            a=Query.assign_subjects_to_teacher(teacher_vijay.key,[subject_english.key])

           
            ##Query.login("Suraj_Singh", "pwd")
            
            
            
            
            topic_number=Query.addTopic(school_key=school.key,name="Know Your Numbers", prerequisite_topics=[],subject_key=subject_maths.key,types=["Comparing Numbers","Numbers Formation","Arrangement_Ascending"])
            topic_trig=Query.addTopic(school_key=school.key,name="Trigonimetric_Ratio", prerequisite_topics=[topic_number.key],subject_key=subject_maths.key,types=["type1","type2","type3"])
            topic_height=Query.addTopic(school_key=school.key,name="Height & Distance", prerequisite_topics=[topic_trig.key,topic_number.key],subject_key=subject_maths.key,types=["type1","type2","type3"])
            topic_circle=Query.addTopic(school_key=school.key,name="Circle_operation", prerequisite_topics=[topic_number.key],subject_key=subject_maths.key,types=["type1","type2","type3"])
           
            
            
            
            topic_part=Query.addTopic(school_key=school.key,name="Part of Speech", prerequisite_topics=[],subject_key=subject_english.key,types=["type1","type2","type3"])
            topic_tenses=Query.addTopic(school_key=school.key,name="Tenses", prerequisite_topics=[],subject_key=subject_english.key,types=["type1","type2","type3"])
            topic_sentences=Query.addTopic(school_key=school.key,name="Sentences", prerequisite_topics=[topic_part.key],subject_key=subject_english.key,types=["type1","type2","type3"])
            topic_voices=Query.addTopic(school_key=school.key,name="Voices", prerequisite_topics=[topic_sentences.key,topic_part.key],subject_key=subject_english.key,types=["type1","type2","type3"])
            #topic5=Query.addTopic(school_key=school.key,name="Ellipse ", prerequisite_topics=[topic.key],subject_key=subject1.key)
            
            
            
            
            
            
            questioninstance_number1=Query.addQuestionInstance(problem_statement="Sum of of 2 and 3 ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["5"],school_key=school.key)
            
            questioninstance_number2=Query.addQuestionInstance(problem_statement="Sum of 12 and 15 ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["17"],school_key=school.key)
            #questioninstance_number3=Query.addQuestionInstance(problem_statement="Which one is greatest ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["1902","1920","9201","9021","9210"], answers=["9210"],school_key=school.key)

            #questioninstance_number4=Query.addQuestionInstance(problem_statement="Which one is smallest ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["1902","1920","9201","9021","9210"], answers=["9210"],school_key=school.key)

            questioninstance_number3=Query.addQuestionInstance(problem_statement="value of : 50-20  \
 ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["30"],school_key=school.key)

            questioninstance_number4=Query.addQuestionInstance(problem_statement="value of 8/2 :\
  ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["4"],school_key=school.key)

            questioninstance_trig1=Query.addQuestionInstance(problem_statement="sin(90+A) ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["sinA","CosA","-SinA","-CosA"], answers=["252"],school_key=school.key)
            questioninstance_trig2=Query.addQuestionInstance(problem_statement="Area of square of arm length a ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["pie*a*a","a*a","a*a*a","-a*a"], answers=["a*a"],school_key=school.key)
            questioninstance_trig3=Query.addQuestionInstance(problem_statement="Area of circle of arm radius a ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["4","6","7","8"], answers=["pie*a*a"],school_key=school.key)
            questioninstance_trig4=Query.addQuestionInstance(problem_statement="Area of circle of arm radius a ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["4","6","7","8"], answers=["pie*a*a"],school_key=school.key)
            
            
            
            
            questioninstance_height1=Query.addQuestionInstance(problem_statement="tanA= CosA/SinA True ? ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["T","F"], answers=["F"],school_key=school.key)
     
            questioninstance_height3=Query.addQuestionInstance(problem_statement="CotA= SinA-CosA True ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["T","F"], answers=["F"],school_key=school.key)
            questioninstance_height4=Query.addQuestionInstance(problem_statement="Sin90 =", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["1","0","2","200"], answers=["1"],school_key=school.key)
            questioninstance_height2=Query.addQuestionInstance(problem_statement="Cos(90+A)", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["-SinA","CosA","SinB","CosecA"], answers=["-SinA"],school_key=school.key)
            
            
            questioninstance_circle1=Query.addQuestionInstance(problem_statement="area of circle  ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["pie*r*r","r*r","r","2r"], answers=["pie*r*r"],school_key=school.key)
            questioninstance_circle2=Query.addQuestionInstance(problem_statement="diameter of circle", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["r","2*r","r*r","pie*r*r"], answers=["2*r"],school_key=school.key)
            questioninstance_circle3=Query.addQuestionInstance(problem_statement="circumference of circle", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["r","2**pie*r","r*r","pie*r*r"], answers=["2**pie*r"],school_key=school.key)
            questioninstance_circle4=Query.addQuestionInstance(problem_statement="if r=4 diameter is ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["4","6","7","8"], answers=["8"],school_key=school.key)
            
           
           
           
            question_number1=Query.addQuestion(questioninstance_number1,school.key)
            question_number2=Query.addQuestion(questioninstance_number2,school.key)
            question_number3=Query.addQuestion(questioninstance_number3,school.key)
            question_number4=Query.addQuestion(questioninstance_number4,school.key)
            #question_number5=Query.addQuestion(questioninstance_number5,school.key)
            #question_number6=Query.addQuestion(questioninstance_number6,school.key)
           
            
            question_trig1=Query.addQuestion(questioninstance_trig1,school.key)
            question_trig2=Query.addQuestion(questioninstance_trig2,school.key)
            question_trig3=Query.addQuestion(questioninstance_trig3,school.key)
            question_trig4=Query.addQuestion(questioninstance_trig4,school.key)
          
           
           
           
            question_height1=Query.addQuestion(questioninstance_height1,school.key)
            question_height2=Query.addQuestion(questioninstance_height2,school.key)
            question_height3=Query.addQuestion(questioninstance_height3,school.key)
            question_height4=Query.addQuestion(questioninstance_height4,school.key)
            
            
            
            
            question_circle1=Query.addQuestion(questioninstance_circle1,school.key)
            question_circle2=Query.addQuestion(questioninstance_circle2,school.key)
            question_circle3=Query.addQuestion(questioninstance_circle3,school.key)
            question_circle4=Query.addQuestion(questioninstance_circle4,school.key)
            
            
            
            
            
            #'''*****************************************************''''
            
            
            questioninstance_part1=Query.addQuestionInstance(problem_statement=" Which of the following words is an example of a preposition? ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["into","if","many","you"], answers=["into"],school_key=school.key)
            
            questioninstance_part2=Query.addQuestionInstance(problem_statement="Which of the following words is an example of an interjection? ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["soon","when","ouch","within"], answers=["ouch"],school_key=school.key)
            questioninstance_part3=Query.addQuestionInstance(problem_statement="Which of the following words is an example of a conjunction? ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["and","run","below","her"], answers=["and"],school_key=school.key)

            questioninstance_part4=Query.addQuestionInstance(problem_statement="Which of the following words is an example of a verb? ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["tastes","late","not","slowly"], answers=["tastes"],school_key=school.key)

        
            
            questioninstance_tense1=Query.addQuestionInstance(problem_statement="Find the correct tense  : Did you play tennis yesterday?  ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["Simple Past","Present Perfect","Past Progressive"," Present Perfect Progressive"], answers=["Simple Past"],school_key=school.key)
            questioninstance_tense2=Query.addQuestionInstance(problem_statement="Find the correct tense : Was John reading the book last night?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["Simple Past","Present Perfect","Past Progressive"," Present Perfect Progressive"], answers=["Past Progressive"],school_key=school.key)
            questioninstance_tense3=Query.addQuestionInstance(problem_statement="Find the correct tense : Have you been waiting for me for long?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["Simple Past","Present Perfect","Past Progressive"," Present Perfect Progressive"], answers=["Present Perfect Progressive"],school_key=school.key)
            questioninstance_tense4=Query.addQuestionInstance(problem_statement="Find the correct tense :Have you ever watched a film in English?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["Simple Past","Present Perfect","Past Progressive"," Present Perfect Progressive"], answers=["Present Perfect"],school_key=school.key)
            
            
            
            
            questioninstance_sentence1=Query.addQuestionInstance(problem_statement="Fill Conjunctions in sentence : I like English ____ I like French very much.", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["and","but","so","or"], answers=["and"],school_key=school.key)
            questioninstance_sentence2=Query.addQuestionInstance(problem_statement="Fill Conjunctions in sentence  :My brother likes Maths but he doesn't like History", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["and","but","so","or"], answers=["but"],school_key=school.key)
            questioninstance_sentence3=Query.addQuestionInstance(problem_statement="Fill Conjunctions in sentence :Can you read and write English words?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["and","but","so","or"], answers=["and"],school_key=school.key)
            questioninstance_sentence4=Query.addQuestionInstance(problem_statement="Fill Conjunctions in sentence :Do we have French or Music after the break?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["and","but","so","or"], answers=["or"],school_key=school.key)
            
         
           
            question_part1=Query.addQuestion(questioninstance_part1,school.key)
            question_part2=Query.addQuestion(questioninstance_part2,school.key)
            question_part3=Query.addQuestion(questioninstance_part3,school.key)
            question_part4=Query.addQuestion(questioninstance_part4,school.key)
           
            
            question_tense1=Query.addQuestion(questioninstance_tense1,school.key)
            question_tense2=Query.addQuestion(questioninstance_tense2,school.key)
            question_tense3=Query.addQuestion(questioninstance_tense3,school.key)
            question_tense4=Query.addQuestion(questioninstance_tense4,school.key)
          
           
           
           
            question_sentence1=Query.addQuestion(questioninstance_sentence1,school.key)
            question_sentence2=Query.addQuestion(questioninstance_sentence1,school.key)
            question_sentence3=Query.addQuestion(questioninstance_sentence1,school.key)
            question_sentence4=Query.addQuestion(questioninstance_sentence1,school.key)
            
            #'''*******************************************'''
            
            
            state1=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state2=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            
           
            state3=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            
           
           
           
           
           
            
            state1=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            
            state2=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state3=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            #class1=None
            
           
            
             
            Query.assign_questions_to_state(state1.key, [question_number1.key,question_number2.key,question_number3.key,question_number4.key,question_circle1.key,question_circle2.key,question_circle3.key,question_circle4.key,question_height1.key,question_height2.key,question_height3.key,question_height4.key,question_circle1.key,question_circle2.key,question_circle3.key,question_circle4.key],school.key)
            Query.assign_questions_to_state(state2.key, [question_sentence1.key,question_sentence2.key,question_sentence3.key,question_sentence4.key,question_part1.key,question_part2.key,question_part3.key,question_part4.key,question_tense1.key,question_tense2.key,question_tense3.key,question_tense4.key],school.key)               
            
            Query.assign_questions_to_topic(topic_number.key,[question_number1.key,question_number2.key,question_number3.key,question_number4.key],school.key,"type1")
            Query.assign_questions_to_topic(topic_trig.key,[question_trig1.key,question_trig2.key,question_trig3.key,question_trig4.key],school.key,"type2")
            Query.assign_questions_to_topic(topic_circle.key,[question_circle1.key,question_circle2.key,question_circle3.key,question_circle4.key],school.key,"type2")
            Query.assign_questions_to_topic(topic_height.key,[question_height1.key,question_height2.key,question_height3.key,question_height4.key],school.key,"type1")
            
            
            
            
            Query.assign_questions_to_topic(topic_part.key,[question_part1.key,question_part2.key,question_part3.key,question_part4.key],school.key,"type31")
            Query.assign_questions_to_topic(topic_sentences.key,[question_sentence2.key,question_sentence3.key,question_sentence4.key,question_sentence1.key],school.key,"type3")
            Query.assign_questions_to_topic(topic_tenses.key,[question_tense1.key,question_tense2.key,question_tense3.key,question_tense4.key],school.key,"type2")
           
            
            #a=Query.assign_states_to_topic_by_name("Number  System",[state1.key,state2.key,state3.key],school.key)            #Query.assign_assessment_state_to_student(student.key, assessment1.key,state1.key)
            
            Query.assign_states_to_topic(topic_number.key, [state1.key,state2.key,state3.key],school.key)
            Query.assign_states_to_topic(topic_height.key, [state1.key,state2.key,state3.key],school.key)
            Query.assign_states_to_topic(topic_trig.key, [state1.key,state2.key,state3.key],school.key)
            Query.assign_states_to_topic(topic_circle.key, [state1.key,state2.key,state3.key],school.key)
            
            Query.assign_states_to_topic(topic_part.key, [state1.key,state2.key,state3.key],school.key)
            Query.assign_states_to_topic(topic_sentences.key, [state1.key,state2.key,state3.key],school.key)
            Query.assign_states_to_topic(topic_tenses.key, [state1.key,state2.key,state3.key],school.key)
            
            
            
          
          
          
            assessment1=Query.addAssessment(name="Know Your Numbers :1",list_topic_key=[topic_number.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            '''assessment2=Query.addAssessment(name="Know Your Numbers :2",list_topic_key=[topic_number.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            assessment3=Query.addAssessment(name="Know Your Numbers :3",list_topic_key=[topic_number.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            assessment4=Query.addAssessment(name="Know Your Numbers :4",list_topic_key=[topic_number.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            assessment5=Query.addAssessment(name="Know Your Numbers :5",list_topic_key=[topic_number.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            
            
            assessment6=Query.addAssessment(name="Know Your Numbers :6",list_topic_key=[topic_number.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            '''
            assessment7=Query.addAssessment(name="Playing with digits :1",list_topic_key=[topic_number.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
           
            
            assessment8=Query.addAssessment(name="Lets Make words :1",list_topic_key=[topic_part.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            assessment9=Query.addAssessment(name="Lets Make words :2",list_topic_key=[topic_part.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            '''assessment10=Query.addAssessment(name="Assessment10",list_topic_key=[topic_part.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            assessment11=Query.addAssessment(name="Assessment11",list_topic_key=[topic_sentences.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            assessment12=Query.addAssessment(name="Assessment12",list_topic_key=[topic_sentences.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            assessment13=Query.addAssessment(name="Assessment13",list_topic_key=[topic_sentences.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            assessment14=Query.addAssessment(name="Assessment14",list_topic_key=[topic_tenses.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            assessment15=Query.addAssessment(name="Assessment15",list_topic_key=[topic_tenses.key,topic_sentences.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            assessment16=Query.addAssessment(name="Assessment16",list_topic_key=[topic_tenses.key,topic_sentences.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            '''
            
           
            #Query.login('Ankit_Bhatia', '')
            #uery.login('Vijay_Mehta', '')
            Query.get_states_of_topic(topic_number.key)
            Query.get_states_of_topic(topic_part.key)
        
            
            Query.get_questions_of_state(state1.key)
            Query.get_questions_of_topic(topic_number.key)
            Query.signup_school("DPS INDIRAPURAM", address1)
            Query.get_subjects_by_student(student_vivek.key)
            Query.get_topics_by_subject(subject_maths.key)
            
            a=Query.update_assessment_detail_of_student(student_key=student_vivek.key, assessment_key=assessment1.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number2.key,score=40,school_key=school.key,completion_date=datetime.datetime.now())
            
            #a=Query.update_assessment_detail_of_student(student_key=student_vivek.key, assessment_key=assessment1.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number2.key,score=40,school_key=school.key,completion_date=datetime.datetime.now())
            a=Query.get_mastery_by_student_of_class(teacher_vijay.key, class_VA.key, subject_maths.key)
            a=Query.get_students_not_logged_in_by_class(teacher_vijay.key,class_VA.key)
            a=Query.update_assessment_detail_of_student(student_key=student_vivek.key, assessment_key=assessment7.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number3.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
           
            Query.update_assessment_detail_of_student(student_key=student_vivek.key, assessment_key=assessment8.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_trig2.key,score=80,school_key=school.key,completion_date=datetime.datetime.now())
           
            
            
            #a=Query.update_assessment_detail_of_student(student_key=student_kavya.key, assessment_key=assessment1.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number2.key,score=70,school_key=school.key,completion_date=datetime.datetime.now())
            
            #a=Query.update_assessment_detail_of_student(student_key=student_kavya.key, assessment_key=assessment2.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number4.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
           
            Query.update_assessment_detail_of_student(student_key=student_kavya.key, assessment_key=assessment1.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_trig3.key,score=40,school_key=school.key,completion_date=datetime.datetime.now())
            a=Query.update_assessment_detail_of_student(student_key=student_kavya.key, assessment_key=assessment1.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_height1.key,score=80,school_key=school.key,completion_date=datetime.datetime.now())
            ##Query.update_assessment_detail_of_student(student_key=student_kavya.key, assessment_key=assessment6.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_circle1.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
            #Query.update_assessment_detail_of_student(student_key=student_kavya.key, assessment_key=assessment7.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_circle3.key,score=34,school_key=school.key,completion_date=datetime.datetime.now())
            
            
           
            
            a=Query.update_assessment_detail_of_student(student_key=student_mishika.key, assessment_key=assessment1.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number2.key,score=30,school_key=school.key,completion_date=datetime.datetime.now())
            
            #a=Query.update_assessment_detail_of_student(student_key=student_mishika.key, assessment_key=assessment2.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number3.key,score=40,school_key=school.key,completion_date=datetime.datetime.now())
           
            #Query.update_assessment_detail_of_student(student_key=student_mishika.key, assessment_key=assessment3.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_trig2.key,score=30,school_key=school.key,completion_date=datetime.datetime.now())
            #a=Query.update_assessment_detail_of_student(student_key=student_mishika.key, assessment_key=assessment4.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_height2.key,score=80,school_key=school.key,completion_date=datetime.datetime.now())
            
            Query.update_assessment_detail_of_student(student_key=student_sarthak.key, assessment_key=assessment8.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_circle4.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
            
            
            
            a=Query.update_assessment_detail_of_student(student_key=student_sarthak.key, assessment_key=assessment1.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number2.key,score=20,school_key=school.key,completion_date=datetime.datetime.now())
            
            a=Query.update_assessment_detail_of_student(student_key=student_sarthak.key, assessment_key=assessment7.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number4.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
           
            Query.update_assessment_detail_of_student(student_key=student_sarthak.key, assessment_key=assessment9.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_trig3.key,score=75,school_key=school.key,completion_date=datetime.datetime.now())
            '''a=Query.update_assessment_detail_of_student(student_key=student_prajjwal.key, assessment_key=assessment4.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_height1.key,score=30,school_key=school.key,completion_date=datetime.datetime.now())
            Query.update_assessment_detail_of_student(student_key=student_prajjwal.key,  assessment_key=assessment5.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_height4.key,score=70,school_key=school.key,completion_date=datetime.datetime.now())
            Query.update_assessment_detail_of_student(student_key=student_prasoon.key, assessment_key=assessment6.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_circle1.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
            Query.update_assessment_detail_of_student(student_key=student_prasoon.key, assessment_key=assessment7.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_circle3.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
            '''
           ###################################################
            '''Query.update_assessment_detail_of_student(student_key=student_vivek.key, assessment_key=assessment8.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number2.key,score=40,school_key=school.key,completion_date=datetime.datetime.now())
            
            a=Query.update_assessment_detail_of_student(student_key=student_vivek.key, assessment_key=assessment9.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number2.key,score=40,school_key=school.key,completion_date=datetime.datetime.now())
            a=Query.get_mastery_by_student_of_class(teacher_vijay.key, class_VA.key, subject_maths.key)
            a=Query.get_students_not_logged_in_by_class(teacher_vijay.key,class_VA.key)
            a=Query.update_assessment_detail_of_student(student_key=student_vivek.key, assessment_key=assessment10.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number3.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
           
            Query.update_assessment_detail_of_student(student_key=student_vivek.key, assessment_key=assessment11.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_trig2.key,score=80,school_key=school.key,completion_date=datetime.datetime.now())
            a=Query.update_assessment_detail_of_student(student_key=student_vivek.key, assessment_key=assessment12.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_height2.key,score=50,school_key=school.key,completion_date=datetime.datetime.now())
            
            Query.update_assessment_detail_of_student(student_key=student_vivek.key, assessment_key=assessment13.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_circle4.key,score=10,school_key=school.key,completion_date=datetime.datetime.now())
            
            
            
            a=Query.update_assessment_detail_of_student(student_key=student_kavya.key, assessment_key=assessment8.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number2.key,score=70,school_key=school.key,completion_date=datetime.datetime.now())
            
            a=Query.update_assessment_detail_of_student(student_key=student_kavya.key, assessment_key=assessment9.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number4.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
           
            Query.update_assessment_detail_of_student(student_key=student_kavya.key, assessment_key=assessment10.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_trig3.key,score=40,school_key=school.key,completion_date=datetime.datetime.now())
            a=Query.update_assessment_detail_of_student(student_key=student_kavya.key, assessment_key=assessment11.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_height1.key,score=80,school_key=school.key,completion_date=datetime.datetime.now())
            Query.update_assessment_detail_of_student(student_key=student_kavya.key,  assessment_key=assessment12.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_height4.key,score=90,school_key=school.key,completion_date=datetime.datetime.now())
            Query.update_assessment_detail_of_student(student_key=student_kavya.key, assessment_key=assessment13.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_circle1.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
            Query.update_assessment_detail_of_student(student_key=student_kavya.key, assessment_key=assessment14.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_circle3.key,score=34,school_key=school.key,completion_date=datetime.datetime.now())
            
            
            
            
            a=Query.update_assessment_detail_of_student(student_key=student_mishika.key, assessment_key=assessment8.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number2.key,score=87,school_key=school.key,completion_date=datetime.datetime.now())
            
            a=Query.update_assessment_detail_of_student(student_key=student_mishika.key, assessment_key=assessment9.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number3.key,score=76,school_key=school.key,completion_date=datetime.datetime.now())
           
            Query.update_assessment_detail_of_student(student_key=student_mishika.key, assessment_key=assessment10.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_trig2.key,score=54,school_key=school.key,completion_date=datetime.datetime.now())
            a=Query.update_assessment_detail_of_student(student_key=student_mishika.key, assessment_key=assessment11.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_height2.key,score=50,school_key=school.key,completion_date=datetime.datetime.now())
            
            Query.update_assessment_detail_of_student(student_key=student_sarthak.key, assessment_key=assessment12.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_circle4.key,score=55,school_key=school.key,completion_date=datetime.datetime.now())
            
            
            
            a=Query.update_assessment_detail_of_student(student_key=student_sarthak.key, assessment_key=assessment13.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number2.key,score=45,school_key=school.key,completion_date=datetime.datetime.now())
            
            a=Query.update_assessment_detail_of_student(student_key=student_sarthak.key, assessment_key=assessment14.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number4.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
           
            Query.update_assessment_detail_of_student(student_key=student_sarthak.key, assessment_key=assessment8.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_trig3.key,score=23,school_key=school.key,completion_date=datetime.datetime.now())
            a=Query.update_assessment_detail_of_student(student_key=student_prajjwal.key, assessment_key=assessment9.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_height1.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
            Query.update_assessment_detail_of_student(student_key=student_prajjwal.key,  assessment_key=assessment10.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_height4.key,score=80,school_key=school.key,completion_date=datetime.datetime.now())
            Query.update_assessment_detail_of_student(student_key=student_prasoon.key, assessment_key=assessment11.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_circle1.key,score=70,school_key=school.key,completion_date=datetime.datetime.now())
            Query.update_assessment_detail_of_student(student_key=student_prasoon.key, assessment_key=assessment12.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_circle3.key,score=60,school_key=school.key,completion_date=datetime.datetime.now())
            a=Query.assign_assessment_to_students(assessment10.key, [student_kavya.key,student_prasoon.key])
            #a=Query.map_state_to_questions_dummy( {1:[question_number1.key,question_number2.key,question_number3.key]}, school.key)
            #a=Query.login("Vijay_Mehta","pass")
            #a=Query.login("sulabh@12","pass")
            #a=Query.signup_teacher("sulabh@12",sulabh_user, "01",'pass')
            #a=Query.signup_student("ankit@123", ankit_user,"01",'pass')
            '''
            '''a=Query.get_all_schools()
            b=Query.get_class_of_school(school.key)
            a=str(a)+"    "+str(b)
            a=Query.get_topic_details_by_subject(subject_maths.key)'''
            
            
            
            '''
            
            a=Query.get_mastery_by_topic(topic_number.key, student_vivek.key)
            a=Query.get_mastery_by_subject(subject_english.key,student_prasoon.key)
            #a=Query.get_student_score_in_assessment(student1.key, assessment1.key)
            Query.get_student_score_in_assessment(student_vivek.key, assessment7.key)
            
            a=Query.get_pending_assessment_subject(subject_maths.key,student_sarthak.key)
            
            a=Query.get_mastery_by_topic(topic_sentences.key,student_prasoon.key)
            #a1=Query.get_mastery_by_topic(topic2.key,student2.key)
            Query.get_assessment_coverage_of_class(teacher_vijay.key,class_VA.key)
            a=Query.get_assessment_coverage_of_subject(teacher_vijay.key, class_VA.key, subject_maths.key)
            # a=Query.login("Vijay_Mehta", '')
            #a3=Query.get_mastery_by_topic(topic2.key,student4.key)
            #a=Query.get_mastery_by_subject(subject_english.key, student_kavya.key)
            #a=Query.get_growth_for_all_subject(student_vivek.key)
            '''
            ''''a=Query.get_ready_to_learn_of_all_topic(subject_maths.key,student_vivek.key)
            a=Query.get_learning_progress_date_wise_dummy( student_vivek.key,subject_maths.key)
            #Query.get_mastery_for_all_subjects(student1.key)
            a=Query.get_average_mastery_by_subject_detailed(teacher_vijay.key, class_VA.key, subject_english.key)
            a=Query.get_average_mastery_all_subject_detailed(teacher_vijay.key, class_VA.key)
            a=Query.get_growth_for_subject(student_vivek.key,subject_maths.key)
            a=Query.get_growth_for_all_subject(student_kavya.key)
            a=Query.get_mastery_by_student_of_class(teacher_vijay.key,class_VA.key, subject_maths)
            a=Query.get_students_not_logged_in_of_all_class(teacher_vijay.key)
            a=Query.get_average_mastery_by_subject_of_all_class(teacher_vijay.key)
            a=Query.get_class_details_of_teacher(teacher_vijay.key)
            a=Query.get_students_not_logged_in_by_class(teacher_vijay.key,class_VA.key)
            a=Query.get_average_mastery_all_subject_detailed(teacher_vijay.key,class_VA.key)
            
            
            a=Query.get_assessment_coverage_of_class(teacher_vijay.key,class_VA.key)#changed
            a=Query.get_subject_details_of_teacher_in_class(teacher_vijay.key,class_VA.key)
            a=Query.get_ready_to_learn_of_class(teacher_vijay.key,class_VA.key,subject_maths.key)# when no attended then ?
            a=Query.get_assessment_coverage_of_subject(teacher_vijay.key,class_VA.key,subject_maths.key)
            a= Query.get_average_mastery_of_a_subject(teacher_vijay.key,class_VA.key,subject_maths.key)
            a=Query.get_subject_details_by_student(student_vivek.key)
            a=Query.login('Ankit_Bhatia','')
            b=None
            
            #a=Query.signup_teacher(sulabh_user, "CVSchool5678",'')
            #b=Query.signup_student(pravesh_user, "CVSchool5678",'')
            #c=Query.login(a,"")
            #d=Query.login(b,"")
            '''
            '''
            old data
            address1=Query.addAddress(type=Constant.Constant.ADDRESS_TYPE_HOME,state="UP",city="Meerut",street="12")
            school=Query.addSchool("CVSchool", address1)
            
            userinfo1=Query.addUserInfo("Trish","Kumar",datetime.date(int(2012),int(6),int(6)),Constant.Constant.SEX_MALE, address1, "yyy", 67757)
            Query.signup_student( userinfo1, school.key,"123")
           
            
            userinfo2=Query.addUserInfo("Ankit","Bhatia",datetime.datetime.now(),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            
            userinfo3=Query.addUserInfo("Suraj","Singh",datetime.datetime.now(),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            userinfo4=Query.addUserInfo("Sarthak","Tiwari",datetime.datetime.now(),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            userinfo5=Query.addUserInfo("Vijay","Mehta",datetime.datetime.now(),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            
            #teacher1=Query.addTeacher("teacher1", userinfo1, school.key)
            
            
            teacher1=Query.addTeacher( userinfo5, school.key,"")
            teacher3=Query.addTeacher( userinfo4, school.key,"")
            teacher4=Query.addTeacher( userinfo4, school.key,"")
            teacher5=Query.addTeacher( userinfo2, school.key,"")
            class1=Query.addClass(name="Class_V",school_key= school.key,section_details="A",year_session="2013-2014")  #to be changed
            class2=Query.addClass(name="Class_VI",school_key= school.key,section_details="B",year_session="2013-2014")  #to be changed
            a=Query.assign_classes_to_teacher(teacher1.key,[class1.key,class2.key])
            student1=Query.addStudent(userinfo2, school.key,'pwd')
            student2=Query.addStudent(userinfo1, school.key,'pwd')
            student3=Query.addStudent(userinfo3, school.key,'pwd')
            student4=Query.addStudent(userinfo4, school.key,'pwd')
            
            Query.login("Ankit_Bhatia", "pwd")
            Query.login("Suraj_Singh", "pwd")
            subject1=Query.addSubject(Constant.Subject.TYPE_CLASS, Constant.Subject.SUBJECT_MATHS,school.key,class1.key)
            subject2=Query.addSubject(Constant.Subject.TYPE_CLASS, Constant.Subject.SUBJECT_SCIENCE,school.key,class1.key)
            
            
            topic=Query.addTopic(school_key=school.key,name="Number  System", prerequisite_topics=[],subject_key=subject1.key)
            topic1=Query.addTopic(school_key=school.key,name="Float division", prerequisite_topics=[topic.key],subject_key=subject1.key)
            #topic2=Query.addTopic(school_key=school.key,name="Circle operations", prerequisite_topics=[topic.key,topic1.key],subject_key=subject1.key)
            #topic3=Query.addTopic(school_key=school.key,name="Square Operations", prerequisite_topics=[topic.key,topic1.key,topic2.key],subject_key=subject2.key)
            #topic4=Query.addTopic(school_key=school.key,name="Triangle", prerequisite_topics=[topic.key,topic1.key,topic2.key,topic3.key],subject_key=subject2.key)
            #topic5=Query.addTopic(school_key=school.key,name="Ellipse ", prerequisite_topics=[topic.key],subject_key=subject1.key)
            
            questioninstance=Query.addQuestionInstance(problem_statement="sum of 2+3 ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["4,6,7,8"], answers=["5"],school_key=school.key)
            
            questioninstance2=Query.addQuestionInstance(problem_statement="sum of 222+30 ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["252,600,227,8"], answers=["252"],school_key=school.key)
            questioninstance3=Query.addQuestionInstance(problem_statement="quotient of 58 by 9 ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["252,600,227,8"], answers=["6"],school_key=school.key)
            
            question1=Query.addQuestion(questioninstance,school.key)
           
            question2=Query.addQuestion(questioninstance3,school.key)
            question3=Query.addQuestion(questioninstance2,school.key)
            state1=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            
            state2=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state3=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            #class1=None
            Query.assign_subjects_to_class(class1.key, [subject1.key,subject2.key])
            Query.assign_students_to_class(class1.key, [student1.key,student2.key,student3.key,student4.key])
            a=Query.assign_subjects_to_teacher(teacher1.key, [subject1.key,subject2.key])
             
            Query.assign_questions_to_state(state1.key, [question1.key],school.key)
            
            Query.assign_questions_to_state(state2.key, [question1.key,question2.key],school.key)
            Query.assign_questions_to_state(state3.key, [question1.key,question2.key,question3.key],school.key)
            Query.assign_questions_to_topic(topic.key,[question1.key,question2.key,question3.key],school.key)
            Query.assign_questions_to_topic(topic1.key,[question1.key,question2.key,question3.key],school.key)
            #Query.assign_questions_to_topic(topic2.key,[question1.key,question2.key,question3.key],school.key)
            #Query.assign_questions_to_topic(topic3.key,[question1.key,question2.key,question3.key],school.key)
            #a=Query.assign_states_to_topic_by_name("Number  System",[state1.key,state2.key,state3.key],school.key)            #Query.assign_assessment_state_to_student(student.key, assessment1.key,state1.key)
            Query.assign_states_to_topic(topic.key, [state1.key,state2.key,state3.key],school.key)
            Query.assign_states_to_topic(topic1.key, [state1.key,state2.key,state3.key],school.key)
            #Query.assign_states_to_topic(topic2.key, [state1.key,state2.key,state3.key],school.key)
            #Query.assign_states_to_topic(topic3.key, [state1.key,state2.key,state3.key],school.key)
            #Query.assign_states_to_topic(topic4.key, [state1.key,state2.key,state3.key],school.key)
          
            assessment1=Query.addAssessment(name="Assessment1",list_topic_key=[topic.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher1.key,class_key=class1.key)
            assessment2=Query.addAssessment(name="Assessment2",list_topic_key=[topic.key,topic1.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher1.key,class_key=class1.key)
            #assessment3=Query.addAssessment(name="Assessment3",list_topic_key=[topic2.key,topic3.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher1.key,class_key=class1.key)
           
            
           
            a=Query.get_states_of_topic(topic.key)
            
            
            Query.get_questions_of_state(state1.key)
            Query.get_questions_of_topic(topic.key)
            Query.signup_school("DPS INDIRAPURAM", address1)
            Query.get_subjects_by_student(student1.key)
            Query.get_topics_by_subject(subject1.key)
            
            Query.update_assessment_detail_of_student(student_key=student1.key, assessment_key=assessment1.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question2.key,score=100,school_key=school.key,start_date=datetime.datetime.now())
            Query.update_assessment_detail_of_student(student_key=student1.key, assessment_key=assessment2.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question3.key,score=40,school_key=school.key,start_date=datetime.datetime.now())
           # Query.update_assessment_detail_of_student(student_key=student1.key, assessment_key=assessment3.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question3.key,score=100,school_key=school.key,start_date=datetime.datetime.now())
            Query.get_assessments_by_topic(student1.key, topic.key)
            a=Query.get_mastery_by_subject(subject1.key,student1.key)
            #a=Query.get_student_score_in_assessment(student1.key, assessment1.key)
            a=Query.get_student_score_in_assessment(student1.key, assessment1.key)
            a=Query.get_pending_assessment_subject(subject1.key,student1.key)
            Query.get_questions_by_topic_name('Number  System')
            #Teacher APIS
            a=Query.get_class_details_of_teacher(teacher1.key)
            Query.get_students_not_logged_in_of_all_class(teacher1.key)
            a=Query.get_average_mastery_by_subject_of_all_class(teacher1.key)
            a=Query.get_students_not_logged_in_by_class(teacher1.key, class1.key)
            a=Query.get_average_mastery_all_subject_detailed(teacher1.key, class1.key)
            a=Query.get_assessment_coverage_of_class(teacher1.key, class1.key)
            a=Query.get_subject_details_of_teacher_in_class(teacher1.key, class1.key)
            a=Query.get_subject_details(subject1.key)
            a=Query.get_ready_to_learn_of_class(teacher1.key, class1.key, subject1.key)
            a=Query.get_assessment_coverage_of_subject(teacher1.key, class1.key, subject1.key)
            a=Query.get_mastery_details_of_subject(teacher1.key, class1.key, subject1.key)
            a=Query.get_average_mastery_of_a_subject(teacher1.key, class1.key, subject1.key)
            Query.get_mastery_by_topic(topic.key,student1.key)
            Query.get_mastery_for_all_subjects(student1.key)
            Query.get_growth_for_all_topic_subject(student1.key,subject1.key)
            Query.get_growth_for_subject(student1.key,subject1.key)
            Query.get_student_next_question_in_assessment(student1.key, assessment1.key)   
            Query.get_ready_to_learn_topic(topic1.key,student1.key) 
            Query.get_ready_to_learn_of_all_topic_dummy(student1.key)
            Query.get_student_start_date_in_assessment(student1.key, assessment1.key)
            Query.get_learning_progress_date_wise_dummy(student1.key)
            Query.get_growth_for_subject(student1.key,subject2.key)
            Query.get_growth_for_all_subject(student1.key)
            Query.login('Vijay_Mehta','jkjk')
            Query.login("Ankit_Bhatia", "pwd")
            Query.get_pending_assessment_subject_dummy(student1.key)
            Query.get_subjects_of_class(class1.key)
            Query.get_average_score_by_subject(subject1.key,teacher1.key)
            Query.get_average_score_all_subject(subject1.key,teacher1.key)
            Query.get_average_mastery_by_subject_detailed(teacher1.key)
            #Query.get_average_mastery_all_subject_detailed(teacher1.key)
            Query.get_ready_to_learn_of_class(teacher1.key)
            Query.get_mastery_by_student_of_class(teacher1.key)
            Query.get_students_not_logged_in_by_class(teacher1.key)'''
            a=str(datetime.datetime.now())
            #a=topic_number.assessments_in_topic
            logging.info('@@@@@@@@@@@@@@@@@@'+str(len(a)))
            return (a)
                        
            
            
      except Exception :
            logging.exception("")
            return Constant.Constant.ERROR_OPERATION_FAIL
        
      return Constant.Constant.UPDATION_SUCCESSFULL  
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
    
