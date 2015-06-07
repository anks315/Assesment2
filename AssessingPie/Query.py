from google.appengine.ext.ndb import Key
from google.appengine.ext import ndb
import logging
from random import randint
import datetime
#from lib.yaml.lib.yaml import scan
import Constant
from models import QuestionInstance, State_Questions, Topic_States, Question, State, Address, Teacher, Class, \
    Assessment_Record, Subject
from models import School, Student, UserInfo, Subject, Assessment, Student_Assessments
from  models import Topic_Questions, State_Questions, Topic_States, Subject_Topics, Assessment_Record
from models import Topic, User,State_Types
from Constant import Constant, UserType, Subject_Name,Default







"""
login for users
            type: determines the user Type from Constant.py
//TODO school_key ancestor key
"""
def login(username, pwd):
      logging.info("CV Logs :Inside login :")
      try:
              
          user_name = User.query((User.username == username), ndb.AND (User.pwd==pwd )).get()

          if user_name == None:
            return Constant.ERROR_NO_DATA_FOUND
          parent_key=user_name.key.parent() 
          type = user_name.type
          if type == Constant.SCHOOL:
            user = School.query(School.code == username).get()
          elif type == Constant.STUDENT:
            logging.info("CV Logs :Inside login : student")
            user = Student.query(Student.username == username,ancestor=parent_key).get()
          elif type == Constant.TEACHER:
            logging.info("CV Logs :Inside login : teacher")
            user = Teacher.query(Teacher.username == username,ancestor=parent_key).get()
          else :
            logging.info("CV Logs : failed to login for username :" + username + ":type " + str(type))
            return Constant.ERROR_BAD_VALUE
      except Exception :
        logging.exception("")
        logging.info("CV Logs : failed to login for username :"+username+":type "+str(type))
        return Constant.ERROR_BAD_VALUE
        
      if user == None:
        return Constant.ERROR_INVALID_USER
      lastlogin = user_name.lastlogin
      user_name.lastlogin = datetime.datetime.now()
      user_name.put()
      logging.info("CV Logs : success to login for username :" + username + ":type " + str(type))
      return [type, user, lastlogin]

"""
Sign up for a school
"""
def signup_school(name, address):
      logging.info("CV Logs : inside signup_school ")
      try:
          school = addSchool(name, address)
          if not  isinstance(school, School):
           logging.info("CV Logs : bad input ")   
           return Constant.ERROR_BAD_VALUE   
      except Exception:
           logging.error("CV Logs : failed to sign up for school :" +name)
           return Constant.ERROR_OPERATION_FAIL 
      logging.info("CV Logs : success to sign up for school :" + school.name)  
      return school
  
  


"""
Sign up for a teacher

basic_info object of UserInfo:
First of all make an address instance : address1=Query.addAddress(type=Constant.Constant.ADDRESS_TYPE_HOME,state="UP",city="Meerut",street="12")
then make a basic_info object using   : user_basicinfo=Query.addUserInfo("Ankit","Bhatia",datetime.date(int(2009),int(8),int(6)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
dummy schoolcode= 01
returns username

usage example : Query.signup_teacher("sulabh@cv",user_basicinfo, "01",'password')
"""
def signup_teacher(username,basic_info, school_code, pwd):
      logging.info("CV Logs : inside signup_teacher ")
      try:
          school = School.query(School.code == school_code).get()
          if school == None:
              logging.error("CV Logs : bad value for school :" )
              return Constant.ERROR_NO_DATA_FOUND
          school_key = school.key
          teacher = addTeacher(username,basic_info, school_key, pwd)
          if not  isinstance(teacher, Teacher):
               logging.error("CV Logs : failed adding teacher :" )
               return Constant.ERROR_BAD_VALUE 
      except Exception:
          logging.exception("")
          logging.error("CV Logs : failed to sign up for teacher :" +basic_info.firstname)
          return Constant.ERROR_OPERATION_FAIL
      logging.info("CV Logs : success to sign up for teacher :" +basic_info.firstname)  
      return username
  
 


def check_username(username):
      logging.info("CV Logs : inside check_username ")
      try:
          
          school_key=School.query(School.name=='CVSchool').get()
          logging.error(""+str(school_key))
          if school_key==None:
              return Constant.ERROR_INCONSISTENT_STATE
          user_name = User.query(User.username == username,ancestor=school_key.key).get()
          if user_name==None:
              return Constant.ERROR_NO_DATA_FOUND
      except Exception:
          logging.exception("")
          logging.error("CV Logs : failed to check_username :")
          return Constant.ERROR_OPERATION_FAIL
      logging.info("CV Logs : success to check_username :")  
      return username



"""
Sign up for a student


basic_info object of UserInfo:
First of all make an address instance : address1=Query.addAddress(type=Constant.Constant.ADDRESS_TYPE_HOME,state="UP",city="Meerut",street="12")
then make a basic_info object using   : user_basicinfo=Query.addUserInfo("Ankit","Bhatia",datetime.date(int(2009),int(8),int(6)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
dummy schoolcode= 01
returns username

usage example : Query.signup_student("ankit@bhatia",user_basicinfo, "01",'pass')
"""

def signup_student(username,basic_info, school_code, pwd):
      logging.info("CV Logs : inside signup_student ")
      try:
          
          school = School.query(School.code == school_code).get()
          if school == None:
              logging.error("CV Logs : bad value for school :" )
              return Constant.ERROR_NO_DATA_FOUND
          school_key = school.key
          student = addStudent(username,basic_info, school_key, pwd)
          if not  isinstance(student, Student):
               logging.error("CV Logs :adding student failed :" )
               return Constant.ERROR_BAD_VALUE
      except Exception:
          logging.exception("")
          logging.info("CV Logs : failed to sign up for student :" +basic_info.firstname)
          return Constant.ERROR_BAD_VALUE 
      logging.info("CV Logs : success to sign up for student :" +basic_info.firstname)
      
      return username


"""
Adds a new question instance 
    problem_statement : Problem Statement String
    type : QUESTION_TYPE_SINGLE or QUESTION_TYPE_MULTIPLE
    choices : List of options e.g. ["1","3","10"]
    answers :: List of correct answer e.g. ["1","3","10"]
"""
def addQuestionInstance(problem_statement, type, school_key, choices=[], answers=[],url=""):
   logging.info("CV Logs : Inside addQuestionInstance") 
   try :
       question_instance = QuestionInstance(parent=school_key, problem_statement=problem_statement, type=type, choices=choices, answer=answers,url=url)
       question_instance.put()
   except Exception:
       logging.exception("")
       logging.error("CV Logs : failed to add question instance :" +problem_statement)
       return Constant.ERROR_BAD_VALUE
   logging.info("CV Logs : success to add question instance :" +str(question_instance))
   return question_instance;
  

"""
Adds a question to db :
                    question_instance: An entity object of kind QuestionInstance
                    
                    ==> raises : BadValueError
"""    
def addQuestion(question_instance, school_key):
   logging.info("CV Logs : Inside addQuestion") 
   try:
       if not isinstance(question_instance, QuestionInstance):
           return Constant.ERROR_BAD_VALUE
       question = Question(parent=school_key, instance=question_instance) 
       question.put()
       logging.info("CV Logs : success to add question  :" )
       return question;  
   except Exception:
       logging.exception("")
       logging.error("CV Logs : failed to add question  :" )
       return Constant.ERROR_BAD_VALUE 

def add_types_to_topic(topic_key, types):
   logging.info("CV Logs : Inside add_types_to_topic") 
   try:
       if not isinstance(types,list):
           return Constant.ERROR_BAD_VALUE
       topic=topic_key.get()
       if len(topic.types)==0:
           topic.types=types
       else:
           topic.extend(types)
       topic.put()
       logging.info("CV Logs : success to add_types_to_topic :" )
       return Constant.UPDATION_SUCCESSFULL;  
   except Exception:
       logging.exception("")
       logging.error("CV Logs : failed to add_types_to_topic  :" )
       return Constant.ERROR_BAD_VALUE 
       

       
"""
update a question :
                    question_instance: An entity object of kind QuestionInstance
                    
                    ==> raises : BadValueError
"""    
def UpdateQuestion(question_key, question_instance=None):
   logging.info("CV Logs : Inside UpdateQuestion") 
   try:
       question = question_key.get()
       if not isinstance(question_instance, QuestionInstance):
           logging.info("CV Logs : Bad value for question instance")
           return Constant.ERROR_BAD_VALUE
       
       if not question_instance == None:
           question_instance = question_instance.get()
           question.question_instance = question_instance
           question.put()
      
       logging.info("CV Logs : success to update question  :" + question.instance.problem_statement)    
       return question;  
   except Exception:
       logging.exception("")
       logging.error("CV Logs : failed to update question  :" + question.instance.problem_statement)
       
       return Constant.ERROR_BAD_VALUE 
   
"""
deletes a question :
                    
"""    
def DeleteQuestion(question_key):
   logging.info("CV Logs : Inside UpdateQuestion") 
   try:
       
       question = question_key.get()
       instance = question.instance
       question.key.delete()
       instance.key.delete()
       logging.info("CV Logs : success to update question  :")    
       return Constant.UPDATION_SUCCESSFULL;  
   except Exception:
       logging.exception("")
       logging.error("CV Logs : failed to update question  :")
       
       return Constant.ERROR_BAD_VALUE 
       


   

"""
Adds a new State:
                type= type of state STATE_IN_TOPIC or STATE_OF_TOPIC
            
"""
def addState(type, school_key):
   logging.info("CV Logs : Inside addState") 
   try:
       state = State(parent=school_key, type=type) 
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
       if not state_key.kind()==State._get_kind():
           Constant.ERROR_BAD_VALUE
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
def addSubject(type, name, school_key, class_key):
   logging.info("CV Logs : Inside addSubject") 
   try: 
       subject = Subject(parent=school_key, type=type, name=name, class_key=class_key) 
       subject.put()
   except Exception :
       logging.exception("")
       logging.error("CV Logs : failed to add subject  :"+name)
       return Constant.ERROR_BAD_VALUE
   logging.info("CV Logs : success to add subject  :"+name)      
   return subject;




"""
updates a  Subject:
               type=Subject.TYPE_CLASS,Subject.TYPE_GLOBAL
               name =from SUBJECT Constants in Constant.py
    
"""
def updateSubject(subject_key, type=None, name=None):
   logging.info("CV Logs : Inside updateSubject") 
   try: 
       subject = subject_key.get()
       if not type == None:
          subject.type = type
       if not name == None:
          subject.name = name  
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
@ndb.transactional(retries=5)
def addTopic(school_key, name, prerequisite_topics, subject_key,types):
   try:
       logging.info("CV Logs : Inside addTopic")
       #subject = subject_key.get()
       for topic_key in prerequisite_topics:
            if not topic_key.kind()==Topic._get_kind():

               return Constant.ERROR_BAD_VALUE
       topic = Topic(parent=school_key, name=name, prerequisite_topic=prerequisite_topics, subject_key=subject_key,types=types,state_count_types=[0]*len(types)) 
       topic.put()
       result = assign_topics_to_subject(subject_key, [topic.key], school_key)
       if result == Constant.UPDATION_SUCCESSFULL:
           logging.info("CV Logs : success to add topic  :" )
           return topic           
   except Exception:
         logging.exception("")
         logging.error("CV Logs : failed to add topic  :" +name)
         return Constant.ERROR_BAD_VALUE   
   logging.error("CV Logs : failed to add topic  :" + name)
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
def updateTopic(topic_key, name=None, prerequisite_topics=None, subject_key=None):
   try:
       logging.info("CV Logs : Inside addTopic")
       topic = topic_key.get()

       if not subject_key == None:
           if not subject_key.kind() ==Subject._get_kind():
               return Constant.ERROR_BAD_VALUE

           topic.subject_key = subject_key
       if not name == None:
        topic.name = name 
       if not prerequisite_topics == None:
             for topic_key in prerequisite_topics:
                 if not topic_key.kind()==Topic._get_kind():
                     return Constant.ERROR_BAD_VALUE
             topic.prerequisite_topics = prerequisite_topics
       topic.put()          
   except Exception:
         logging.exception("")
         logging.error("CV Logs : failed to update topic  :" )
         return Constant.ERROR_BAD_VALUE   
   logging.info("CV Logs : success to update topic  :" )
   return topic; 




"""
Adds a new Address:
                    type : ADDRESS_TYPE_HOME,ADDRESS_TYPE_WORK,ADDRESS_TYPE_OTHER
                    street : String
                    city  :String
"""
def addAddress(type, street, city, state):
   try:
       logging.info("CV Logs : Inside addAddress")
       address = Address(type=type, street=street, city=city, state=state) 
       # address.put()  
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
def addSchool(name, address):
     try:
       logging.info("CV Logs : Inside addSchool")
       if not isinstance(address, Address):
            logging.error("Bad Instance of address")
            return Constant.ERROR_BAD_VALUE      
       school = School(name=name, address=address, code="01")
       school.put()  
       logging.info("CV Logs : success to add school  :"+ name)
       return school;
     except Exception:
         logging.exception("")
         logging.error("CV Logs : failed to add school  :" +name)
         return Constant.ERROR_BAD_VALUE
     
"""
Updates a new School:
                address: should be an Address entity



"""
def updateSchool(school_key, name=None, address=None):
     try:
       logging.info("CV Logs : Inside updateSchool")
       school = school_key.get()
        
       if not name == None:
           school.name = name
       if not address == None:
           if not isinstance(address, Address):
            return Constant.ERROR_BAD_VALUE
           school.address = address
       school.put()  
       logging.info("CV Logs : success to add school  :" + school.name)
       return school;
     except Exception:
         logging.exception("")
         logging.error("CV Logs : failed to add school  :" + school.name)
         return Constant.ERROR_BAD_VALUE


"""
delete a  School:
                
 
"""
def deleteSchool(school_key):
     try:
       logging.info("CV Logs : Inside deleteSchool")
       if not school_key.kind()==School._get_kind():
           return Constant.ERROR_BAD_VALUE
       school_key.delete()
       logging.info("CV Logs : success to delete school  :")
       return Constant.UPDATION_SUCCESSFULL;
     except Exception:
         logging.exception("")
         logging.error("CV Logs : failed to delete school  :")
         return Constant.ERROR_BAD_VALUE
     




"""
Adds a new Teacher:
                address: should be an Address entity
"""
def addTeacher(username,basic_info, school_key, pwd):
    logging.info("CV Logs : Inside addTeacher")
    school = None
    if not isinstance(basic_info, UserInfo):
            return Constant.ERROR_BAD_VALUE      
    try:
         if not school_key.kind() == School._get_kind():
             logging.error("check @@@@@@@")
             return Constant.ERROR_BAD_VALUE
         schoolkey=School.query(School.name=='CVSchool').get()
         if schoolkey==None:
              return Constant.ERROR_INCONSISTENT_STATE
         teacher = Teacher(parent=school_key, username=username, basic_info=basic_info, school=school_key) 
         teacher.put()  
         vaultinfo = User(username=username, type=Constant.TEACHER, key=teacher.key, pwd=pwd,parent=schoolkey.key)
         vaultinfo.put()
    except Exception:
        logging.exception("")
        logging.error("CV Logs : failed to add teacher  :" )
        # raise ndb.Rollback()
        return Constant.ERROR_BAD_VALUE 
    
    logging.info("CV Logs : success to add teacher  :" )
    return teacher;     
    
"""
update a Teacher:
                address: should be an Address entity
 
"""
def updateTeacher(teacher_key, username=None, basic_info=None):
    logging.info("CV Logs : Inside updateTeacher")
     
    try:
         teacher = teacher_key.get()     
         if  not username == None:
            teacher.username = username
         if  not basic_info == None:
            if not isinstance(basic_info, UserInfo):
                return Constant.ERROR_BAD_VALUE      
            teacher.basic_info = basic_info
         teacher.put()  
         logging.info("CV Logs : success to update teacher  :" )
         return teacher;     
    except Exception:
        logging.exception("")
        logging.error("CV Logs : failed to update teacher  :" )
        return Constant.ERROR_BAD_VALUE 
    


def deleteTeacher(teacher_key):
    logging.info("CV Logs : Inside deleteTeacher")
       
    try:
         teacher_key.delete()   
         
    except Exception:
        logging.exception("")
        logging.error("CV Logs : failed to delete teacher  :")
        # raise ndb.Rollback()
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
@ndb.transactional(xg=True,retries=5)
def addClass(name, school_key, section_details, year_session):  
    try:
        logging.info("CV Logs : Inside addClass")
        school = school_key.get()
    except Exception :
        logging.exception("")
        logging.error("CV Logs : failed to add class  :" + name + ":" + section_details)
        return Constant.ERROR_BAD_VALUE
    class_entity = Class(parent=school_key, name=name, school_key=school_key, section_details=section_details, year_session=year_session) 
    class_entity.put()  
    school.classes_in_school_keys.append(class_entity.key)
    school.put()
    logging.info("CV Logs : success to add class  :" + name + ":" + section_details)
    return class_entity;



"""
update a  Class:
                school_key: key of school under which the class is to be added
                name : from Class in Constant.py
                section : from Section in Constant.py
                year_session="YYYY-YYYY"
                
  
"""
def updateClass(class_key, name=None, section_details=None, year_session=None):  
    try:
        logging.info("CV Logs : Inside updateClass")
        class_entity = class_key.get()
        if not name == None:
            class_entity.name = name
        if not section_details == None:
            class_entity.section_details = section_details
        if not year_session == None:
            class_entity.year_session = year_session
        class_entity.put()
        logging.info("CV Logs : success to update class  :" + class_entity.name + ":" + class_entity.section_details)
        return class_entity;
    except Exception :
        logging.exception("")
        logging.error("CV Logs : failed to update class  :" + class_entity.name + ":" + class_entity.section_details)
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
def addUserInfo(firstname, lastname, date_of_birth, sex, address, email, contact_no):
    try :   
            logging.info("CV Logs : Inside addUserInfo")  
            user = UserInfo(firstname=firstname, lastname=lastname, date_of_birth=date_of_birth, sex=sex, address=address, email=email, contact_no=contact_no) 
            user.put()  
            logging.info("CV Logs : success to add userinfo  :" + lastname)
            return user;
    except Exception :
        logging.exception("")
        logging.error("CV Logs : failed to add userinfo  :" + lastname)
        return Constant.ERROR_BAD_VALUE



"""
//TODO Add states of pre-requisite topics also to assessmnet
Adds a new Assessment:
                list_topic_key: list of topics covered in the assessment
"""
# @ndb.transactional(xg=True,retries=5)
def addAssessment(name, list_topic_key, school_key, date, due_date, published, teacher_key, class_key,):
    try :     
        logging.info("CV Logs : Inside addAssessment")
        subject_key=list_topic_key[0].get().subject_key
        assessment = Assessment(parent=school_key, name=name, topics_in_assessment_key=list_topic_key, date=date, due_date=due_date, published=published, teacher_key=teacher_key, class_key=class_key,subject_key=subject_key) 
        assessment.put()
        '''logging.info("CV Logs : Inside addAssessment added "+str(assessment))
        output=Assessment.query(ancestor=school_key).fetch()
        
        logging.info("CV Logs : Inside addAssessment added "+str(output))'''
        for topic in list_topic_key:
            topic_entity = topic.get()
            if topic_entity.assessments_in_topic==None:
                topic_entity.assessments_in_topic=[assessment.key]
            else :
                topic_entity.assessments_in_topic.append(assessment.key)
            topic_entity.assessment_count+=1
            topic_entity.put()
            topic_states_keys = get_state_keys_of_topic(topic)
            for topic_state_key in topic_states_keys:
                assessment.states_in_assessment_key.append(topic_state_key)
        assessment.put()
        '''In case want to assig''' 
        students_keys = get_student_keys_by_class(class_key)
        result = Constant.ERROR_OPERATION_FAIL;
        for student_key in students_keys:
            result = assign_assessment_to_student(student_key, assessment.key)
        
        if result == Constant.UPDATION_SUCCESSFULL:
            logging.info("CV Logs : success to add assessment  :" + name)
            return assessment
        logging.info("CV Logs : failed to add assessment  :" + name) 
        return result  
              
       
    except Exception :
        logging.exception("")
        logging.error("CV Logs : failed to add assessment  :" + name)
        return Constant.ERROR_BAD_VALUE
    
def deleteAssessment(assessment_key):
    try :     
        logging.info("CV Logs : Inside deleteAssessment")
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
def addStudent(username,basic_info, school_key, pwd):
    logging.info("CV Logs : Inside addStudent")
    if not (isinstance(basic_info, UserInfo)) :
            return Constant.ERROR_BAD_VALUE           
    try:

         if not school_key.kind()==School._get_kind():
             return Constant.ERROR_BAD_VALUE
         schoolkey=School.query(School.name=='CVSchool').get()
         logging.error(""+str(school_key))
         if schoolkey==None:
              return Constant.ERROR_INCONSISTENT_STATE
         student = Student(parent=school_key,school=school_key, username=username, basic_info=basic_info)
         student.put()  
         vaultinfo = User(username=username, type=Constant.STUDENT, key=student.key, pwd=pwd,parent=schoolkey.key)
         vaultinfo.put()
         logging.info("CV Logs : success to add student  :" + basic_info.firstname)
         return student;

    except Exception:
        logging.exception("")
        logging.error("CV Logs : failed to add student  :" + basic_info.firstname)
        return Constant.ERROR_BAD_VALUE
     
    

"""
update a  Student:
                address: should be an Address entity
                basic_info : StructuredProperty as UserInfo
                school : key of school enrolled in
                class_deatils=  class name from Class in Constant.py
                section_details=section name from Section in Constant.py
"""
def updateStudent(student_key, username=None, basic_info=None):
    logging.info("CV Logs : Inside updateStudent")
    if not (isinstance(basic_info, UserInfo)) :
            return Constant.ERROR_BAD_VALUE           
    try:
         student = student_key.get()
         if not username == None:
            student.username = username 
         if not basic_info == None:
            student.basic_info = basic_info 
         student.put()            
    except Exception:
        logging.exception("")
        logging.error("CV Logs : failed to update student  :")
        return Constant.ERROR_BAD_VALUE 
    logging.info("CV Logs : success to update student  :")
    return student;


def deleteStudent(student_key):
    logging.info("CV Logs : Inside deleteStudent")
     
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
@ndb.transactional(xg=True,retries=5)
def assign_assessment_to_student(student_key, assessment_key):
    student_assessment = None
    logging.info("CV Logs : Inside assign_assessment_to_student")
    try:
        student = student_key.get()  
        student_assessment_key = student.student_assessment_key
        school_key = student.school     
        assessment = assessment_key.get()
        logging.error(student)
    
        if student_assessment_key == None:   
            student_assessment = Student_Assessments(parent=school_key, student_key=student_key, attended_assessment_key=[assessment_key])
            student_assessment.put()    
            student.student_assessment_key = student_assessment.key
            student_assessment_record = Assessment_Record(parent=school_key,assessment_key=assessment_key)
            student_assessment_record.put()
            student_assessment.assessment_record = [student_assessment_record.key]
            student_assessment.put()  
            student.put()     
        else:
            student_assessment = student_assessment_key.get()
            student_assessment.attended_assessment_key.append(assessment.key)
            student_assessment_record = Assessment_Record(parent=school_key, assessment_key=assessment_key)
            student_assessment_record.put()
            student_assessment.assessment_record.append(student_assessment_record.key)
            student_assessment.put()
    except Exception :
        logging.exception("")
        logging.error("CV Logs : failed to assign assessment to student ")
        return Constant.ERROR_BAD_VALUE  
    logging.info("CV Logs : success to assign assessment :" + assessment.name + " to student :" + student.basic_info.firstname)
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
def update_assessment_detail_of_student(total_score,topic_scores,topic_times, student_key, assessment_key, current_state_key, next_state_key, next_question_key, school_key, completion_date):
    student_assessment = None
    try:
        
        assessment = assessment_key.get()
        logging.info("CV Logs: Inside update_assessment_detail_of_student ")
        length=len(assessment.topics_in_assessment_key)
        student = student_key.get()
        school_key=student.school
        student_assessment = student.student_assessment_key
        if student_assessment==None:
            logging.info("CV Logs: No Assessment details found:") 
            return Constant.ERROR_NO_DATA_FOUND 
        assessment_record = None
        if not (isinstance(current_state_key,list) or isinstance(next_state_key.kind(),list) or isinstance(next_question_key.kind(),list)):
            return Constant.ERROR_BAD_VALUE
        if not (len(topic_scores)==len(current_state_key)) or not (len(current_state_key)==len(next_state_key)): 
            return Constant.ERROR_BAD_VALUE
    except Exception :
        logging.exception("")
        logging.error("CV Logs : failed to update assessment :")
        return Constant.ERROR_BAD_VALUE
   
    try:
                final_current_state=[]
                
                for state in current_state_key:
                    
                    if  state == None:
                        
                        state_inavlid=addState(type=Constant.STATE_INVALID,school_key=school_key)
                        final_current_state.append(state_inavlid.key)
                    else :
                         final_current_state.append(state)
                         
                       
                final_topic_times=[]
                
                for time in topic_times:
                    
                    if  time == None:
                        
                       
                        final_topic_times.append(0.0)
                    else :
                         final_topic_times.append(time)
                         
                       
                final_next_state=[]

                
                
                
                
                for state in next_state_key:
                  
                    if state ==None:
                        
                        state_inavlid=addState(type=Constant.STATE_INVALID,school_key=school_key)
                        
                        final_next_state.append(state_inavlid.key)
                    else :
                         final_next_state.append(state)
               
                student_assessmnet_entity = student_assessment.get()
                students_assessments = student_assessmnet_entity.attended_assessment_key
                if students_assessments==None:
                    logging.error("CV Logs: students attended assessment not found") 
                if not assessment_key in students_assessments:
                    return Constant.ERROR_INCONSISTENT_STATE
                
                index = students_assessments.index(assessment_key)
                student_records = student_assessmnet_entity.assessment_record
                logging.info("CV Logs: reched`1"+str(student_records)) 
                if  len(student_records) == 0 or len(student_records) == index:
                    logging.info("CV Logs: reched`2"+str(index)) 
                    assessment_record = Assessment_Record(total_score=total_score,topic_scores=topic_scores,topic_times=final_topic_times, assessment_key=assessment_key, current_state=final_current_state, next_state=final_next_state, question_ready_to_learn=next_question_key, parent=school_key, completion_date=completion_date)
                    assessment_record.put()
                    '''logging.error("CV Logs: reched 3"+str(assessment_record)) 
                    asess=Assessment_Record.query(ancestor=school_key).fetch()
                    logging.error("CV Logs: reched 4"+str(asess)) '''
                    
                    
                    
                    student_assessmnet_entity.assessment_record[index] = (assessment_record.key)
                    student_assessmnet_entity.put()
                else :
                    assessment_record_key = student_records[index]
                    assessment_record = assessment_record_key.get()
                    assessment_record.current_state = final_current_state
                    assessment_record.next_state = final_next_state
                    assessment_record.question_ready_to_learn = next_question_key
                    assessment_record.total_score = total_score
                    assessment_record.topic_scores=topic_scores
                    assessment_record.topic_times=final_topic_times
                    assessment_record.completion_date = completion_date
                    assessment_record.put()
                assessment.no_of_user_completed += 1
                assessment.put()
                logging.info("CV Logs : success to update assessment :" + assessment.name + " for student :" + student.basic_info.firstname)
    except Exception :
            logging.exception("")
            logging.info("CV Logs : failed to update assessment :")
            return Constant.ERROR_BAD_VALUE
    return Constant.UPDATION_SUCCESSFULL
   
    
        
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
@ndb.transactional(retries=5)
def assign_questions_to_topic(topic_key, questions_in_topic_keys, school_key,topic_type):
    topic = None
    topic_question = None
    try:
        logging.info("CV Logs: Inside assign_questions_to_topic ")
        topic = topic_key.get() 
        for question_key in questions_in_topic_keys:
                   if not question_key.kind()==Question._get_kind():
                       return Constant.ERROR_BAD_VALUE
                   question_entity=question_key.get()
                   question_entity.topic_key=topic_key
                   question_entity.topic_type=topic_type
                   question_entity.put()
        topic_question_key = topic.questions_in_topic_key
    except Exception :
        logging.exception("")
        logging.error("CV Logs: failed to assign questions to topic : " )
        return Constant.ERROR_BAD_VALUE
        
    if topic_question_key == None:   
        topic_question = Topic_Questions(parent=school_key, topic_key=topic_key, questions_in_topic_keys=questions_in_topic_keys)
        topic_question.put()    
        topic.questions_in_topic_key = topic_question.key
        topic.put()
    else:
        topic_question = topic_question_key.get()
        topic_question.questions_in_topic_keys.extend(questions_in_topic_keys)
        topic_question.put()
    
    logging.info("CV Logs: success to assign questons to topic : " + topic.name)          
    return Constant.UPDATION_SUCCESSFULL


def get_all_schools():
    dict_school = {}
    try:
        schools=School.query().fetch()
        for school in schools:
            dict_school.update({school.name:school.key.urlsafe()})
        return dict_school
    except Exception :
        logging.exception("")
        logging.error("CV Logs: failed to assign questions to topic : " )
        return Constant.ERROR_BAD_VALUE
    
    
    logging.info("CV Logs: success to assign questons to topic : " )          
    return Constant.UPDATION_SUCCESSFULL


    
    


def get_class_of_school(school_key):
    dict_class = {}
    try:
        logging.error("@@@@@@@@@@@@@@@@@@@"+str(school_key))
        classes=Class.query(Class.school_key==school_key).fetch()
        if classes==None:
            return dict_class
        for class_entity in classes:
            dict_class.update({class_entity.name+" "+class_entity.section_details:class_entity.key.urlsafe()})
        return dict_class
        
    except Exception :
        logging.exception("")
        logging.error("CV Logs: failed to assign questions to topic : " )
        return Constant.ERROR_BAD_VALUE
    
    
    logging.info("CV Logs: success to assign questons to topic : " )          
    return Constant.UPDATION_SUCCESSFULL



"""
Assigns  existing questions  to an existing state:
                            topic_key: key to state entity
                            questions_in_topic_keys : list of keys of questions covered in topic
"""
@ndb.transactional(xg=True,retries=5)
def assign_questions_to_state(state_key, questions_in_state_keys, school_key):
    state = None
    question_state = None
    try:
        logging.info("CV Logs: Inside assign_questions_to_topic ")
        state = state_key.get() 
        for question_key in questions_in_state_keys:
                   if not question_key.kind()==Question._get_kind():
                       return Constant.ERROR_BAD_VALUE
        question_state_key = state.question_in_state_key
    except Exception :
        logging.exception("")
        logging.error("CV Logs: invalid values")
    if question_state_key == None:   
        
        question_state = State_Questions(parent=school_key, state_key=state_key, questions_in_state_keys=questions_in_state_keys)
        question_state.put()    
        state.question_in_state_key = question_state.key
        state.put()
    else:
        
         question_state = question_state_key.get()
         question_state.questions_in_state_keys.extend(questions_in_state_keys)
         question_state.put()
    for question_key in questions_in_state_keys:
         question = question_key.get()

         question.no_states_contained_in = question.no_states_contained_in + 1
         question.put()
    logging.info("CV Logs: success to  assign questions to state  ")     
    return Constant.UPDATION_SUCCESSFULL


def assign_types_to_state(state_key,topic_key, types_in_state, school_key):
    state = None
    type_state = None
    try:
        logging.info("CV Logs: Inside assign_questions_to_topic ")
        state = state_key.get() 
        topic=topic_key.get()
        type_state_key = state.type_in_state_key
    except Exception :
        logging.exception("")
        logging.error("CV Logs: invalid values")
    if type_state_key == None:   
        
        type_state = State_Types(parent=school_key, state_key=state_key, types_in_state=types_in_state)
        type_state.put()    
        state.type_in_state_key = type_state.key
        state.put()
    else:
        
         type_state = type_state_key.get()
         type_state.types_in_state.extend(types_in_state)
         type_state.put()
    topic_types=topic.types
    #logging.info("CV Logs:@@@@@ "+str(topic_types)) 
    
    for types in types_in_state:
        
        
        index=topic.types.index(types)
        count=topic.state_count_types[index]
        topic.state_count_types[index]=count+1
        
        topic.put()
    logging.info("CV Logs: success to  assign questions to state  ")     
    return Constant.UPDATION_SUCCESSFULL



def get_state_count_of_types(topic_key):
    dict_states={}
    try:
        logging.info("CV Logs: get_state_count_of_type")
        topic= topic_key.get() 
        topic_types=topic.types
        for types in topic_types:
            index=topic_types.index(types)
            count=topic.state_count_types[index]
            dict_states[types]=count
    except Exception :
            logging.exception("")  
    return dict_states




"""
Assigns  existing questions  to an existing state:
                            topic_key: key to state entity
                            questions_in_topic_keys : list of keys of questions covered in topic
"""
@ndb.transactional(xg=True,retries=5)
def map_state_to_questions(topic_key, state_questions_map,school_key):
    state = None
    question_state = None
    topic_states=[]

    try:

        topic=topic_key.get()
        questions=get_questions_of_topic(topic_key)
        for question in questions:
            question.no_states_contained_in=0
        logging.info("CV Logs: Inside map_state_to_questions ")
        topic = topic_key.get()

        states=[]
        result=Constant.ERROR_OPERATION_FAIL
        for key in state_questions_map.keys():
            state=addState(type=Constant.STATE_IN_TOPIC,school_key=school_key)
            states.append(state.key)
            result=assign_questions_to_state(state.key,state_questions_map[key], school_key)

            if not result==Constant.UPDATION_SUCCESSFULL:
                return Constant.ERROR_OPERATION_FAIL

        result1=assign_states_to_topic(topic_key,states,school_key)
        if not result1==Constant.UPDATION_SUCCESSFULL:
                return Constant.ERROR_OPERATION_FAIL
        logging.info("CV Logs: Success to map_state_to_questions")
        return result 
    except Exception :
        logging.exception("")
        logging.error("CV Logs: failed to map_state_to_questions")
    

@ndb.transactional(xg=True,retries=5)
def map_state_to_topic_type(topic_key, state_types_map,school_key):
    state = None
    question_state = None
    topic_states=[]

    try:

        topic=topic_key.get()
        
        topic.state_count_types=[0]*len(topic.types)
        logging.info("CV Logs: ######## Inside map_state_to_questions "+str(topic.state_count_types))
        topic.put()
        
        logging.info("CV Logs: Inside map_state_to_questions ")
       
        states=[]
        result=Constant.ERROR_OPERATION_FAIL
        for key in state_types_map.keys():
            state=addState(type=Constant.STATE_IN_TOPIC,school_key=school_key)
            states.append(state.key)
            result=assign_types_to_state(state.key,topic_key,state_types_map[key], school_key)

            if not result==Constant.UPDATION_SUCCESSFULL:
                return Constant.ERROR_OPERATION_FAIL

        result1=assign_states_to_topic(topic_key,states,school_key)
        if not result1==Constant.UPDATION_SUCCESSFULL:
                return Constant.ERROR_OPERATION_FAIL
        logging.info("CV Logs: Success to map_state_to_questions")
        return result 
    except Exception :
        logging.exception("")
        logging.error("CV Logs: failed to map_state_to_questions")






@ndb.transactional(xg=True,retries=5)
def map_state_to_questions_dummy( state_questions_map,school_key):
    state = None
    question_state = None
    try:
        topic=Topic.query(Topic.name=='Number_System',ancestor=school_key).get()
        topic_key=topic.key
        
        logging.info("#######################CV Logs: Inside map_state_to_questions "+str(topic))
        topic = topic_key.get() 
        result=Constant.ERROR_OPERATION_FAIL
        for key in state_questions_map.keys():
            state=addState(type=Constant.STATE_IN_TOPIC,school_key=school_key)
            result=assign_questions_to_state(state.key,state_questions_map[key], school_key)
            if not result==Constant.UPDATION_SUCCESSFULL:
                return Constant.ERROR_OPERATION_FAIL
        logging.info("CV Logs: Success to map_state_to_questions")
        return result 
    except Exception :
        logging.exception("")
        logging.error("CV Logs: failed to map_state_to_questions")




"""
Assigns  existing topics  to an existing state:
                            topic_key: key to state entity
                            states_in_topic_keys : list of keys of states covered in topic
"""
@ndb.transactional(xg=True,retries=5)
def assign_states_to_topic(topic_key, states_in_topic_keys, school_key):
    topic = None
    state_topic = None
    logging.info("CV Logs : inside assign_states_to_topic ")
    try:
        topic = topic_key.get() 
        for state_key in states_in_topic_keys:
                   state = state_key.get()
                   if not state.type == Constant.STATE_IN_TOPIC:
                       return Constant.ERROR_BAD_VALUE
        state_topic_key = topic.states_in_topic_key
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
    state_topic = Topic_States(parent=school_key, topic_key=topic_key, states_in_topic_keys=states_in_topic_keys)
    state_topic.put()
    topic.states_in_topic_key = state_topic.key
    topic.put()
    logging.info("CV Logs : success to assign states to topic :" + topic.name)     
    return Constant.UPDATION_SUCCESSFULL




"""
Assigns  existing topics  to an existing state:
                            topic_key: key to state entity
                            states_in_topic_keys : list of keys of states covered in topic

@ndb.transactional(xg=True)
def assign_states_to_topic_by_name(topic_name, states_in_topic_keys, school_key):
    topic = None
    state_topic = None
    logging.info("CV Logs : inside assign_states_to_topic_by_name ")
    try:

        
        topic = Topic.query(Topic.name == topic_name, ancestor=school_key).get()
  
        for state_key in states_in_topic_keys:
                   state = state_key.get()
                   if not state.type == Constant.STATE_IN_TOPIC:
                       return Constant.ERROR_BAD_VALUE
        state_topic_key = topic.states_in_topic_key
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
  
    if state_topic_key == None:   
        
        state_topic = Topic_States(parent=school_key, topic_key=topic.key, states_in_topic_keys=states_in_topic_keys)
        state_topic.put()    
        topic.states_in_topic_key = state_topic.key
        topic.put()
        # logging.info("CV Logs "+str(state_topic.key))
    else:
         
         state_topic = state_topic_key.get()
         state_topic.states_in_topic_keys.extend(states_in_topic_keys)
         state_topic.put()     
    logging.info("CV Logs : success to assign states to topic :" + topic.name)     
    return Constant.UPDATION_SUCCESSFULL


"""
"""
Assigns  existing topics  to an existing subject:
                            topic_key: key to state entity
                            states_in_topic_keys : list of keys of states covered in topic
"""
@ndb.transactional(xg=True,retries=5)
def assign_topics_to_subject(subject_key, topics_in_subject_key, school_key):
    subject = None
    topic_subject = None
    try:
        logging.info("CV Logs : inside assign_topics_to_subject ")
        subject = subject_key.get() 
        for topic_key in topics_in_subject_key:
                   topic = topic_key.get()
        topic_subject_key = subject.topics_in_subject_key
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
   
    if topic_subject_key == None:   
        
        topic_subject = Subject_Topics(parent=school_key, subject_key=subject_key, topics_in_subject_key=topics_in_subject_key)
        topic_subject.put()    
        subject.topics_in_subject_key = topic_subject.key
        subject.put()
    else:
         
         topic_subject = topic_subject_key.get()
         topic_subject.topics_in_subject_key.extend(topics_in_subject_key)
         topic_subject.put() 
    logging.info("CV Logs : success to  assign topics to subject " )
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
@ndb.transactional(xg=True,retries=5)
def assign_students_to_class(class_key, students_in_class_key):
    class_entity = None
    logging.info("CV Logs : Inside assign_students_to_class ")
    try:
        
        class_entity = class_key.get() 
        for student_key in students_in_class_key:
                   if not student_key.kind()==Student._get_kind():
                       return Constant.ERROR_BAD_VALUE
    except Exception :
        logging.exception("")
        logging.error("CV Logs : Bad values ")
        return Constant.ERROR_BAD_VALUE
    try:
        for student_key in students_in_class_key:
                   student = student_key.get()
                   student.class_details = class_key
                   student.put()
                   
    except Exception:
        logging.exception("")
        logging.error("CV Logs : Bad values")
        
    class_entity.students_in_class_key.extend(students_in_class_key)              
    class_entity.put() 
    logging.error("CV Logs : Success assign students to class")    
    return Constant.UPDATION_SUCCESSFULL  



@ndb.transactional(xg=True,retries=5)
def assign_assessments_to_class(class_key, assessment_keys):
    class_entity = None
    students = []
    logging.info("CV Logs : Inside assign_assessments_to_class ")
    try:
        

        for assessment_key in assessment_keys:
                  if not assessment_key.kind()==Assessment._get_kind():
                       return Constant.ERROR_BAD_VALUE
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
    try:
        students = get_students_by_class(class_key)
        for student in students:
                for assessment_key in assessment_keys:
                    assessment = assessment_key.get()
                    assigned = assign_assessment_to_student(student.key, assessment.key)
                    if not assigned == Constant.UPDATION_SUCCESSFULL:
                        return Constant.ERROR_OPERATION_FAIL
                    logging.error(str(student.class_details)) 
    except Exception:
        logging.exception("")
        logging.error("CV Logs :Failed Assign asssessment to class ") 
    logging.error("CV Logs :Success assign asssessment to class ")    
    return Constant.UPDATION_SUCCESSFULL  


@ndb.transactional(xg=True,retries=5)
def assign_assessment_to_students(assessment_key, student_keys):
    class_entity = None
    students = []
    logging.info("CV Logs : Inside assign_assessment_to_students ")
    try:
        students = ndb.get_multi(student_keys)
        for student in students:
                    assessment = assessment_key.get()
                    assigned = assign_assessment_to_student(student.key, assessment.key)
                    if not assigned == Constant.UPDATION_SUCCESSFULL:
                        return Constant.ERROR_OPERATION_FAIL
                    logging.error(str(student.class_details)) 
    except Exception:
        logging.exception("")
        logging.error("CV Logs :Failed assign_assessment_to_students ") 
    logging.error("CV Logs :Success assign_assessment_to_students ")    
    return Constant.UPDATION_SUCCESSFULL  






"""
Assigns  existing classes  to an existing teacher:
                            teacher_key: key to Class entity
                            students_in_class_key : list of keys of students enrolled  in class
"""
@ndb.transactional(xg=True,retries=5)
def assign_classes_to_teacher(teacher_key, classes_under_teacher):
    
    logging.info("CV Logs :Inside  assign_classes_to_teacher():")
    teacher_entity = None
    class_names = ""
    try:
        teacher_entity = teacher_key.get() 
        for class_key in classes_under_teacher:
                   if not class_key.kind()==Class._get_kind():
                       return  Constant.ERROR_BAD_VALUE
    except Exception :
        logging.exception("")
        logging.info("CV Logs :Failed in Assigning classes :")
        return Constant.ERROR_BAD_VALUE

    teacher_entity.classes_under_teacher.extend(classes_under_teacher)              
    teacher_entity.put()     
    logging.info("CV Logs :Success Assigned classes :" + class_names + "to teacher " + teacher_entity.basic_info.firstname)
    return Constant.UPDATION_SUCCESSFULL  



"""
Assigns  existing teachers  to an existing school:
                            school_key: key to school entity
                            states_in_topic_keys : list of keys of states covered in topic
a
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
@ndb.transactional(xg=True,retries=5)
def assign_subjects_to_class(class_key, subjects_in_class_key):
    class_entity = None
    try:
        class_entity = class_key.get() 
        for subject_key in subjects_in_class_key:
                   if not subject_key.kind()==Subject._get_kind():
                       return  Constant.ERROR_BAD_VALUE
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
    class_entity.subjects_in_class_key.extend(subjects_in_class_key)              
    class_entity.put()     
    return Constant.UPDATION_SUCCESSFULL  

@ndb.transactional(xg=True,retries=5)
def assign_subjects_to_teacher(teacher_key, subjects_in_class_key):
    class_entity = None
    try:
        teacher_entity = teacher_key.get() 
        for subject_key in subjects_in_class_key:
                    if not subject_key.kind()==Subject._get_kind():
                       return  Constant.ERROR_BAD_VALUE
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
    states = []
    
    try:
        topic = topic_key.get()
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE    
    try:
        state_in_topic_reln_key = topic.states_in_topic_key
        
        states_in_topic = state_in_topic_reln_key.get()
        state_key_list = states_in_topic.states_in_topic_keys
        states = ndb.get_multi(state_key_list)
    except Exception :
        logging.exception("")
        return Constant.ERROR_INCONSISTENT_STATE

    return states



def get_states_of_topic_type(topic_key,topic_type):
    states = []
    
    try:
        topic = topic_key.get()
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE    
    try:
        state_in_topic_reln_key = topic.states_in_topic_key
        
        states_in_topic = state_in_topic_reln_key.get()
        state_key_list = states_in_topic.states_in_topic_keys
        states = ndb.get_multi(state_key_list)
    except Exception :
        logging.exception("")
        return Constant.ERROR_INCONSISTENT_STATE

    return states




def get_state_keys_of_topic(topic_key):
    states = []

    try:
        topic = topic_key.get()
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
    try:
        state_in_topic_reln_key = topic.states_in_topic_key

        states_in_topic = state_in_topic_reln_key.get()
        state_key_list = states_in_topic.states_in_topic_keys

    except Exception :
        logging.exception("")
        return Constant.ERROR_INCONSISTENT_STATE

    return state_key_list

"""
lists questions associated to a topic 
"""
def get_questions_of_topic(topic_key):
    questions = []
    try:
        topic = topic_key.get()
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE    
    try:
        question_in_topic_reln_key = topic.questions_in_topic_key
        if question_in_topic_reln_key == None:
            return Constant.ERROR_NO_DATA_FOUND 
        questions_in_topic = question_in_topic_reln_key.get()
        question_key_list = questions_in_topic.questions_in_topic_keys
        questions = ndb.get_multi(question_key_list)
    except Exception :
        logging.exception("")
        return Constant.ERROR_INCONSISTENT_STATE

    return questions 


def get_questions_of_topic_type(topic_key,topic_type):
    questions = []
    question_of_types=[]
    try:
        topic = topic_key.get()
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE    
    try:
        question_in_topic_reln_key = topic.questions_in_topic_key
        if question_in_topic_reln_key == None:
            return Constant.ERROR_NO_DATA_FOUND 
        questions_in_topic = question_in_topic_reln_key.get()
        question_key_list = questions_in_topic.questions_in_topic_keys
        questions = ndb.get_multi(question_key_list)
        for question in questions:
            if question.topic_type==topic_type:
                question_of_types.append(question.key)
    except Exception :
        logging.exception("")
        return Constant.ERROR_INCONSISTENT_STATE

    return question_of_types 

def get_a_question_of_each_type(topic_key):
    questions = []
    question_of_types={}
    question_dict={}
    try:
        topic = topic_key.get()
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE    
    try:
        question_in_topic_reln_key = topic.questions_in_topic_key
        logging.error("DEBUG: topic is "+str(topic)+"question_in_topic_reln_key "+str(question_in_topic_reln_key))
        if question_in_topic_reln_key == None:
            return Constant.ERROR_NO_DATA_FOUND 
        questions_in_topic = question_in_topic_reln_key.get()
        
        logging.error("DEBUG: questions_in_topic is "+str(questions_in_topic))
        question_key_list = questions_in_topic.questions_in_topic_keys
        logging.error("DEBUG: ququestion_key_list is "+str(question_key_list))
        questions = ndb.get_multi(question_key_list)
        logging.error("DEBUG: ququestion is "+str(questions))
        for question in questions:
                type=question.topic_type
                if type in question_of_types:
                    logging.error("DEBUG: ququestion is "+str(question)+"typeis"+str(type))
                    question_of_types[type].append(question.key)
                else :
                    logging.error("DEBUG: else ququestion is "+str(question)+"typeis"+str(type))
                    question_of_types[type]=[question.key]
        logging.error("DEBUG: question_of_types is "+str(question_of_types))
        for type_multi in question_of_types:
            length=len(question_of_types[type_multi])
            logging.error("DEBUG: (question_of_types[type_multi]) is "+str(question_of_types[type_multi]))
            if length>1:
                random_index=randint(0,length-1)
                question_dict[type_multi]=question_of_types[type_multi][random_index]
            elif length ==1:
                question_dict[type_multi]=question_of_types[type_multi][0]
            else :
                logging.error("DEBUG: Inside None is "+str(question_of_types[type_multi]))
                question_dict[type_multi]=None
            
        
                    
    except Exception :
        logging.exception("")
        return Constant.ERROR_INCONSISTENT_STATE

    return question_dict 


def get_random_question_of_type(topic_key,topic_type):
    questions = []
    question_of_types=[]
    
    try:
        topic = topic_key.get()
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE    
    try:
        question_in_topic_reln_key = topic.questions_in_topic_key
        if question_in_topic_reln_key == None:
            return Constant.ERROR_NO_DATA_FOUND 
        questions_in_topic = question_in_topic_reln_key.get()
        question_key_list = questions_in_topic.questions_in_topic_keys
        questions = ndb.get_multi(question_key_list)
        for question in questions:
                
                if topic_type == question.topic_type:
                    question_of_types.append(question.key)
                
        
        length=len(question_of_types)
        if length>1:
                random_index=randint(0,length-1)
                question=question_of_types[random_index]
        elif length ==0:
                question=question_of_types[0]
        else :
                question=None
            
        
                    
    except Exception :
        logging.exception("")
        return Constant.ERROR_INCONSISTENT_STATE

    return question














"""
lists questions associated to a state 
"""
def get_questions_of_state(state_key):
    questions = []
    try:
        logging.info("CV Logs : Inside get_questions_of_state ")
        state = state_key.get()
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE    
    try:
        question_in_state_reln_key = state.question_in_state_key 
        questions_in_state = question_in_state_reln_key.get()
        question_key_list = questions_in_state.questions_in_state_keys
        questions = ndb.get_multi(question_key_list)
        logging.info("CV Logs : Success to Inside get_questions_of_state ")
    except Exception :
        logging.exception("")
        logging.info("CV Logs : Failed to Inside get_questions_of_state ")
        return Constant.ERROR_INCONSISTENT_STATE

    return questions 


def get_types_of_state(state_key):
    type_list = []
    try:
        logging.info("CV Logs : Inside get_types_of_state ")
        state = state_key.get()
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE    
    try:
        type_in_state_reln_key = state.type_in_state_key 
        type_in_state = type_in_state_reln_key.get()
        type_list = type_in_state.types_in_state
        
        logging.info("CV Logs : Success to get_types_of_state ")
    except Exception :
        logging.exception("")
        logging.info("CV Logs : Failed to get_types_of_state ")
        return Constant.ERROR_INCONSISTENT_STATE

    return type_list 



"""
lists states (STATE_IN_TOPIC) associated to a topic name
"""
def get_states_by_topic_name(topic_name):
    states = []

    try:

        topic = Topic.query(Topic.name == topic_name).get()
        logging.error(topic)
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
    try:
        state_in_topic_reln_key = topic.states_in_topic_key
        states_in_topic = state_in_topic_reln_key.get()
        state_key_list = states_in_topic.states_in_topic_keys
        states = ndb.get_multi(state_key_list)
    except Exception :
        logging.exception("")
        return Constant.ERROR_INCONSISTENT_STATE

    return states


"""
lists questions associated to a topic name
"""
def get_questions_by_topic_name(topic_name):
    questions = []
    try:
        topic = Topic.query(Topic.name == topic_name).get()
        logging.error(topic)
    except Exception :
        logging.exception("")
        return Constant.ERROR_BAD_VALUE
    try:
        question_in_topic_reln_key = topic.questions_in_topic_key
        logging.info("############" + str(topic))
        if question_in_topic_reln_key == None:
            return Constant.ERROR_NO_DATA_FOUND
        questions_in_topic = question_in_topic_reln_key.get()
        question_key_list = questions_in_topic.questions_in_topic_keys
        questions = ndb.get_multi(question_key_list)
    except Exception :
        logging.exception("")
        return Constant.ERROR_INCONSISTENT_STATE

    return questions


"""
lists subjects associated to a student 
"""
def get_subjects_by_student(student_key):
    logging.info("CV Logs : Inside get_subjects_by_student ")
    subjects = []
    try:
        student = student_key.get()
        class_details_key = student.class_details
        if class_details_key == None:
            return Constant.ERROR_NO_DATA_FOUND
        class_details = class_details_key.get()
        subject_keys = class_details.subjects_in_class_key
        if subject_keys == None:
            return Constant.ERROR_NO_DATA_FOUND
        subjects = ndb.get_multi(subject_keys)
    except Exception:
            logging.exception("")
            logging.info("CV Logs : failed to get subjects for student :")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get subjects for student :" )
    return subjects

"""
lists subjects associated to a student 
"""
def get_subject_details_by_student(student_key):
    logging.info("CV Logs : Inside get_subjects_by_student ")
    dict_subject_details = {}
    try:
        student = student_key.get()
        class_details_key = student.class_details
        if class_details_key == None:
            return Constant.ERROR_NO_DATA_FOUND
        # class_details = class_details_key.get()
        dict_subject_details = get_subject_details_of_class(class_details_key)
        
        
       
    except Exception:
            logging.exception("")
            logging.info("CV Logs : failed to get subjects for student :")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get subjects for student :" )
    return dict_subject_details


"""
lists topics associated to a subject 
"""
def get_topics_by_subject(subject_key):
    logging.info("CV Logs : Inside get_topics_by_subject ")
    topics = []
    try:
        subject = subject_key.get()
        topics_in_subject_key = subject.topics_in_subject_key
        if topics_in_subject_key == None:
            return Constant.ERROR_NO_DATA_FOUND
        topic_keys_entity = topics_in_subject_key.get()
        topic_keys = topic_keys_entity.topics_in_subject_key
        if topic_keys == None:
            return Constant.ERROR_NO_DATA_FOUND
        topics = ndb.get_multi(topic_keys)
        return topics

    except Exception:
            logging.info("CV Logs : failed to get topics for subject :" )
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get topics for subject :" )




def get_topic_details_by_subject(subject_key):
    logging.info("CV Logs : Inside get_topics_by_subject ")
    dict_topics = {}
    try:
        subject = subject_key.get()
        topics_in_subject_key = subject.topics_in_subject_key
        if topics_in_subject_key == None:
            return Constant.ERROR_NO_DATA_FOUND
        topic_keys_entity = topics_in_subject_key.get()
        topic_keys = topic_keys_entity.topics_in_subject_key
        if topic_keys == None:
            return dict_topics
        topics = ndb.get_multi(topic_keys)
        for topic in topics:
            dict_topics.update({topic.name:topic.key.urlsafe()})
        return dict_topics

    except Exception:
            logging.info("CV Logs : failed to get topics for subject :" )
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
    


    
"""
lists assessments associated to a student 
"""
def get_assessments_by_student(student_key):
    logging.info("CV Logs : get_assessments_by_student ")
    assessments = []
    try:
        student = student_key.get()
        assesments_of_student_key = student.student_assessment_key
        student_assessments_key = assesments_of_student_key.get() 
        if student_assessments_key == None:
            return Constant.ERROR_NO_DATA_FOUND
        assessments = ndb.get_multi(student_assessments_key.attended_assessment_key)
    except Exception:
            logging.info("CV Logs : failed to get assessments for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get assessments for student :" )
    return assessments

def get_assessment_score_of_student(student_key,assessment_key):
    logging.info("CV Logs : get_assessments_by_student ")
    assessment_records = []
    try:
        student = student_key.get()
        assesments_of_student_key = student.student_assessment_key
        if assesments_of_student_key == None:
            return Constant.ERROR_NO_DATA_FOUND
        student_assessments = assesments_of_student_key.get() 
        attended_assessment=student_assessments.attended_assessment_key
        index = attended_assessment.index(assessment_key)
        if (index <0):
            return Constant.ERROR_NO_DATA_FOUND
        
        assessment_records = student_assessments.assessment_record
        assessment_record=assessment_records[index]
        return assessment_record.get().total_score
    except Exception:
            logging.info("CV Logs : failed to get assessments for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
 


def get_recent_assessment_score_of_student(student_key,subject_key):
    logging.info("CV Logs : get_assessments_by_student ")
    assessment_records = []
    try:
        student=student_key.get()
        if not (student_key.kind()==Student._get_kind() or subject_key.kind()==Subject._get_kind()):
            return Constant.ERROR_BAD_VALUE
        
    
        assessments_records = get_completed_assessment_records_by_subject(student_key,subject_key)
        logging.info("CV Logs : get_completed_assessment_records_by_subject"+str(assessments_records ))
        if len(assessments_records) == 0:
                return Constant.ERROR_NO_DATA_FOUND
                
        else :
                
                assesmentss=Assessment_Record.query(ancestor=student.school).fetch()
                logging.info("CV Logs : #######"+str(assesmentss))
                
                q_sorted_assessments_records = Assessment_Record.query(Assessment_Record.key.IN(assessments_records), ancestor=student.school)
                sorted_assessments_records = q_sorted_assessments_records.order(-Assessment_Record.completion_date).fetch() 
               
               
                #logging.error("CV Logs : failed to get get_mastery_by_subject_sc :"+str(len(q_sorted_assessments_records)))
                if sorted_assessments_records[0].total_score <=0:
                    return 0
                return sorted_assessments_records[0].total_score
    except Exception:
            logging.info("CV Logs : failed to get assessments for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL       
        
def get_recent_assessment_topic_times_of_student(student_key,subject_key):
    logging.info("CV Logs : get_assessments_by_student ")
    assessment_records = []
    try:
        student=student_key.get()
        if not (student_key.kind()==Student._get_kind() or subject_key.kind()==Subject._get_kind()):
            return Constant.ERROR_BAD_VALUE
        
    
        assessments_records = get_completed_assessment_records_by_subject(student_key,subject_key)
        logging.info("CV Logs : get_completed_assessment_records_by_subject"+str(assessments_records ))
        if len(assessments_records) == 0:
                return Constant.ERROR_NO_DATA_FOUND
                
        else :
                
                assesmentss=Assessment_Record.query(ancestor=student.school).fetch()
                logging.info("CV Logs : #######"+str(assesmentss))
                
                q_sorted_assessments_records = Assessment_Record.query(Assessment_Record.key.IN(assessments_records), ancestor=student.school)
                sorted_assessments_records = q_sorted_assessments_records.order(-Assessment_Record.completion_date).fetch() 
               
               
                #logging.error("CV Logs : failed to get get_mastery_by_subject_sc :"+str(len(q_sorted_assessments_records)))
                topic_times= sorted_assessments_records[0].topic_times
                i=0
                 
                       
                topic_times_dict={}
                topic_times_list=[]
                for topic_time in topic_times:
                    
                    if topic_time==0.0:
                        topic_times_list.append(None)
                    else :
                         topic_times_list.append(topic_time)
               
                
                logging.info("len1"+str(len(topic_times_list)))
                topics=sorted_assessments_records[0].assessment_key.get().topics_in_assessment_key
                logging.info("len2"+str(len(topics)))
                for topic_key in topics:
                    topic_times_dict[topic_key.get().name]=topic_times_list[i]
                    i=i+1
                return topic_times_dict
                
    except Exception:
            logging.info("CV Logs : failed to get assessments for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL        



def get_recent_assessment_next_states_of_student(student_key,subject_key):
    logging.info("CV Logs : get_assessments_by_student ")
    
    dict_next_states={}
    try:
        student=student_key.get()
        if not (student_key.kind()==Student._get_kind() or subject_key.kind()==Subject._get_kind()):
            return Constant.ERROR_BAD_VALUE
        
    
        assessments_records = get_completed_assessment_records_by_subject(student_key,subject_key)
        logging.info("CV Logs : get_completed_assessment_records_by_subject"+str(assessments_records ))
        if len(assessments_records) == 0:
                return Constant.ERROR_NO_DATA_FOUND
                
        else :
                
                assesmentss=Assessment_Record.query(ancestor=student.school).fetch()
                logging.info("CV Logs : #######"+str(assesmentss))
                
                q_sorted_assessments_records = Assessment_Record.query(Assessment_Record.key.IN(assessments_records), ancestor=student.school)
                sorted_assessments_records = q_sorted_assessments_records.order(-Assessment_Record.completion_date).fetch()  
               
                #logging.error("CV Logs : failed to get get_mastery_by_subject_sc :"+str(len(q_sorted_assessments_records)))
                
                next_state_list= sorted_assessments_records[0].next_state
                i=0
                 
                       
                final_next_state=[]
                for state_key in next_state_list:
                    state=state_key.get()
                    if state.type==Constant.STATE_INVALID:
                        final_next_state.append(None)
                    else :
                         final_next_state.append(state)
               
                
                
                topics=sorted_assessments_records[0].assessment_key.get().topics_in_assessment_key
                for topic_key in topics:
                    dict_next_states[topic_key.get().name]=final_next_state[i]
                    i=i+1
                return dict_next_states
    except Exception:
            logging.info("CV Logs : failed to get assessments for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL        


def get_recent_assessment_topic_scores_of_student(student_key,subject_key):
    logging.info("CV Logs : get_assessments_by_student ")
    
    dict_topic_scores={}
    try:
        student=student_key.get()
        if not (student_key.kind()==Student._get_kind() or subject_key.kind()==Subject._get_kind()):
            return Constant.ERROR_BAD_VALUE
        
    
        assessments_records = get_completed_assessment_records_by_subject(student_key,subject_key)
        logging.info("CV Logs : get_completed_assessment_records_by_subject"+str(assessments_records ))
        if len(assessments_records) == 0:
                return Constant.ERROR_NO_DATA_FOUND
                
        else :
                
                assesmentss=Assessment_Record.query(ancestor=student.school).fetch()
                logging.info("CV Logs : #######"+str(assesmentss))
                
                q_sorted_assessments_records = Assessment_Record.query(Assessment_Record.key.IN(assessments_records), ancestor=student.school)
                sorted_assessments_records = q_sorted_assessments_records.order(-Assessment_Record.completion_date).fetch()  
               
                #logging.error("CV Logs : failed to get get_mastery_by_subject_sc :"+str(len(q_sorted_assessments_records)))
                
                topic_score_list= sorted_assessments_records[0].topic_scores
                i=0
                topics=sorted_assessments_records[0].assessment_key.get().topics_in_assessment_key
                for topic_key in topics:
                    dict_topic_scores[topic_key.get().name]=topic_score_list[i]
                    i=i+1
                return dict_topic_scores
    except Exception:
            logging.info("CV Logs : failed to get assessments for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL        

def get_recent_assessment_next_questions_of_student(student_key,subject_key):
    logging.info("CV Logs : get_assessments_by_student ")
    
    dict_topic_questions={}
    try:
        student=student_key.get()
        if not (student_key.kind()==Student._get_kind() or subject_key.kind()==Subject._get_kind()):
            return Constant.ERROR_BAD_VALUE
        
    
        assessments_records = get_completed_assessment_records_by_subject(student_key,subject_key)
        logging.info("CV Logs : get_completed_assessment_records_by_subject"+str(assessments_records ))
        if len(assessments_records) == 0:
                return Constant.ERROR_NO_DATA_FOUND
                
        else :
                
                assesmentss=Assessment_Record.query(ancestor=student.school).fetch()
                logging.info("CV Logs : #######"+str(assesmentss))
                
                q_sorted_assessments_records = Assessment_Record.query(Assessment_Record.key.IN(assessments_records), ancestor=student.school)
                sorted_assessments_records = q_sorted_assessments_records.order(-Assessment_Record.completion_date).fetch()  
               
                #logging.error("CV Logs : failed to get get_mastery_by_subject_sc :"+str(len(q_sorted_assessments_records)))
                
                question_list= sorted_assessments_records[0].question_ready_to_learn
                i=0
                topics=sorted_assessments_records[0].assessment_key.get().topics_in_assessment_key
                for question in question_list:
                    topic_name=question.get().topic_key.get().name
                    if(dict_topic_questions.has_key(topic_name)):
                        value=dict_topic_questions[topic_name]
                        if not isinstance(value,list):
                           dict_topic_questions[topic_name]=[value] 
                        dict_topic_questions[topic_name].append(question.get().instance.problem_statement)                                         
                    else:
                        dict_topic_questions[topic_name]=question.get().instance.problem_statement
                    
                
                return dict_topic_questions
    except Exception:
            logging.info("CV Logs : failed to get assessments for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL  






def get_recent_assessment_next_type_url_of_student(student_key,subject_key):
    logging.info("CV Logs : get_assessments_by_student ")
    
    dict_topic_questions={}
    dict_topic_type_url={}
    try:
        student=student_key.get()
        if not (student_key.kind()==Student._get_kind() or subject_key.kind()==Subject._get_kind()):
            return Constant.ERROR_BAD_VALUE
        
    
        assessments_records = get_completed_assessment_records_by_subject(student_key,subject_key)
        logging.info("CV Logs : get_completed_assessment_records_by_subject"+str(assessments_records ))
        if len(assessments_records) == 0:
                return Constant.ERROR_NO_DATA_FOUND
                
        else :
                
                assesmentss=Assessment_Record.query(ancestor=student.school).fetch()
                logging.info("CV Logs : #######"+str(assesmentss))
                
                q_sorted_assessments_records = Assessment_Record.query(Assessment_Record.key.IN(assessments_records), ancestor=student.school)
                sorted_assessments_records = q_sorted_assessments_records.order(-Assessment_Record.completion_date).fetch()  
               
                #logging.error("CV Logs : failed to get get_mastery_by_subject_sc :"+str(len(q_sorted_assessments_records)))
                
                question_list= sorted_assessments_records[0].question_ready_to_learn
                i=0
                topics=sorted_assessments_records[0].assessment_key.get().topics_in_assessment_key
                for question in question_list:
                    topic_name=question.get().topic_key.get().name
                    if(dict_topic_questions.has_key(topic_name)):
                        value=dict_topic_questions[topic_name]
                        if not isinstance(value,list):
                           dict_topic_questions[topic_name]=[value] 
                        dict_topic_questions[topic_name].append(question.get())                                         
                    else:
                        dict_topic_questions[topic_name]=[question.get()]
                    
                for key in dict_topic_questions:
                    question=dict_topic_questions[key][0]
                    dict_topic_type_url[key]=[question.topic_type,question.instance.url]
                return dict_topic_type_url
    except Exception:
            logging.info("CV Logs : failed to get assessments for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL  






'''' 
def get_recent_assessment_score_of_student(student_key,subject_key):
    logging.info("CV Logs : get_assessments_by_student ")
    assessment_records = []
    try:
        student = student_key.get()
        assesments_of_student_key = student.student_assessment_key
        if assesments_of_student_key == None:
            return Constant.ERROR_NO_DATA_FOUND
        assessment_key=get_recent_assessment_of_student(student_key,subject_key)
        if not (assessment_key.kind()==Assessment._get_kind() ):
            return Constant.ERROR_BAD_VALUE
        
        return assessment_key.get().total_score
    except Exception:
            logging.info("CV Logs : failed to get assessments for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL        
'''
def get_assessment_next_states_of_student(student_key,assessment_key):
    logging.info("CV Logs : get_assessments_by_student ")
    dict_next_states = {}
    try:
        student = student_key.get()
        topics=assessment_key.get().topics_in_assessment_key
        assesments_of_student_key = student.student_assessment_key
        if assesments_of_student_key == None:
            return Constant.ERROR_NO_DATA_FOUND
        student_assessments = assesments_of_student_key.get() 
        attended_assessment=student_assessments.attended_assessment_key
        index = attended_assessment.index(assessment_key)
        if (index <0):
            return Constant.ERROR_NO_DATA_FOUND
        
        assessment_records = student_assessments.assessment_record
        assessment_record=assessment_records[index]
        next_state_list= assessment_record.get().next_state
        i=0
        for topic_key in topics:
            dict_next_states[topic_key.get().name]=next_state_list[i]
            i=i+1
        return dict_next_states
    except Exception:
            logging.info("CV Logs : failed to get assessments for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL

def get_assessment_next_questions_of_student(student_key,assessment_key):
    logging.info("CV Logs : get_assessments_by_student ")
    dict_next_questions = {}
    try:
        student = student_key.get()
        topics=assessment_key.get().topics_in_assessment_key
        assesments_of_student_key = student.student_assessment_key
        if assesments_of_student_key == None:
            return Constant.ERROR_NO_DATA_FOUND
        student_assessments = assesments_of_student_key.get() 
        attended_assessment=student_assessments.attended_assessment_key
        index = attended_assessment.index(assessment_key)
        if (index <0):
            return Constant.ERROR_NO_DATA_FOUND
        
        assessment_records = student_assessments.assessment_record
        assessment_record=assessment_records[index]
        next_question_list= assessment_record.get().question_ready_to_learn
        i=0
        for topic_key in topics:
            dict_next_questions[topic_key.get().name]=next_question_list[i].get().instance.problem_statement
            i=i+1
        return dict_next_questions
    except Exception:
            logging.info("CV Logs : failed to get assessments for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL            
 
 
def get_assessment_scores_of_student(student_key,assessment_key):
    logging.info("CV Logs : get_assessments_by_student ")
    dict_topic_scores = {}
    try:
        student = student_key.get()
        topics=assessment_key.get().topics_in_assessment_key
        assesments_of_student_key = student.student_assessment_key
        if assesments_of_student_key == None:
            return Constant.ERROR_NO_DATA_FOUND
        student_assessments = assesments_of_student_key.get() 
        attended_assessment=student_assessments.attended_assessment_key
        index = attended_assessment.index(assessment_key)
        if (index <0):
            return Constant.ERROR_NO_DATA_FOUND
        
        assessment_records = student_assessments.assessment_record
        assessment_record=assessment_records[index]
        topic_score_list= assessment_record.get().topic_scores
        i=0
        for topic_key in topics:
            dict_topic_scores[topic_key.get().name]=topic_score_list[i]
            i=i+1
        return dict_topic_scores
    except Exception:
            logging.info("CV Logs : failed to get assessments for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL            
  
   






def get_assessment_record_by_student(student_key):
    logging.info("CV Logs : get_assessments_by_student ")
    assessment_records = []
    try:
        student = student_key.get()
        assesments_of_student_key = student.student_assessment_key
        if assesments_of_student_key == None:
            return Constant.ERROR_NO_DATA_FOUND
        student_assessments_key = assesments_of_student_key.get() 
        
        assessment_records = ndb.get_multi(student_assessments_key.assessment_record)
    except Exception:
            logging.info("CV Logs : failed to get assessments for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get assessments for student :" + student.basic_info.firstname)
    return assessment_records


"""
lists assessments associated to a topic for a student 
"""
def get_assessments_by_topic(student_key, topic_key):
    logging.info("CV Logs : get_assessments_by_topic ")
    assessments = []
    try:
        if not topic_key.kind()==Topic._get_kind():
            return  Constant.ERROR_BAD_VALUE
        assesments_of_student = get_assessments_by_student(student_key)
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
lists assessments associated to a topic for a student 
"""
def get_assessment_records_by_topic(student_key, topic_key):
    logging.info("CV Logs : get_assessments_by_topic ")
    assessment_records = []
    try:
        if not topic_key.kind()==Topic._get_kind():
            return  Constant.ERROR_BAD_VALUE
        assessment_records_of_student = get_assessment_record_by_student(student_key)
        for assessment_record in assessment_records_of_student:
            if topic_key in assessment_record.assessment_key.get().topics_in_assessment_key:
                assessment_records.append(assessment_record)
            
        
    except Exception:
            logging.info("CV Logs : failed to get assessments of topic  for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get assessments for student :")
    return assessment_records




"""
lists assessments associated to a topic for a student 
"""
def get_assessment_record_keys_by_topic(student_key, topic_key):
    logging.info("CV Logs : get_assessments_by_topic ")
    assessment_records = []
    try:
        if not topic_key.kind()==Topic._get_kind():
            return  Constant.ERROR_BAD_VALUE
        assessment_records_of_student = get_assessment_record_by_student(student_key)
        for assessment_record in assessment_records_of_student:
            if topic_key in assessment_record.assessment_key.get().topics_in_assessment_key:
                assessment_records.append(assessment_record.key)
            
        
    except Exception:
            logging.info("CV Logs : failed to get assessments of topic  for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get assessments for student :")
    return assessment_records


"""
lists assessments associated to a topic for a student 
"""
def get_completed_assessment_record_keys_by_topic(student_key, topic_key):
    logging.info("CV Logs : get_assessments_by_topic ")
    assessment_records = []
    try:
        if not topic_key.kind()==Topic._get_kind():
            return  Constant.ERROR_BAD_VALUE
        assessment_records_of_student = get_assessment_record_by_student(student_key)
        for assessment_record in assessment_records_of_student:
            if topic_key in assessment_record.assessment_key.get().topics_in_assessment_key:
                if assessment_record.score == -1:
                    continue
                assessment_records.append(assessment_record.key)
            
        
    except Exception:
            logging.info("CV Logs : failed to get assessments of topic  for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get assessments for student :")
    return assessment_records




def get_completed_assessment_records_by_subject(student_key, subject_key):
    logging.info("CV Logs : get_completed_assessment_records_by_subject")
    assessment_records = []
    try:
        if not subject_key.kind()==Subject._get_kind():
            return  Constant.ERROR_BAD_VALUE
        assessment_records_of_student = get_assessment_record_by_student(student_key)
        for assessment_record in assessment_records_of_student:
            if assessment_record.assessment_key.get().subject_key ==subject_key and not assessment_record.completion_date ==Default.date:
                assessment_records.append(assessment_record.key)
        
    except Exception:
            logging.info("CV Logs : failed to get_completed_assessment_records_by_subject :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get_completed_assessment_records_by_subject:")
    return assessment_records









"""
lists assessments associated to a topic for a student 
"""
def get_completed_assessment_records_by_topic(student_key, topic_key):
    logging.info("CV Logs : get_assessments_by_topic ")
    assessment_records = []
    try:
        if not topic_key.kind()==Topic._get_kind():
            return  Constant.ERROR_BAD_VALUE
        assessment_records_of_student = get_assessment_record_by_student(student_key)
        for assessment_record in assessment_records_of_student:
            if topic_key in assessment_record.assessment_key.get().topics_in_assessment_key:
                if assessment_record.score == -1:
                    continue
                assessment_records.append(assessment_record)
            
        
    except Exception:
            logging.info("CV Logs : failed to get assessments of topic  for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get assessments for student :")
    return assessment_records


"""
get assessment score associated to a student 
"""
def get_student_score_in_assessment(student_key, assessment_key):
    logging.info("CV Logs : get_student_score_in_assessment ")
    try:
        student = student_key.get()
        assesments_of_student_key = student.student_assessment_key
        student_assessments = assesments_of_student_key.get()
        assessment = assessment_key.get()
        if student_assessments == None:
            return Constant.ERROR_NO_DATA_FOUND
        pos = student_assessments.attended_assessment_key.index(assessment_key)
        if not pos >= 0 : 
            return Constant.ERROR_NO_DATA_FOUND 
        
        if len(student_assessments.assessment_record) == pos - 1:
            return Constant.ERROR_NO_DATA_FOUND
        logging.error("!!!!!!!!!!!!!!!!1" + str(len(student_assessments.assessment_record)))
        if len(student_assessments.assessment_record) == 0:
            return 0
        assessment_record_key = student_assessments.assessment_record[pos]
        assessment_record = assessment_record_key.get()
        
       
        if assessment_record == None:
            return Constant.ERROR_OPERATION_FAIL
        return assessment_record.score
        
       
    except Exception:
            # logging.info("CV Logs : failed to get score of assessment"+ assessment.name+" for student :"+student.basic_info.firstname)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get score of assessment" + assessment.name + " for student :" + student.basic_info.firstname)


"""
get assessment score associated to a student 
"""
def get_student_completion_date_in_assessment(student_key, assessment_key):
    logging.info("CV Logs : get_student_score_in_assessment ")
    try:
        student = student_key.get()
        assesments_of_student_key = student.student_assessment_key
        student_assessments = assesments_of_student_key.get()
        assessment = assessment_key.get()
        if student_assessments == None:
            return Constant.ERROR_NO_DATA_FOUND
        pos = student_assessments.attended_assessment_key.index(assessment_key)
        if not pos >= 0 : 
            return Constant.ERROR_NO_DATA_FOUND 
        
        if len(student_assessments.assessment_record) == pos - 1:
            return Constant.ERROR_NO_DATA_FOUND  
        assessment_record_key = student_assessments.assessment_record[pos - 1]
        assessment_record = assessment_record_key.get()
        
       
        if assessment_record == None:
            return Constant.ERROR_OPERATION_FAIL
        return assessment_record.completion_date
        
       
    except Exception:
            # logging.info("CV Logs : failed to get score of assessment"+ assessment.name+" for student :"+student.basic_info.firstname)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get score of assessment" + assessment.name + " for student :" + student.basic_info.firstname)

"""
//TODO
get assessment state associated to a student 
""" 
def get_student_current_state_in_assessment(student_key, assessment_key):
    logging.info("CV Logs : get_student_state_in_assessment ")
    
    try:
        student = student_key.get()
        assesments_of_student_key = student.student_assessment_key
        student_assessments = assesments_of_student_key.get()
        assessment = assessment_key.get()
        if student_assessments == None:
            return Constant.ERROR_NO_DATA_FOUND
        pos = student_assessments.attended_assessment_key.index(assessment_key)
        if not pos >= 0 : 
            return Constant.ERROR_NO_DATA_FOUND  
        if assessment.current_state == None:
            return Constant.ERROR_NO_DATA_FOUND
       
        return assessment.current_state.get()
       
    except Exception:
            logging.info("CV Logs : failed to get state of assessment" )
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get state of assessment" )
  



"""
//TODO
get assessment next state associated to a student 
def get_student_next_state_in_assessment(student_key, assessment_key):
    logging.info("CV Logs : get_student_state_in_assessment ")
    
    try:
        student = student_key.get()
        assesments_of_student_key = student.student_assessment_key
        student_assessments = assesments_of_student_key.get()
        if not assessment_key.kind()==Assessment._get_kind():
            return Constant.ERROR_BAD_VALUE
        if student_assessments == None:
            return Constant.ERROR_NO_DATA_FOUND
        pos = student_assessments.attended_assessment_key.index(assessment_key)
        if not pos >= 0 : 
            return Constant.ERROR_NO_DATA_FOUND  
        if assessment.next_state == None:
            return Constant.ERROR_NO_DATA_FOUND
        logging.info("CV Logs : success to get next state of assessment" + assessment.name + " for student :" + student.basic_info.firstname)
        return assessment.next_state.get()
       
    except Exception:
            logging.info("CV Logs : failed to get next state of assessment" + assessment.name + " for student :" + student.basic_info.firstname)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    
  

"""
"""
get assessment next state associated to a student 
""" 
def get_student_next_question_in_assessment(student_key, assessment_key):
    logging.info("CV Logs : get_student_state_in_assessment ")
    
    try:
        student = student_key.get()
        assesments_of_student_key = student.student_assessment_key
        student_assessments = assesments_of_student_key.get()
        if not assessment_key.kind()==Assessment._get_kind():
            return Constant.ERROR_BAD_VALUE
        if student_assessments == None:
            return Constant.ERROR_NO_DATA_FOUND
        pos = student_assessments.attended_assessment_key.index(assessment_key)
        if not pos >= 0 : 
            return Constant.ERROR_NO_DATA_FOUND  
        if len(student_assessments.assessment_record) == 0:
            return Constant.ERROR_NO_DATA_FOUND
        assessment_record_key = student_assessments.assessment_record[pos]
        assessment_record = assessment_record_key.get()
        
       
        if assessment_record == None:
            return Constant.ERROR_OPERATION_FAIL
        question_entity = assessment_record.question_ready_to_learn
        question = question_entity.get().instance.problem_statement
        return question
            
    except Exception:
            # logging.info("CV Logs : failed to get next question ready to learn of assessment" + assessment.name + " for student :" + student.basic_info.firstname)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
  


"""
get assessment next state associated to a student 
""" 
def get_topper_mastery_in_subject(subject_key, student_key):
    logging.info("CV Logs : get_topper_mastery_in_subject ")
    
    try:
        g_mastry = 0.0
        student = student_key.get()
        class_key = student.class_details.get()
        students = get_students_by_class(class_key)
        for students in students:
            mastry = get_mastery_by_subject(subject_key, students.key)
            if g_mastry < mastry:
                g_mastry = mastry
                topper = students
        
            logging.info("CV Logs : success to get topper ")
        return {topper:g_mastry}
       
    except Exception:
            logging.info("CV Logs : failed to get ")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            


"""
get_pending_assessment_subject  Add max marks logic
""" 
def get_pending_assessment_subject(subject_key, student_key):
    logging.info("CV Logs : get_pending_assessment_subject ")
    assessments = []
    assessment_topic = []
    pending_assessments = []
    pending_assesments_dict = {}
    try:
            assessment_record = get_assessment_records_by_topic(student_key, topic.key)
            
            if len(assessment_record) > 0:
                    assessments.extend(assessment_record)
            for assesment_final in assessments:
                  assessment_date = assesment_final.completion_date
                  if assessment_date == None:
                      assessment_key = assesment_final.assessment_key
                      assessment = assessment_key.get()
                      # pending_assessments.append(assesment_final) 
                      pending_assesments_dict.update({assessment_key.urlsafe():[assessment.name, assessment.due_date.strftime("%d-%m-%y:%H-%M")]})
            logging.error("CV Logs :Success to get_pending_assessment_subject ")
            return pending_assesments_dict
    except Exception:
        logging.error("CV Logs : Failed to get_pending_assessment_subject ")
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
        teacher = teacher_key.get()
        classes_of_teacher_keys = teacher.classes_under_teacher
        classes_of_teacher = ndb.get_multi(classes_of_teacher_keys)        
        logging.info("CV Logs : success to get classes of teacher" + teacher.basic_info.firstname)
        return classes_of_teacher
    except Exception:
            logging.info("CV Logs : failed to get classes of teacher" + teacher.basic_info.firstname)
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get classes of teacher" + teacher.basic_info.firstname)


def get_class_details_of_teacher(teacher_key):
    logging.info("CV Logs : get_classes_of_teacher ")
    try:
        dict_class = {}
        teacher = teacher_key.get()
        classes_of_teacher_keys = teacher.classes_under_teacher
        classes_of_teacher = ndb.get_multi(classes_of_teacher_keys)
        for class_entity in classes_of_teacher:
            dict_class.update({class_entity.key.urlsafe():class_entity.name + " " + class_entity.section_details})
        logging.info("CV Logs : success to get class details of teacher" )
        return dict_class
    except Exception:
            logging.error("CV Logs : failed to get class details of teacher")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            



"""
get subjects  associated to a teacher 
"""
def get_subjects_of_teacher_in_class(teacher_key, class_key):
    logging.info("CV Logs : get_subjects_of_teacher ")
    try:
        subjects = []
        teacher_entity = teacher_key.get()
        if not class_key.kind()==Class._get_kind():
            return Constant.ERROR_BAD_VALUE
        subjects_of_teacher_keys = teacher_entity.subjects
        subjects_of_teacher = ndb.get_multi(subjects_of_teacher_keys)
        for subject in subjects_of_teacher:
            if subject.class_key == class_key:
                subjects.append(subject)       
        logging.info("CV Logs : success to get subjects of teacher")
        return subjects
    except Exception:
            logging.error("CV Logs : to get subjects of teacher" )
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
        
 
"""
get subjects  associated to a teacher 
"""
def get_subject_details_of_teacher_in_class(teacher_key, class_key):
    logging.info("CV Logs : get_subject_details_of_teacher_in_class ")
    try:
        subjects = []
        dict_subjects = {}
        teacher_entity = teacher_key.get()
        if not class_key.kind()==Class._get_kind():
            return Constant.ERROR_BAD_VALUE
        subjects_of_teacher_keys = teacher_entity.subjects
        subjects_of_teacher = ndb.get_multi(subjects_of_teacher_keys)
        for subject in subjects_of_teacher:
            if subject.class_key == class_key:
                dict_subjects.update({subject.key.urlsafe():subject.name})       
        logging.info("CV Logs : success to get subject details  of class for teacher")
        return dict_subjects
    except Exception:
            logging.error("CV Logs : Failed to subject details  of class for teacher" )
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL       
            


def get_assessment_count_by_topic(topic_key,school_key):
    logging.info("CV Logs : get_assessments_by_topic ")
    assessments = []
    try:
        assessments=Assessment.query(ancestor=school_key).fetch()
        for assessment in assessments:
            if topic_key in assessment.topics_in_assessment_key:
                assessments.append(assessment)
        count=len(assessments)
    except Exception:
            logging.info("CV Logs : failed to get assessments of topic  for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL

    logging.info("CV Logs : success to get assessments for student :")
    return count



def get_basic_details_of_teacher(teacher_key, class_key):
    logging.info("CV Logs : get_subject_details_of_teacher_in_class ")
    try:
        subjects = []
        dict_subjects = {}
        teacher_entity = teacher_key.get()
        if not class_key.kind()==Class._get_kind():
            return Constant.ERROR_BAD_VALUE
        subjects_of_teacher_keys = teacher_entity.subjects
        subjects_of_teacher = ndb.get_multi(subjects_of_teacher_keys)
        for subject in subjects_of_teacher:
            if subject.class_key == class_key:
                dict_subjects.update({subject.key.urlsafe():subject.name})       
        #logging.info("CV Logs : success to get subject details  of class for teacher" + class_entity.name + ":" + class_entity.section_details)
        return dict_subjects
    except Exception:
            logging.error("CV Logs : Failed to subject details  of class for teacher" )
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL       
            

"""
get subjects  associated to a class 
"""
def get_subjects_of_class(class_key):
    logging.info("CV Logs : get_subjects_of_class ")
    try:
        class_entity = class_key.get()
        subjects_of_class_keys = class_entity.subjects_in_class_key
        subjects_of_class = ndb.get_multi(subjects_of_class_keys)        
        logging.info("CV Logs : success to get subjects of class" )
        return subjects_of_class
    except Exception:
            logging.error("CV Logs : failed to get subjects of class")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL


def get_pending_assessments_by_subject(student_key, subject_key):
    logging.info("CV Logs : get_pending_assessments_by_subject")
    assessment_records = []
    pending_assesments_dict={}
    try:
        if not subject_key.kind()==Subject._get_kind():
            return  Constant.ERROR_BAD_VALUE
        assessment_records_of_student = get_assessment_record_by_student(student_key)
        for assessment_record in assessment_records_of_student:
            if assessment_record.assessment_key.get().subject_key ==subject_key and not (assessment_record.completion_date > Default.date):
                assessment=assessment_record.assessment_key.get()
                pending_assesments_dict.update({assessment.key.urlsafe():[assessment.name, assessment.due_date.strftime("%d-%m-%y:%H-%M")]})
                
    except Exception:
            logging.info("CV Logs : failed to get_pending_assessments_by_subject :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL
            
    logging.info("CV Logs : success to get_pending_assessments_by_subject:")
    return pending_assesments_dict


def get_subject_details_of_class(class_key):
    
    logging.info("CV Logs : get_subject_details_of_class ")
    try:
        dict_subjects = {}
        class_entity = class_key.get()
        subjects_of_class_keys = class_entity.subjects_in_class_key
        subjects_of_class = ndb.get_multi(subjects_of_class_keys) 
        a = len(subjects_of_class)
        for subject in subjects_of_class:
            dict_subjects.update({subject.name:subject.key.urlsafe()})       
        logging.info("CV Logs : success to get subjects of class" + class_entity.name + ":" + class_entity.section_details)
        return dict_subjects
    except Exception:
            logging.error("CV Logs : to get subjects of class")
            logging.exception("")

            return Constant.ERROR_OPERATION_FAIL


"""
get subjects  associated to a class 
"""
def get_subject_details(subject_key):
    logging.info("CV Logs : Inside get_subject_details ")
    try:
        dict_subjectinfo = {}
        topic_names = []
        subject_entity = subject_key.get()
        subject_name = subject_entity.name
        subject_topic_keys = subject_entity.topics_in_subject_key
        subject_topic = subject_topic_keys.get()
        topic_keys = subject_topic.topics_in_subject_key
        for topic_key in topic_keys:
            topic = topic_key.get()
            topic_names.append(topic.name)
        dict_subjectinfo.update({subject_name:topic_names})
        logging.info("CV Logs : Success to  get_subject_details ")
        return dict_subjectinfo
    except Exception:
            logging.error("CV Logs : Failed to  get_subject_details ")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL




            
"""
lists students  associated to a class 
"""
def get_students_by_class(class_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    students = []
    try:
        class_entity = class_key.get()
        students_in_class_keys = class_entity.students_in_class_key
        students = ndb.get_multi(students_in_class_keys)
        logging.info("CV Logs : success to get students for class :" + class_entity.name + ":" + class_entity.section_details)
        return students
    except Exception:
        logging.error("CV Logs : failed to get students for class :" )
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL



def get_student_count_by_subject(subject_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    students = []
    try:
        subject_entity = subject_key.get()
        class_entity=subject_entity.class_key.get()
        students_in_class_keys = class_entity.students_in_class_key
        students = ndb.get_multi(students_in_class_keys)
        logging.info("CV Logs : success to get students for class :" + class_entity.name + ":" + class_entity.section_details)
        return len(students)
    except Exception:
        logging.error("CV Logs : failed to get students for class :" )
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL


def get_course_detail_by_subject(subject_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    students = []
    dict_details={}
    try:
        subject_entity = subject_key.get()
        class_entity=subject_entity.class_key.get()
        students_in_class_keys = class_entity.students_in_class_key
        students = ndb.get_multi(students_in_class_keys)
        average_score=0
        total_score=0
        total_students=len(students)
        count=0
        for student in students:
            score=get_recent_assessment_score_of_student(student.key,subject_key)
            logging.info("CV Logs : Score is"+str(score))
            if score <0:
               continue
            if score == 100:
               count=count+1 
            total_score=total_score+score
        average_score=total_score/total_students
        dict_details['Total_Students']=total_students
        dict_details['Average_Score']=average_score
        dict_details['100_Score_Students']=count  
        logging.info("CV Logs : success to get students for class :" + class_entity.name + ":" + class_entity.section_details)
        return dict_details
    except Exception:
        logging.error("CV Logs : failed to get students for class :" )
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL



def get_student_keys_by_class(class_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    students = []
    try:
        class_entity = class_key.get()
        students_in_class_keys = class_entity.students_in_class_key
        logging.info("CV Logs : success to get students for class :" )
        return students_in_class_keys
    except Exception:
        logging.error("CV Logs : failed to get students for class :" )
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL


'''//TODO

'''
def get_average_score_by_subject(subject_key, teacher_key, class_key):
    logging.info("CV Logs : Inside get_average_score_by_subject ")
    students = []
    mastery = 0
    count = 0
    try:
        teacher_entity = teacher_key.get()
        classess = teacher_entity.classes_under_teacher
        students_in_class = get_students_by_class(class_key)
        for student in students_in_class:
            mastery = mastery + get_mastery_by_subject(subject_key, student.key)
            count += 1
        average_mastery = mastery / float(count)  
    
        logging.info("CV Logs : Success to get_average_score_by_subject ")
        return (average_mastery)
    except Exception:
        logging.error("CV Logs : Failed  to get_average_score_by_subject ")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL



'''//TODO

'''
def get_average_mastery_by_subject_detailed(teacher_key, class_key, subject_key):
    logging.info("CV Logs : Inside get_average_mastery_by_subject_detailed ")
    students = []
    mastery = 0
    mastery_topic = 0
    count = 0
    count1 = 0
    dict_average_topic_mastery = {}
    try:
        teacher_entity = teacher_key.get()
       
        if not (subject_key.kind()==Subject._get_kind() or teacher_key.kind()==Teacher._get_kind() ):
            return Constant.ERROR_BAD_VALUE
        students_in_class = get_students_by_class(class_key)
        topics = get_topics_by_subject(subject_key)
        if isinstance(topics, int):
             dict_average_topic_mastery = {}
             return [0, dict_average_topic_mastery]
        for student in students_in_class:
            a = get_mastery_by_subject(subject_key, student.key)
            mastery = mastery + a
            count += 1
        average_mastery = int(mastery / float(count)) 
        for topic in topics:
                mastery_topic = 0
                count1 = 0
                for student in students_in_class:
                    a = get_mastery_by_topic(topic.key, student.key)
                    mastery_topic = mastery_topic + get_mastery_by_topic(topic.key, student.key)
                    count1 += 1
                average_topic_mastery = mastery_topic / float(count1)
                dict_average_topic_mastery.update({topic.name:int(average_topic_mastery)})
        logging.info("CV Logs : Success to get_average_mastery_by_subject_detailed ")
        return [average_mastery, dict_average_topic_mastery]
    except Exception:
        logging.error("CV Logs : Failed to get_average_mastery_by_subject_detailed ")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL



'''//TODO

'''
def get_average_mastery_by_subject_of_all_class(teacher_key):
    logging.info("CV Logs : get_average_mastery_by_subject_of_all_class ")
    dict_mastery_class = {}
    dict_mastery = {}
    try:

        teacher_entity=teacher_key.get()
        classes = teacher_entity.classes_under_teacher
        for class_key in classes:
            subjects = get_subjects_of_teacher_in_class(teacher_key, class_key)
            for subject in subjects:
                 mastery = get_average_mastery_by_subject_detailed(teacher_key, class_key, subject.key)
                 dict_mastery_class.update({subject.name:mastery[0]})
            class_entity = class_key.get()
            class_name = class_entity.name + class_entity.section_details
            dict_mastery.update({class_name:dict_mastery_class})       
        logging.info("CV Logs : success to get_average_mastery_by_subject_of_all_class ")
        return dict_mastery
    except Exception:
        logging.error("CV Logs : success to get_average_mastery_by_subject_of_all_class ")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL




'''TODO'''
def get_mastery_by_student_of_class(teacher_key, class_key, subject_key):
    logging.info("CV Logs : Inside get_mastery_by_student_of_class ")

    dict__mastery = {}
    try:
        if not teacher_key.kind()==Teacher._get_kind():
            return Constant.ERROR_BAD_VALUE

               
        students_in_class = get_students_by_class(class_key)
        
        for student in students_in_class:
            mastery = get_mastery_by_subject(subject_key, student.key)
            dict__mastery.update({student.basic_info.firstname + student.basic_info.lastname:mastery})
            
        logging.info("CV Logs : Success to get_mastery_by_student_of_class ")
        return dict__mastery
    except Exception:
        logging.error("CV Logs : failed  to get_mastery_by_student_of_class ")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL


def get_prerequisite_topics_of_topic(topic_key):
    logging.info("CV Logs : Inside get_prerequisite_topics_of_topic ")

    #dict_prerequiste_topic = {}
    try:
        if not topic_key.kind()==Topic._get_kind():
            return Constant.ERROR_BAD_VALUE


        prerequisite_topics_keys=topic_key.get().prerequisite_topic
        
        return prerequisite_topics_keys
    except Exception:
        logging.error("CV Logs : failed  to get_mastery_by_student_of_class ")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL


'''
//TODO Threhsold need to be set 
'''
def get_students_not_logged_in_by_class(teacher_key, class_key):
    logging.info("CV Logs : Inside get_students_not_logged_in_by_class ")

    dict_users_not_logged_in = {}
    try:
        teacher_entity = teacher_key.get()
        classess = teacher_entity.classes_under_teacher

        class_entity = class_key.get()
        students_in_class_keys = class_entity.students_in_class_key
        students = ndb.get_multi(students_in_class_keys)
        
        for student in students:
            user_name = student.basic_info.firstname + "_" + student.basic_info.lastname
            student_user = User.query(User.username == user_name).get()
            if not student_user == None: 
                login_detail = student_user.lastlogin
                if login_detail == None:
                    login = "--"
                else :
                    login = login_detail.strftime("%d-%m-%y:%H-%M")
                # threshold need to be set
                # if login_detail == None :
                 #   pass
                # else:
                dict_users_not_logged_in.update({student.basic_info.firstname + " " + student.basic_info.lastname:login})
                # dict_users_not_logged_in={student.basic_info.firstname+" "+student.basic_info.lastname:student_user.lastlogin}
        logging.info("CV Logs : success to  get_students_not_logged_in_by_class ")
        return dict_users_not_logged_in
    except Exception:
        logging.error("CV Logs : failed to  get_students_not_logged_in_by_class ")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL



def get_students_not_logged_in_of_all_class(teacher_key):
    logging.info("CV Logs : Inside get_students_not_logged_in_of_all_class ")
    students = []
    dict_users_not_logged_in = {}
    try:
        
        teacher_entity = teacher_key.get()
        classess = teacher_entity.classes_under_teacher
        for class_key in classess:
               students = get_students_not_logged_in_by_class(teacher_key, class_key)
               dict_users_not_logged_in.update(students)
        logging.info("CV Logs : success to get_students_not_logged_in_of_all_class ")
        return dict_users_not_logged_in
    except Exception:
        logging.error("CV Logs : failed to get_students_not_logged_in_of_all_class ")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL
   
    

def get_average_mastery_all_subject_detailed(teacher_key, class_key):
    logging.info("CV Logs : Inside get_students_by_class ")

    dict_data = {}
    try:

        if not teacher_key.kind()==Teacher._get_kind():
            return Constant.ERROR_BAD_VALUE
        subjects = get_subjects_of_teacher_in_class(teacher_key, class_key)
        for subject in subjects:
            mastery = get_average_mastery_by_subject_detailed(teacher_key, class_key, subject.key)
            dict_data.update({subject.name:mastery})
         
        logging.info("CV Logs : success to get_average_mastery_all_subject_detailed :")
        return dict_data
    except Exception:
        logging.exception("")
        logging.error("CV Logs : failed to get_average_mastery_all_subject_detailed :")
        return Constant.ERROR_OPERATION_FAIL



def get_average_mastery_of_a_subject(teacher_key, class_key, subject_key):
    logging.info("CV Logs : Inside get_average_mastery_of_a_subject")

    dict_data = {}
    try:
        subject =subject_key.get()
        if not ( teacher_key.kind()==Teacher._get_kind()):
            return Constant.ERROR_BAD_VALUE
        mastery = get_average_mastery_by_subject_detailed(teacher_key, class_key, subject_key)
        dict_data.update({subject.name:mastery})
         
        logging.info("CV Logs : success to get_average_mastery_of_a_subject")
        return dict_data
    except Exception:
        logging.exception("")
        logging.error("CV Logs : failed to get_average_mastery_of_a_subject")
        return Constant.ERROR_OPERATION_FAIL


   

def get_assessment_coverage_of_class(teacher_key, class_key):
    logging.info("CV Logs : Inside get_assessment_coverage_of_class ")
    dict_assessment_data = {}
    dict_assessment_coverage = {}
    try:
        teacher_entity = teacher_key.get()
        assessments = Assessment.query(Assessment.class_key == class_key, ancestor=teacher_entity.school).fetch()
        if assessments == None:
            return {}
        for assessment in assessments:
            topics = assessment.topics_in_assessment_key
            topic = topics[0].get()
            subject_key = topic.subject_key
            subject_name = subject_key.get().name
            percentage_covered = (assessment.no_of_user_completed / float(len(get_students_by_class(class_key)))*Constant.MAX_MARKS)
            dict_assessment_data.update({assessment.name:{subject_name:(percentage_covered)}})
        logging.info("CV Logs : Success to get_assessment_coverage_of_class ")
        return dict_assessment_data
    except Exception:
        logging.exception("")
        logging.error("CV Logs : failed to  get_assessment_coverage_of_class ")
        return Constant.ERROR_OPERATION_FAIL
        
                
def get_assessment_coverage_of_subject(teacher_key, class_key, subject_key):
    logging.info("CV Logs : Inside get_assessment_coverage_of_subject ")
    dict_assessment_data = {}
    dict_assessment_coverage = {}
    try:

        if not teacher_key.kind()==Teacher._get_kind():
            return Constant.ERROR_BAD_VALUE
        assessments = Assessment.query(Assessment.class_key == class_key).fetch()
        if assessments == None:
            return {}
        for assessment in assessments:
            topics = assessment.topics_in_assessment_key
            topic = topics[0].get()

            if subject_key == topic.subject_key:
                percentage_covered = (assessment.no_of_user_completed / float(len(get_students_by_class(class_key)))*Constant.MAX_MARKS)
                dict_assessment_data.update({assessment.name:(percentage_covered)})
        
        logging.info("CV Logs : success to get_assessment_coverage_of_subject :")
        return dict_assessment_data
    except Exception:
        logging.error("CV Logs : failed to get_assessment_coverage_of_subject")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL





"""
todo 
"""
def get_ready_to_learn_of_class(teacher_key, class_key, subject_key):
    logging.info("CV Logs : Inside get_ready_to_learn_of_class ")

    dict_ready_to_learn = {}
    try:
        count=0
        if not (teacher_key.kind()==Teacher._get_kind() or subject_key.kind()==Subject._get_kind()):
            return Constant.ERROR_BAD_VALUE
        students = get_students_by_class(class_key)
        topics = get_topics_by_subject(subject_key)
        for topic in topics :
            for student in students:
                count += 1
                ready_to_learn = get_ready_to_learn_topic(topic.key, student.key)
                if isinstance(ready_to_learn, int):
                    continue
                if ready_to_learn == None:
                    continue
                    
                if ready_to_learn in dict_ready_to_learn:
                    dict_ready_to_learn[ready_to_learn] += 1
                else:
                    dict_ready_to_learn[ready_to_learn] = 0
        for key in dict_ready_to_learn.keys():
            dict_ready_to_learn[key] = ((dict_ready_to_learn[key] / float(count)) * 100)
        
         
        logging.info("CV Logs : success to get_ready_to_learn_of_class")
        return dict_ready_to_learn
    except Exception:
        logging.error("CV Logs : failed to get_ready_to_learn_of_class")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL

'''
def get_ready_to_learn_of_class(teacher_key, class_key, subject_key):
    logging.info("CV Logs : Inside get_ready_to_learn_of_class ")

    dict_ready_to_learn = {}
    try:
        count=0
        if not (teacher_key.kind()==Teacher._get_kind() or subject_key.kind()==Subject._get_kind()):
            return Constant.ERROR_BAD_VALUE
        students = get_students_by_class(class_key)
        topics = get_topics_by_subject(subject_key)
        for topic in topics :
            for student in students:
                count += 1
                ready_to_learn = get_ready_to_learn_topic(topic.key, student.key)
                if isinstance(ready_to_learn, int):
                    continue
                if ready_to_learn == None:
                    continue

                if ready_to_learn in dict_ready_to_learn:
                    dict_ready_to_learn[ready_to_learn] += 1
                else:
                    dict_ready_to_learn[ready_to_learn] = 0
        for key in dict_ready_to_learn.keys():
            dict_ready_to_learn[key] = ((dict_ready_to_learn[key] / float(count)) * 100)


        logging.info("CV Logs : success to get_ready_to_learn_of_class")
        return dict_ready_to_learn
    except Exception:
        logging.error("CV Logs : failed to get_ready_to_learn_of_class")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL

'''

def get_ready_to_learn_of_assessment(assessment_key, student_key):
    logging.info("CV Logs : get_ready_to_learn_of_assessment")
    ready_to_learn_topics = {}
    questions = []
    completed = 0
    total = 0
    question_key = None
    try:

        if not (student_key.kind()==Student._get_kind() or assessment_key.kind()==Assessment._get_kind()):
            return Constant.ERROR_BAD_VALUE
        student=student_key.get()
        topics_keys = assessment_key.get().topics_in_assessment_key;
        for topic in topics_keys:
            question = get_ready_to_learn_topic(topic, student.key)
            if not isinstance(question, int):
                ready_to_learn_topics[topic.get().name] = question
        logging.info("CV Logs : success to get_ready_to_learn_of_assessment"+str(ready_to_learn_topics))
        return ready_to_learn_topics
    except Exception:
        logging.error("CV Logs :failed  to get_ready_to_learn_of_assessment")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL





'''TODO
def get_average_score_all_subject(subject_key, teacher_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    dict_averagescore = {}
    
    try:
        teacher_entity = teacher_key.get()
        classess = teacher_entity.classes_under_teacher
        
        for class_dummy in classess:
            if class_dummy.get().name == "Class_V":
                class_entity = class_dummy
                
        subjects = get_subjects_of_teacher_in_class(teacher_key, class_entity)
       
        for subject in subjects:
            average_score = get_average_score_by_subject(subject.key, teacher_key)
            dict_averagescore.update({subject.name:average_score})
        # logging.info("CV Logs : success to get average mastery for subject for class :"+class_entity.name+":"+class_entity.section_details)
        return dict_averagescore
    except Exception:
        # logging.info("CV Logs : failed to get average mastery for subject for class :"+class_entity.name+":"+class_entity.section_details)
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL
'''
"""
get mastery by subjects  
"""
def get_mastery_by_subject(subject_key, student_key):
    logging.info("CV Logs : Inside get_mastery_by_subject ")
    assessments = []
    completed = 0
    total = 0
    try:

        if not (student_key.kind()==Student._get_kind() or subject_key.kind()==Subject._get_kind()):
            return Constant.ERROR_BAD_VALUE
        topics_sub = get_topics_by_subject(subject_key)
        if topics_sub == None or not isinstance(topics_sub, list):
            return 0
        total = len(topics_sub)
        topic_mastery = 0
        
        for topic in topics_sub:
            a = get_mastery_by_topic(topic.key, student_key)
            if  a < 0 :
                continue
            topic_mastery += a
        mastry = topic_mastery / (float(total) * 100)
        logging.info("CV Logs : success to get_mastery_by_subject  :")
        final_mastery = (mastry * Constant.MAX_MARKS)
        return final_mastery
    except Exception:
        logging.error("CV Logs : failed to get get_mastery_by_subject :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL


def get_mastery_by_subject_sc(subject_key, student_key):
    logging.info("CV Logs : Inside get_mastery_by_subject_sc ")
    mastery = 0
    try:
        student=student_key.get()
        if not (student_key.kind()==Student._get_kind() or subject_key.kind()==Subject._get_kind()):
            return Constant.ERROR_BAD_VALUE
        
    
        assessments_records = get_completed_assessment_records_by_subject(student_key,subject_key)
        logging.info("CV Logs : get_completed_assessment_records_by_subject"+str(assessments_records ))
        if len(assessments_records) == 0:
                mastery=0
        else :
                
                assesmentss=Assessment_Record.query(ancestor=student.school).fetch()
                logging.info("CV Logs : #######"+str(assesmentss))
                
                q_sorted_assessments_records = Assessment_Record.query(Assessment_Record.key.IN(assessments_records), ancestor=student.school)
                sorted_assessments_records = q_sorted_assessments_records.order(-Assessment_Record.completion_date).fetch()  
               
                #logging.error("CV Logs : failed to get get_mastery_by_subject_sc :"+str(len(q_sorted_assessments_records)))
                mastery=sorted_assessments_records[0].total_score
                
        return mastery
    except Exception:
        logging.error("CV Logs : failed to get get_mastery_by_subject_sc :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL
'''
def get_mastery_of_subjects_sc( student_key):
    logging.info("CV Logs : Inside get_mastery_by_subject_sc ")
    dict_mastery = {}
    try:
        student=student_key.get()
        if not (student_key.kind()==Student._get_kind() or subject_key.kind()==Subject._get_kind()):
            return Constant.ERROR_BAD_VALUE
        subjects=get_subjects_by_student(student_key)
        for subject in subjects 
        
        
                
        return mastery
    except Exception:
        logging.error("CV Logs : failed to get get_mastery_by_subject_sc :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL
'''






"""
//TODO Sorting highest lowest
get mastery by subjects  
"""
def get_mastery_details_of_subject(teacher_key, class_key, subject_key):
    logging.info("CV Logs : Inside get_mastery_details_of_subject ")
    highest_mastery = {}
    lowest_mastery = {}
    mastery_subject = {}
    completed = 0
    total = 0
    try:

        if not teacher_key.kind()==Teacher._get_kind():
            return Constant.ERROR_BAD_VALUE
        students = get_students_by_class(class_key)
        for student in students:
            mastery = get_mastery_by_subject(subject_key, student.key)

            highest_mastery.update({student.basic_info.firstname + " " + student.basic_info.lastname:mastery})
            lowest_mastery.update({student.basic_info.firstname + " " + student.basic_info.lastname:mastery})
        mastery_subject.update({'Highest':highest_mastery})
        mastery_subject.update({'Lowest':lowest_mastery})
        
        logging.info("CV Logs : success to get_mastery_details_of_subject :")
        return mastery_subject
    except Exception:
        logging.error("CV Logs : failed to get_mastery_details_of_subject :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL




"""
get mastery for all subjects  
"""
def get_mastery_for_all_subjects(student_key):
    logging.info("CV Logs : Inside get_mastery_for_all_subjects ")
    assessments = []
    mastry_info = {}
    completed = 0
    total = 0
    try:
        subjects = get_subjects_by_student(student_key)
        student = student_key.get()
        for subject in subjects:
            mastry = get_mastery_by_subject(subject.key, student.key)
            logging.info("CV Logs : success to get_mastery_for_all_subjects  :" + str(mastry))
            mastry_info.update({subject.name:mastry})
        return mastry_info
    except Exception:
        logging.error("CV Logs : failed to get_mastery_for_all_subjects :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL




"""
get growth by subjects  
"""
def get_growth_for_subject(student_key, subject_key):
    logging.info("CV Logs : Inside get_growth_for_subject ")
    
    assessments = []
    dict_growth = {}
    completed = 0
    total = 0
    count = 0
    try:
        topics_sub = get_topics_by_subject(subject_key) 
        student=student_key.get()
        if not (student_key.kind()==Student._get_kind() or subject_key.kind()==Subject._get_kind()):
            return Constant.ERROR_BAD_VALUE
        if topics_sub == Constant.ERROR_NO_DATA_FOUND:
            total = 0
            return dict_growth
        total = len(topics_sub)
        growth = 0
        i = 0
        for topic in topics_sub:
                assessments_records = get_completed_assessment_record_keys_by_topic(student_key, topic.key)
                # No assessment completed growth=0
                if len(assessments_records) == 0:
                    growth = 0
                    dict_growth.update({i:int(growth)})
                    continue
                q_sorted_assessments_records = Assessment_Record.query(Assessment_Record.key.IN(assessments_records), ancestor=student.school)
                sorted_assessments_records = q_sorted_assessments_records.order(-Assessment_Record.completion_date).fetch()        
                # only one topic is present and only one assessment completed growth is the score of assessment
                if len(sorted_assessments_records) == 1 and not total == 1:
                    i += 1
                    growth = sorted_assessments_records[0].score
                    dict_growth.update({i:(growth)})
                    continue
                length = len(sorted_assessments_records)
                score_last = sorted_assessments_records[length - 1].score
                score_secondlast = sorted_assessments_records[length - 2].score
                # only one topic need to show growth only of that topic show last two assessmnt marks 
                if total == 1:
                    i += 1
                    dict_growth.update({i:(score_secondlast)})
                    i += 1
                    dict_growth.update({i:(score_last)})
                    continue
                # Acutal growth from last assessment for a topic
                diff_growth = score_last - score_secondlast
                i += 1
                dict_growth.update({i:(diff_growth)})  
                
                logging.info("CV Logs : success to get_growth_for_subject  :")
        return dict_growth
    except Exception:
        logging.error("CV Logs : failed to get_growth_for_subject:")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL


"""
get growth for all subjects
"""
def get_growth_for_all_subject(student_key):
    logging.info("CV Logs : Inside get_growth_for_all_subject ")

    assessments = []
    dict_growth = {}
    dict_subject_growth = {}
    subjects = []
    completed = 0

    total = 0

    try:


        if not student_key.kind()==Student._get_kind():
            return Constant.ERROR_BAD_VALUE
        subjects = get_subjects_by_student(student_key)
        for subject in subjects:
            growth = get_growth_for_subject(student_key, subject.key)
            dict_subject_growth.update({subject.name:growth})
        
        logging.info("CV Logs : success toget_growth_for_all_subject")
        return dict_subject_growth
    except Exception:
        logging.error("CV Logs : failed to get_growth_for_all_subject :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL





"""
get growth for all topic by subject
returns a dictionry   

def get_growth_for_all_topic_subject(student_key, subject_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    logging.info("CV Logs : Inside get_students_by_class ")
    assessments = []
    dict_growth = {}
    completed = 0
    total = 0
    try:
        topics_sub = get_topics_by_subject(subject_key)
        subject = subject_key.get()
        student = student_key.get()
        for topic in topics_sub:
            assessments = get_assessments_by_topic(student_key, topic.key)
            logging.error("&&&&&&&&&&&&&&&&&&&" + str(assessments))
            if assessments == None:
                return Constant.ERROR_NO_DATA_FOUND
            for assessment_final in assessments:
                score = get_student_score_in_assessment(student_key, assessment_final.key)
                if  score == 100:
                    completed += 1
            
            total = len(assessments)
            if total == 0:
                growth = 0
            else:    
                logging.error("set ############")
                growth = (completed / float(total)) * 100
                
                dict_growth.update({topic.name:growth})    
        logging.info("CV Logs : success to get mastry for  student  :")
        return dict_growth
    except Exception:
        logging.info("CV Logs : failed to get mastry for  student :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL




"""
"""
returns mastery in that subject in percentage

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
        date_latest=assessments[0].date
        for assessment_final in assessments:
            if assessment_final.
            
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

'''

returns mastery in the topic in percentage
"""
def get_mastery_by_topic(topic_key, student_key):
    logging.info("CV Logs : Inside get_mastery_by_topic ")
    assessments = []
    completed = 0
    total = 0
    try:
        subject = topic_key.get().subject_key.get()

        if not student_key.kind()==Student._get_kind():
            return  Constant.ERROR_BAD_VALUE
        
        assessment_records = get_assessment_records_by_topic(student_key, topic_key)
        
        if assessment_records == None or len(assessment_records) == 0:
            return 0
        date_latest = assessment_records[0].completion_date
        
        assessment_latest = None
        for assessment_final in assessment_records:
            logging.error(str(assessment_final))
            if assessment_final.completion_date == None :
                continue
            if date_latest == None:
                date_latest = assessment_final.completion_date
            if assessment_final.completion_date >= date_latest:
                assessment_latest = assessment_final
        
        if assessment_latest == None:
            return 0
        assessment_score = assessment_latest.score
        if assessment_score == -1:
            assessment_score = 0
        
        
        logging.info("CV Logs : success to get_mastery_by_topic  :")
        return assessment_score
    except Exception:
        logging.error("CV Logs : failed to get_mastery_by_topic :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL





def get_global_subjects(school_key):
    logging.info("CV Logs : Inside get_global_subjects ")
    #subjects=Subject.query(Subject.type==Subject_Name.TYPE_GLOBAL,ancestor=school_key).fetch()
    dict_subjects={}
    try:
            subjects=Subject.query(Subject.type==Subject_Name.TYPE_GLOBAL,ancestor=school_key).fetch()
            logging.info("CV Logs : success to get_global_subjects :")
            for subject in subjects:
                
                dict_subjects[subject.name]=subject.key.urlsafe()
            return dict_subjects
    except Exception:
        logging.error("CV Logs : failed to get_global_subjects:")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL





"""
returns ready to learn topics of a student of a class 
"""
def get_ready_to_learn_topic(topic_key, student_key):
    logging.info("CV Logs : Inside get_ready_to_learn_topic ")
    assessments = []
    assessments_temp = []
    questions = []
    completed = 0
    total = 0
    question_key = None
    try:
        subject = topic_key.get().subject_key.get()

        if not student_key.kind()==Student._get_kind():
            return Constant.ERROR_BAD_VALUE
        assessments = get_completed_assessment_records_by_topic(student_key, topic_key)
        if assessments == None:
            return Constant.ERROR_NO_DATA_FOUND
        for assessment_final in assessments:
            score = assessment_final.score
            if not score == 100:
                assessments_temp.append(assessment_final)
                
        if len(assessments_temp) == 0:
            return Constant.UPDATION_SUCCESSFULL       
        for assessment_temp2 in assessments_temp:
            if not assessment_temp2.completion_date == None:
                
                question_temp = assessment_temp2.question_ready_to_learn.get()
                
                for question_entity in questions:
                    if question_temp.instance.problem_statement == question_entity.instance.problem_statement:
                 
                        question_key = question_temp
       
        logging.info("CV Logs : success to get_ready_to_learn_topic  :")
        return question_temp.instance.problem_statement
    except Exception:
        logging.error("CV Logs : failed to get_ready_to_learn_topic:")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL


"""
returns {date:[passed,failed]}


def get_learning_progress_date_wise(topic_key, student_key):
    logging.info("CV Logs : Inside get_learning_progress_date_wise ")
    assessments = []
    assessments_temp = []
    learning_by_date = {}
    mastered = 0
    prev_pass = 0
    prev_failed = 0
    question_key = None
    try:
        subject = topic_key.get().subject_key.get()
        student = student_key.get()
        assessments = get_completed_assessment_records_by_topic(student_key, topic_key)
        logging.error("##########################################################" + str(assessments))
        questions = get_questions_of_topic(topic_key)
        logging.error("##########################################################" + str(questions))
        if assessments == None:
            return Constant.ERROR_NO_DATA_FOUND
        for assessment_final in assessments:
            if not assessment_final.completion_date == None:
                date_asessment = assessment_final.completion_date
                if date_asessment in learning_by_date:
                     prev_pass, prev_failed = learning_by_date[date_asessment]
                if assessment_final.score == 100:
                    prev_pass += 1
                else :
                    prev_failed += 1
                learning_by_date[date_asessment] = [prev_pass, prev_failed]
            else :
                if assessment_final.score == 100:
                    prev_pass += 1
                else :
                    prev_failed += 1
                learning_by_date.update({date_asessment:[prev_pass, prev_failed]}) 
                        
        logging.info("CV Logs : success to get_learning_progress_date_wise  :")
        return learning_by_date
    except Exception:
        logging.info("CV Logs : failed to get_learning_progress_date_wise :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL

"""    

"""
TODO : Change as per dependent topics

"""
def get_ready_to_learn_of_all_topic(subject_key, student_key):
    logging.info("CV Logs : get_ready_to_learn_of_all_topic")
    ready_to_learn_topics = {}
    questions = []
    completed = 0
    total = 0
    question_key = None
    try:

        if not (student_key.kind()==Student._get_kind() or subject_key.kind()==Subject._get_kind()):
            return Constant.ERROR_BAD_VALUE
        student=student_key.get()
        topics = get_topics_by_subject(subject_key)
        for topic in topics:
            question = get_ready_to_learn_topic(topic.key, student.key)
            if not isinstance(question, int):
                ready_to_learn_topics[topic.name] = question
        logging.info("CV Logs : success to get_ready_to_learn_of_all_topic:")
        return ready_to_learn_topics
    except Exception:
        logging.error("CV Logs : failed to get_ready_to_learn_of_all_topic:")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL

def get_ready_to_learn_of_all_topic_dummy(student_key):
    logging.info("CV Logs : Inside get_students_by_class ")
    ready_to_learn_topics = {}
    questions = []
    completed = 0
    total = 0
    question_key = None
    try:
        subjects = get_subjects_by_student(student_key)
        for subject_dummy in subjects:
            if subject_dummy.name == "Mathematics":
                subject = subject_dummy
                break

        student = student_key.get()
        topics = get_topics_by_subject(subject.key)
        for topic in topics:
            question = get_ready_to_learn_topic(topic.key, student.key)
            if not question == -4:
                ready_to_learn_topics[topic.name] = question

        return ready_to_learn_topics
    except Exception:
        logging.error("CV Logs : failed to get mastry for  student :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL



"""
get get_pending_assessment_subject  // List of names
"""
def get_pending_assessment_subject_dummy(student_key):
    logging.info("CV Logs : get_topper_mastery_in_subject ")
    assessments = []
    assessment_topic = []
    pending_assessments = []
    try:
        subjects = get_subjects_by_student(student_key)
        for subject_dummy in subjects:
            if subject_dummy.name == "Mathematics":
                subject = subject_dummy
                break
        topics_sub = get_topics_by_subject(subject.key)
        if topics_sub == None:
            return Constant.ERROR_NO_DATA_FOUND
        total = len(topics_sub)
        for topic in topics_sub:
            assessment = get_assessments_by_topic(student_key, topic.key)

            if len(assessment) > 0:
                    assessments.extend(assessment)

            for assesment_final in assessments:
                score = get_student_score_in_assessment(student_key, assesment_final.key)
                if not score == 100:
                    pending_assessments.append(assesment_final)

            return pending_assessments
    except Exception:
        logging.info("CV Logs : failed to get mastry for  student :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL



"""
returns mastery in that subject in percentage
"""
def get_learning_progress_date_wise_dummy(student_key, subject_key):
    logging.info("CV Logs : Inside get_learning_progress_date_wise ")
    assessments = []
    assessments_temp = []
    learning_by_date = {}
    mastered = 0
    prev_pass = 0
    prev_failed = 0
    question_key = None
    try:

        if not subject_key.kind()==Subject._get_kind():
            return Constant.ERROR_BAD_VALUE
        topics = get_topics_by_subject(subject_key)
        for topic in topics:
            assessments = get_assessments_by_topic(student_key, topic.key)
            questions = get_questions_of_topic(topic.key)
            if assessments == None:
                return Constant.ERROR_NO_DATA_FOUND
            for assessment_final in assessments:
                date_asessment = get_student_completion_date_in_assessment(student_key, assessment_final.key)
                
                if not date_asessment == None:
                    score = get_student_score_in_assessment(student_key, assessment_final.key)
                    if date_asessment in learning_by_date:
                        prev_pass, prev_failed = learning_by_date[date_asessment]
                        if score == 100:
                            prev_pass += 1
                        else :
                            prev_failed += 1
                        learning_by_date[str(date_asessment)] = [prev_pass, prev_pass + prev_failed]
                    else :
                        if score == 100:
                            prev_pass += 1
                        else :
                            prev_failed += 1
                        learning_by_date.update({str(date_asessment):[prev_pass, prev_pass + prev_failed]})

        logging.info("CV Logs : success to get_learning_progress_date_wise  :")
        return learning_by_date

    except Exception:
        logging.info("CV Logs : failed to get_learning_progress_date_wise :")
        logging.exception("")
        return Constant.ERROR_OPERATION_FAIL






def get_learning_progress(student_key, subject_key):
    logging.info("CV Logs : Inside get_learning_progress_date_wise ")
    try:
        student = student_key.get()
        dict_progress={}
        assesments_of_student_key = student.student_assessment_key
        if assesments_of_student_key == None:
            return Constant.ERROR_NO_DATA_FOUND
        student_assessments = assesments_of_student_key.get() 
        attended_assessment=student_assessments.attended_assessment_key
        assessment_records=student_assessments.assessment_record
        i=0;
        for assessment in attended_assessment:
            assesment_record=assessment_records[i]
            dict_progress[assessment.get().name]=assesment_record.get().total_score
        logging.info("CV Logs : success to get_learning_progress_date_wise  :")
        return dict_progress

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


def get_assessment_report():

    dict_final_report = {}
    try:

        students_list=ndb.gql("select * from Student where username>='Demo_1'").fetch()
        records=[]
        records_final=[]
        score=[]
        #logging.info("CV Logs :students_list :"+str(students_list[0].key))
        for student in students_list:
            #student_id=ndb.Key(urlsafe=student.key)
            records=Student_Assessments.query().fetch()
            #logging.info("CV Logs  records :"+str(records))
            for record in records:
                #logging.info("CV Logs  STUDENT KEY :"+str(record.student_key))
                #logging.info("CV Logs  STUDENT KEY2 :"+str(student.key))
                if record.student_key==student.key:
                    records_final.append(record)
                    #logging.info("CV Logs :records_final :"+str(records_final))
            dict_final_report[student.username]=[]
        #logging.info("CV Logs :finaL records :"+str(records_final))
        for record in records_final:
            student_name=record.student_key.get().username
            #logging.info("CV Logs :student_name :"+str(student_name))
            student_assessment_record=record.assessment_record;
            #logging.info("CV Logs :student_assessment_record :"+str(student_assessment_record))
            #student_name=student_assessment_record.
            if not student_assessment_record ==None :
                actual_record=student_assessment_record[0].get()
                #logging.info("CV Logs :actual_record :"+str(actual_record))
                topic_scores=actual_record.topic_scores
                #logging.info("CV Logs :topic_scores :"+str(topic_scores))
                if len(topic_scores)==2:
                    score=[]
                    score.append(topic_scores[0])
                    score.append(topic_scores[1])
                    question_keys=actual_record.question_ready_to_learn
                    if not topic_scores[0] ==100 and not topic_scores[1]==100:


                        i=0;
                        for question_key in question_keys:

                            question=question_key.get()
                            question_name=question.instance.problem_statement
                            question_type=question.topic_type
                            question_topic=question.topic_key.get().name
                            if not i==0:
                                score_final= score[1]
                            else :
                                score_final= score[0]
                            dict_final_report[student_name].append([question_topic,question_type,question_name,score_final])
                            #logging.info("CV Logs :dict_final_report :"+str(dict_final_report))
                            i=i+1
                    else :

                        if not score[0]==100:
                             index =0
                        else :
                            index = 1
                        for question_key in question_keys:
                            question=question_key.get()
                            question_name=question.instance.problem_statement
                            question_type=question.topic_type
                            question_topic=question.topic_key.get().name


                            dict_final_report[student_name].append([question_topic,question_type,question_name,score[index]])
                            #logging.info("CV Logs : dict_final_report :"+str(dict_final_report))
                        topic_list=["Multiplication","Division"]
                        if topic_list.index(question_topic)==0:
                           index=1
                        else :
                            index=0;
                        dict_final_report[student_name].append([topic_list[index],"NA","NA",100])

        return dict_final_report
    except Exception:
            logging.info("CV Logs : failed to get assessments report for student :")
            logging.exception("")
            return Constant.ERROR_OPERATION_FAIL

def get_school_by_name(name):
    dict_school = {}
    try:
        schools=School.query((School.name == name)).fetch()
        if(not schools[0] == None):
            logging.info("CV Logs: success to get school key  by name : " )
            return schools[0].key.urlsafe();
    except Exception :
        logging.exception("")
        logging.error("CV Logs: failed to get school key  by name  : " )
        return Constant.ERROR_BAD_VALUE


def add_topic_from_excel(school_key,name, prerequisite_topics,subject_key,types,state_nos):

    state_list = []
    try:
        count = 0;
        while (count < st):
            state_list.append(addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school_key))
            count = count + 1
        topic=addTopic(school_key=school_key,name=name, prerequisite_topics=prerequisite_topics,subject_key=subject_key,types=types)
        assign_states_to_topic(topic.key,[state_chapone_one.key,state_chapone_two.key,state_chapone_six.key,state_chapone_eight.key],school.key)
        return topic.key.urlsafe()
    except Exception :
        logging.exception("")
        logging.error("CV Logs: failed to get school key  by name  : " )
        return Constant.ERROR_BAD_VALUE


def  addQuestion_from_excel(problem_statement, type, choices, answers,school_key,topic_type):
    try:
        questioninstance_base_one=Query.addQuestionInstance(problem_statement=problem_statement, type=type,choices=choices , answers=answers,school_key=school_key,url="")
        question_base_one=addQuestion(questioninstance_base_one,school.key)
        assign_questions_to_topic(topic_chap_one.key,[question_base_one.key],school_key,topic_type=topic_type)
        return question_base_one.key.urlsafe()
    except Exception :
        logging.exception("")
        logging.error("CV Logs: failed to get school key  by name  : " )
        return Constant.ERROR_BAD_VALUE

