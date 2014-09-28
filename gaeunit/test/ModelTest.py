__author__ = 'rahul'

import unittest,logging
from google.appengine.ext import testbed
from google.appengine.ext import ndb
import logging
import datetime

from AssessingPie import models,Query,Constant
from AssessingPie.models import Address ,QuestionInstance, State_Questions, Topic_States, Question, State, Address, Teacher, Class, \
    Assessment_Record
from AssessingPie.models import School, Student, UserInfo, Subject, Assessment, Student_Assessments
from AssessingPie.models import Topic_Questions, State_Questions, Topic_States, Subject_Topics, Assessment_Record,Topic,User
from google.appengine.ext import ndb
from google.appengine.datastore import datastore_stub_util
#from google.appengine.api.logservice import logservice_stub_util


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()


class ModelTest(unittest.TestCase):

  def setUp(self):
    self.testbed = testbed.Testbed()
    #self.testbed = testbed.Testbed()
    # Then activate the testbed, which prepares the service stubs for use.
    self.testbed.activate()
    self.testbed.setup_env(app_id='assesmentaleks')
    # Next, declare which service stubs you want to use.
    self.policy = datastore_stub_util.PseudoRandomHRConsistencyPolicy(probability=1)
    # Initialize the datastore stub with this policy.
    self.testbed.init_datastore_v3_stub(consistency_policy=self.policy)
    #self.testbed,init_logservice_stub()

    #self.testbed.init_datastore_v3_stub()
    # Populate test entities.
    self._logger = logging.getLogger()
    self._old_log_level = self._logger.getEffectiveLevel()
    logging.info("############")
    #key = ndb.Key(  'Student', 'Ankit')
    entity =Query.addAddress(type=Constant.Constant.ADDRESS_TYPE_HOME,state="UP",city="Meerut",street="12")
    self.assertTrue((isinstance(entity,Address)))
    address1=Query.addAddress(type=Constant.Constant.ADDRESS_TYPE_HOME,state="UP",city="Meerut",street="12")
    if True :
            school=Query.addSchool("CVSchool", address1)
            self.assertTrue((isinstance(school,School)))
            #self.assertIsNone(school.key)
            self.school=school

            ankit_user=Query.addUserInfo("Ankit","Bhatia",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            self.assertTrue((isinstance(ankit_user,UserInfo)))
            self.ankit_user=ankit_user
            kavya_user=Query.addUserInfo("Kavya","Singh",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "kavya@gmail.com", 7667654766)
            self.assertTrue((isinstance(kavya_user,UserInfo)))
            self.kavya_user=kavya_user


            prajjwal_user=Query.addUserInfo("Prajjwal","Ojha",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "prajjwal@gmail.com", 87654766)
            self.assertTrue((isinstance(prajjwal_user,UserInfo)))
            self.prajjwal_user=prajjwal_user


            shiv_user=Query.addUserInfo("Shiv","Sahay",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            self.assertTrue((isinstance(shiv_user,UserInfo)))
            self.shiv_user=shiv_user

            sarthaj_user=Query.addUserInfo("Sarthak","Tiwari",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            self.assertTrue((isinstance(sarthaj_user,UserInfo)))
            self.sarthaj_user=sarthaj_user


            mishika_user=Query.addUserInfo("Mishika","Singh",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "kavya@gmail.com", 7667654766)
            self.assertTrue((isinstance(mishika_user,UserInfo)))
            self.mishika_user=mishika_user





            prasoon_user=Query.addUserInfo("Prasoon","Garg",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "prajjwal@gmail.com", 87654766)
            self.assertTrue((isinstance(prasoon_user,UserInfo)))
            self.prasoon_user=prasoon_user




            pravesh_user=Query.addUserInfo("Pravesh Pal","Sahay",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            self.assertTrue((isinstance(pravesh_user,UserInfo)))
            self.pravesh_user=pravesh_user


            vijay_user=Query.addUserInfo("Vijay","Mehta",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            self.assertTrue((isinstance(vijay_user,UserInfo)))
            self.vijay_user=vijay_user






            sulabh_user=Query.addUserInfo("Sulabj","Jain",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            self.assertTrue((isinstance(sulabh_user,UserInfo)))
            self.sulabh_user=sulabh_user



            #userinfo7=Query.addUserInfo("Smriti","Arora",datetime.datetime.now(),Constant.SEX_FEMALE, address1, "8778", 654766)
            #userinfo8=Query.addUserInfo("Samarath","Tiwari",datetime.datetime.now(),Constant.SEX_FEMALE, address1, "8778", 654766)





            student_vivek=Query.addStudent(ankit_user, school.key,'password')
            self.assertTrue((isinstance(student_vivek,Student)))
            self.student_vivek=student_vivek
            student_kavya=Query.addStudent(kavya_user, school.key,'pwd')
            self.assertTrue((isinstance(student_kavya,Student)))
            self.student_kavya=student_kavya




            student_prajjwal=Query.addStudent(prajjwal_user, school.key,'pwd')
            self.assertTrue((isinstance(student_prajjwal,Student)))
            self.student_prajjwal=student_prajjwal


            student_shiv=Query.addStudent(shiv_user, school.key,'pwd')
            self.assertTrue((isinstance(student_shiv,Student)))
            self.student_shiv=student_shiv

            student_sarthak=Query.addStudent(sarthaj_user, school.key,'pwd')
            self.assertTrue((isinstance(student_sarthak,Student)))
            self.student_sarthak=student_sarthak

            student_mishika=Query.addStudent(mishika_user, school.key,'pwd')
            self.assertTrue((isinstance(student_mishika,Student)))
            self.student_mishika=student_mishika


            student_prasoon=Query.addStudent(prasoon_user, school.key,'pwd')
            self.assertTrue((isinstance(student_prasoon,Student)))
            self.student_prasoon=student_prasoon


            student_pravesh=Query.addStudent(pravesh_user, school.key,'pwd')
            self.assertTrue((isinstance(student_pravesh,Student)))
            self.student_pravesh=student_pravesh



            #teacher1=Query.addTeacher("teacher1", userinfo1, school.key)



            class_VA=Query.addClass(name="Class_V",school_key= school.key,section_details="A",year_session="2013-2014")  #to be changed
            self.assertTrue((isinstance(class_VA,Class)))
            self.class_VA=class_VA


            class_VIB=Query.addClass(name="Class_VI",school_key= school.key,section_details="B",year_session="2013-2014")  #to be changed
            self.assertTrue((isinstance(class_VIB,Class)))
            self.class_VIB=class_VIB



            result=Query.assign_students_to_class(class_VA.key, [student_vivek.key,student_kavya.key,student_prajjwal.key,student_shiv.key])
            self.assertEqual(Constant.Constant.UPDATION_SUCCESSFULL ,result)


            Query.assign_students_to_class(class_VA.key, [student_sarthak.key,student_mishika.key,student_prasoon.key,student_pravesh.key])
            self.assertEqual(Constant.Constant.UPDATION_SUCCESSFULL ,result)






            teacher_vijay=Query.addTeacher( vijay_user, school.key,"password")
            self.assertTrue((isinstance(teacher_vijay,Teacher)))
            self.teacher_vijay=teacher_vijay

            teacher_sulabh=Query.addTeacher( sulabh_user, school.key,"")
            self.assertTrue((isinstance(teacher_sulabh,Teacher)))
            self.teacher_sulabh=teacher_sulabh




            result=Query.assign_classes_to_teacher(teacher_vijay.key,[class_VA.key])
            self.assertEqual(Constant.Constant.UPDATION_SUCCESSFULL ,result)







            Query.assign_classes_to_teacher(teacher_vijay.key,[class_VA.key])
            self.assertEqual(Constant.Constant.UPDATION_SUCCESSFULL ,result)



            subject_maths=Query.addSubject(Constant.Subject.TYPE_CLASS, Constant.Subject.SUBJECT_MATHS,school.key,class_VA.key)
            self.assertTrue((isinstance(subject_maths,Subject)))
            self.subject_maths=subject_maths



            #subject2=Query.addSubject(Subject.TYPE_CLASS, Subject.SUBJECT_SCIENCE,school.key,class1.key)
            subject_english=Query.addSubject(Constant.Subject.TYPE_CLASS, Constant.Subject.SUBJECT_ENGLISH,school.key,class_VA.key)
            self.assertTrue((isinstance(subject_english,Subject)))
            self.subject_english=subject_english





            #subject4=Query.addSubject(Subject.TYPE_CLASS, Subject.SUBJECT_GEOLOGY,school.key,class1.key)

            result=Query.assign_subjects_to_class(class_VA.key, [subject_maths.key])
            self.assertEqual(Constant.Constant.UPDATION_SUCCESSFULL ,result)



            result=Query.assign_subjects_to_class(class_VA.key, [subject_english.key])
            self.assertEqual(Constant.Constant.UPDATION_SUCCESSFULL ,result)

            result=Query.assign_subjects_to_teacher(teacher_vijay.key,[subject_maths.key])
            self.assertEqual(Constant.Constant.UPDATION_SUCCESSFULL ,result)


            result=Query.assign_subjects_to_teacher(teacher_vijay.key,[subject_english.key])
            self.assertEqual(Constant.Constant.UPDATION_SUCCESSFULL ,result)







            topic_number=Query.addTopic(school_key=school.key,name="Number_System", prerequisite_topics=[],subject_key=subject_maths.key)
            self.assertTrue((isinstance(topic_number,Topic)))
            self.topic_number=topic_number





            topic_trig=Query.addTopic(school_key=school.key,name="Trigonimetric_Ratio", prerequisite_topics=[topic_number.key],subject_key=subject_maths.key)
            self.assertTrue((isinstance(topic_trig,Topic)))
            self.topic_trig=topic_trig




            topic_height=Query.addTopic(school_key=school.key,name="Height & Distance", prerequisite_topics=[topic_trig.key,topic_number.key],subject_key=subject_maths.key)
            self.assertTrue((isinstance(topic_height,Topic)))
            self.topic_height=topic_height





            topic_circle=Query.addTopic(school_key=school.key,name="Circle_operation", prerequisite_topics=[topic_number.key],subject_key=subject_maths.key)
            self.assertTrue((isinstance(topic_circle,Topic)))
            self.topic_circle=topic_circle



            topic_part=Query.addTopic(school_key=school.key,name="Part of Speech", prerequisite_topics=[],subject_key=subject_english.key)
            self.assertTrue((isinstance(topic_part,Topic)))
            self.topic_part=topic_part




            topic_tenses=Query.addTopic(school_key=school.key,name="Tenses", prerequisite_topics=[],subject_key=subject_english.key)
            self.assertTrue((isinstance(topic_tenses,Topic)))
            self.topic_tenses=topic_tenses


            topic_sentences=Query.addTopic(school_key=school.key,name="Sentences", prerequisite_topics=[topic_part.key],subject_key=subject_english.key)
            self.assertTrue((isinstance(topic_sentences,Topic)))
            self.topic_sentences=topic_sentences



            topic_voices=Query.addTopic(school_key=school.key,name="Voices", prerequisite_topics=[topic_sentences.key,topic_part.key],subject_key=subject_english.key)
            self.assertTrue((isinstance(topic_voices,Topic)))
            self.topic_voices=topic_voices




            #topic5=Query.addTopic(school_key=school.key,name="Ellipse ", prerequisite_topics=[topic.key],subject_key=subject1.key)
            questioninstance_number1=Query.addQuestionInstance(problem_statement="sum of 2+3 ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["4","6","7","8"], answers=["5"],school_key=school.key)
            self.assertTrue((isinstance(questioninstance_number1,QuestionInstance)))
            self.questioninstance_number1=questioninstance_number1



            questioninstance_number2=Query.addQuestionInstance(problem_statement="sum of 222+30 ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["252","600","227","8"], answers=["252"],school_key=school.key)
            self.assertTrue((isinstance(questioninstance_number2,QuestionInstance)))
            self.questioninstance_number2=questioninstance_number2


            questioninstance_number3=Query.addQuestionInstance(problem_statement="quotient of 58 by 9 ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["252","600","227","8"], answers=["6"],school_key=school.key)
            self.assertTrue((isinstance(questioninstance_number3,QuestionInstance)))
            self.questioninstance_number3=questioninstance_number3




            questioninstance_number4=Query.addQuestionInstance(problem_statement="Value of sin 90 ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["-1","2","0","1"], answers=["1"],school_key=school.key)
            self.assertTrue((isinstance(questioninstance_number4,QuestionInstance)))
            self.questioninstance_number4=questioninstance_number4


            questioninstance_trig1=Query.addQuestionInstance(problem_statement="sin(90+A) ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["sinA","CosA","-SinA","-CosA"], answers=["252"],school_key=school.key)
            self.assertTrue((isinstance(questioninstance_trig1,QuestionInstance)))
            self.questioninstance_trig1=questioninstance_trig1


            questioninstance_trig2=Query.addQuestionInstance(problem_statement="Area of square of arm length a ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["pie*a*a","a*a","a*a*a","-a*a"], answers=["a*a"],school_key=school.key)
            self.assertTrue((isinstance(questioninstance_trig2,QuestionInstance)))
            self.questioninstance_trig2=questioninstance_trig2


            questioninstance_trig3=Query.addQuestionInstance(problem_statement="Area of circle of arm radius a ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["4","6","7","8"], answers=["pie*a*a"],school_key=school.key)
            self.assertTrue((isinstance(questioninstance_trig3,QuestionInstance)))
            self.questioninstance_trig3=questioninstance_trig3




            questioninstance_trig4=Query.addQuestionInstance(problem_statement="Area of circle of arm radius a ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["4","6","7","8"], answers=["pie*a*a"],school_key=school.key)
            self.assertTrue((isinstance(questioninstance_trig4,QuestionInstance)))
            self.questioninstance_trig4=questioninstance_trig4



            questioninstance_height1=Query.addQuestionInstance(problem_statement="tanA= CosA/SinA True ? ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["T","F"], answers=["F"],school_key=school.key)
            self.assertTrue((isinstance(questioninstance_height1,QuestionInstance)))
            self.questioninstance_height1=questioninstance_height1

            questioninstance_height3=Query.addQuestionInstance(problem_statement="CotA= SinA-CosA True ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["T","F"], answers=["F"],school_key=school.key)
            self.assertTrue((isinstance(questioninstance_height3,QuestionInstance)))
            self.questioninstance_height3=questioninstance_height3



            questioninstance_height4=Query.addQuestionInstance(problem_statement="Sin90 =", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["1","0","2","200"], answers=["1"],school_key=school.key)
            self.assertTrue((isinstance(questioninstance_height4,QuestionInstance)))
            self.questioninstance_height4=questioninstance_height4




            questioninstance_height2=Query.addQuestionInstance(problem_statement="Cos(90+A)", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["-SinA","CosA","SinB","CosecA"], answers=["-SinA"],school_key=school.key)
            self.assertTrue((isinstance(questioninstance_height2,QuestionInstance)))
            self.questioninstance_height2=questioninstance_height2


            questioninstance_circle1=Query.addQuestionInstance(problem_statement="area of circle  ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["pie*r*r","r*r","r","2r"], answers=["pie*r*r"],school_key=school.key)
            self.assertTrue((isinstance(questioninstance_circle1,QuestionInstance)))
            self.questioninstance_circle1=questioninstance_circle1


            questioninstance_circle2=Query.addQuestionInstance(problem_statement="diameter of circle", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["r","2*r","r*r","pie*r*r"], answers=["2*r"],school_key=school.key)
            self.assertTrue((isinstance(questioninstance_circle2,QuestionInstance)))
            self.questioninstance_circle2=questioninstance_circle2

            questioninstance_circle3=Query.addQuestionInstance(problem_statement="circumference of circle", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["r","2**pie*r","r*r","pie*r*r"], answers=["2**pie*r"],school_key=school.key)
            self.assertTrue((isinstance(questioninstance_circle3,QuestionInstance)))
            self.questioninstance_circle3=questioninstance_circle3

            questioninstance_circle4=Query.addQuestionInstance(problem_statement="if r=4 diameter is ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["4","6","7","8"], answers=["8"],school_key=school.key)
            self.assertTrue((isinstance(questioninstance_circle4,QuestionInstance)))
            self.questioninstance_circle4=questioninstance_circle4



            question_number1=Query.addQuestion(questioninstance_number1,school.key)
            self.assertTrue((isinstance(question_number1,Question)))
            self.question_number1=question_number1

            question_number2=Query.addQuestion(questioninstance_number2,school.key)
            self.assertTrue((isinstance(question_number2,Question)))
            self.question_number2=question_number2

            question_number3=Query.addQuestion(questioninstance_number3,school.key)
            self.assertTrue((isinstance(question_number3,Question)))
            self.question_number3=question_number3

            question_number4=Query.addQuestion(questioninstance_number4,school.key)
            self.assertTrue((isinstance(question_number4,Question)))
            self.question_number4=question_number4




            question_trig1=Query.addQuestion(questioninstance_trig1,school.key)
            self.assertTrue((isinstance(question_trig1,Question)))
            self.question_trig1=question_trig1

            question_trig2=Query.addQuestion(questioninstance_trig2,school.key)
            self.assertTrue((isinstance(question_trig2,Question)))
            self.question_trig2=question_trig2


            question_trig3=Query.addQuestion(questioninstance_trig3,school.key)
            self.assertTrue((isinstance(question_trig3,Question)))
            self.question_trig3=question_trig3

            question_trig4=Query.addQuestion(questioninstance_trig4,school.key)
            self.assertTrue((isinstance(question_trig4,Question)))
            self.question_trig4=question_trig4



            question_height1=Query.addQuestion(questioninstance_height1,school.key)
            self.assertTrue((isinstance(question_height1,Question)))
            self.question_height1=question_height1

            question_height2=Query.addQuestion(questioninstance_height2,school.key)
            self.assertTrue((isinstance(question_height2,Question)))
            self.question_height2=question_height2

            question_height3=Query.addQuestion(questioninstance_height3,school.key)
            self.assertTrue((isinstance(question_height3,Question)))
            self.question_height3=question_height3



            question_height4=Query.addQuestion(questioninstance_height4,school.key)
            self.assertTrue((isinstance(question_height4,Question)))
            self.question_height4=question_height4




            question_circle1=Query.addQuestion(questioninstance_circle1,school.key)
            self.assertTrue((isinstance(question_circle1,Question)))
            self.question_circle1=question_circle1

            question_circle2=Query.addQuestion(questioninstance_circle2,school.key)
            self.assertTrue((isinstance(question_circle2,Question)))
            self.question_circle2=question_circle2


            question_circle3=Query.addQuestion(questioninstance_circle3,school.key)
            self.assertTrue((isinstance(question_circle3,Question)))
            self.question_circle3=question_circle3

            question_circle4=Query.addQuestion(questioninstance_circle4,school.key)
            self.assertTrue((isinstance(question_circle4,Question)))
            self.question_circle4=question_circle4






            state1=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            self.assertTrue((isinstance(state1,State)))
            self.state1=state1


            state2=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            self.assertTrue((isinstance(state2,State)))
            self.state2=state2


            state3=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            self.assertTrue((isinstance(state3,State)))
            self.state3=state3






            result=Query.assign_questions_to_state(state1.key, [question_number1.key,question_number2.key,question_number3.key,question_number4.key,question_circle1.key,question_circle2.key,question_circle3.key,question_circle4.key,question_height1.key,question_height2.key,question_height3.key,question_height4.key,question_circle1.key,question_circle2.key,question_circle3.key,question_circle4.key],school.key)
            self.assertEqual(Constant.Constant.UPDATION_SUCCESSFULL ,result)






            result=Query.assign_questions_to_topic(topic_number.key,[question_number1.key,question_number2.key,question_number3.key,question_number4.key],school.key)
            self.assertEqual(Constant.Constant.UPDATION_SUCCESSFULL ,result)


            result=Query.assign_questions_to_topic(topic_trig.key,[question_trig1.key,question_trig2.key,question_trig3.key,question_trig4.key],school.key)
            self.assertEqual(Constant.Constant.UPDATION_SUCCESSFULL ,result)


            result=Query.assign_questions_to_topic(topic_circle.key,[question_circle1.key,question_circle2.key,question_circle3.key,question_circle4.key],school.key)
            self.assertEqual(Constant.Constant.UPDATION_SUCCESSFULL ,result)


            result=Query.assign_questions_to_topic(topic_height.key,[question_height1.key,question_height2.key,question_height3.key,question_height4.key],school.key)
            self.assertEqual(Constant.Constant.UPDATION_SUCCESSFULL ,result)




            #a=Query.assign_states_to_topic_by_name("Number  System",[state1.key,state2.key,state3.key],school.key)            #Query.assign_assessment_state_to_student(student.key, assessment1.key,state1.key)

            result=Query.assign_states_to_topic(topic_number.key, [state1.key,state2.key,state3.key],school.key)
            self.assertEqual(Constant.Constant.UPDATION_SUCCESSFULL ,result)



            result=Query.assign_states_to_topic(topic_height.key, [state1.key,state2.key,state3.key],school.key)
            self.assertEqual(Constant.Constant.UPDATION_SUCCESSFULL ,result)



            result=Query.assign_states_to_topic(topic_trig.key, [state1.key,state2.key,state3.key],school.key)
            self.assertEqual(Constant.Constant.UPDATION_SUCCESSFULL ,result)

            result=Query.assign_states_to_topic(topic_circle.key, [state1.key,state2.key,state3.key],school.key)
            self.assertEqual(Constant.Constant.UPDATION_SUCCESSFULL ,result)







            assessment1=Query.addAssessment(name="Assessment1",list_topic_key=[topic_number.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            self.assertTrue((isinstance(assessment1,Assessment)))
            self.assessment1=assessment1


            assessment2=Query.addAssessment(name="Assessment2",list_topic_key=[topic_number.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            self.assertTrue((isinstance(assessment2,Assessment)))
            self.assessment2=assessment2


            assessment3=Query.addAssessment(name="Assessment3",list_topic_key=[topic_trig.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            self.assertTrue((isinstance(assessment3,Assessment)))
            self.assessment3=assessment3


            assessment4=Query.addAssessment(name="Assessment4",list_topic_key=[topic_height.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            self.assertTrue((isinstance(assessment4,Assessment)))
            self.assessment4=assessment4

            assessment5=Query.addAssessment(name="Assessment5",list_topic_key=[topic_height.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            self.assertTrue((isinstance(assessment5,Assessment)))
            self.assessment5=assessment5

            assessment6=Query.addAssessment(name="Assessment6",list_topic_key=[topic_circle.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            self.assertTrue((isinstance(assessment6,Assessment)))
            self.assessment6=assessment6


            assessment7=Query.addAssessment(name="Assessment7",list_topic_key=[topic_circle.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime.now(),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)
            self.assertTrue((isinstance(assessment7,Assessment)))
            self.assessment7=assessment7




            result=Query.update_assessment_detail_of_student(student_key=student_vivek.key, assessment_key=assessment1.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number2.key,score=40,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))





            result=Query.update_assessment_detail_of_student(student_key=student_vivek.key, assessment_key=assessment1.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number2.key,score=40,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))







            result=Query.update_assessment_detail_of_student(student_key=student_vivek.key, assessment_key=assessment2.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number3.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))



            result=Query.update_assessment_detail_of_student(student_key=student_vivek.key, assessment_key=assessment3.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_trig2.key,score=80,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))

            result=Query.update_assessment_detail_of_student(student_key=student_kavya.key, assessment_key=assessment1.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number2.key,score=70,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))



            result=Query.update_assessment_detail_of_student(student_key=student_kavya.key, assessment_key=assessment2.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number4.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))


            result=Query.update_assessment_detail_of_student(student_key=student_kavya.key, assessment_key=assessment3.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_trig3.key,score=40,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))



            result=Query.update_assessment_detail_of_student(student_key=student_kavya.key, assessment_key=assessment4.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_height1.key,score=80,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))




            result=Query.update_assessment_detail_of_student(student_key=student_kavya.key,  assessment_key=assessment5.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_height4.key,score=90,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))


            result=Query.update_assessment_detail_of_student(student_key=student_kavya.key, assessment_key=assessment6.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_circle1.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))


            result=Query.update_assessment_detail_of_student(student_key=student_kavya.key, assessment_key=assessment7.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_circle3.key,score=34,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))



            result=Query.update_assessment_detail_of_student(student_key=student_mishika.key, assessment_key=assessment1.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number2.key,score=30,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))


            result=Query.update_assessment_detail_of_student(student_key=student_mishika.key, assessment_key=assessment2.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number3.key,score=40,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))


            result=Query.update_assessment_detail_of_student(student_key=student_mishika.key, assessment_key=assessment3.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_trig2.key,score=30,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))



            result=Query.update_assessment_detail_of_student(student_key=student_mishika.key, assessment_key=assessment4.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_height2.key,score=80,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))



            result=Query.update_assessment_detail_of_student(student_key=student_sarthak.key, assessment_key=assessment7.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_circle4.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))


            result=Query.update_assessment_detail_of_student(student_key=student_sarthak.key, assessment_key=assessment1.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number2.key,score=20,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))


            result=Query.update_assessment_detail_of_student(student_key=student_sarthak.key, assessment_key=assessment2.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_number4.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))


            result=Query.update_assessment_detail_of_student(student_key=student_sarthak.key, assessment_key=assessment3.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_trig3.key,score=75,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))



            result=Query.update_assessment_detail_of_student(student_key=student_prajjwal.key, assessment_key=assessment4.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_height1.key,score=30,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))



            result=Query.update_assessment_detail_of_student(student_key=student_prajjwal.key,  assessment_key=assessment5.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_height4.key,score=70,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))



            result=Query.update_assessment_detail_of_student(student_key=student_prasoon.key, assessment_key=assessment6.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_circle1.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))



            result=Query.update_assessment_detail_of_student(student_key=student_prasoon.key, assessment_key=assessment7.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question_circle3.key,score=100,school_key=school.key,completion_date=datetime.datetime.now())
            self.assertTrue((isinstance(result,Assessment_Record)))

            #self.assertEqual(3,len(userinfo))


  def tearDown(self):
    # There is no need to delete test entities.
    pass

  def test_teacher(self):

    userinfo=Query.login("Vijay_Mehta", "password")
    logging.error("TC Log: Login returns " +str(userinfo))
    self.assertIsNotNone(userinfo,"None retured from login")
    self.assertTrue(isinstance(userinfo,list),"Return type not list for login")
    self.assertEqual(3,len(userinfo)," list for login is not of length 3")
    self.assertEqual(Constant.Constant.TEACHER,userinfo[0],"type of user is not teacher")
    self.assertTrue(isinstance(userinfo[1],Teacher),"user's kind  is not teacher")
    self.assertTrue(isinstance(userinfo[2],datetime.datetime) or (userinfo[2]==None),"user's login time is neither time or None ")



    states=Query.get_states_of_topic(self.topic_number.key)
    logging.error("TC Log: get_states_of_topic " +str(states))
    self.assertIsNotNone(states,"None retured from get_states_of_topic")
    self.assertTrue(isinstance(states,list),"Return type not list for get_states_of_topic")



    questions=Query.get_questions_of_topic(self.topic_number.key)
    logging.error("TC Log: get_questions_of_topic " +str(questions))
    self.assertIsNotNone(questions,"None retured from get_questions_of_topic")
    self.assertTrue(isinstance(questions,list),"Return type not list for get_questions_of_topic")




    questions=Query.get_questions_of_state(self.state1.key)
    logging.error("TC Log: get_questions_of_state " +str(questions))
    self.assertIsNotNone(questions,"None retured from get_questions_of_state")
    self.assertTrue(isinstance(questions,list),"Return type not list for get_questions_of_state")


    subjects=Query.get_subjects_by_student(self.student_vivek.key)
    logging.error("TC Log: get_subjects_by_student " +str(subjects))
    self.assertIsNotNone(subjects,"None retured from get_subjects_by_student")
    self.assertTrue(isinstance(subjects,list),"Return type not list for get_subjects_by_student")
    self.assertTrue(len(subjects)>0,"length list <0")



    subjects=Query.get_subject_details_by_student(self.student_vivek.key)
    logging.error("TC Log: get_subject_details_by_student " +str(subjects))
    self.assertIsNotNone(subjects,"None retured from get_subject_details_by_student")
    self.assertTrue(isinstance(subjects,dict),"Return type not dict for get_subject_details_by_student")
    self.assertTrue(len(subjects)>0,"length dict <0")



    students=Query.get_students_by_class(self.class_VA.key)
    logging.error("TC Log: get_students_by_class " +str(students))
    self.assertIsNotNone(students,"None retured from get_students_by_class")
    self.assertTrue(isinstance(students,list),"Return type not dict for get_students_by_class")
    self.assertTrue(len(subjects)>0,"length list <0")
    for student in students:
            self.assertTrue(isinstance(student,Student),"List element is not student")



    score=Query.get_average_score_by_subject(self.subject_maths.key,self.teacher_vijay.key,self.class_VA.key)
    logging.error("TC Log: get_average_score_by_subject " +str(score))
    self.assertIsNotNone(score,"None retured from get_average_score_by_subject")
    self.assertTrue(isinstance(score,float),"Return type not float for get_average_score_by_subject")
    self.assertTrue(score>0,"score <0")


    mastery=Query.get_average_mastery_by_subject_detailed(self.teacher_vijay.key,self.class_VA.key,self.subject_maths.key)
    logging.error("TC Log: get_average_mastery_by_subject_detailed " +str(mastery))
    self.assertIsNotNone(mastery,"None retured from get_average_mastery_by_subject_detailed")
    self.assertTrue(isinstance(mastery,list),"Return type not list for get_average_mastery_by_subject_detailed")
    self.assertTrue(len(mastery)>0,"length list <0")



    mastery=Query.get_average_mastery_by_subject_of_all_class(self.teacher_vijay.key)
    logging.error("TC Log: get_average_mastery_by_subject_of_all_class " +str(mastery))
    self.assertIsNotNone(mastery,"None retured from get_average_mastery_by_subject_of_all_class")
    self.assertTrue(isinstance(mastery,dict),"Return type not dict for get_average_mastery_by_subject_of_all_class")
    self.assertTrue(len(mastery)>0,"length dict <0")

    mastery=Query.get_mastery_by_student_of_class(self.teacher_vijay.key, self.class_VA.key, self.subject_maths.key)
    logging.error("TC Log: get_mastery_by_student_of_class " +str(mastery))
    self.assertIsNotNone(mastery,"None retured from get_mastery_by_student_of_class")
    self.assertTrue(isinstance(mastery,dict),"Return type not dict for get_mastery_by_student_of_class")
    self.assertTrue(len(mastery)>0,"length dict <0")


    students=Query.get_students_not_logged_in_by_class(self.teacher_vijay.key, self.class_VA.key)
    logging.error("TC Log: get_students_not_logged_in_by_class " +str(students))
    self.assertIsNotNone(students,"None retured from get_students_not_logged_in_by_class")
    self.assertTrue(isinstance(students,dict),"Return type not dict for get_students_not_logged_in_by_class")
    self.assertTrue(len(students)>0,"length dict <0")


    students=Query.get_students_not_logged_in_of_all_class(self.teacher_vijay.key)
    logging.error("TC Log: get_students_not_logged_in_of_all_class " +str(students))
    self.assertIsNotNone(students,"None retured from get_students_not_logged_in_of_all_class")
    self.assertTrue(isinstance(students,dict),"Return type not dict for get_students_not_logged_in_of_all_class")
    self.assertTrue(len(students)>0,"length dict <0")



    mastery=Query.get_average_mastery_all_subject_detailed(self.teacher_vijay.key, self.class_VA.key)
    logging.error("TC Log: get_average_mastery_all_subject_detailed " +str(mastery))
    self.assertIsNotNone(mastery,"None retured from get_average_mastery_all_subject_detailed")
    self.assertTrue(isinstance(mastery,dict),"Return type not dict for get_average_mastery_all_subject_detailed")
    self.assertTrue(len(mastery)>0,"length dict <0")


    coverage=Query.get_assessment_coverage_of_class(self.teacher_vijay.key, self.class_VA.key)
    logging.error("TC Log: get_assessment_coverage_of_class " +str(coverage))
    self.assertIsNotNone(mastery,"None retured from get_assessment_coverage_of_class")
    self.assertTrue(isinstance(coverage,dict),"Return type not dict for get_assessment_coverage_of_class")
    self.assertTrue(len(coverage)>0,"length dict <0")


    coverage=Query.get_assessment_coverage_of_class(self.teacher_vijay.key, self.class_VA.key)
    logging.error("TC Log: get_assessment_coverage_of_class " +str(coverage))
    self.assertIsNotNone(mastery,"None retured from get_assessment_coverage_of_class")
    self.assertTrue(isinstance(coverage,dict),"Return type not dict for get_assessment_coverage_of_class")
    self.assertTrue(len(coverage)>0,"length dict <0")


    ready_to_learn=Query.get_ready_to_learn_of_class(self.teacher_vijay.key, self.class_VA.key,self.subject_maths.key)
    logging.error("TC Log: get_ready_to_learn_of_class " +str(ready_to_learn))
    self.assertIsNotNone(mastery,"None retured from get_ready_to_learn_of_class")
    self.assertTrue(isinstance(ready_to_learn,dict),"Return type not dict for get_ready_to_learn_of_class")
    self.assertTrue(len(ready_to_learn)>0,"length dict <0")



    mastery=Query.get_mastery_by_subject(self.subject_maths.key,self.student_vivek.key)
    logging.error("TC Log: get_mastery_by_subject " +str(score))
    self.assertIsNotNone(mastery,"None retured from get_mastery_by_subject")
    self.assertTrue(isinstance(mastery,float),"Return type not float for get_mastery_by_subject")
    self.assertTrue(mastery>0,"score <0")


    mastery=Query.get_mastery_for_all_subjects(self.student_vivek.key)
    logging.error("TC Log: get_mastery_for_all_subjects " +str(ready_to_learn))
    self.assertIsNotNone(mastery,"None retured from get_mastery_for_all_subjects")
    self.assertTrue(isinstance(mastery,dict),"Return type not dict for get_mastery_for_all_subjects")
    self.assertTrue(len(mastery)>0,"length dict <0")

    growth=Query.get_growth_for_subject(self.student_vivek.key,self.subject_maths.key)
    logging.error("TC Log: get_growth_for_subject " +str(ready_to_learn))
    self.assertIsNotNone(growth,"None retured from get_growth_for_subject")
    self.assertTrue(isinstance(growth,dict),"Return type not dict for get_growth_for_subject")
    self.assertTrue(len(growth)>0,"length dict <0")


    growth=Query.get_growth_for_all_subject(self.student_vivek.key)
    logging.error("TC Log: get_growth_for_all_subject " +str(ready_to_learn))
    self.assertIsNotNone(growth,"None retured from get_growth_for_all_subject")
    self.assertTrue(isinstance(growth,dict),"Return type not dict for get_growth_for_all_subject")
    self.assertTrue(len(growth)>0,"length dict <0")



    mastery=Query.get_mastery_by_topic(self.topic_number.key,self.student_vivek.key)
    logging.error("TC Log: get_mastery_by_topic " +str(score))
    self.assertIsNotNone(mastery,"None retured from get_mastery_by_topic")
    self.assertTrue(isinstance(mastery,int),"Return type not float for get_mastery_by_topic")
    self.assertTrue(mastery>0,"score <0")



    ready_to_learn=Query.get_ready_to_learn_topic(self.topic_number.key,self.student_vivek.key)
    logging.error("TC Log: get_ready_to_learn_topic " +str(ready_to_learn))
    self.assertIsNotNone(ready_to_learn,"None retured from get_ready_to_learn_topic")
    self.assertTrue(isinstance(ready_to_learn,basestring),"Return type not str for get_ready_to_learn_topic")





    ready_to_learn=Query.get_ready_to_learn_of_all_topic(self.subject_maths.key,self.student_vivek.key)
    logging.error("TC Log: get_ready_to_learn_of_all_topic " +str(ready_to_learn))
    self.assertIsNotNone(mastery,"None retured from get_ready_to_learn_of_all_topic")
    self.assertTrue(isinstance(ready_to_learn,dict),"Return type not dict for get_ready_to_learn_of_all_topic")
    self.assertTrue(len(ready_to_learn)>0,"length dict <0")

    '''
    result=Query.get_states_of_topic(self.subject_maths.key,self.topic_number.key)
    self.assertIsNotNone(userinfo)






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

            a=Query.get_ready_to_learn_of_all_topic(subject_maths.key,student_vivek.key)
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
    '''





