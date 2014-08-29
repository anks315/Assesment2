from google.appengine.ext.ndb import Key
from google.appengine.ext import ndb
import logging
import datetime
import Constant
from models import QuestionInstance,State_Questions,Topic_States,Question,State,Topic,Address,Teacher,Class
from models import School,Student,UserInfo,Subject,Assessment,Student_Assessments,School_Assessments
from  models import Assessment_States,Topic_Questions,State_Questions,Topic_States,Subject_Topics
from Constant import Constant,UserType





"""
login for users
            type: determines the user Type from Constant.py
"""
def login(username,type):
      logging.info("CV Logs :Inside login :")
      try: 
        if type==UserType.SCHOOL:
            user=School.query(School.code == username).get()
        elif type==UserType.STUDENT:
            user=Student.query(Student.username == username).get()
        elif type==UserType.TEACHER:
            user=Teacher.query(Teacher.username == username).get()
        else :
            logging.info("CV Logs : failed to login for username :"+username+":type "+type)
            return Constant.ERROR_BAD_VALUE
      except Exception :
        logging.exception("")
        logging.info("CV Logs : failed to login for username :"+username+":type "+type)
        return Constant.ERROR_BAD_VALUE
        
      if user==None:
        return Constant.ERROR_INVALID_USER
      logging.info("CV Logs : success to login for username :"+username+":type "+type)
      return user

"""
Sign up for a school
"""
def signup_school(name,address):
      logging.info("CV Logs : inside signup_school ")
      try:
          school=addSchool(name,address)
          if not  isinstance(school, School):
              
           return Constant.ERROR_BAD_VALUE   
      except Exception:
           logging.error("CV Logs : failed to sign up for school :"+school.name)
           return Constant.ERROR_OPERATION_FAIL 
      logging.info("CV Logs : success to sign up for school :"+school.name)  
      return school

"""
Sign up for a teacher

"""
def signup_teacher(username,basic_info,school_key):
      logging.info("CV Logs : inside signup_teacher ")
      try:
          teacher=addTeacher(username,basic_info,school_key)
          if not  isinstance(teacher, Teacher):
               return Constant.ERROR_BAD_VALUE 
      except Exception:
          logging.error("CV Logs : failed to sign up for teacher :"+teacher.basic_info.name)
          return Constant.ERROR_OPERATION_FAIL
      logging.info("CV Logs : success to sign up for teacher :"+teacher.basic_info.name)  
      return teacher

"""
Sign up for a student

"""

def signup_student(username,basic_info,school_key):
      logging.info("CV Logs : inside signup_student ")
      try:
          student=addStudent(username,basic_info,school_key)
          if not  isinstance(student, Student):
               return Constant.ERROR_BAD_VALUE
      except Exception:
          logging.error("CV Logs : failed to sign up for student :"+student.basic_info.name)
          return Constant.ERROR_BAD_VALUE 
      logging.info("CV Logs : success to sign up for student :"+student.basic_info.name)
      return student


"""
Adds a new question instance 
    problem_statement : Problem Statement String
    type : QUESTION_TYPE_SINGLE or QUESTION_TYPE_MULTIPLE
    choices : List of options e.g. ["1","3","10"]
    answers :: List of correct answer e.g. ["1","3","10"]
"""
def addQuestionInstance(problem_statement, type,school_key, choices=[], answers=[]):
   logging.info("CV Logs : Inside addQuestionInstance") 
   try :
       question_instance = QuestionInstance(parent=school_key,problem_statement=problem_statement, type=type, choices=choices, answer=answers)
       question_instance.put()
   except Exception:
       logging.exception("")
       logging.error("CV Logs : failed to add question instance :"+question_instance.problem_statement)
       return Constant.ERROR_BAD_VALUE
   logging.info("CV Logs : success to add question instance :"+question_instance.problem_statement) 
   return question_instance;
  

"""
Adds a question to db :
                    question_instance: An entity object of kind QuestionInstance
                    
                    ==> raises : BadValueError
"""    
def addQuestion(question_instance,school_key):
   logging.info("CV Logs : Inside addQuestion") 
   try:
       if not isinstance(question_instance,QuestionInstance):
           return Constant.ERROR_BAD_VALUE
       question = Question(parent=school_key,instance=question_instance) 
       question.put()
       logging.info("CV Logs : success to add question  :"+question.instance.problem_statement)    
       return question;  
   except Exception:
       logging.exception("")
       logging.error("CV Logs : failed to add question  :"+question.instance.problem_statement)
       return Constant.ERROR_BAD_VALUE 
       
"""
upadte a question :
                    question_instance: An entity object of kind QuestionInstance
                    
                    ==> raises : BadValueError
"""    
def UpdateQuestion(question_key,question_instance=None):
   logging.info("CV Logs : Inside UpdateQuestion") 
   try:
       question=question_key.get()
       if not isinstance(question_instance,QuestionInstance):
           return Constant.ERROR_BAD_VALUE
       
       if not question_instance==None:
           question_instance=question_instance.get()
           question.question_instance=question_instance
           question.put()
      
       logging.info("CV Logs : success to update question  :"+question.instance.problem_statement)    
       return question;  
   except Exception:
       logging.exception("")
       logging.error("CV Logs : failed to update question  :"+question.instance.problem_statement)
       
       return Constant.ERROR_BAD_VALUE 
   
    


   

"""
Adds a new State:
                type= type of state STATE_IN_TOPIC or STATE_OF_TOPIC
            
"""
def addState(type,school_key):
   logging.info("CV Logs : Inside addState") 
   try:
       state = State(parent=school_key,type=type) 
       state.put()  
   except Exception :
       logging.exception("")
       logging.error("CV Logs : failed to add state  :")
       return Constant.ERROR_BAD_VALUE
   logging.info("CV Logs : success to add state  :")    
   return state;


"""
Adds a new Subject:
               type=Subject.TYPE_CLASS,Subject.TYPE_GLOBAL
               name =from SUBJECT Constants in Constant.py
    
"""
def addSubject(type,name,school_key):
   logging.info("CV Logs : Inside addSubject") 
   try: 
       subject = Subject(parent=school_key,type=type,name=name) 
       subject.put()
   except Exception :
       logging.exception("")
       logging.error("CV Logs : failed to add subject  :")
       return Constant.ERROR_BAD_VALUE
   logging.info("CV Logs : success to add state  :")      
   return subject;

"""
updates a  Subject:
               type=Subject.TYPE_CLASS,Subject.TYPE_GLOBAL
               name =from SUBJECT Constants in Constant.py
    
"""
def updateSubject(subject_key,type=None,name=None):
   logging.info("CV Logs : Inside updateSubject") 
   try: 
       subject = subject_key.get()
       if not type==None:
          subject.type=type
       if not name==None:
          subject.name=name  
       subject.put()
       logging.info("CV Logs : success to update subject  :")
       return subject;
   except Exception :
       logging.exception("")
       logging.error("CV Logs : failed to update subject  :")
       return Constant.ERROR_BAD_VALUE
   



"""
Adds a new Topic:
                prerequisite_topics should have Type list of  Key of kind Topic
                subject_key list of  Key of kind Subject
"""
def addTopic(school_key,name,prerequisite_topics,subject_key):
   try:
       logging.info("CV Logs : Inside addTopic")
       subject=subject_key.get()
       for topic_key in prerequisite_topics:
            topic=topic_key.get()
       topic = Topic(parent=school_key,name=name,prerequisite_topic=prerequisite_topics,subject_key=subject_key) 
       topic.put()          
   except Exception:
         logging.exception("")
         logging.error("CV Logs : failed to add topic  :"+topic.name)
         return Constant.ERROR_BAD_VALUE   
   logging.info("CV Logs : success to add topic  :"+topic.name)
   return topic;                                                                      


"""
update a  Topic:
                prerequisite_topics should have Type list of  Key of kind Topic
                subject_key list of  Key of kind Subject
"""
def updateTopic(topic_key,name=None,prerequisite_topics=None,subject_key=None):
   try:
       logging.info("CV Logs : Inside addTopic")
       topic=topic_key.get()
       if not subject_key==None:
        subject=subject_key.get()
        topic.subject_key=subject_key
       if not name==None:
        topic.name=name 
       if not prerequisite_topics==None:
             for topic_key in prerequisite_topics:
                 topic=topic_key.get()
                 topic.prerequisite_topics=prerequisite_topics
       topic.put()          
   except Exception:
         logging.exception("")
         logging.error("CV Logs : failed to update topic  :"+topic.name)
         return Constant.ERROR_BAD_VALUE   
   logging.info("CV Logs : success to update topic  :"+topic.name)
   return topic; 




"""
Adds a new Address:
                    type : ADDRESS_TYPE_HOME,ADDRESS_TYPE_WORK,ADDRESS_TYPE_OTHER
                    street : String
                    city  :String
"""
def addAddress(type,street,city,state):
   try:
       logging.info("CV Logs : Inside addAddress")
       address = Address(type=type,street=street,city=city,state=state) 
       address.put()  
       logging.info("CV Logs : success to add address  :")
       return address;
   except Exception:
         logging.exception("")
         logging.error("CV Logs : failed to add address  :")
         return Constant.ERROR_BAD_VALUE   

"""
Adds a new School:
                address: should be an Address entity
 
"""
def addSchool(name,address):
     try:
       logging.info("CV Logs : Inside addSchool")
       if not isinstance(address, Address):
            return Constant.ERROR_BAD_VALUE      
       school = School(name=name,address=address,code=name+"34567") 
       school.put()  
       logging.info("CV Logs : success to add school  :"+school.name)
       return school;
     except Exception:
         logging.exception("")
         logging.error("CV Logs : failed to add school  :"+school.name)
         return Constant.ERROR_BAD_VALUE
     
"""
Updates a new School:
                address: should be an Address entity
 
"""
def updateSchool(school_key,name=None,address=None):
     try:
       logging.info("CV Logs : Inside updateSchool")
       school=school_key.get()
        
       if not name==None:
           school.name=name
       if not address==None:
           if not isinstance(address, Address):
            return Constant.ERROR_BAD_VALUE
           school.address=address
       school.put()  
       logging.info("CV Logs : success to add school  :"+school.name)
       return school;
     except Exception:
         logging.exception("")
         logging.error("CV Logs : failed to add school  :"+school.name)
         return Constant.ERROR_BAD_VALUE

"""


Testing pending

Adds a new Teacher:
                address: should be an Address entity
 
"""



@ndb.transactional(xg=True)
def addTeacher(username,basic_info,school_key):
    logging.info("CV Logs : Inside addTeacher")
    school=None
    if not isinstance(basic_info, UserInfo):
            return Constant.ERROR_BAD_VALUE      
    try:
         school=school_key.get()     
         
    except Exception:
        logging.exception("")
        logging.error("CV Logs : failed to add teacher  :"+basic_info.name)
        #raise ndb.Rollback()
        return Constant.ERROR_BAD_VALUE 
    teacher = Teacher(parent=school_key,username=username,basic_info=basic_info,school=school_key) 
    teacher.put()  
    school.teachers_in_school_keys.append(teacher.key)
    school.put()
    logging.info("CV Logs : success to add teacher  :"+teacher.basic_info.name)
    return teacher;     
    
"""
update a Teacher:
                address: should be an Address entity
 
"""
def updateTeacher(teacher_key,username=None,basic_info=None):
    logging.info("CV Logs : Inside updateTeacher")
     
    try:
         teacher=teacher_key.get()     
         if  not username==None:
            teacher.username=username
         if  not basic_info==None:
            if not isinstance(basic_info, UserInfo):
                return Constant.ERROR_BAD_VALUE      
            teacher.basic_info=basic_info
         teacher.put()  
         logging.info("CV Logs : success to update teacher  :"+teacher.basic_info.name)
         return teacher;     
    except Exception:
        logging.exception("")
        logging.error("CV Logs : failed to update teacher  :"+teacher.basic_info.name)
        return Constant.ERROR_BAD_VALUE 
    



"""
Adds a new Class:
                school_key: key of school under which the class is to be added
                name : from Class in Constant.py
                section : from Section in Constant.py
                year_session="YYYY-YYYY"
                
  
"""
@ndb.transactional(xg=True)
def addClass(name,school_key,section_details,year_session):  
    try:
        logging.info("CV Logs : Inside addClass")
        school=school_key.get()
    except Exception :
        logging.exception("")
        logging.error("CV Logs : failed to add class  :"+name+":"+section_details)
        return Constant.ERROR_BAD_VALUE
    class_entity = Class(parent=school_key,name=name,school_key=school_key,section_details=section_details,year_session=year_session) 
    class_entity.put()  
    school.classes_in_school_keys.append(class_entity.key)
    school.put()
    logging.info("CV Logs : success to add class  :"+name+":"+section_details)
    return class_entity;



"""
update a  Class:
                school_key: key of school under which the class is to be added
                name : from Class in Constant.py
                section : from Section in Constant.py
                year_session="YYYY-YYYY"
                
  
"""
def updateClass(class_key,name=None,section_details=None,year_session=None):  
    try:
        logging.info("CV Logs : Inside updateClass")
        class_entity=class_key.get()
        if not name==None:
            class_entity.name=name
        if not section_details==None:
            class_entity.section_details=section_details
        if not year_session==None:
            class_entity.year_session=year_session
        class_entity.put()
        logging.info("CV Logs : success to update class  :"+class_entity.name+":"+class_entity.section_details)
        return class_entity;
    except Exception :
        logging.exception("")
        logging.error("CV Logs : failed to update class  :"+class_entity.name+":"+class_entity.section_details)
        return Constant.ERROR_BAD_VALUE

"""
Adds a new UserInfo:
                address: should be an Address entity
                name = String
                date_of_birth = ndb.DateProperty
                sex = Integer Constant.SEX_MALE, Constant.SEX_FEMALE 
               email = String
              contact_no =Integer
  
"""
def addUserInfo(name,date_of_birth,sex,address,email,contact_no):
    try :   
            logging.info("CV Logs : Inside addUserInfo" )  
            user = UserInfo(name=name,date_of_birth=date_of_birth,sex=sex,address=address,email=email,contact_no=contact_no) 
            user.put()  
            logging.info("CV Logs : success to add userinfo  :"+name)
            return user;
    except Exception :
        logging.exception("")
        logging.error("CV Logs : failed to add userinfo  :"+name)
        return Constant.ERROR_BAD_VALUE



"""
Adds a new Assessment:
                list_topic_key: list of topics covered in the assessment
"""
def addAssessment(name,list_topic_key,school_key):
    try :     
        logging.info("CV Logs : Inside addAssessment" )
        assessment = Assessment(parent=school_key,name=name,topics_in_assessment_key=list_topic_key) 
        for topic in list_topic_key:
            topic_states=get_states_of_topic(topic)
            logging.info(str(topic_states))
            for topic_state in topic_states:
                assessment.states_in_assessment_key.append(topic_state.key)
        assessment.put()  
        logging.info("CV Logs : success to add assessment  :"+name)        
        return assessment;
    except Exception :
        logging.exception("")
        logging.error("CV Logs : failed to add assessment  :"+name)
        return Constant.ERROR_BAD_VALUE

"""
Adds a new Student:
                address: should be an Address entity
                basic_info : StructuredProperty as UserInfo
                school : key of school enrolled in
                class_deatils=  class name from Class in Constant.py
                section_details=section name from Section in Constant.py
"""
def addStudent(username,basic_info,school_key):
    logging.info("CV Logs : Inside addStudent" )
    if not (isinstance(basic_info, UserInfo)) :
            return Constant.ERROR_BAD_VALUE           
    try:
         school=school_key.get()
         student = Student(parent=school.key,username=username,basic_info=basic_info,school=school.key) 
         student.put()  
         logging.info("CV Logs : success to add student  :"+basic_info.name)
         return student;

    except Exception:
        logging.exception("")
        logging.error("CV Logs : failed to add student  :"+basic_info.name)
        return Constant.ERROR_BAD_VALUE
     
    

"""
update a  Student:
                address: should be an Address entity
                basic_info : StructuredProperty as UserInfo
                school : key of school enrolled in
                class_deatils=  class name from Class in Constant.py
                section_details=section name from Section in Constant.py
"""
def updateStudent(student_key,username=None,basic_info=None):
    logging.info("CV Logs : Inside updateStudent" )
    if not (isinstance(basic_info, UserInfo)) :
            return Constant.ERROR_BAD_VALUE           
    try:
         student=student_key.get()
         if not username==None:
            student.username=username 
         if not basic_info==None:
            student.basic_info=basic_info 
         student.put()            
    except Exception:
        logging.exception("")
        logging.error("CV Logs : failed to update student  :")
        return Constant.ERROR_BAD_VALUE 
    logging.info("CV Logs : success to update student  :")
    return student;


"""
Assigns an exsisting assessment to an existing student:
                            student_key: key to student entity
                            assessment_key: key of assessment entity
"""
@ndb.transactional(xg=True)
def assign_assessment_to_student(student_key,assessment_key):
    student_assessment=None
    
    try:
        logging.info("CV Logs : Inside assign_assessment_to_student" )
        student=student_key.get()  
        student_assessment_key=student.student_assessment_key       
        #logging.error(assess)
        assessment=assessment_key.get()
        logging.error(student)
    except Exception :
        logging.exception("")
        logging.error("CV Logs : failed to assign assessment to student " )
        return Constant.ERROR_BAD_VALUE    
    if student_assessment_key==None:   
        student_assessment=Student_Assessments(student_key=student.key,attended_assessment_key=[assessment.key])
        student_assessment.put()    
        student.student_assessment_key=student_assessment.key
        student.put()     
    else:
         student_assessment=student_assessment_key.get()
         student_assessment.attended_assessment_key.append(assessment.key)
         student_assessment.put()
    '''result=assign_assessment_to_school(student.school, [assessment_key])
    if not result==Constant.UPDATION_SUCCESSFULL:
        return Constant.ERROR_OPERATION_FAIL'''
    logging.info("CV Logs : success to assign assessment :"+assessment.name+" to student :"+ student.basic_info.name)
    return Constant.UPDATION_SUCCESSFULL
 
 
"""
Assigns an exsisting assessment to an existing student:
                            student_key: key to student entity
                            assessment_key: key of assessment entity

def assign_assessment_to_class(class_key,assessment_key):
    class_assessment=None
    try:
        class_entity=class_key.get()  
        
        assessments_in_class_key=class_entity.assessments_in_class_key       
        #logging.error(assess)
        assessment=assessment_key.get()
        students_keys=class_entity.students_in_class_key
        students=ndb.get_multi(students_keys)
        #logging.error(student)
    except Exception :
        logging.exception("")
        logging.info("CV Logs : failed  Assigned assessment:"+assessment.name+"to class "+class_entity.name+":"+class_entity.section_details)
        return Constant.ERROR_BAD_VALUE    
    if assessments_in_class_key==None:   
        class_assessment=Class_Assessments(class_key=class_key,assessments_in_class_keys=[assessment.key])
        class_assessment.put()    
         
    else:
         class_assessment=assessments_in_class_key.get()
         class_assessment.assessments_in_class_keys.append(assessment.key)
         class_assessment.put()
    result=Constant.ERROR_OPERATION_FAIL   
    for student in students:
         result=assign_assessment_to_student(student.key, assessment_key)
                     
    if not result==Constant.UPDATION_SUCCESSFULL:
        logging.info("CV Logs : Failed  Assigned assessment:"+assessment.name+"to class "+class_entity.name+":"+class_entity.section_details)
        return Constant.ERROR_OPERATION_FAIL
    logging.info("CV Logs : Success  Assigned assessment:"+assessment.name+"to class "+class_entity.name+":"+class_entity.section_details)
    return Constant.UPDATION_SUCCESSFULL
         
        
"""        
"""
Assigns an existing assessment to an existing student:
                            student_key: key to student entity
                            assessment_key: key of assessment entity
                            states_of_or_in_assessments: key of state corresponding to assessment with key assessment_key
"""
def update_assessment_detail_of_student(student_key,assessment_key,current_state_key,next_state_key,next_question_key,score):
    student_assessment=None
    try:
        logging.info("CV Logs: Inside update_assessment_detail_of_student ")
        student=student_key.get()
        student_assessment=student.student_assessment_key.get() 
              
        assessment=assessment_key.get()
        current_state=current_state_key.get()
        next_state=next_state_key.get()
        next_question=next_question_key.get()
        #logging.error(assess)
    except Exception :
        logging.exception("")
        logging.info("CV Logs : failed to update assessment :")
        return Constant.ERROR_BAD_VALUE
    if  len(student_assessment.attended_assessment_key)==0:   
        return Constant.ERROR_INCONSISTENT_STATE
    if  not student_assessment.attended_assessment_key.index(assessment_key)>=0:   
        return Constant.ERROR_INCONSISTENT_STATE
    assessment.current_state= current_state_key
    assessment.next_state =next_state_key
    assessment.question_ready_to_learn=next_question_key
    assessment.score=score
    assessment.put()
    logging.info("CV Logs : success to update assessment :"+assessment.name+" for student :"+ student.basic_info.name)
    return assessment
        
"""
Assigns an exsisting assessment to an existing student:
                            student_key: key to student entity
                            assessment_key: key of assessment entity
                            states_of_or_in_assessments: key of state corresponding to assessment with key assessment_key
                            scores_in_assessments: Integer , Score of student corresponding to assessment with key assessment_key 
                            questions_ready_to_learn:key of question ready to learn corresponding to the assessment id 

def assign_assessment_score_next_question_to_student(student_key,assessment_key,states_of_or_in_assessment, scores_in_assessments,questions_ready_to_learn ):
    student_assessment=None
    try:
        student=student_key.get()        
        assessment=assessment_key.get()
        student_assessment=student.student_assessment_key.get()
        state=states_of_or_in_assessment.get()
        #question=questions_ready_to_learn.get()
        logging.error(student)
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE    
    
    if  len(student_assessment.attended_assessment_key)==0: 
        logging.error("found here")  
        return Constant.ERROR_INCONSISTENT_STATE
        '''student_assessment=Student_Assessments(student_key=student.key,attended_assessment_key=[assessment.key])
        student_assessment.put()    
        student.student_assessment_key=student_assessment.key'''     
    else:
         
         pos_assessment=student_assessment.attended_assessment_key.index(assessment_key)
         pos_state=student_assessment.states_of_or_in_assessments.index(states_of_or_in_assessment)
         if pos_assessment != pos_state:
              
             return Constant.ERROR_INCONSISTENT_STATE
         student_assessment.states_of_or_in_assessments.insert(pos_assessment,states_of_or_in_assessment)
         student_assessment.questions_ready_to_learn.insert(pos_assessment,questions_ready_to_learn)
         
         student_assessment.put()     
    #student.put()
    return Constant.UPDATION_SUCCESSFULL
"""        
"""
Assigns  existing assessments to an existing school:
                            school_key: key to school entity
                            assessments_in_school_keys : lits of keys of assessments t be assigned to the school 

@ndb.transactional(xg=True)(retries=3)
def assign_assessment_to_school(school_key,assessments_in_school_keys):
    school=None
    school_assessment=None
    try:
        logging.info("CV Logs: Inside assign_assessment_to_school ")
        school=school_key.get() 
        for assessment_key in assessments_in_school_keys:
                   assessment=assessment_key.get()
        school_assessment_key=school.assessments_in_school_key
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE    
    if school_assessment_key==None:   
        school_assessment=School_Assessments(school_key=school_key,assessments_in_school_keys=assessments_in_school_keys)
        school_assessment.put()    
        school.assessments_in_school_key=school_assessment.key 
        school.put()
    else:
        
         school_assessment=school_assessment_key.get()
         school_assessment.assessments_in_school_key.extend(assessments_in_school_keys)
         school_assessment.put()
    logging.info("CV Logs: success to assign assessmr")  
    return Constant.UPDATION_SUCCESSFULL

"""
"""
Assigns  existing assessment to an existing topic:
                            assessment_key: key to assessment entity
                            topics_in_assessment_keys : list of keys of topics covered in assessment
"""
"""def assign_assessment_to_topic(assessment_key,topics_in_assessment_keys):
    assessment=None
    topic_assessment=None
    try:
        assessment=assessment_key.get() 
        for topic_key in topics_in_assessment_keys:
                   topic=topic_key.get()
        topic_assessment_key=assessment.topics_in_assessment_key
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE    
   
    if topic_assessment_key==None:   
        
        assessment_topic=Assessment_Topics(assessment_key=assessment_key,topics_in_assessment_keys=topics_in_assessment_keys)
        assessment_topic.put()    
        assessment.topics_in_assessment_key=assessment_topic.key
        assessment.put()
    else:
        
         assessment_topic=topic_assessment_key.get()
         assessment_topic.topics_in_assessment_keys.extend(topics_in_assessment_keys)
         assessment_topic.put()     
    return Constant.UPDATION_SUCCESSFULL
"""




"""
Assigns  existing assessment to an existing state:
                            assessment_key: key to assessment entity
                            states_in_assessment_keys : list of keys of states covered in assessment

@ndb.transactional(xg=True)
def assign_states_to_assessment(assessment_key,states_in_assessment_keys):
    assessment=None
    state_asessment=None
    
    try:
        assessment=assessment_key.get() 
        for state_key in states_in_assessment_keys:
                   state=state_key.get()
        state_asessment_key=assessment.states_in_assessment_key           
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE    
   
    if state_asessment_key==None:   
        
        assessment_state=Assessment_States(assessment_key=assessment_key,states_in_assessment_keys=states_in_assessment_keys)
        assessment_state.put()    
        assessment.states_in_assessment_key=assessment_state.key
        assessment.put()
    else:
         
         assessment_state=state_asessment_key.get()
         assessment_state.states_in_assessment_keys.extend(states_in_assessment_keys)
         assessment_state.put()     
    return Constant.UPDATION_SUCCESSFULL


"""
"""
Assigns  existing questions  to an existing topic:
                            topic_key: key to topic entity
                            questions_in_topic_keys : list of keys of questions covered in topic
"""
@ndb.transactional(xg=True)
def assign_questions_to_topic(topic_key,questions_in_topic_keys):
    topic=None
    topic_question=None
    try:
        logging.info("CV Logs: Inside assign_questions_to_topic ")
        topic=topic_key.get() 
        for question_key in questions_in_topic_keys:
                   question=question_key.get()
        topic_question_key=topic.questions_in_topic_key
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE    
    
    if topic_question_key==None:   
        
        topic_question=Topic_Questions(topic_key=topic_key,questions_in_topic_keys=questions_in_topic_keys)
        topic_question.put()    
        topic.questions_in_topic_key=topic_question.key
        topic.put()
    else:
         
         topic_question=topic_question_key.get()
         topic_question.questions_in_topic_keys.extend(questions_in_topic_keys)
         topic_question.put()
    logging.info("CV Logs: success to assign questons to topic : "+topic.name)          
    return Constant.UPDATION_SUCCESSFULL



"""
Assigns  existing questions  to an existing state:
                            topic_key: key to state entity
                            questions_in_topic_keys : list of keys of questions covered in topic
"""
@ndb.transactional(xg=True)
def assign_questions_to_state(state_key,questions_in_state_keys):
    state=None
    question_state=None
    try:
        logging.info("CV Logs: Inside assign_questions_to_topic ")
        state=state_key.get() 
        for question_key in questions_in_state_keys:
                   question=question_key.get()
        question_state_key=state.question_in_state_key
    except Exception :
        logging.exception("")

    if question_state_key==None:   
        
        question_state=State_Questions(state_key=state_key,questions_in_state_keys=questions_in_state_keys)
        question_state.put()    
        state.question_in_state_key=question_state.key
        state.put()
    else:
        
         question_state=question_state_key.get()
         question_state.questions_in_state_keys.extend(questions_in_state_keys)
         question_state.put()
    for question_key in questions_in_state_keys:
         question=question_key.get()
         question.no_states_contained_in=question.no_states_contained_in+1
         question.put()
    logging.info("CV Logs: success to  assign questions to state  ")     
    return Constant.UPDATION_SUCCESSFULL

"""
Assigns  existing topics  to an existing state:
                            topic_key: key to state entity
                            states_in_topic_keys : list of keys of states covered in topic
"""
@ndb.transactional(xg=True)
def assign_states_to_topic(topic_key,states_in_topic_keys):
    topic=None
    state_topic=None
    logging.info("CV Logs : inside assign_states_to_topic ")
    try:
        topic=topic_key.get() 
        for state_key in states_in_topic_keys:
                   state=state_key.get()
                   if not state.type==Constant.STATE_IN_TOPIC:
                       return Constant.ERROR_BAD_VALUE
        state_topic_key=topic.states_in_topic_key
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
  
    if state_topic_key==None:   
        
        state_topic=Topic_States(topic_key=topic_key,states_in_topic_keys=states_in_topic_keys)
        state_topic.put()    
        topic.states_in_topic_key=state_topic.key
        topic.put()
        #logging.info("CV Logs "+str(state_topic.key))
    else:
         
         state_topic=state_topic_key.get()
         state_topic.states_in_topic_keys.extend(states_in_topic_keys)
         state_topic.put()     
    logging.info("CV Logs : success to assign states to topic :"+topic.name)     
    return Constant.UPDATION_SUCCESSFULL


"""
Assigns  existing topics  to an existing state:
                            topic_key: key to state entity
                            states_in_topic_keys : list of keys of states covered in topic
"""
@ndb.transactional(xg=True)
def assign_states_to_topic_by_name(topic_name,states_in_topic_keys):
    topic=None
    state_topic=None
    logging.info("CV Logs : inside assign_states_to_topic_by_name ")
    try:

        topic=Topic.query(Topic.name==topic_name).get()
  
        for state_key in states_in_topic_keys:
                   state=state_key.get()
                   if not state.type==Constant.STATE_IN_TOPIC:
                       return Constant.ERROR_BAD_VALUE
        state_topic_key=topic.states_in_topic_key
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
  
    if state_topic_key==None:   
        
        state_topic=Topic_States(topic_key=topic.key,states_in_topic_keys=states_in_topic_keys)
        state_topic.put()    
        topic.states_in_topic_key=state_topic.key
        topic.put()
        #logging.info("CV Logs "+str(state_topic.key))
    else:
         
         state_topic=state_topic_key.get()
         state_topic.states_in_topic_keys.extend(states_in_topic_keys)
         state_topic.put()     
    logging.info("CV Logs : success to assign states to topic :"+topic.name)     
    return Constant.UPDATION_SUCCESSFULL



"""
Assigns  existing topics  to an existing subject:
                            topic_key: key to state entity
                            states_in_topic_keys : list of keys of states covered in topic
"""
@ndb.transactional(xg=True)
def assign_topics_to_subject(subject_key,topics_in_subject_key):
    subject=None
    topic_subject=None
    try:
        logging.info("CV Logs : inside assign_topics_to_subject ")
        subject=subject_key.get() 
        for topic_key in topics_in_subject_key:
                   topic=topic_key.get()
        topic_subject_key=subject.topics_in_subject_key
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
   
    if topic_subject_key==None:   
        
        topic_subject=Subject_Topics(subject_key=subject_key,topics_in_subject_key=topics_in_subject_key)
        topic_subject.put()    
        subject.topics_in_subject_key=topic_subject.key
        subject.put()
    else:
         
         topic_subject=topic_subject_key.get()
         topic_subject.topics_in_subject_key.extend(topics_in_subject_key)
         topic_subject.put() 
    logging.info("CV Logs : success to  assign topics to subject "+subject.name)         
    return Constant.UPDATION_SUCCESSFULL  

"""
Assigns  existing teachers  to an existing school:
                            school_key: key to school entity
                            states_in_topic_keys : list of keys of states covered in topic

def assign_teachers_to_school(school_key,teachers_in_school_keys):
    school=None
    try:
        school=school_key.get() 
        for teacher_key in teachers_in_school_keys:
                   teacher=teacher_key.get()
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
    for teacher_key in teachers_in_school_keys:
                   teacher=teacher_key.get()
                   teacher.put()  
    school.teachers_in_school_keys.extend(teachers_in_school_keys)              
    school.put()     
    return Constant.UPDATION_SUCCESSFULL 
"""
"""
Assigns  existing students  to an existing class:
                            class_key: key to Class entity
                            students_in_class_key : list of keys of students enrolled  in class
"""
@ndb.transactional(xg=True)
def assign_students_to_class(class_key,students_in_class_key):
    class_entity=None
    try:
        class_entity=class_key.get() 
        for student_key in students_in_class_key:
                   student=student_key.get()
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
    try:
        for student_key in students_in_class_key:
                   student=student_key.get()
                   student.class_details=class_entity.key
                   #memcache.add(name, person)
                   a=student.put()
                   logging.error(str(student.class_details)) 
    except Exception:
        logging.exception("")
        logging.error("here")
        
    class_entity.students_in_class_key.extend(students_in_class_key)              
    class_entity.put()     
    return Constant.UPDATION_SUCCESSFULL  




"""
Assigns  existing classes  to an existing teacher:
                            teacher_key: key to Class entity
                            students_in_class_key : list of keys of students enrolled  in class
"""
@ndb.transactional(xg=True)
def assign_classes_to_teacher(teacher_key,classes_under_teacher):
    
    logging.info("CV Logs :Inside  assign_classes_to_teacher():")
    teacher_entity=None
    class_names=""
    try:
        teacher_entity=teacher_key.get() 
        for class_key in classes_under_teacher:
                   class_entity=class_key.get()
                   class_names+=class_entity.name+":"+class_entity.section_details+" "
    except Exception :
        logging.exception("")
        logging.info("CV Logs :Failed in Assigning classes :"+class_names+"to teacher "+teacher_entity.basic_info.name)
        return Constant.ERROR_BAD_VALUE

    teacher_entity.classes_under_teacher.extend(classes_under_teacher)              
    teacher_entity.put()     
    logging.info("CV Logs :Success Assigned classes :"+class_names+"to teacher "+teacher_entity.basic_info.name)
    return Constant.UPDATION_SUCCESSFULL  



"""
Assigns  existing teachers  to an existing school:
                            school_key: key to school entity
                            states_in_topic_keys : list of keys of states covered in topic

def assign_teachers_to_school(school_key,teachers_in_school_keys):
    school=None
    try:
        school=school_key.get() 
        for teacher_key in teachers_in_school_keys:
                   teacher=teacher_key.get()
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
    for teacher_key in teachers_in_school_keys:
                   teacher=teacher_key.get()
                   teacher.put()  
    school.teachers_in_school_keys.extend(teachers_in_school_keys)              
    school.put()     
    return Constant.UPDATION_SUCCESSFULL 
"""
"""
Assigns  existing students  to an existing class:
                            class_key: key to Class entity
                            students_in_class_key : list of keys of students enrolled  in class
"""
@ndb.transactional(xg=True)
def assign_subjects_to_class(class_key,subjects_in_class_key):
    class_entity=None
    try:
        class_entity=class_key.get() 
        for subject_key in subjects_in_class_key:
                   subject=subject_key.get()
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
    class_entity.subjects_in_class_key.extend(subjects_in_class_key)              
    class_entity.put()     
    return Constant.UPDATION_SUCCESSFULL  

"""
lists states (STATE_IN_TOPIC) associated to a topic 
"""

def get_states_of_topic(topic_key):
    states=[]
    
    try:
        topic=topic_key.get()
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE    
    try:
        state_in_topic_reln_key=topic.states_in_topic_key
        
        states_in_topic=state_in_topic_reln_key.get()
        state_key_list=states_in_topic.states_in_topic_keys
        states=ndb.get_multi(state_key_list)
    except Exception :
        logging.exception("")
        return Constant.ERROR_INCONSISTENT_STATE

    return states 

"""
lists questions associated to a topic 
"""
def get_questions_of_topic(topic_key):
    questions=[]
    try:
        topic=topic_key.get()
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE    
    try:
        question_in_topic_reln_key=topic.questions_in_topic_key
        if question_in_topic_reln_key==None:
            return Constant.ERROR_NO_DATA_FOUND 
        questions_in_topic=question_in_topic_reln_key.get()
        question_key_list=questions_in_topic.questions_in_topic_keys
        questions=ndb.get_multi(question_key_list)
    except Exception :
        logging.exception("")
        return Constant.ERROR_INCONSISTENT_STATE

    return questions 

"""
lists questions associated to a state 
"""
def get_questions_of_state(state_key):
    questions=[]
    try:
        state=state_key.get()
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE    
    try:
        question_in_state_reln_key=state.question_in_state_key 
        questions_in_state=question_in_state_reln_key.get()
        question_key_list=questions_in_state.questions_in_state_keys
        questions=ndb.get_multi(question_key_list)
    except Exception :
        logging.exception("")
        return Constant.ERROR_INCONSISTENT_STATE

    return questions 


"""
lists states (STATE_IN_TOPIC) associated to a topic name
"""
def get_states_by_topic_name(topic_name):
    states=[]

    try:

        topic=Topic.query(Topic.name==topic_name).get()
        logging.error(topic)
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
    try:
        state_in_topic_reln_key=topic.states_in_topic_key
        states_in_topic=state_in_topic_reln_key.get()
        state_key_list=states_in_topic.states_in_topic_keys
        states=ndb.get_multi(state_key_list)
    except Exception :
        logging.exception("")
        return Constant.ERROR_INCONSISTENT_STATE

    return states


"""
lists questions associated to a topic name
"""
def get_questions_by_topic_name(topic_name):
    questions=[]
    try:
        topic=Topic.query(Topic.name==topic_name).get()
        logging.error(topic)
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
    try:
        question_in_topic_reln_key=topic.questions_in_topic_key
        if question_in_topic_reln_key==None:
            return Constant.ERROR_NO_DATA_FOUND
        questions_in_topic=question_in_topic_reln_key.get()
        question_key_list=questions_in_topic.questions_in_topic_keys
        questions=ndb.get_multi(question_key_list)
    except Exception :
        logging.exception("")
        return Constant.ERROR_INCONSISTENT_STATE

    return questions


"""
lists subjects associated to a student 
"""
def get_subjects_by_student(student_key):
    logging.info("CV Logs : Inside get_subjects_by_student ")
    subjects=[]
    try:
        student=student_key.get()
        class_details_key=student.class_details
        if class_details_key==None:
            return Constant.ERROR_NO_DATA_FOUND
        class_details=class_details_key.get()
        subject_keys=class_details.subjects_in_class_key
        if subject_keys==None:
            return Constant.ERROR_NO_DATA_FOUND
        subjects=ndb.get_multi(subject_keys)
    except Exception:
            logging.info("CV Logs : failed to get subjects for student :"+student.basic_info.name)
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get subjects for student :"+student.basic_info.name)
    return subjects

"""
lists topics associated to a subject 
"""
def get_topics_by_subject(subject_key):
    logging.info("CV Logs : Inside get_topics_by_subject ")
    topics=[]
    try:
        subject=subject_key.get()
        topics_in_subject_key=subject.topics_in_subject_key
        topic_keys_entity=topics_in_subject_key.get()
        topic_keys=topic_keys_entity.topics_in_subject_key
        if topic_keys==None:
            return Constant.ERROR_NO_DATA_FOUND
        topics=ndb.get_multi(topic_keys)
    except Exception:
            logging.info("CV Logs : failed to get topics for subject :"+subject.name)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get topics for subject :"+subject.name)
    return topics
    
"""
lists assessments associated to a student 
"""
def get_assessments_by_student(student_key):
    logging.info("CV Logs : get_assessments_by_student ")
    assessments=[]
    try:
        student=student_key.get()
        assesments_of_student_key=student.student_assessment_key
        student_assessments_key=assesments_of_student_key.get() 
        if student_assessments_key==None:
            return Constant.ERROR_NO_DATA_FOUND
        assessments=ndb.get_multi(student_assessments_key.attended_assessment_key)
    except Exception:
            logging.info("CV Logs : failed to get assessments for student :"+student.basic_info.name)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get assessments for student :"+student.basic_info.name)
    return assessments

"""
get assessment score associated to a student 
"""
def get_student_score_in_assessment(student_key,assessment_key):
    logging.info("CV Logs : get_student_score_in_assessment ")
    try:
        student=student_key.get()
        assesments_of_student_key=student.student_assessment_key
        student_assessments=assesments_of_student_key.get()
        assessment=assessment_key.get()
        if student_assessments==None:
            return Constant.ERROR_NO_DATA_FOUND
        pos= student_assessments.attended_assessment_key.index(assessment_key)
        if not pos >= 0 : 
            return Constant.ERROR_NO_DATA_FOUND  
        if assessment.score==None:
            return Constant.ERROR_NO_DATA_FOUND
       
        return assessment.score
       
    except Exception:
            logging.info("CV Logs : failed to get score of assessment"+ assessment.name+" for student :"+student.basic_info.name)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get score of assessment"+ assessment.name+" for student :"+student.basic_info.name)
  
"""
get assessment state associated to a student 
""" 
def get_student_current_state_in_assessment(student_key,assessment_key):
    logging.info("CV Logs : get_student_state_in_assessment ")
    
    try:
        student=student_key.get()
        assesments_of_student_key=student.student_assessment_key
        student_assessments=assesments_of_student_key.get()
        assessment=assessment_key.get()
        if student_assessments==None:
            return Constant.ERROR_NO_DATA_FOUND
        pos= student_assessments.attended_assessment_key.index(assessment_key)
        if not pos >= 0 : 
            return Constant.ERROR_NO_DATA_FOUND  
        if assessment.current_state==None:
            return Constant.ERROR_NO_DATA_FOUND
       
        return assessment.current_state.get()
       
    except Exception:
            logging.info("CV Logs : failed to get state of assessment"+ assessment.name+" for student :"+student.basic_info.name)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get state of assessment"+ assessment.name+" for student :"+student.basic_info.name)
  



"""
get assessment next state associated to a student 
""" 
def get_student_next_state_in_assessment(student_key,assessment_key):
    logging.info("CV Logs : get_student_state_in_assessment ")
    
    try:
        student=student_key.get()
        assesments_of_student_key=student.student_assessment_key
        student_assessments=assesments_of_student_key.get()
        assessment=assessment_key.get()
        if student_assessments==None:
            return Constant.ERROR_NO_DATA_FOUND
        pos= student_assessments.attended_assessment_key.index(assessment_key)
        if not pos >= 0 : 
            return Constant.ERROR_NO_DATA_FOUND  
        if assessment.next_state==None:
            return Constant.ERROR_NO_DATA_FOUND
        logging.info("CV Logs : success to get next state of assessment"+ assessment.name+" for student :"+student.basic_info.name)
        return assessment.next_state.get()
       
    except Exception:
            logging.info("CV Logs : failed to get next state of assessment"+ assessment.name+" for student :"+student.basic_info.name)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    
  


"""
get assessment next state associated to a student 
""" 
def get_student_next_question_in_assessment(student_key,assessment_key):
    logging.info("CV Logs : get_student_state_in_assessment ")
    
    try:
        student=student_key.get()
        assesments_of_student_key=student.student_assessment_key
        student_assessments=assesments_of_student_key.get()
        assessment=assessment_key.get()
        if student_assessments==None:
            return Constant.ERROR_NO_DATA_FOUND
        pos= student_assessments.attended_assessment_key.index(assessment_key)
        if not pos >= 0 : 
            return Constant.ERROR_NO_DATA_FOUND  
        if assessment.question_ready_to_learn==None:
            return Constant.ERROR_NO_DATA_FOUND
        logging.info("CV Logs : success to get next question ready to learn of assessment"+ assessment.name+" for student :"+student.basic_info.name)
        return assessment.question_ready_to_learn.get()
       
    except Exception:
            logging.info("CV Logs : failed to get next question ready to learn of assessment"+ assessment.name+" for student :"+student.basic_info.name)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
  
  

  
"""
get assessment state associated to a student 

def get_student_state_in_assessment(student_key,assessment_key):
    logging.info("CV Logs : get_assessments_by_student ")
    assessments=[]
    try:
        student=student_key.get()
        assesments_of_student_key=student.student_assessment_key
        student_assessments=assesments_of_student_key.get()
        assessment=assessment_key.get()
        if student_assessments==None:
            return Constant.ERROR_NO_DATA_FOUND
        pos= student_assessments.attended_assessment_key.index(assessment_key)
        if not pos >= 0 : 
            return Constant.ERROR_NO_DATA_FOUND  
        if student_assessments.states_of_or_in_assessments==None:
            return Constant.ERROR_NO_DATA_FOUND
        state_key=student_assessments.states_of_or_in_assessments[pos]
        if state_key==None:
            return Constant.ERROR_NO_DATA_FOUND
        return state_key.get()
       
    except Exception:
            logging.info("CV Logs : failed to get state of assessment"+ assessment.name+" for student :"+student.basic_info.name)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get state of assessment"+ assessment.name+" for student :"+student.basic_info.name)
  
"""
"""
get classes  associated to a teacher 
"""
def get_classes_of_teacher(teacher_key):
    logging.info("CV Logs : get_classes_of_teacher ")
    try:
        teacher=teacher_key.get()
        classes_of_teacher_keys=teacher.classes_under_teacher
        classes_of_teacher=ndb.get_multi(classes_of_teacher_keys)        
        logging.info("CV Logs : success to get classes of teacher"+teacher.basic_info.name)
        return classes_of_teacher
    except Exception:
            logging.info("CV Logs : failed to get classes of teacher"+teacher.basic_info.name)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get classes of teacher"+teacher.basic_info.name)
  

"""
get subjects  associated to a class 
"""
def get_subjects_of_class(class_key):
    logging.info("CV Logs : get_subjects_of_class ")
    try:
        class_entity=class_key.get()
        subjects_of_class_keys=class_entity.subjects_in_class_key
        subjects_of_class=ndb.get_multi(subjects_of_class_keys)        
        logging.info("CV Logs : success to get subjects of class"+class_entity.name+":"+class_entity.section_details)
        return class_entity
    except Exception:
            logging.info("CV Logs : to get subjects of class"+class_entity.name+":"+class_entity.section_details)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
"""
lists students  associated to a class 
"""
def get_students_by_class(class_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    students=[]
    try:
        class_entity=class_key.get()
        students_in_class_keys=class_entity.students_in_class_key
        students=ndb.get_multi(students_in_class_keys)
        logging.info("CV Logs : success to get students for class :"+class_entity.name+":"+class_entity.section_details)
        return students
    except Exception:
        logging.info("CV Logs : failed to get students for class :"+class_entity.name+":"+class_entity.section_details)
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL
            
    
  


