
from google.appengine.ext import ndb
import Query
import logging
import datetime

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
            
            userinfo1=Query.addUserInfo("Trish","Kumar",datetime.date(int(2012),int(6),int(6)),Constant.Constant.SEX_MALE, address1, "yyy", 67757)
            Query.signup_student( userinfo1, school.key,"123")
           
            
            userinfo2=Query.addUserInfo("Ankit","Bhatia",datetime.date(int(2012),int(6),int(8)),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            
            userinfo3=Query.addUserInfo("Suraj","Singh",datetime.date(int(2012),int(6),int(8)),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            userinfo4=Query.addUserInfo("Sarthak","Tiwari",datetime.date(int(2012),int(6),int(8)),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            userinfo5=Query.addUserInfo("Vijay","Mehta",datetime.date(int(2012),int(6),int(8)),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            
            #teacher1=Query.addTeacher("teacher1", userinfo1, school.key)
            
            
            teacher1=Query.addTeacher( userinfo5, school.key,"")
            teacher3=Query.addTeacher( userinfo4, school.key,"")
            teacher4=Query.addTeacher( userinfo4, school.key,"")
           # teacher5=Query.addTeacher( userinfo2, school.key,"")
            class1=Query.addClass(name="Class_V",school_key= school.key,section_details="A",year_session="2013-2014")  #to be changed
            class2=Query.addClass(name="Class_VI",school_key= school.key,section_details="B",year_session="2013-2014")  #to be changed
            b=Query.assign_classes_to_teacher(teacher1.key,[class1.key,class2.key])
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
            topic2=Query.addTopic(school_key=school.key,name="Circle operations", prerequisite_topics=[topic.key,topic1.key],subject_key=subject1.key)
            topic3=Query.addTopic(school_key=school.key,name="Square Operations", prerequisite_topics=[topic.key,topic1.key,topic2.key],subject_key=subject2.key)
            topic4=Query.addTopic(school_key=school.key,name="Triangle", prerequisite_topics=[topic.key,topic1.key,topic2.key,topic3.key],subject_key=subject2.key)
            #topic5=Query.addTopic(school_key=school.key,name="Ellipse ", prerequisite_topics=[topic.key],subject_key=subject1.key)
            
            questioninstance=Query.addQuestionInstance(problem_statement="sum of 2+3 ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["4,6,7,8"], answers=["5"],school_key=school.key)
            
            questioninstance2=Query.addQuestionInstance(problem_statement="sum of 222+30 ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["252,600,227,8"], answers=["252"],school_key=school.key)
            questioninstance3=Query.addQuestionInstance(problem_statement="quotient of 58 by 9 ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["252,600,227,8"], answers=["6"],school_key=school.key)
            
            question1=Query.addQuestion(questioninstance,school.key)
           
            question2=Query.addQuestion(questioninstance2,school.key)
            question3=Query.addQuestion(questioninstance3,school.key)
            state1=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            
            state2=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state3=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            #class1=None
            Query.assign_subjects_to_class(class1.key, [subject1.key,subject2.key])
            Query.assign_students_to_class(class1.key, [student1.key,student2.key,student3.key,student4.key])
            
             
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
          
            assessment1=Query.addAssessment(name="Assessment1",list_topic_key=[topic.key],school_key=school.key,date=datetime.date.today(),due_date=datetime.date.today(),published=True,teacher_key=teacher1.key,class_key=class1.key)
            assessment2=Query.addAssessment(name="Assessment2",list_topic_key=[topic.key,topic1.key],school_key=school.key,date=datetime.date.today(),due_date=datetime.date.today(),published=True,teacher_key=teacher1.key,class_key=class1.key)
            assessment3=Query.addAssessment(name="Assessment3",list_topic_key=[topic2.key,topic3.key],school_key=school.key,date=datetime.date.today(),due_date=datetime.date.today(),published=True,teacher_key=teacher1.key,class_key=class1.key)
           
            
           
            Query.get_states_of_topic(topic.key)
            
            
            Query.get_questions_of_state(state1.key)
            Query.get_questions_of_topic(topic.key)
            Query.signup_school("DPS INDIRAPURAM", address1)
            Query.get_subjects_by_student(student1.key)
            Query.get_topics_by_subject(subject1.key)
            
            Query.update_assessment_detail_of_student(student_key=student1.key, assessment_key=assessment1.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question2.key,score=100,school_key=school.key,start_date=datetime.date(int(2012),int(6),int(8)))
            #Query.update_assessment_detail_of_student(student_key=student1.key, assessment_key=assessment2.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question3.key,score=40,school_key=school.key,start_date=datetime.date(int(2012),int(6),int(8)))
            #Query.update_assessment_detail_of_student(student_key=student1.key, assessment_key=assessment3.key,current_state_key= state2.key, next_state_key=state3.key,next_question_key=question3.key,score=100,school_key=school.key,start_date=datetime.date(int(2012),int(6),int(8)))
            Query.get_assessments_by_topic(student1.key, topic.key)
            Query.get_mastery_by_subject(subject1.key,student1.key)
            #a=Query.get_student_score_in_assessment(student1.key, assessment1.key)
            Query.get_student_score_in_assessment(student1.key, assessment1.key)
            Query.get_pending_assessment_subject(subject1.key,student1.key)
            
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
            a=Query.login('Vijay_Mehta','jkjk')
            Query.login("Ankit_Bhatia", "pwd")
            Query.get_pending_assessment_subject_dummy(student1.key)
            Query.get_subjects_of_class(class1.key)
            Query.get_average_score_by_subject(subject1.key,teacher1.key)
            Query.get_average_score_all_subject(subject1.key,teacher1.key)
            Query.get_average_mastery_by_subject_detailed(teacher1.key)
            #Query.get_average_mastery_all_subject_detailed(teacher1.key)
            Query.get_class_details_of_teacher(teacher1.key)
            #tecaher dashboard without any selection
            Query.get_students_not_logged_in_of_all_class(teacher1.key)
            a=Query.get_average_mastery_by_subject_of_all_class(teacher1.key)
            #teacher dashboard when class selected
            Query.get_class_details_of_teacher(teacher1.key)
            '''
            {classkey:classname}
            '''
            Query.get_students_not_logged_in_by_class(teacher1.key, class1.key)
            '''
            {Studentname: date}
            '''
            Query.get_average_mastery_all_subject_detailed(teacher1.key, class1.key)
            '''
            {subjectname: [mastery, {topicname:mastery}]}
            '''
            Query.get_assessment_coverage_of_class(teacher1.key, class1.key)
            '''
            {subjectname: {assessmentId: percntage of people attended}}
            '''
            return a
                        
            
            
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
       
    
