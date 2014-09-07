
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
            school=Query.addSchool("CVSchool", address1)

            userinfo1=Query.addUserInfo("Trish","Kumar",datetime.date(int(2012),int(6),int(6)),Constant.SEX_MALE, address1, "yyy", 67757)
            Query.signup_student( userinfo1, school.key,"123")


            userinfo2=Query.addUserInfo("Ankit","Bhatia",datetime.date(int(2012),int(6),int(8)),Constant.SEX_FEMALE, address1, "8778", 654766)
            userinfo3=Query.addUserInfo("Suraj","Singh",datetime.date(int(2012),int(6),int(8)),Constant.SEX_FEMALE, address1, "8778", 654766)
            userinfo4=Query.addUserInfo("Sarthak","Tiwari",datetime.date(int(2012),int(6),int(8)),Constant.SEX_FEMALE, address1, "8778", 654766)
            #school=Query.addSchool("CVSchool", address1)'''
            teacher1=Query.addTeacher("teacher1", userinfo1, school.key)
            teacher2=Query.addTeacher("teacher2", userinfo2, school.key)
            teacher3=Query.addTeacher("teacher2", userinfo2, school.key)
            teacher4=Query.addTeacher("teacher2", userinfo2, school.key)
            teacher5=Query.addTeacher("teacher2", userinfo2, school.key)
            class1=Query.addClass(name="Class_V",school_key= school.key,section_details="A",year_session="2013-2014")  #to be changed
            class2=Query.addClass(name="Class_VI",school_key= school.key,section_details="B",year_session="2013-2014")  #to be changed

            student1=Query.addStudent(userinfo2, school.key,'pwd')
            student2=Query.addStudent(userinfo1, school.key,'pwd')
            student3=Query.addStudent(userinfo3, school.key,'pwd')
            student4=Query.addStudent(userinfo4, school.key,'pwd')
            Query.login("Ankit_Bhatia", "pwd")
            Query.login("Suraj_Singh", "pwd")
            subject1=Query.addSubject(Subject.TYPE_CLASS, Subject.SUBJECT_MATHS,school.key)
            subject2=Query.addSubject(Subject.TYPE_CLASS, Subject.SUBJECT_SCIENCE,school.key)


            topic=Query.addTopic(school_key=school.key,name="Number  System", prerequisite_topics=[],subject_key=subject1.key)
            topic1=Query.addTopic(school_key=school.key,name="Float division", prerequisite_topics=[topic.key],subject_key=subject1.key)
            topic2=Query.addTopic(school_key=school.key,name="Circle operations", prerequisite_topics=[],subject_key=subject1.key)
            topic3=Query.addTopic(school_key=school.key,name="Square Operations", prerequisite_topics=[topic.key],subject_key=subject1.key)
            topic4=Query.addTopic(school_key=school.key,name="Triangle", prerequisite_topics=[],subject_key=subject1.key)
            topic5=Query.addTopic(school_key=school.key,name="Ellipse ", prerequisite_topics=[topic.key],subject_key=subject1.key)

            questioninstance=Query.addQuestionInstance(problem_statement="sum of 2+3 ", type=Constant.QUESTION_TYPE_SINGLE, choices=["4,6,7,8"], answers=["5"],school_key=school.key)

            questioninstance2=Query.addQuestionInstance(problem_statement="sum of 222+30 ", type=Constant.QUESTION_TYPE_SINGLE, choices=["252,600,227,8"], answers=["252"],school_key=school.key)
            questioninstance3=Query.addQuestionInstance(problem_statement="quotient of 58 by 9 ", type=Constant.QUESTION_TYPE_SINGLE, choices=["252,600,227,8"], answers=["6"],school_key=school.key)

            question1=Query.addQuestion(questioninstance,school.key)

            question2=Query.addQuestion(questioninstance3,school.key)
            question3=Query.addQuestion(questioninstance2,school.key)
            state1=Query.addState(type=Constant.STATE_IN_TOPIC,school_key=school.key)

            state2=Query.addState(type=Constant.STATE_IN_TOPIC,school_key=school.key)
            state3=Query.addState(type=Constant.STATE_IN_TOPIC,school_key=school.key)
            #class1=None'''
            Query.assign_subjects_to_class(class1.key, [subject1.key,subject1.key])
            Query.assign_students_to_class(class1.key, [student1.key,student2.key])


            Query.assign_questions_to_state(state1.key, [question1.key],school.key)

            Query.assign_questions_to_state(state2.key, [question1.key,question2.key],school.key)
            Query.assign_questions_to_state(state3.key, [question1.key,question2.key,question3.key],school.key)
            Query.assign_questions_to_topic(topic.key,[question1.key,question2.key,question3.key],school.key)
            Query.assign_questions_to_topic(topic1.key,[question1.key,question2.key,question3.key],school.key)
            Query.assign_questions_to_topic(topic2.key,[question1.key,question2.key,question3.key],school.key)
            Query.assign_questions_to_topic(topic3.key,[question1.key,question2.key,question3.key],school.key)
            #a=Query.assign_states_to_topic_by_name("Number  System",[state1.key,state2.key,state3.key],school.key)            #Query.assign_assessment_state_to_student(student.key, assessment1.key,state1.key)
            Query.assign_states_to_topic(topic.key, [state1.key,state2.key,state3.key],school.key)
            Query.assign_states_to_topic(topic1.key, [state1.key,state2.key,state3.key],school.key)
            Query.assign_states_to_topic(topic2.key, [state1.key,state2.key,state3.key],school.key)
            Query.assign_states_to_topic(topic3.key, [state1.key,state2.key,state3.key],school.key)
            Query.assign_states_to_topic(topic4.key, [state1.key,state2.key,state3.key],school.key)
            Query.assign_topics_to_subject(subject1.key, [topic.key,topic1.key,topic3.key,topic4.key],school.key)

            assessment1=Query.addAssessment(name="Assessment1",school_key=school.key,list_topic_key=[topic.key],date=datetime.date.today())
            assessment2=Query.addAssessment(name="Assessment2",school_key=school.key,list_topic_key=[topic1.key],date=datetime.date.today())
            assessment3=Query.addAssessment(name="Assessment3",school_key=school.key,list_topic_key=[topic3.key],date=datetime.date.today())
            assessment4=Query.addAssessment(name="Assessment4",school_key=school.key,list_topic_key=[topic4.key],date=datetime.date.today())


            Query.assign_assessment_to_student(student1.key, assessment1.key)
            Query.assign_assessment_to_student(student1.key, assessment2.key)
            Query.assign_assessment_to_student(student1.key, assessment3.key)
            Query.assign_assessment_to_student(student1.key, assessment4.key)
            Query.get_states_of_topic(topic.key)

            Query.update_assessment_detail_of_student(student1.key, assessment1.key, state2.key, state3.key,question2.key, 16)
            Query.update_assessment_detail_of_student(student1.key, assessment2.key, state2.key, state3.key,question2.key, 16)
            '''
            Query.get_questions_of_state(state1.key)
            Query.get_questions_of_topic(topic.key)
            Query.signup_school("DPS INDIRAPURAM", address1)
            Query.get_subjects_by_student(student1.key)
            Query.get_topics_by_subject(subject1.key)

            a=Query.get_assessments_by_topic(student1.key, topic.key)
            Query.get_mastery_by_subject(subject1.key,student1.key)
            Query.get_student_score_in_assessment(student1.key, assessment1.key)
            Query.get_pending_assessment_subject(subject1.key,student1.key)

            Query.get_mastery_by_topic(topic.key,student1.key)
            Query.get_mastery_for_all_subjects(student1.key)
            Query.get_growth_for_all_topic_subject(student1.key,subject1.key)
            Query.get_growth_for_subject(student1.key,subject1.key)
            a=Query.get_ready_to_learn_topic(topic.key,student1.key)'''
      except Exception :
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
        
      return Constant.UPDATION_SUCCESSFULL  
          
    
      