from Constant import Constant
from google.appengine.ext import ndb
import Query
import logging
import datetime
from Constant import Subject
def fill():
      try: 
       
            subject=Query.addSubject(type=Subject.TYPE_CLASS,name="Maths")
            topic=Query.addTopic(name="Number  System", prerequisite_topics=[],subject_key=subject.key)
            topic1=Query.addTopic(name="jbbjjb", prerequisite_topics=[topic.key],subject_key=subject.key)
            #topic=Query.addTopic(name="ththtth", prerequisite_topics=[],subject_key=subject.key)
            
            questioninstance=Query.addQuestionInstance(problem_statement="sum of 2+3 ", type=Constant.QUESTION_TYPE_SINGLE, choices=["4,6,7,8"], answers=["5"])
            questioninstance2=Query.addQuestionInstance(problem_statement="sum of 222+30 ", type=Constant.QUESTION_TYPE_SINGLE, choices=["252,600,227,8"], answers=["252"])
            questioninstance3=Query.addQuestionInstance(problem_statement="quotient of 58 by 9 ", type=Constant.QUESTION_TYPE_SINGLE, choices=["252,600,227,8"], answers=["6"])
            question1=Query.addQuestion(questioninstance)
            question2=Query.addQuestion(questioninstance2)
            question3=Query.addQuestion(questioninstance3)
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
            Query.assign_states_to_topic(topic.key, [state1.key,state2.key,state3.key])
            Query.assign_topics_to_subject(subject.key, [topic.key,topic1.key])
            Query.assign_assessment_to_student(student.key, assessment1.key)
            Query.get_questions_of_state(state1.key)
            Query.get_questions_of_topic(topic.key)
            #Query.assign_assessment_state_to_student(student.key, assessment1.key,state1.key)
            #Query.assign_assessment_score_next_question_to_student(student.key, assessment1.key, state1.key,34,question1.key)
      except Exception :
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
        
      return Constant.UPDATION_SUCCESSFULL  
          
    
      