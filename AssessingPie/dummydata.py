
from Constant import Constant
from google.appengine.ext import ndb
import Query
import logging
import datetime

from Constant import Subject,Constant,UserType
from Query import addSubject, addTopic
def fill():
      try: 
            
            address1=Query.addAddress(type=Constant.ADDRESS_TYPE_HOME,state="UP",city="Meerut",street="12")
            userinfo1=Query.addUserInfo("user1",datetime.date(int(2012),int(6),int(6)),Constant.SEX_MALE, address1, "yyy", 67757)
            userinfo2=Query.addUserInfo("user2",datetime.date(int(2012),int(6),int(8)),Constant.SEX_FEMALE, address1, "8778", 654766)
            school=Query.addSchool("school1", address1)
            teacher1=Query.addTeacher("teacher1", userinfo1, school.key)
            teacher2=Query.addTeacher("teacher2", userinfo2, school.key)
            class1=Query.addClass(name="Class_V",school_key= school.key,section_details="A",year_session="2013-2014")  #to be changed
           # class1=Query.addClass("Class1",  school.key, "A,B", "2012-2013")
            student1=Query.addStudent("anks.315",userinfo2, school.key)
            student2=Query.addStudent("rahulshri",userinfo1, school.key)
            subject1=Query.addSubject(Subject.TYPE_CLASS, Subject.SUBJECT_MATHS,school.key)
            subject2=Query.addSubject(Subject.TYPE_CLASS, Subject.SUBJECT_ENGLISH,school.key)
            subject3=Query.addSubject(Subject.TYPE_CLASS, Subject.SUBJECT_SCIENCE,school.key)

         
            
            #Query.addSubject(type=Subject.TYPE_CLASS,name="Maths",school_key=school.key)
            topic=Query.addTopic(school_key=school.key,name="  Number  System", prerequisite_topics=[],subject_key=subject1.key)
            topic1=Query.addTopic(school_key=school.key,name="jbbjjb", prerequisite_topics=[topic.key],subject_key=subject1.key)
            #topic=Query.addTopic(name="ththtth", prerequisite_topics=[],subject_key=subject.key)
            
            questioninstance=Query.addQuestionInstance(problem_statement="sum of 2+3 ", type=Constant.QUESTION_TYPE_SINGLE, choices=["4,6,7,8"], answers=["5"],school_key=school.key)
            questioninstance2=Query.addQuestionInstance(problem_statement="sum of 222+30 ", type=Constant.QUESTION_TYPE_SINGLE, choices=["252,600,227,8"], answers=["252"],school_key=school.key)
            questioninstance3=Query.addQuestionInstance(problem_statement="quotient of 58 by 9 ", type=Constant.QUESTION_TYPE_SINGLE, choices=["252,600,227,8"], answers=["6"],school_key=school.key)
            question1=Query.addQuestion(questioninstance,school.key)
            question2=Query.addQuestion(questioninstance2,school.key)
            question3=Query.addQuestion(questioninstance3,school.key)
            state1=Query.addState(type=Constant.STATE_IN_TOPIC,school_key=school.key)
            state2=Query.addState(type=Constant.STATE_IN_TOPIC,school_key=school.key)
            state3=Query.addState(type=Constant.STATE_IN_TOPIC,school_key=school.key)
           
            userinfo=Query.addUserInfo("jhjjj",datetime.date(int(2012),int(6),int(6)),Constant.SEX_MALE, address1, "yyy", 67757)
              
            Query.assign_students_to_class(class1.key, [student1.key,student2.key])
            Query.assign_subjects_to_class(class1.key, [subject1.key,subject2.key,subject3.key])
            
            Query.assign_questions_to_state(state1.key, [question1.key])
            Query.assign_questions_to_state(state2.key, [question1.key,question2.key])
            Query.assign_questions_to_state(state3.key, [question1.key,question2.key,question3.key])
            Query.assign_questions_to_topic(topic.key,[question1.key,question2.key,question3.key])
            Query.assign_states_to_topic(topic.key, [state1.key,state2.key,state3.key])
            Query.assign_topics_to_subject(subject1.key, [topic.key,topic1.key])
            
            assessment1=Query.addAssessment(name="Assessment1",school_key=school.key,list_topic_key=[topic.key])
            Query.assign_assessment_to_student(student1.key, assessment1.key)
            Query.get_states_of_topic(topic.key)
            #Query.assign_assessment_to_topic(assessment1.key, topic.key)
            #Query.assign_assessment_to_topic(student1.key, assessment1.key)
            #Query.assign_assessment_state_to_student(student1.key, assessment1.key, states_of_or_in_assessment)
            Query.get_questions_of_state(state1.key)
            Query.get_questions_of_topic(topic.key)
            Query.signup_school("DPS INDIRAPURAM", address1)
            Query.signup_student("kapilaaaaa", userinfo1, school.key)
            ndb.Rollback( Query.signup_student("kapilaaaaa", userinfo1, school.key))
            Query.signup_teacher("kapil", userinfo1, school.key)
            Query.assign_classes_to_teacher(teacher1.key, [class1.key])
            Query.assign_subjects_to_class(class1.key,[subject1.key,subject2.key,subject3.key])
            Query.login("kapil",UserType.STUDENT)
            Query.get_subjects_by_student(student1.key)
            Query.get_topics_by_subject(subject1.key)
            Query.update_assessment_detail_of_student(student1.key, assessment1.key, state2.key, state3.key,question2.key, 16)
            Query.get_assessments_by_student(student1.key)
            Query.get_classes_of_teacher(teacher1.key)
            Query.get_subjects_of_class(class1.key)
            Query.get_student_current_state_in_assessment(student1.key, assessment1.key)
            Query.get_student_next_question_in_assessment(student1.key, assessment1.key)
            Query.get_student_score_in_assessment(student1.key, assessment1.key)
            Query.get_topics_by_subject(subject1.key)
            a=Query.get_students_by_class(class1.key)
            """subject=Query.addSubject(type=Subject.TYPE_CLASS,name="hhj")
            topic=Query.addTopic(name="ththtth", prerequisite_topics=[],subject_key=subject.key)
            topic1=Query.addTopic(name="jbbjjb", prerequisite_topics=[topic.key],subject_key=subject.key)
            #topic=Query.addTopic(name="ththtth", prerequisite_topics=[],subject_key=subject.key)
            
            questioninstance=Query.addQuestionInstance(problem_statement="sum of 2+3 ", type=Constant.QUESTION_TYPE_SINGLE, choices=["4,6,7,8"], answers=["5"])
            questioninstance2=Query.addQuestionInstance(problem_statement="sum of 222+30 ", type=Constant.QUESTION_TYPE_SINGLE, choices=["252,600,227,8"], answers=["252"])
            questioninstance3=Query.addQuestionInstance(problem_statement="sum of 222+30 ", type=Constant.QUESTION_TYPE_SINGLE, choices=["252,600,227,8"], answers=["252"])
            question1=Query.addQuestion(questioninstance)
            question2=Query.addQuestion(questioninstance3)
            question3=Query.addQuestion(questioninstance2)
            logging.error("%554544454544344444444444444444444444444"+str(question3.instance.problem_statement))
            state1=Query.addState(type=Constant.STATE_IN_TOPIC)
            state2=Query.addState(type=Constant.STATE_IN_TOPIC)
            state3=Query.addState(type=Constant.STATE_IN_TOPIC)
            assessment1=Query.addAssessment()
            address=Query.addAddress(Constant.ADDRESS_TYPE_HOME,"gg","rgge")
            userinfo=Query.addUserInfo("jhjjj",datetime.date(int(2012),int(6),int(6)),Constant.SEX_MALE, address, "yyy", 67757)
            school=Query.addSchool("jhhj", address)
            #basic_info,school,class_deatils,section_details
            student=Query.addStudent("anks.315",userinfo, school,"Class1","Section1")
            Query.assign_questions_to_state(state1.key, [question1.key])
            Query.assign_questions_to_state(state2.key, [question1.key,question2.key])
            Query.assign_questions_to_state(state3.key, [question1.key,question2.key,question3.key])
            Query.assign_questions_to_topic(topic.key,[question1.key,question2.key,question3.key])
            Query.assign_states_to_topic(topic.key, [state1.key,state2.key])
            Query.assign_topics_to_subject(subject.key, [topic.key,topic1.key])
            Query.assign_assessment_to_student(student.key, assessment1.key)
            Query.get_questions_of_state(state1.key)
            Query.get_questions_of_topic(topic.key)
            Query.get_questions_by_topic_name(topic_name="ththtth")
            
            
            return a"""
      except Exception :
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
        
      return Constant.UPDATION_SUCCESSFULL  
          
    
      