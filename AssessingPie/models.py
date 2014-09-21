from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import ndb
from Constant import Constant
from Constant import Subject




"""
This class contains the basic info of a user : id 
""" 
class User(ndb.Model):   
    username=ndb.StringProperty(required=True)
    type=ndb.IntegerProperty(choices=set([Constant.TEACHER,Constant.STUDENT,Constant.SCHOOL,Constant.TEACHER]))
    key=ndb.KeyProperty(required=True)
    pwd=ndb.StringProperty(required=True)
    lastlogin=ndb.DateProperty()
    
       
    

"""
This class contains the basic info of a question instance
""" 
class QuestionInstance(ndb.Model):   
    problem_statement = ndb.StringProperty(required=True)
    type = ndb.IntegerProperty(choices=set([Constant.QUESTION_TYPE_SINGLE, Constant.QUESTION_TYPE_MULTIPLE]))# QUESTION_TYPE_SINGLE=0,QUESTION_TYPE_MULTIPLE=1 
    choices = ndb.StringProperty(repeated=True)
    answer = ndb.StringProperty(repeated=True)

  
"""
This class models the  info of a question entity 
Structured Property: Uses QuestionInstance class as a property for basic question instance info
"""    
class Question(ndb.Model):
    
    no_states_contained_in = ndb.IntegerProperty(default=0)
    instance = ndb.StructuredProperty(QuestionInstance, required=True)
    
"""
This class models a state entity 
state can be of two types :
    1: A general State: 
                    type:STATE_IN_TOPIC
    2: A  State made of Topics: 
                    type:STATE_OF_TOPIC
                    Dynamic properties associated:
                                 topic_in_states: the list of topic keys covered in a particular state
                                                =ndb.KeyProperty(kind='State_Topics')
                                 student_level_count: the count of students falling in a level 
                                                 =ndb.IntegerProperty(repeated=True)# NO_STUDENT_LEVEL_UPTO_25=0,NO_STUDENT_LEVEL_UPTO_50=1,
                                                 NO_STUDENT_LEVEL_UPTO_75=2,NO_STUDENT_LEVEL_UPTO_100=3
                                                
                    
key Property: Uses question_in_state_key: contains key of relationship entity State_Questions which contains
                                        question keys associated to a state
"""     
    

class State(ndb.Expando):  # Dynamic property will be applied in case of type STATE_OF_TOPIC [List of topic_ids]
    type = ndb.IntegerProperty(choices=set([Constant.STATE_IN_TOPIC, Constant.STATE_OF_TOPIC]))  # STATE_IN_TOPIC=0,STATE_OF_TOPIC=1
    question_in_state_key = ndb.KeyProperty(kind='State_Questions')
    
    

"""
This class models  a Subject entity 

                        type : Subject.TYPE_GLOBAL
                                                : this subject is meant for global assessment 
                                                 
                              Subject.TYPE_CLASS
                                                : this subject is meant for local class wise school assessment
                                                has dynamic property 
                                                 class_deatils= ndb.StringProperty()# class name from Class in Constant.py
                                                 section_details= ndb.StringProperty()# section name from Section in Constant.py
                                                 
                                                 
                        topics_in_subject_key : key of relationship table Subject_Topics entity for topics contained in the subject
                            
"""    
        
class Subject(ndb.Expando):
    name = ndb.StringProperty(required=True)# from SUBJECT Constants in Constant.py
    type=ndb.IntegerProperty(required=True,choices=[Subject.TYPE_CLASS,Subject.TYPE_GLOBAL])
    topics_in_subject_key=ndb.KeyProperty(kind='Subject_Topics')
    class_key=ndb.KeyProperty(kind='Class')
    





"""
This class models  a one to many Subject to Topics relationship 
key Property: topics_in_subject_key: contains key of r entity Topic  which are contained
                                        in a Subject
               
"""    
        
class Subject_Topics(ndb.Model):
    
    subject_key = ndb.KeyProperty(kind='Subject', required=True)
    topics_in_subject_key = ndb.KeyProperty(kind='Topic',repeated=True)
    




"""
This class models  a Topic entity 
key Property: states_in_topic_key: contains key of relationship entity Topic_States which contains
                                        state keys associated to a topic
              questions_in_topic_key: contains key of relationship entity Topic_Questions which contains
                                        question keys associated to a topic  
                   
"""    
        
class Topic(ndb.Model):
    name = ndb.StringProperty(required=True) # From Topic Class in Constant.py
    subject_key=ndb.KeyProperty(kind='Subject')
    prerequisite_topic = ndb.KeyProperty(kind='Topic', repeated=True)  # Need to verify
    student_level_count = ndb.IntegerProperty(repeated=True)  # NO_STUDENT_LEVEL_UPTO_25=0,NO_STUDENT_LEVEL_UPTO_50=1,NO_STUDENT_LEVEL_UPTO_75=2,NO_STUDENT_LEVEL_UPTO_100=3
    states_in_topic_key = ndb.KeyProperty(kind='Topic_States')
    questions_in_topic_key = ndb.KeyProperty(kind='Topic_Questions')
    assessments_in_topic=ndb.KeyProperty(kind='Assessment')
    
    
    
"""
This class models  a one to many Topic to States relationship
key Property: topic_key: contains key of  a topic
              states_in_topic_keys: contains keys States which are contained 
                                        in a topic       
""" 
    
class Topic_States(ndb.Model):   
    topic_key = ndb.KeyProperty(kind=Topic, required=True)
    states_in_topic_keys = ndb.KeyProperty(kind=State, repeated=True)

"""
*******
This class models  a one to many  State to Topic relationship
key Property: state_key: contains key of  a state
              topics_in_state_keys: contains keys of Topics which are contained 
                                        in a state       
"""


class State_Topics(ndb.Model):   
    state_key = ndb.KeyProperty(kind=State, required=True)
    topics_in_state_keys = ndb.KeyProperty(kind=Topic, repeated=True)


"""
This class models  a one to many  State to Questions relationship
key Property: state_key: contains key of  a state
              questions_in_state_keys: contains keys of Questions which are contained 
                                        in a state       
"""    
    
    

class State_Questions(ndb.Model):   
    state_key = ndb.KeyProperty(kind=State, required=True)
    questions_in_state_keys = ndb.KeyProperty(kind=Question, repeated=True)
 

"""
This class models  a one to many  Question to States relationship
key Property: question_key: contains key of  a question
              states_in_question_keys: contains keys of States in which question is contained 
                                              
     
class Question_States(ndb.Model):   
    question_key = ndb.KeyProperty(kind=Question, required=True)
    states_in_question_keys = ndb.KeyProperty(kind=State, repeated=True)
"""

"""
This class models  a one to many  Topic to Questions relationship
key Property: topic_key: contains key of  a topic
              questions_in_topic_keys: contains keys of States associated to a topic
                                              
"""

class Topic_Questions(ndb.Model):   
    topic_key = ndb.KeyProperty(kind=Topic, required=True)
    questions_in_topic_keys = ndb.KeyProperty(kind=Question, repeated=True)


"""
********
This class models  a one to many  Question to Topics relationship
key Property: question_key: contains key of  a Question
              topics_in_question_keys: contains keys of Topics in which a question is contained
                                              
"""    


class Question_Topics(ndb.Model):   
    question_key = ndb.KeyProperty(kind=Question, required=True)
    topics_in_question_keys = ndb.KeyProperty(kind=Topic, repeated=True)

"""
This class models  a Assessment entity
key Property: topics_in_assessment_key: contains keys of  a topics in an assessment
              states_in_assessment_key: contains keys of States in which an assessment is contained
                                              
"""

class Assessment(ndb.Model):
    name=ndb.StringProperty(required=True)
    date=ndb.DateProperty(required=True)
    due_date=ndb.DateProperty(required=True)
    published=ndb.BooleanProperty(required=True,default=True)
    teacher_key=ndb.KeyProperty(kind='Teacher',required=True)
    topics_in_assessment_key = ndb.KeyProperty(kind='Topic', repeated=True)
    states_in_assessment_key = ndb.KeyProperty(kind='State', repeated=True)
    class_key=ndb.KeyProperty(kind='Class',required=True)
    no_of_user_completed=ndb.IntegerProperty(default=0)
    
    
    
class Assessment_Record(ndb.Model):  
    start_date=ndb.DateProperty()
    completion_date=ndb.DateProperty()
    assessment_key=ndb.KeyProperty(kind=Assessment,required=True)
    current_state=ndb.KeyProperty(kind=State)
    next_state=ndb.KeyProperty(kind=State)
    score=ndb.IntegerProperty(default=-1)
    question_ready_to_learn=ndb.KeyProperty(kind=Question)
   
 
"""
This class models  a one to many  Assessment to States relationship
key Property: assessment_key: contains key of  a Assessment
              states_in_assessment_keys: contains keys of states in  an assessment
                                              
    
class Assessment_States(ndb.Model):   
    assessment_key = ndb.KeyProperty(kind=Assessment, required=True)
    states_in_assessment_keys = ndb.KeyProperty(kind=State, repeated=True)   
    
"""
"""
This class models  an Address entity
                                              
"""
    
class Address(ndb.Model):
  type = ndb.IntegerProperty(choices=set([Constant.ADDRESS_TYPE_HOME,Constant.ADDRESS_TYPE_WORK,Constant.ADDRESS_TYPE_OTHER]))  # E.g., 'home', 'work'
  street = ndb.StringProperty()
  city = ndb.StringProperty()
  state=ndb.StringProperty()
     
"""
This class models  a school entity
key Property: 
              assessments_in_school_key: contains key of school to assessment one to many relationship entity of kind School_Assessments
                                                                                            
"""

class School(ndb.Model):
  name = ndb.StringProperty(required=True) 
   
  code=ndb.StringProperty(required=True) 
  address = ndb.StructuredProperty(Address, required=True)
  #assessments_in_school_key = ndb.KeyProperty(kind='School_Assessments')
  classes_in_school_keys= ndb.KeyProperty(kind='Class', repeated=True)
  teachers_in_school_keys= ndb.KeyProperty(kind='Teacher', repeated=True)
  
  
"""
This class models  a school entity
key Property: 
              assessments_in_school_key: contains key of school to assessment one to many relationship entity of kind School_Assessments
                                                                                            
"""

class Class(ndb.Model):
  name = ndb.StringProperty(required=True)#from Constant.py  
  school_key=ndb.KeyProperty(kind='School')
  subjects_in_class_key=ndb.KeyProperty(kind='Subject',repeated=True)
  section_details= ndb.StringProperty()
  year_session=ndb.StringProperty()
  students_in_class_key=ndb.KeyProperty(kind='Student',repeated=True)
      
"""
This class models  a basic user information subentity
                                                                                            
"""  

  
class UserInfo(ndb.Model):
  firstname = ndb.StringProperty(required=True)
  lastname=ndb.StringProperty(required=True)
  date_of_birth = ndb.DateProperty(required=True)
  # age=ndb.IntegerProperty(required=True) 
  sex = ndb.IntegerProperty(required=True, choices=set([Constant.SEX_MALE, Constant.SEX_FEMALE])) 
  address = ndb.StructuredProperty(Address, required=True)
  email = ndb.StringProperty()
  contact_no = ndb.IntegerProperty()
  


"""
*******************************Gaurdian details 
This class models  a student entity

"""
class Student(ndb.Model):   
    username=ndb.StringProperty()
    basic_info = ndb.StructuredProperty(UserInfo,required=True)
    school = ndb.KeyProperty(kind=School, required=True)
    parent_detail= ndb.KeyProperty(kind='Parent')
    class_details= ndb.KeyProperty(kind=Class)
    class_history=ndb.KeyProperty(kind=Class,repeated=True)# class name from Class in Constant.py
    student_assessment_key=ndb.KeyProperty(kind='Student_Assessments')
    

"""
*******************************Gaurdian details 
This class models  a student entity

"""
class Parent(ndb.Model):   
    username=ndb.StringProperty()
    basic_info = ndb.StructuredProperty(UserInfo,required=True)
    
    
    


"""
This class models  a class to students one to many  entity 

class Class_Students(ndb.Model):   
    class_key= ndb.KeyProperty(kind=Class,repeated=True)# class name from Class in Constant.py
    students_in_class=ndb.KeyProperty(kind='Student',repeated=True)
 """   
    
    

"""
This class models  a Teacher entity 
"""
class Teacher(ndb.Model):   
    username=ndb.StringProperty()
    basic_info = ndb.StructuredProperty(UserInfo,required=True)
    school = ndb.KeyProperty(kind=School, required=True) 
    classes_under_teacher= ndb.KeyProperty(kind=Class,repeated=True)
    class_history=ndb.KeyProperty(kind=Class,repeated=True)
    subjects=ndb.KeyProperty(kind=Subject,repeated=True)
    
    
        
"""
This class models  a one to many  student to Assessment relationship
key Property: school_key: contains key of  a School
              attended_assessment_key: contains keys of assessments attended by the student
              states_of_or_in_assessments: contains keys of states present in corresponding assessment attended by student
              scores_in_assessments: contains scores of corresponding assessments attended by the student
"""

class Student_Assessments(ndb.Model):   
    student_key = ndb.KeyProperty(kind=Student,required=True)
    attended_assessment_key = ndb.KeyProperty(kind=Assessment, repeated=True)
    #assessment_record= ndb.KeyProperty(kind=Assessment_Record,repeated=True,default=None)
    assessment_record= ndb.KeyProperty(kind=Assessment_Record,repeated=True)
   
   
    