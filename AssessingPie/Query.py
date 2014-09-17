from google.appengine.ext.ndb import Key
from google.appengine.ext import ndb
import logging
import Constant
from models import QuestionInstance,State_Questions,Topic_States,Question,State,Address,Teacher,Class,\
    Assessment_Record
from models import School,Student,UserInfo,Subject,Assessment,Student_Assessments
from  models import Topic_Questions,State_Questions,Topic_States,Subject_Topics,Assessment_Record
from models import Topic,User
from Constant import Constant,UserType
import datetime





"""
login for users
            type: determines the user Type from Constant.py
"""
def login(username,pwd):
      logging.info("CV Logs :Inside login :")
      try: 
          user_name=User.query(User.username == username).get()
          
          logging.error("#############################  "+ str(user_name))
          if user_name ==None:
            logging.error("##########################")
            return Constant.ERROR_NO_DATA_FOUND
          type=user_name.type
          if type==Constant.SCHOOL:
            user=School.query(School.code == username).get()
          elif type==Constant.STUDENT:
            logging.error("#############################  ")  
            user=Student.query(Student.username == username).get()
          elif type==Constant.TEACHER:
            user=Teacher.query(Teacher.username == username).get()
          else :
            logging.info("CV Logs : failed to login for username :"+username+":type "+str(type))
            return Constant.ERROR_BAD_VALUE
      except Exception :
        logging.exception("")
        #logging.info("CV Logs : failed to login for username :"+username+":type "+str(type))
        return Constant.ERROR_BAD_VALUE
        
      if user==None:
        return Constant.ERROR_INVALID_USER
      lastlogin= user_name.lastlogin
      user_name.lastlogin=datetime.date.today()
      user_name.put()
      logging.info("CV Logs : success to login for username :"+username+":type "+str(type))
      return [type,user,lastlogin]

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
def signup_teacher(basic_info,school_key,pwd):
      logging.info("CV Logs : inside signup_teacher ")
      try:
          teacher=addTeacher(basic_info,school_key,pwd)
            
          if not  isinstance(teacher, Teacher):
               return Constant.ERROR_BAD_VALUE 
      except Exception:
          logging.error("CV Logs : failed to sign up for teacher :"+teacher.basic_info.firstname)
          return Constant.ERROR_OPERATION_FAIL
      logging.info("CV Logs : success to sign up for teacher :"+teacher.basic_info.firstname)  
      return teacher

"""
Sign up for a student

"""

def signup_student(basic_info,school_key,pwd):
      logging.info("CV Logs : inside signup_student ")
      try:
          student=addStudent(basic_info,school_key,pwd)
          if not  isinstance(student, Student):
               return Constant.ERROR_BAD_VALUE
      except Exception:
          logging.error("CV Logs : failed to sign up for student :"+student.basic_info.firstname)
          return Constant.ERROR_BAD_VALUE 
      logging.info("CV Logs : success to sign up for student :"+student.basic_info.firstname)
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
deletes a question :
                    
"""    
def DeleteQuestion(question_key):
   logging.info("CV Logs : Inside UpdateQuestion") 
   try:
       question=question_key.get()
       instance=question.instance
       question.key.delete()
       instance.key.delete()
       logging.info("CV Logs : success to update question  :"+question.instance.problem_statement)    
       return Constant.UPDATION_SUCCESSFULL;  
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
deletes a  State:
                
            
"""
def deleteState(state_key):
   logging.info("CV Logs : Inside addState") 
   try:
       state=state_key.get()
       state_key.delete() 
   except Exception :
       logging.exception("")
       logging.error("CV Logs : failed to add state  :")
       return Constant.ERROR_BAD_VALUE
   logging.info("CV Logs : success to add state  :")    
   return Constant.UPDATION_SUCCESSFULL;


"""
Adds a new Subject:
               type=Subject.TYPE_CLASS,Subject.TYPE_GLOBAL
               name =from SUBJECT Constants in Constant.py
    
"""
def addSubject(type,name,school_key,class_key):
   logging.info("CV Logs : Inside addSubject") 
   try: 
       subject = Subject(parent=school_key,type=type,name=name,class_key=class_key) 
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
delete a  Subject:
               
    
"""
def deleteSubject(subject_key):
   logging.info("CV Logs : Inside deleteSubject") 
   try: 
       subject = subject_key.get()
       subject_key.delete()
       '''topics_key=subject.topics_in_subject_key
       topics_rel_key=topics_key.get()
       topics=topics_rel_key.topics_in_subject_key
       if not topics==None:
           
       
       
       
       '''     
       logging.info("CV Logs : success to delete subject  :")
       return Constant.UPDATION_SUCCESSFULL;
   except Exception :
       logging.exception("")
       logging.error("CV Logs : failed to delete subject  :")
       return Constant.ERROR_BAD_VALUE
   



"""
Adds a new Topic:
                prerequisite_topics should have Type list of  Key of kind Topic
                subject_key list of  Key of kind Subject
"""
@ndb.transactional
def addTopic(school_key,name,prerequisite_topics,subject_key):
   try:
       logging.info("CV Logs : Inside addTopic")
       subject=subject_key.get()
       for topic_key in prerequisite_topics:
            topic=topic_key.get()
       topic = Topic(parent=school_key,name=name,prerequisite_topic=prerequisite_topics,subject_key=subject_key) 
       topic.put()
       result=assign_topics_to_subject(subject_key,[topic.key],school_key)
       if result==Constant.UPDATION_SUCCESSFULL:
           logging.info("CV Logs : success to add topic  :"+topic.name)
           return topic           
   except Exception:
         logging.exception("")
         logging.error("CV Logs : failed to add topic  :"+topic.name)
         return Constant.ERROR_BAD_VALUE   
   logging.error("CV Logs : failed to add topic  :"+topic.name)
   return result;                                                                      



"""
deletes a new Topic:
                prerequisite_topics should have Type list of  Key of kind Topic
                subject_key list of  Key of kind Subject
"""
def deleteTopic(topic_key):
   try:
       logging.info("CV Logs : Inside addTopic")
       topic_key.delete()      
   except Exception:
         logging.exception("")
         logging.error("CV Logs : failed to delete topic  :")
         return Constant.ERROR_BAD_VALUE   
   logging.info("CV Logs : success to delete topic  :")
   return Constant.UPDATION_SUCCESSFULL;                                                                      




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
       #address.put()  
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
delete a  School:
                
 
"""
def deleteSchool(school_key):
     try:
       logging.info("CV Logs : Inside deleteSchool")
       
       logging.info("CV Logs : success to delete school  :")
       return Constant.UPDATION_SUCCESSFULL;
     except Exception:
         logging.exception("")
         logging.error("CV Logs : failed to delete school  :")
         return Constant.ERROR_BAD_VALUE
     




"""


Testing pending

Adds a new Teacher:
                address: should be an Address entity
 
"""
def addTeacher(basic_info,school_key,pwd):
    logging.info("CV Logs : Inside addTeacher")
    school=None
    if not isinstance(basic_info, UserInfo):
            return Constant.ERROR_BAD_VALUE      
    try:
         school=school_key.get()     
         school=school_key.get()
         username=basic_info.firstname+"_"+basic_info.lastname
         teacher = Teacher(parent=school_key,username=username,basic_info=basic_info,school=school_key) 
         teacher.put()  
         vaultinfo=User(username=username,type=Constant.TEACHER,key=teacher.key,pwd=pwd)
         vaultinfo.put()
    except Exception:
        logging.exception("")
        logging.error("CV Logs : failed to add teacher  :"+basic_info.firstname)
        #raise ndb.Rollback()
        return Constant.ERROR_BAD_VALUE 
    
    logging.info("CV Logs : success to add teacher  :"+teacher.basic_info.firstname)
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
         logging.info("CV Logs : success to update teacher  :"+teacher.basic_info.firstname)
         return teacher;     
    except Exception:
        logging.exception("")
        logging.error("CV Logs : failed to update teacher  :"+teacher.basic_info.firstname)
        return Constant.ERROR_BAD_VALUE 
    


def deleteTeacher(teacher_key):
    logging.info("CV Logs : Inside deleteTeacher")
       
    try:
         teacher_key.delete()   
         
    except Exception:
        logging.exception("")
        logging.error("CV Logs : failed to delete teacher  :")
        #raise ndb.Rollback()
        return Constant.ERROR_BAD_VALUE 
    
    logging.info("CV Logs : success to delete teacher  :")
    return Constant.UPDATION_SUCCESSFULL;     



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




def deleteClass(class_key):  
    try:
        logging.info("CV Logs : Inside deleteClass")
        class_key.delete()
    except Exception :
        logging.exception("")
        logging.error("CV Logs : failed to delete class  :")
        return Constant.ERROR_BAD_VALUE
    
    logging.info("CV Logs : success to delete class  :")
    return Constant.UPDATION_SUCCESSFULL;


"""
Adds a new UserInfo:
                address: should be an Address entity
                name = String
                date_of_birth = ndb.DateProperty
                sex = Integer Constant.SEX_MALE, Constant.SEX_FEMALE 
               email = String
              contact_no =Integer
  
"""
def addUserInfo(firstname,lastname,date_of_birth,sex,address,email,contact_no):
    try :   
            logging.info("CV Logs : Inside addUserInfo" )  
            user = UserInfo(firstname=firstname,lastname=lastname,date_of_birth=date_of_birth,sex=sex,address=address,email=email,contact_no=contact_no) 
            user.put()  
            logging.info("CV Logs : success to add userinfo  :"+lastname)
            return user;
    except Exception :
        logging.exception("")
        logging.error("CV Logs : failed to add userinfo  :"+lastname)
        return Constant.ERROR_BAD_VALUE



"""
//TODO Add states of pre-requisite topics also to assessmnet
Adds a new Assessment:
                list_topic_key: list of topics covered in the assessment
"""
@ndb.transactional(xg=True)
def addAssessment(name,list_topic_key,school_key,date,due_date,published,teacher_key,class_key):
    try :     
        logging.info("CV Logs : Inside addAssessment" )
        assessment = Assessment(parent=school_key,name=name,topics_in_assessment_key=list_topic_key,date=date,due_date=due_date,published=published,teacher_key=teacher_key,class_key=class_key) 
        assessment.put() 
        for topic in list_topic_key:
            topic_entity=topic.get()
            topic_entity.assessments_in_topic=assessment.key
            topic_entity.put()
            topic_states=get_states_of_topic(topic)
            logging.info(str(topic_states))
            for topic_state in topic_states:
                assessment.states_in_assessment_key.append(topic_state.key)
        assessment.put() 
        students=get_students_by_class(class_key)
        result=Constant.ERROR_OPERATION_FAIL;
        for student in students:
            result=assign_assessment_to_student(student.key, assessment.key)
        
        if result== Constant.UPDATION_SUCCESSFULL:
            logging.info("CV Logs : success to add assessment  :"+name)
            return assessment
        logging.info("CV Logs : failed to add assessment  :"+name) 
        return result  
              
       
    except Exception :
        logging.exception("")
        logging.error("CV Logs : failed to add assessment  :"+name)
        return Constant.ERROR_BAD_VALUE
    
def deleteAssessment(assessment_key):
    try :     
        logging.info("CV Logs : Inside deleteAssessment" )
        assessment_key.delete()
        logging.info("CV Logs : success to delete assessment  :")        
        return Constant.UPDATION_SUCCESSFULL;
    except Exception :
        logging.exception("")
        logging.error("CV Logs : failed to delete assessment  :")
        return Constant.ERROR_BAD_VALUE
       
    
    
    

"""
Adds a new Student:
                address: should be an Address entity
                basic_info : StructuredProperty as UserInfo
                school : key of school enrolled in
                class_deatils=  class name from Class in Constant.py
                section_details=section name from Section in Constant.py
"""
def addStudent(basic_info,school_key,pwd):
    logging.info("CV Logs : Inside addStudent" )
    if not (isinstance(basic_info, UserInfo)) :
            return Constant.ERROR_BAD_VALUE           
    try:
         school=school_key.get()
         username=basic_info.firstname+"_"+basic_info.lastname
         student = Student(parent=school.key,username=username,basic_info=basic_info,school=school.key) 
         student.put()  
         vaultinfo=User(username=username,type=Constant.STUDENT,key=student.key,pwd=pwd)
         vaultinfo.put()
         logging.info("CV Logs : success to add student  :"+basic_info.firstname)
         return student;

    except Exception:
        logging.exception("")
        logging.error("CV Logs : failed to add student  :"+basic_info.firstname)
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


def deleteStudent(student_key):
    logging.info("CV Logs : Inside deleteStudent" )
     
    try:
         student_key.delete()
         logging.info("CV Logs : success to add student  :")
         return Constant.UPDATION_SUCCESSFULL;

    except Exception:
        logging.exception("")
        logging.error("CV Logs : failed to add student  :")
        return Constant.ERROR_BAD_VALUE


"""
Assigns an exsisting assessment to an existing student:
                            student_key: key to student entity
                            assessment_key: key of assessment entity
"""
@ndb.transactional(xg=True)
def assign_assessment_to_student(student_key,assessment_key):
    student_assessment=None
    logging.info("CV Logs : Inside assign_assessment_to_student" )
  
    try:
        logging.error(""+str(student_key)+"655665656 "+str(assessment_key))
        student=student_key.get()  
        student_assessment_key=student.student_assessment_key
        school_key=student.school     
        #logging.error(assess)
        assessment=assessment_key.get()
        logging.error(student)
    except Exception :
        logging.exception("")
        logging.error("CV Logs : failed to assign assessment to student " )
        return Constant.ERROR_BAD_VALUE    
    if student_assessment_key==None:   
        student_assessment=Student_Assessments(parent=school_key,student_key=student.key,attended_assessment_key=[assessment_key])
        student_assessment.put()    
        student.student_assessment_key=student_assessment.key
        student.put()     
    else:
         student_assessment=student_assessment_key.get()
         student_assessment.attended_assessment_key.append(assessment.key)
         #student_assessment.assessment_record.append(None)
         student_assessment.put()
    '''result=assign_assessment_to_school(student.school, [assessment_key])
    if not result==Constant.UPDATION_SUCCESSFULL:
        return Constant.ERROR_OPERATION_FAIL'''
    logging.info("CV Logs : success to assign assessment :"+assessment.name+" to student :"+ student.basic_info.firstname)
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
Update an existing assessment 
"""
def update_assessment_detail_of_student(score,student_key,assessment_key,current_state_key,next_state_key,next_question_key,school_key,start_date):
    student_assessment=None
    try:
        assessment=assessment_key.get()
        logging.info("##############CV Logs1: Inside update_assessment_detail_of_student "+str(assessment.name))
        student=student_key.get()
        #logging.info("CV Logs: Inside update_assessment_detail_of_student "+student.name)
        logging.error("##############  1 @@@@@@@@@@@@@@@@@@@"+str(student))
        student_assessment=student.student_assessment_key 
        logging.info("###############CV Logs 1:found student assessment "+str(student_assessment))
        assessment_record=None      
        #assessment=assessment_key.get()
        current_state=current_state_key.get()
        next_state=next_state_key.get()
        next_question=next_question_key.get()
        #logging.error(assess)
    except Exception :
        logging.exception("")
        logging.info("CV Logs : failed to update assessment :")
        return Constant.ERROR_BAD_VALUE
   
    try:
                
                if student_assessment==None:
                    logging.info("0")
                    return Constant.ERROR_INCONSISTENT_STATE
                logging.info("1")
                
                
                student_assessmnet_entity=student_assessment.get()
                logging.info("#############CV Logs 1: failed to update assessment :")
                students_assessments=student_assessmnet_entity.attended_assessment_key
                if not assessment_key in students_assessments:
                    return Constant.ERROR_INCONSISTENT_STATE
                
                index=students_assessments.index(assessment_key)
                
                    
                student_records=student_assessmnet_entity.assessment_record
                
                logging.error("index is$$$$$$$$$$$  1"+str(index)+"  rgggg"+str(student_records))
                if  len(student_records)==0 or len(student_records)==index:
                    assessment_record=Assessment_Record(score=score,assessment_key=assessment_key,current_state=current_state_key,next_state =next_state_key,question_ready_to_learn=next_question_key,parent=school_key,start_date=start_date)
                    assessment_record.put()
                    student_assessmnet_entity.assessment_record.append(assessment_record.key)
                    student_assessmnet_entity.put()
                else :
                    assessment_record_key=student_records[index]
                    assessment_record=assessment_record_key.get()
                    assessment_record.current_state=current_state_key
                    assessment_record.next_state =next_state_key
                    assessment_record.question_ready_to_learn=next_question_key
                    assessment_record.score=score
                    assessment_record.start_date=start_date
                    assessment_record.put()
                assessment.no_of_user_completed+=1
                
    except Exception :
            logging.exception("")
            logging.info("CV Logs : failed to update assessment :")
            return Constant.ERROR_BAD_VALUE
    return assessment_record
    logging.info("CV Logs : success to update assessment :"+assessment.name+" for student :"+ student.basic_info.firstname)
    
        
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
@ndb.transactional
def assign_questions_to_topic(topic_key,questions_in_topic_keys,school_key):
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
        
        topic_question=Topic_Questions(parent=school_key,topic_key=topic_key,questions_in_topic_keys=questions_in_topic_keys)
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
def assign_questions_to_state(state_key,questions_in_state_keys,school_key):
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
        
        question_state=State_Questions(parent=school_key,state_key=state_key,questions_in_state_keys=questions_in_state_keys)
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
def assign_states_to_topic(topic_key,states_in_topic_keys,school_key):
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
        
        state_topic=Topic_States(parent=school_key,topic_key=topic_key,states_in_topic_keys=states_in_topic_keys)
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
def assign_states_to_topic_by_name(topic_name,states_in_topic_keys,school_key):
    topic=None
    state_topic=None
    logging.info("CV Logs : inside assign_states_to_topic_by_name ")
    try:

        
        topic=Topic.query(Topic.name==topic_name,ancestor=school_key).get()
  
        for state_key in states_in_topic_keys:
                   state=state_key.get()
                   if not state.type==Constant.STATE_IN_TOPIC:
                       return Constant.ERROR_BAD_VALUE
        state_topic_key=topic.states_in_topic_key
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
  
    if state_topic_key==None:   
        
        state_topic=Topic_States(parent=school_key,topic_key=topic.key,states_in_topic_keys=states_in_topic_keys)
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
def assign_topics_to_subject(subject_key,topics_in_subject_key,school_key):
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
        
        topic_subject=Subject_Topics(parent=school_key,subject_key=subject_key,topics_in_subject_key=topics_in_subject_key)
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
    logging.info("CV Logs : Inside assign_students_to_class ")
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
                   logging.error("assigning students to class "+str(student)+"@@@@@@@@@"+str(class_entity))
                   student.class_details=class_key
                   #memcache.add(name, person)
                   a=student.put()
                   logging.error(str(student.class_details)) 
    except Exception:
        logging.exception("")
        logging.error("here")
        
    class_entity.students_in_class_key.extend(students_in_class_key)              
    class_entity.put()     
    return Constant.UPDATION_SUCCESSFULL  



@ndb.transactional(xg=True)
def assign_assessments_to_class(class_key,assessment_keys):
    class_entity=None
    students=[]
    logging.info("CV Logs : Inside assign_assessments_to_class ")
    try:
        
        class_entity=class_key.get() 
        for assessment_key in assessment_keys:
                   assessment=assessment_key.get()
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
    try:
        students=get_students_by_class(class_key)
        for student in students:
                for assessment_key in assessment_keys:
                    assessment=assessment_key.get()
                    assigned=assign_assessment_to_student(student.key, assessment.key)
                    if not assigned==Constant.UPDATION_SUCCESSFULL:
                        return Constant.ERROR_OPERATION_FAIL
                    logging.error(str(student.class_details)) 
    except Exception:
        logging.exception("")
        logging.error("here")    
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
        logging.info("CV Logs :Failed in Assigning classes :"+class_names+"to teacher "+teacher_entity.basic_info.firstname)
        return Constant.ERROR_BAD_VALUE

    teacher_entity.classes_under_teacher.extend(classes_under_teacher)              
    teacher_entity.put()     
    logging.info("CV Logs :Success Assigned classes :"+class_names+"to teacher "+teacher_entity.basic_info.firstname)
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

@ndb.transactional(xg=True)
def assign_subjects_to_teacher(teacher_key,subjects_in_class_key):
    class_entity=None
    try:
        teacher_entity=teacher_key.get() 
        for subject_key in subjects_in_class_key:
                   subject=subject_key.get()
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
    teacher_entity.subjects.extend(subjects_in_class_key)              
    teacher_entity.put()     
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
        logging.info("############"+str(topic))
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
            logging.exception("")
            logging.info("CV Logs : failed to get subjects for student :")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get subjects for student :"+student.basic_info.firstname)
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
        if topics_in_subject_key==None:
            return Constant.ERROR_NO_DATA_FOUND
        topic_keys_entity=topics_in_subject_key.get()
        topic_keys=topic_keys_entity.topics_in_subject_key
        if topic_keys==None:
            return Constant.ERROR_NO_DATA_FOUND
        topics=ndb.get_multi(topic_keys)
        return topics
        logging.error("!!!!!!!!!!!!!!@@@@@@@@@@@@@"+str(topics))
    except Exception:
            logging.info("CV Logs : failed to get topics for subject :"+subject.name)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get topics for subject :"+subject.name)
    
    
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
            logging.info("CV Logs : failed to get assessments for student :"+student.basic_info.firstname)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get assessments for student :"+student.basic_info.firstname)
    return assessments


"""
lists assessments associated to a topic for a student 
"""
def get_assessments_by_topic(student_key,topic_key):
    logging.info("CV Logs : get_assessments_by_topic ")
    assessments=[]
    try:
        topic=topic_key.get()
        assesments_of_student= get_assessments_by_student(student_key)
        for assessment in assesments_of_student:
            if topic_key in assessment.topics_in_assessment_key:
                assessments.append(assessment)
        
    except Exception:
            logging.info("CV Logs : failed to get assessments of topic  for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get assessments for student :")
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
        
        if len(student_assessments.assessment_record) ==pos-1:
            return Constant.ERROR_NO_DATA_FOUND
        logging.error("!!!!!!!!!!!!!!!!1"+str(len(student_assessments.assessment_record)))
        if len(student_assessments.assessment_record)==0:
            return 0
        assessment_record_key= student_assessments.assessment_record[pos-1]
        assessment_record=assessment_record_key.get()
        
       
        if assessment_record==None:
            return Constant.ERROR_OPERATION_FAIL
        return assessment_record.score
        
       
    except Exception:
            #logging.info("CV Logs : failed to get score of assessment"+ assessment.name+" for student :"+student.basic_info.firstname)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get score of assessment"+ assessment.name+" for student :"+student.basic_info.firstname)


"""
get assessment score associated to a student 
"""
def get_student_start_date_in_assessment(student_key,assessment_key):
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
        
        if len(student_assessments.assessment_record) ==pos-1:
            return Constant.ERROR_NO_DATA_FOUND  
        assessment_record_key= student_assessments.assessment_record[pos-1]
        assessment_record=assessment_record_key.get()
        
       
        if assessment_record==None:
            return Constant.ERROR_OPERATION_FAIL
        return assessment_record.start_date
        
       
    except Exception:
            #logging.info("CV Logs : failed to get score of assessment"+ assessment.name+" for student :"+student.basic_info.firstname)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get score of assessment"+ assessment.name+" for student :"+student.basic_info.firstname)
    
"""
//TODO
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
            logging.info("CV Logs : failed to get state of assessment"+ assessment.name+" for student :"+student.basic_info.firstname)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get state of assessment"+ assessment.name+" for student :"+student.basic_info.firstname)
  



"""
//TODO
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
        logging.info("CV Logs : success to get next state of assessment"+ assessment.name+" for student :"+student.basic_info.firstname)
        return assessment.next_state.get()
       
    except Exception:
            logging.info("CV Logs : failed to get next state of assessment"+ assessment.name+" for student :"+student.basic_info.firstname)
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
        
        if len(student_assessments.assessment_record)==pos-1:
            return Constant.ERROR_NO_DATA_FOUND  
        if len(student_assessments.assessment_record)==0:
            return 0
        assessment_record_key= student_assessments.assessment_record[pos-1]
        assessment_record=assessment_record_key.get()
        
       
        if assessment_record==None:
            return Constant.ERROR_OPERATION_FAIL
        question_entity=assessment_record.question_ready_to_learn
        question=question_entity.get().instance.problem_statement
        return question
            
    except Exception:
            logging.info("CV Logs : failed to get next question ready to learn of assessment"+ assessment.name+" for student :"+student.basic_info.firstname)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
  


"""
get assessment next state associated to a student 
""" 
def get_topper_mastery_in_subject(subject_key,student_key):
    logging.info("CV Logs : get_topper_mastery_in_subject ")
    
    try:
        g_mastry=0.0
        student=student_key.get()
        class_key=student.class_details.get()
        students=get_students_by_class(class_key)
        for students in students:
            mastry=get_mastery_by_subject(subject_key, students.key)
            if g_mastry<mastry:
                g_mastry=mastry
                topper=students
        
            logging.info("CV Logs : success to get topper ")
        return {topper:g_mastry}
       
    except Exception:
            logging.info("CV Logs : failed to get ")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            


"""
//TODO Check pending assessment logic : suspicious behavior
get get_pending_assessment_subject  Add max marks logic
""" 
def get_pending_assessment_subject(subject_key,student_key):
    logging.info("CV Logs : get_pending_assessment_subject ")
    assessments=[]
    assessment_topic=[]
    pending_assessments=[]
    pending_assesments_dict={}
    try:
        topics_sub=get_topics_by_subject(subject_key)
        logging.error("##$%$%$%$%%%%%%%%%%%%"+str(topics_sub))
        if topics_sub==None:
            return Constant.ERROR_NO_DATA_FOUND
        
        total=len(topics_sub)
        logging.error("@2222222222length"+str((total)))
        for topic in topics_sub:
            assessment=get_assessments_by_topic(student_key,topic.key)
            logging.error("@2222222222length"+str(len(assessment)))
            
            if len(assessment) > 0:
                    assessments.extend(assessment)
            logging.error("@2222222$$$$$$$"+str(len(assessments)))
            for assesment_final in assessments:
                  assessment_score=get_student_score_in_assessment(student_key, assesment_final.key)
                  logging.error("%%%%%%%%%%%%%"+str(assessment_score))
                  
                  pending_assessments.append(assesment_final) 
                  pending_assesments_dict.update({assesment_final.key.urlsafe():[assesment_final.name,assesment_final.due_date]})
        return pending_assesments_dict
    except Exception:
        logging.info("CV Logs : failed to get mastry for  student :")
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
            logging.info("CV Logs : failed to get state of assessment"+ assessment.name+" for student :"+student.basic_info.firstname)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get state of assessment"+ assessment.name+" for student :"+student.basic_info.firstname)
  
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
        logging.info("CV Logs : success to get classes of teacher"+teacher.basic_info.firstname)
        return classes_of_teacher
    except Exception:
            logging.info("CV Logs : failed to get classes of teacher"+teacher.basic_info.firstname)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get classes of teacher"+teacher.basic_info.firstname)


def get_class_details_of_teacher(teacher_key):
    logging.info("CV Logs : get_classes_of_teacher ")
    try:
        dict_class={}
        teacher=teacher_key.get()
        classes_of_teacher_keys=teacher.classes_under_teacher
        classes_of_teacher=ndb.get_multi(classes_of_teacher_keys)
        for class_entity in classes_of_teacher:
            dict_class.update({class_entity.key.urlsafe():class_entity.name+" "+class_entity.section_details})
        logging.info("CV Logs : success to get classes of teacher"+teacher.basic_info.firstname)
        return dict_class
    except Exception:
            logging.info("CV Logs : failed to get classes of teacher"+teacher.basic_info.firstname)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get classes of teacher"+teacher.basic_info.firstname)




"""
get subjects  associated to a teacher 
"""
def get_subjects_of_teacher_in_class(teacher_key,class_key):
    logging.info("CV Logs : get_subjects_of_teacher ")
    try:
        subjects=[]
        teacher_entity=teacher_key.get()
        class_entity=class_key.get()
        subjects_of_teacher_keys=teacher_entity.subjects
        subjects_of_teacher=ndb.get_multi(subjects_of_teacher_keys)
        for subject in subjects_of_teacher:
            if subject.class_key==class_key:
                subjects.append(subject)       
        logging.info("CV Logs : success to get subjects of class"+class_entity.name+":"+class_entity.section_details)
        return subjects
    except Exception:
            logging.info("CV Logs : to get subjects of class"+class_entity.name+":"+class_entity.section_details)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
        
 
"""
get subjects  associated to a teacher 
"""
def get_subject_details_of_teacher_in_class(teacher_key,class_key):
    logging.info("CV Logs : get_subject_details_of_teacher_in_class ")
    try:
        subjects=[]
        dict_subjects={}
        teacher_entity=teacher_key.get()
        class_entity=class_key.get()
        subjects_of_teacher_keys=teacher_entity.subjects
        subjects_of_teacher=ndb.get_multi(subjects_of_teacher_keys)
        for subject in subjects_of_teacher:
            if subject.class_key==class_key:
                dict_subjects.update({subject.key.urlsafe():subject.name})       
        logging.info("CV Logs : success to get subject details  of class for teacher"+class_entity.name+":"+class_entity.section_details)
        return dict_subjects
    except Exception:
            logging.info("CV Logs : to subject details  of class for teacher"+class_entity.name+":"+class_entity.section_details)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL       
            

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
        return subjects_of_class
    except Exception:
            #logging.info("CV Logs : to get subjects of class"+class_entity.name+":"+class_entity.section_details)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL



def get_subject_details_of_class(class_key):
    
    logging.info("CV Logs : get_subject_details_of_class ")
    try:
        dict_subjects={}
        class_entity=class_key.get()
        subjects_of_class_keys=class_entity.subjects_in_class_key
        subjects_of_class=ndb.get_multi(subjects_of_class_keys) 
        for subject in subjects_of_class:
            dict_subjects.update({subject.key:subject.name})       
        logging.info("CV Logs : success to get subjects of class"+class_entity.name+":"+class_entity.section_details)
        return dict_subjects
    except Exception:
            #logging.info("CV Logs : to get subjects of class"+class_entity.name+":"+class_entity.section_details)
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

'''//TODO

'''
def get_average_score_by_subject(subject_key,teacher_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    students=[]
    mastery=0
    count=0
    try:
        teacher_entity=teacher_key.get()
        classess=teacher_entity.classes_under_teacher
        logging.error("dsssss"+str(classess))
        for class_dummy in classess:
            if class_dummy.get().name=="Class_V":
                class_entity=class_dummy
                
        
        students_in_class=get_students_by_class(class_entity)
        for student in students_in_class:
            mastery=mastery+get_mastery_by_subject(subject_key, student.key)
            count+=1
        average_mastery=  mastery/count  
    
        #logging.info("CV Logs : success to get average mastery for subject for class :"+class_entity.name+":"+class_entity.section_details)
        return average_mastery
    except Exception:
        #logging.info("CV Logs : failed to get average mastery for subject for class :"+class_entity.name+":"+class_entity.section_details)
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL



'''//TODO

'''
def get_average_mastery_by_subject_detailed(teacher_key,class_key,subject_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    students=[]
    mastery=0
    mastery_topic=0
    count=0
    count1=0
    try:
        teacher_entity=teacher_key.get()
       
        subject=subject_key.get()
               
        students_in_class=get_students_by_class(class_key)
        logging.error("@@@@@@@@@@@@@@@@@@@@@@@@@@"+str(subject))
        topics=get_topics_by_subject(subject_key)
        if isinstance(topics, int):
             dict_average_topic_mastery={}
             return [0,dict_average_topic_mastery]
        #logging.error("@@@@@@@@@@@@@@@@@@@@@@@@@@"+str(len(topics)))
        for student in students_in_class:
            mastery=mastery+get_mastery_by_subject(subject.key, student.key)
            count+=1
        average_mastery=  mastery/count  
        for topic in topics:
                count1=0
                for student in students_in_class:
                    mastery_topic=mastery_topic+get_mastery_by_topic(topic.key, student.key)
                    count1+=1
                average_topic_mastery=  mastery_topic/count1
        dict_average_topic_mastery={topic.name:average_topic_mastery}    
        #logging.info("CV Logs : success to get average mastery for subject for class :"+class_entity.name+":"+class_entity.section_details)
        return [average_mastery,dict_average_topic_mastery]
    except Exception:
        #logging.info("CV Logs : failed to get average mastery for subject for class :"+class_entity.name+":"+class_entity.section_details)
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL



'''//TODO

'''
def get_average_mastery_by_subject_of_all_class(teacher_key):
    logging.info("CV Logs : get_average_mastery_by_subject_of_all_class ")
    dict_mastery_class={}
    dict_mastery={}
    try:
        teacher_entity=teacher_key.get()
        classes=teacher_entity.classes_under_teacher
        for class_key in classes:
            subjects=get_subjects_of_teacher_in_class(teacher_key, class_key)
            for subject in subjects:
                 mastery=get_average_mastery_by_subject_detailed(teacher_key, class_key, subject.key)
                 dict_mastery_class.update({subject.name:mastery[0]})
            class_entity=class_key.get()
            class_name=class_entity.name+class_entity.section_details
            dict_mastery.update({class_name:dict_mastery_class})       
        return dict_mastery
    except Exception:
        #logging.info("CV Logs : failed to get average mastery for subject for class :"+class_entity.name+":"+class_entity.section_details)
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL




'''TODO'''
def get_mastery_by_student_of_class(teacher_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    students=[]
    mastery=0
    mastery_topic=0
    count=0
    count1=0
    dict__mastery={}
    try:
        teacher_entity=teacher_key.get()
        
        classess=teacher_entity.classes_under_teacher
        logging.error("dsssss"+str(classess))
        
        for class_dummy in classess:
            if class_dummy.get().name=="Class_V":
                class_entity=class_dummy
                
        subjects=get_subjects_of_class(class_entity)
        for subject_entity in subjects:
            if subject_entity.name=="Mathematics":
               subject=subject_entity
               
        students_in_class=get_students_by_class(class_entity)
        
        for student in students_in_class:
            mastery=get_mastery_by_subject(subject.key, student.key)
            dict__mastery.update({student.basic_info.firstname+student.basic_info.lastname:mastery})
            
        #logging.info("CV Logs : success to get average mastery for subject for class :"+class_entity.name+":"+class_entity.section_details)
        return dict__mastery
    except Exception:
        #logging.info("CV Logs : failed to get average mastery for subject for class :"+class_entity.name+":"+class_entity.section_details)
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL

'''
//TODO
'''
def get_students_not_logged_in_by_class(teacher_key,class_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    students=[]
    dict_users_not_logged_in={}
    try:
        teacher_entity=teacher_key.get()
        classess=teacher_entity.classes_under_teacher
        logging.error("dsssss"+str(classess))
        class_entity=class_key.get()
               
                
        
        students_in_class_keys=class_entity.students_in_class_key
        students=ndb.get_multi(students_in_class_keys)
        logging.info("CV Logs : success to get students for class :"+class_entity.name+":"+class_entity.section_details)
        
        for student in students:
            user_name=student.basic_info.firstname+"_"+student.basic_info.lastname
            student_user=User.query(User.username==user_name).get()
            if not student_user==None: 
                login_detail=student_user.lastlogin
                if login_detail==None :
                    pass
                else:
                    dict_users_not_logged_in.update({student.basic_info.firstname+" "+student.basic_info.lastname:student_user.lastlogin})
                #dict_users_not_logged_in={student.basic_info.firstname+" "+student.basic_info.lastname:student_user.lastlogin}
        return dict_users_not_logged_in
    except Exception:
        #logging.info("CV Logs : failed to get students for class :"+class_entity.name+":"+class_entity.section_details)
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL



def get_students_not_logged_in_of_all_class(teacher_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    students=[]
    dict_users_not_logged_in={}
    try:
        
        teacher_entity=teacher_key.get()
        classess=teacher_entity.classes_under_teacher
        logging.error("dsssss"+str(classess))
        for class_key in classess:
               students=get_students_not_logged_in_by_class(teacher_key, class_key)
               dict_users_not_logged_in.update(students)
        return dict_users_not_logged_in
    except Exception:
        #logging.info("CV Logs : failed to get students for class :"+class_entity.name+":"+class_entity.section_details)
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL
   
    
'''TODO'''    
def get_average_mastery_all_subject_detailed(teacher_key,class_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    students=[]
    mastery=0
    mastery_topic=0
    count=0
    count1=0
    dict_data={}
    try:
        teacher_entity=teacher_key.get()
        subjects=get_subjects_of_teacher_in_class(teacher_key, class_key)
        for subject in subjects:
            mastery=get_average_mastery_by_subject_detailed(teacher_key,class_key,subject.key)
            logging.error("&&&&&&&&&&&&&&&&&&&&"+str(mastery))
            dict_data.update({subject.name:mastery})
         
        #logging.info("CV Logs : success to get average mastery for subject for class :"+class_entity.name+":"+class_entity.section_details)
        return dict_data
    except Exception:
        #logging.info("CV Logs : failed to get average mastery for subject for class :"+class_entity.name+":"+class_entity.section_details)
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL



   
'''TODO'''    
def get_assessment_coverage_of_class(teacher_key,class_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    dict_assessment_data={}
    dict_assessment_coverage={}
    try:
        teacher_entity=teacher_key.get()
        subjects=get_subjects_of_teacher_in_class(teacher_key, class_key)
        assessments=Assessment.query(Assessment.class_key==class_key).fetch()
        if assessments==None:
            return {}
        for assessment in assessments:
            topics=assessment.topics_in_assessment_key
            topic=topics[0].get()
            subject_key=topic.subject_key
            subject_name=subject_key.get().name
            percentage_covered=assessment.no_of_user_completed/float(len(get_students_by_class(class_key)))
            dict_assessment_data.update({subject_name:{assessment.name:(percentage_covered)}})
            
                
                
         
        #logging.info("CV Logs : success to get average mastery for subject for class :"+class_entity.name+":"+class_entity.section_details)
        return dict_assessment_data
    except Exception:
        #logging.info("CV Logs : failed to get average mastery for subject for class :"+class_entity.name+":"+class_entity.section_details)
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL





"""
todo 
"""
def get_ready_to_learn_of_class(teacher_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    students=[]
    mastery=0
    mastery_topic=0
    count=0
    count1=0
    dict_ready_to_learn={}
    try:
        teacher_entity=teacher_key.get()
        
        classess=teacher_entity.classes_under_teacher
        logging.error("dsssss"+str(classess))
        for class_dummy in classess:
            if class_dummy.get().name=="Class_V":
                class_entity=class_dummy
                
        students=get_students_by_class(class_entity)
        subjects=get_subjects_of_teacher_in_class(teacher_key, class_entity)
        #subjects=get_subjects_of_class(class_entity)
        for subject in subjects:
            if subject.name=="Mathematics":
               subject_entity=subject
        topics=get_topics_by_subject(subject_entity.key) 
        for topic in topics :
            for student in students:
                count+=1
                ready_to_learn=get_ready_to_learn_topic(topic.key, student.key)
                if isinstance(ready_to_learn,int):
                    continue
                if ready_to_learn==None:
                    continue
                    
                if ready_to_learn in dict_ready_to_learn:
                    dict_ready_to_learn[ready_to_learn]+=1
                else:
                    dict_ready_to_learn[ready_to_learn]=0
        for key in dict_ready_to_learn.keys():
            dict_ready_to_learn[key]=int((dict_ready_to_learn[key]/float(count))*100)
        
         
        #logging.info("CV Logs : success to get average mastery for subject for class :"+class_entity.name+":"+class_entity.section_details)
        return dict_ready_to_learn
    except Exception:
        #logging.info("CV Logs : failed to get average mastery for subject for class :"+class_entity.name+":"+class_entity.section_details)
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL

'''TODO'''
def get_average_score_all_subject(subject_key,teacher_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    dict_averagescore={}
    
    try:
        teacher_entity=teacher_key.get()
        classess=teacher_entity.classes_under_teacher
        logging.error("dsssss"+str(classess))
        for class_dummy in classess:
            if class_dummy.get().name=="Class_V":
                class_entity=class_dummy
                
        subjects=get_subjects_of_teacher_in_class(teacher_key, class_entity)
        logging.info("!!!!!!!!!!!!!!!!!!!!!!!FFF"+str(subjects))
        for subject in subjects:
            average_score=get_average_score_by_subject(subject.key, teacher_key)
            dict_averagescore.update({subject.name:average_score})
        #logging.info("CV Logs : success to get average mastery for subject for class :"+class_entity.name+":"+class_entity.section_details)
        return dict_averagescore
    except Exception:
        #logging.info("CV Logs : failed to get average mastery for subject for class :"+class_entity.name+":"+class_entity.section_details)
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL

"""
get mastery by subjects  
"""
def get_mastery_by_subject(subject_key,student_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    assessments=[]
    completed=0
    total=0
    try:
        subject=subject_key.get()
        student=student_key.get()
        topics_sub=get_topics_by_subject(subject_key)
        if topics_sub==None or not isinstance(topics_sub, list):
            return 0
        total=len(topics_sub)
        logging.error("dffffffffffffff"+str(total))
        for topic in topics_sub:
            assessment=get_assessments_by_topic(student_key,topic.key)
            logging.error("~~~~~~~~~~~~~~~~~"+str(len(assessment)))
            
            if len(assessment) > 0:
                assessments.extend(assessment)
        
        for assesment_final in assessments:
            assessment_score=get_student_score_in_assessment(student_key, assesment_final.key)
            if  assessment_score>=-1:
                completed+=1
                
        mastry=completed/float(total)
        logging.info("CV Logs : success to get mastry for  student  :"+str(mastry))
        return int(mastry*Constant.MAX_MARKS)
    except Exception:
        logging.info("CV Logs : failed to get mastry for  student :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL




"""
get mastery for all subjects  
"""
def get_mastery_for_all_subjects(student_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    assessments=[]
    mastry_info={}
    completed=0
    total=0
    try:
        subjects=get_subjects_by_student(student_key)
        student=student_key.get()
        for subject in subjects:
            mastry=get_mastery_by_subject(subject.key, student.key)
            logging.info("CV Logs : success to get mastry for  student  :"+str(mastry))
            mastry_info.update({subject.name:mastry})
        return mastry_info
    except Exception:
        logging.info("CV Logs : failed to get mastry for  student :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL




"""
get growth by subjects  
"""
def get_growth_for_subject(student_key,subject_key):
    logging.info("CV Logs : Inside get_growth_for_subject ")
    
    assessments=[]
    dict_growth={}
    completed=0
    total=0
    count=0
    try:
        topics_sub=get_topics_by_subject(subject_key) 
        logging.error("###################"+str(topics_sub))
        subject=subject_key.get()
        student=student_key.get()
        if topics_sub==Constant.ERROR_NO_DATA_FOUND:
            total=0
            return dict_growth
        total=len(topics_sub)
        growth=0
        
        for topic in topics_sub:
                topic_mastery=get_mastery_by_topic(topic.key, student_key)
                logging.info("CV Logs : success to get mastery for  student111  :"+str(topic_mastery))
                if topic_mastery==100:
                    completed+=1
                
                growth=(completed/float(total))*100
                logging.info("CV Logs : success to get mastery for  student  :"+str(growth))
                if completed ==0:
                    pass
                else :
                    dict_growth.update({completed:int(growth)})  
        logging.info("CV Logs : success to get mastery for  student  :")
        return dict_growth
    except Exception:
        logging.info("CV Logs : failed to get mastery for  student :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL


"""
get growth for all subjects
"""
def get_growth_for_all_subject(student_key):
    logging.info("CV Logs : Inside get_growth_for_subject ")

    assessments=[]
    dict_growth={}
    dict_subject_growth={}
    subjects=[]
    completed=0

    total=0

    try:

        #subject=subject_key.get()
        student=student_key.get()
        subjects=get_subjects_by_student(student_key)

        logging.error("(((((((((((((("+str(len(subjects)))
        for subject in subjects:
            growth=get_growth_for_subject(student_key, subject.key)
            dict_subject_growth.update({subject.name:growth})
        return dict_subject_growth
    except Exception:
        logging.info("CV Logs : failed to get mastry for  student :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL





"""
get growth for all topic by subject
returns a dictionry   
"""
def get_growth_for_all_topic_subject(student_key,subject_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    logging.info("CV Logs : Inside get_students_by_class ")
    assessments=[]
    dict_growth={}
    completed=0
    total=0
    try:
        topics_sub=get_topics_by_subject(subject_key)
        subject=subject_key.get()
        student=student_key.get()
        for topic in topics_sub:
            assessments=get_assessments_by_topic(student_key, topic.key)
            logging.error("&&&&&&&&&&&&&&&&&&&"+str(assessments))
            if assessments==None:
                return Constant.ERROR_NO_DATA_FOUND
            for assessment_final in assessments:
                score=get_student_score_in_assessment(student_key, assessment_final.key)
                if  score== 100:
                    completed+=1
            
            total=len(assessments)
            if total==0:
                growth=0
            else:    
                logging.error("set ############")
                growth=(completed/float(total))*100
                
                dict_growth.update({topic.name:growth})    
        logging.info("CV Logs : success to get mastry for  student  :")
        return dict_growth
    except Exception:
        logging.info("CV Logs : failed to get mastry for  student :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL





"""
returns mastery in that subject in percentage
"""
def get_mastery_by_topic(topic_key,student_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    assessments=[]
    completed=0
    total=0
    try:
        subject=topic_key.get().subject_key.get()
        student=student_key.get()
        
        
        assessments=get_assessments_by_topic(student_key, topic_key)
        if assessments==None:
            return Constant.ERROR_NO_DATA_FOUND
        for assessment_final in assessments:
            assessment_score=get_student_score_in_assessment(student_key, assessment_final.key)
            if  assessment_score== Constant.MAX_MARKS:
                completed+=1
            logging.info("CV Logs :@@@@@@@@ :"+str(completed))
        total=len(assessments)
        if total==0:
            growth=0
        else:
            growth=completed/float(total)
        logging.info("CV Logs : success to get mastry for  student  :")
        return int(growth*100)
    except Exception:
        logging.info("CV Logs : failed to get mastry for  student :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL




"""
returns mastery in that subject in percentage
"""
def get_ready_to_learn_topic(topic_key,student_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    assessments=[]
    assessments_temp=[]
    questions=[]
    completed=0
    total=0
    question_key=None
    try:
        subject=topic_key.get().subject_key.get()
        student=student_key.get()
        assessments=get_assessments_by_topic(student_key, topic_key)
        logging.error("##########################################################"+str(assessments))
        questions=get_questions_of_topic(topic_key)
        logging.error("##########################################################"+str(questions))
        if assessments==None:
            return Constant.ERROR_NO_DATA_FOUND
        for assessment_final in assessments:
            score=get_student_score_in_assessment(student_key, assessment_final.key)
            if not score==100:
                assessments_temp.append(assessment_final)
                logging.error("##########################################################"+str(assessments_temp))
        if len(assessments_temp)==0:
            return Constant.UPDATION_SUCCESSFULL       
        for assessment_temp2 in assessments_temp:
            if not assessment_temp2.date==None:
                logging.error("##########################################################")
                question_temp=get_student_next_question_in_assessment(student_key, assessment_temp2.key)
                logging.error("$$$$$$$$$$$$"+str(question_temp))
                for question_entity in questions:
                    if question_temp == question_entity.instance.problem_statement:
                 
                        question_key= question_temp
       
        logging.info("CV Logs : success to get mastry for  student  :")
        return question_key
    except Exception:
        logging.info("CV Logs : failed to get mastry for  student :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL


"""
returns {date:[passed,failed]}

"""
def get_learning_progress_date_wise(topic_key,student_key):
    logging.info("CV Logs : Inside get_learning_progress_date_wise ")
    assessments=[]
    assessments_temp=[]
    learning_by_date={}
    mastered=0
    prev_pass=0
    prev_failed=0
    question_key=None
    try:
        subject=topic_key.get().subject_key.get()
        student=student_key.get()
        assessments=get_assessments_by_topic(student_key, topic_key)
        logging.error("##########################################################"+str(assessments))
        questions=get_questions_of_topic(topic_key)
        logging.error("##########################################################"+str(questions))
        if assessments==None:
            return Constant.ERROR_NO_DATA_FOUND
        for assessment_final in assessments:
            if not assessment_final.date==None:
                date_asessment=assessment_final.date
                if date_asessment in learning_by_date:
                     prev_pass,prev_failed=learning_by_date[date_asessment]
                if assessment_final.score==100:
                    prev_pass+=1
                else :
                    prev_failed+=1
                learning_by_date[date_asessment]=[prev_pass,prev_failed]
            else :
                if assessment_final.score==100:
                    prev_pass+=1
                else :
                    prev_failed+=1
                learning_by_date.update({date_asessment:[prev_pass,prev_failed]}) 
                          
                    
                
                
                
        logging.info("CV Logs : success to get_learning_progress_date_wise  :")
        return learning_by_date
    except Exception:
        logging.info("CV Logs : failed to get_learning_progress_date_wise :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL

    

"""
TODO : Change as per dependent topics

"""
def get_ready_to_learn_of_all_topic(subject_key,student_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    ready_to_learn_topics={}
    questions=[]
    completed=0
    total=0
    question_key=None
    try:
        subject=subject_key.get()
        student=student_key.get()
        topics=get_topics_by_subject(subject_key)
        for topic in topics:
            question=get_ready_to_learn_topic(topic.key, student.key)
            if not question==-4:
                ready_to_learn_topics[topic.name]=question

        return ready_to_learn_topics
    except Exception:
        logging.info("CV Logs : failed to get mastry for  student :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL

def get_ready_to_learn_of_all_topic_dummy(student_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    ready_to_learn_topics={}
    questions=[]
    completed=0
    total=0
    question_key=None
    try:
        logging.error(str(student_key))
        subjects=get_subjects_by_student(student_key)
        for subject_dummy in subjects:
            if subject_dummy.name=="Mathematics":
                subject=subject_dummy
                break

        student=student_key.get()
        topics=get_topics_by_subject(subject.key)
        for topic in topics:
            question=get_ready_to_learn_topic(topic.key, student.key)
            if not question==-4:
                ready_to_learn_topics[topic.name]=question

        return ready_to_learn_topics
    except Exception:
        logging.info("CV Logs : failed to get mastry for  student :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL



"""
get get_pending_assessment_subject  // List of names
"""
def get_pending_assessment_subject_dummy(student_key):
    logging.info("CV Logs : get_topper_mastery_in_subject ")
    assessments=[]
    assessment_topic=[]
    pending_assessments=[]
    try:
        subjects=get_subjects_by_student(student_key)
        for subject_dummy in subjects:
            if subject_dummy.name=="Mathematics":
                subject=subject_dummy
                break
        topics_sub=get_topics_by_subject(subject.key)
        if topics_sub==None:
            return Constant.ERROR_NO_DATA_FOUND
        total=len(topics_sub)
        for topic in topics_sub:
            assessment=get_assessments_by_topic(student_key,topic.key)

            if len(assessment) > 0:
                    assessments.extend(assessment)

            for assesment_final in assessments:
                score=get_student_score_in_assessment(student_key, assesment_final.key)
                if not score== 100:
                    pending_assessments.append(assesment_final)

            return pending_assessments
    except Exception:
        logging.info("CV Logs : failed to get mastry for  student :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL



"""
returns mastery in that subject in percentage
"""
def get_learning_progress_date_wise_dummy(student_key):
    logging.info("CV Logs : Inside get_learning_progress_date_wise ")
    assessments=[]
    assessments_temp=[]
    learning_by_date={}
    mastered=0
    prev_pass=0
    prev_failed=0
    question_key=None
    try:
        subjects=get_subjects_by_student(student_key)
        for subject_dummy in subjects:
            if subject_dummy.name=="Mathematics":
                subject=subject_dummy
                break

        topics=get_topics_by_subject(subject.key)
        for topic in topics:
            assessments=get_assessments_by_topic(student_key, topic.key)
            logging.error("##########################################################"+str(assessments))
            questions=get_questions_of_topic(topic.key)
            logging.error("##########################################################"+str(questions))
            if assessments==None:
                return Constant.ERROR_NO_DATA_FOUND
            for assessment_final in assessments:
                date_asessment=get_student_start_date_in_assessment(student_key, assessment_final.key)
                
                if not date_asessment==None:
                    score=get_student_score_in_assessment(student_key, assessment_final.key)
                    if date_asessment in learning_by_date:
                        prev_pass,prev_failed=learning_by_date[date_asessment]
                        if score==100:
                            prev_pass+=1
                        else :
                            prev_failed+=1
                        learning_by_date[str(date_asessment)]=[prev_pass,prev_pass+prev_failed]
                    else :
                        if score==100:
                            prev_pass+=1
                        else :
                            prev_failed+=1
                        learning_by_date.update({str(date_asessment):[prev_pass,prev_pass+prev_failed]})

        logging.info("CV Logs : success to get_learning_progress_date_wise  :")
        return learning_by_date

    except Exception:
        logging.info("CV Logs : failed to get_learning_progress_date_wise :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL








    
            
"""

lists students  associated to a class 

def add_topic_dummy(topic_name):
    logging.info("CV Logs : Inside get_students_by_class ")
    students=[]
    topic=None
    
    logging.info("CV Logs : inside assign_states_to_topic_by_name ")
    try:  
        school=School.query(School.name=="CVSchool").get()
        #topic=Topic.query(Topic.name==topic_name).get()
        Topic =None
        classes=school.classes_in_school_keys
        class_entity=None
        for class_key in classes:
            if class_key.get().name=="Class_V":
                class_entity=class_key.get()
        subjects=(class_entity.subjects_in_class_key)
        subject=subjects[0].get()        
        topic=addTopic(school_key=school.key,name=topic_name, prerequisite_topics=[],subject_key=subject.key)
       
        assign_topics_to_subject(subject.key, [topic.key], school.key)
        
        
        
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
    
def add_states_to_topic_dummy(topic_name,states_in_topic_keys):
    logging.info("CV Logs : Inside get_students_by_class ")
    
    #topic=None
    
    state_topic=None
    logging.info("CV Logs : inside assign_states_to_topic_by_name ")
    try:
        topic=Topic.query(Topic.name==topic_name).get()
        school=School.query(School.name=="CVSchool").get()
        #topic=Topic.query(Topic.name==topic_name,ancestor=school.key).get()
        #topic=Topic.query(Topic.name==topic_name).get()
        
        for state_key in states_in_topic_keys:
                   state=state_key.get()
                   if not state.type==Constant.STATE_IN_TOPIC:
                       return Constant.ERROR_BAD_VALUE
        state_topic_key=topic.states_in_topic_key
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
  
    if state_topic_key==None:   
        
        state_topic=Topic_States(parent=school.key,topic_key=topic.key,states_in_topic_keys=states_in_topic_keys)
        state_topic.put()    
        topic.states_in_topic_key=state_topic.key
        topic.put()
        #logging.info("CV Logs "+str(state_topic.key))
    else:
         
         state_topic=state_topic_key.get()
         state_topic.states_in_topic_keys.extend(states_in_topic_keys)
         state_topic.put()     
    logging.info("CV Logs : success to assign states to topic :"+topic.name)     
    return Constant.UPDATION_SUCCESSFULL'''
"""




