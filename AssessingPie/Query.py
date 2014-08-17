
from google.appengine.ext.ndb import Key
from google.appengine.ext import ndb
import logging
import datetime
from models import QuestionInstance,State_Questions,Topic_States,Question,State,Topic,Address
from models import School,Student,UserInfo,Subject,Assessment,Student_Assessments,School_Assessments
from  models import Assessment_Topics,Assessment_States,Topic_Questions,State_Questions,Topic_States,Subject_Topics
from Constant import Constant






def login(username):
      try: 
        query=Student.query(Student.username == username)
      except Exception :
        logging.exception("")
        return Constant.ERROR_FAILED_QUERY
      if query.count()==0:   
        return Constant.ERROR_INVALID_USER
        '''student_assessment=Student_Assessments(student_key=student.key,attended_assessment_key=[assessment.key])
        student_assessment.put()    
        student.student_assessment_key=student_assessment.key'''     
      else:
         student_list=query.fetch()
         student=student_list[0]
        
      return student




      

"""
Adds a new question instance 
    problem_statement : Problem Statement String
    type : QUESTION_TYPE_SINGLE or QUESTION_TYPE_MULTIPLE
    choices : List of options e.g. ["1","3","10"]
    answers :: List of correct answer e.g. ["1","3","10"]
"""
def addQuestionInstance(problem_statement, type, choices=[], answers=[]):
    # question_instance=new QuestionInstance()
   # Add both the parameters and return them."
   question_instance = QuestionInstance(problem_statement=problem_statement, type=type, choices=choices, answer=answers)
   question_instance.put()
   
   return question_instance;
  

"""
Adds a question to db :
                    question_instance: An entity object of kind QuestionInstance
                    
                    ==> raises : BadValueError
"""    
def addQuestion(question_instance):
   
    # question_instance=new QuestionInstance()
   # Add both the parameters and return them."
   if not isinstance(question_instance,QuestionInstance):
       return Constant.ERROR_BAD_VALUE
   question = Question(instance=question_instance) 
   question.put()  
   return question;

"""
Adds a new State:
                type= type of state STATE_IN_TOPIC or STATE_OF_TOPIC
            
"""
def addState(type):
    # question_instance=new QuestionInstance()
   # Add both the parameters and return them."
   print "called"
   state = State(type=type) 
   state.put()  
   return state;


"""
Adds a new Subject:
               type=Subject.TYPE_CLASS,Subject.TYPE_GLOBAL
               name =from SUBJECT Constants in Constant.py
    
"""
def addSubject(type,name):
   subject = Subject(type=type,name=name) 
   subject.put()  
   return subject;

"""
Adds a new Topic:
                prerequisite_topics should have Type list of  Key of kind Topic

"""
def addTopic(name,prerequisite_topics,subject_key):
   try:
       
       subject=subject_key.get()
       logging.error("DONE ADDING TOPIC 1")
       for topic_key in prerequisite_topics:
            topic=topic_key.get()
            
   except Exception:
         logging.exception("")
         return Constant.ERROR_BAD_VALUE
  
      
   topic = Topic(name=name,prerequisite_topic=prerequisite_topics,subject_key=subject_key) 
   topic.put()  
   logging.error("DONE ADDING TOPIC")
   return topic;                                                                      


"""
Adds a new Address:
                    type : ADDRESS_TYPE_HOME,ADDRESS_TYPE_WORK,ADDRESS_TYPE_OTHER
                    street : String
                    city  :String

"""
def addAddress(type,street,city):

   address = Address(type=type,street=street,city=city) 
   address.put()  
   return address;


"""
Adds a new School:
                address: should be an Address entity
 
"""
def addSchool(name,address):
    if not isinstance(address, Address):
            return Constant.ERROR_BAD_VALUE      
    school = School(name=name,address=address) 
    school.put()  
    return school;

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
         
    user = UserInfo(name=name,date_of_birth=date_of_birth,sex=sex,address=address,email=email,contact_no=contact_no) 
    user.put()  
    return user;


"""
Adds a new Student:
                address: should be an Address entity
 basic_info = ndb.StructuredProperty(UserInfo, required=True)
    school
"""
def addAssessment():     
    assessment = Assessment() 
    assessment.put()  
    return assessment;

"""
Adds a new Student:
                address: should be an Address entity
                basic_info : StructuredProperty as UserInfo
                school : key of school enrolled in
                class_deatils=  class name from Class in Constant.py
                section_details=section name from Section in Constant.py
"""
def addStudent(username,basic_info,school,class_deatils,section_details):
    if not (isinstance(basic_info, UserInfo) or isinstance(school, School)) :
            return Constant.ERROR_BAD_VALUE      
    student = Student(username=username,basic_info=basic_info,school=school.key,section_details=section_details,class_deatils=class_deatils) 
    student.put()  
    return student;

"""
Assigns an exsisting assessment to an existing student:
                            student_key: key to student entity
                            assessment_key: key of assessment entity
"""
def assign_assessment_to_student(student_key,assessment_key):
    student_assessment=None
    try:
        student=student_key.get()  
        
        student_assessment_key=student.student_assessment_key       
        #logging.error(assess)
        assessment=assessment_key.get()
        logging.error(student)
    except Exception :
        logging.exception("")
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
   
    return Constant.UPDATION_SUCCESSFULL
        
        
"""
Assigns an exsisting assessment to an existing student:
                            student_key: key to student entity
                            assessment_key: key of assessment entity
                            states_of_or_in_assessments: key of state corresponding to assessment with key assessment_key
"""
def assign_assessment_state_to_student(student_key,assessment_key,states_of_or_in_assessment):
    student_assessment=None
    try:
        student=student_key.get()
        student_assessment=student.student_assessment_key.get()       
        assessment=assessment_key.get()
        state=states_of_or_in_assessment.get()
        #logging.error(assess)
    except Exception :
        logging.exception("")
    if  len(student_assessment.attended_assessment_key)==0:   
        return Constant.ERROR_INCONSISTENT_STATE
          
    pos=student_assessment.attended_assessment_key.index(assessment_key)
    student_assessment.states_of_or_in_assessments.insert(pos,states_of_or_in_assessment)
    #logging.error( "vffff"+str(student_assessment[0].states_of_or_in_assessments))
    student_assessment.put()
    logging.error("****"+str(student_assessment))     
    return Constant.UPDATION_SUCCESSFULL
        
"""
Assigns an exsisting assessment to an existing student:
                            student_key: key to student entity
                            assessment_key: key of assessment entity
                            states_of_or_in_assessments: key of state corresponding to assessment with key assessment_key
                            scores_in_assessments: Integer , Score of student corresponding to assessment with key assessment_key 
                            questions_ready_to_learn:key of question ready to learn corresponding to the assessment id 
"""
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
Assigns  existing assessments to an existing school:
                            school_key: key to school entity
                            assessments_in_school_keys : lits of keys of assessments t be assigned to the school 
"""
def assign_assessment_to_school(school_key,assessments_in_school_keys):
    school=None
    school_assessment=None
    try:
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
    return Constant.UPDATION_SUCCESSFULL


"""
Assigns  existing assessment to an existing topic:
                            assessment_key: key to assessment entity
                            topics_in_assessment_keys : list of keys of topics covered in assessment
"""
def assign_assessment_to_topic(assessment_key,topics_in_assessment_keys):
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
Assigns  existing assessment to an existing state:
                            assessment_key: key to assessment entity
                            states_in_assessment_keys : list of keys of states covered in assessment
"""
def assign_assessment_to_state(assessment_key,states_in_assessment_keys):
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
Assigns  existing questions  to an existing topic:
                            topic_key: key to topic entity
                            questions_in_topic_keys : list of keys of questions covered in topic
"""
def assign_questions_to_topic(topic_key,questions_in_topic_keys):
    topic=None
    topic_question=None
    try:
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
    return Constant.UPDATION_SUCCESSFULL



"""
Assigns  existing questions  to an existing state:
                            topic_key: key to state entity
                            questions_in_topic_keys : list of keys of questions covered in topic
"""
def assign_questions_to_state(state_key,questions_in_state_keys):
    state=None
    question_state=None
    try:
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
    return Constant.UPDATION_SUCCESSFULL

"""
Assigns  existing topics  to an existing state:
                            topic_key: key to state entity
                            states_in_topic_keys : list of keys of states covered in topic
"""
def assign_states_to_topic(topic_key,states_in_topic_keys):
    topic=None
    state_topic=None
    try:
        topic=topic_key.get() 
        for state_key in states_in_topic_keys:
                   state=state_key.get()
                   if not state.type==Constant.STATE_IN_TOPIC:
                       return Constant.ERROR_BAD_VALUE
        state_topic_key=topic.states_in_topic_key
    except Exception :
        logging.exception("")
  
    if state_topic_key==None:   
        
        state_topic=Topic_States(topic_key=topic_key,states_in_topic_keys=states_in_topic_keys)
        state_topic.put()    
        topic.states_in_topic_key=state_topic.key
        topic.put()
    else:
         
         state_topic=state_topic_key.get()
         state_topic.states_in_topic_keys.extend(states_in_topic_keys)
         state_topic.put()     
    return Constant.UPDATION_SUCCESSFULL

"""
Assigns  existing topics  to an existing subject:
                            topic_key: key to state entity
                            states_in_topic_keys : list of keys of states covered in topic
"""
def assign_topics_to_subject(subject_key,topics_in_subject_key):
    subject=None
    topic_subject=None
    try:
        subject=subject_key.get() 
        for topic_key in topics_in_subject_key:
                   topic=topic_key.get()
        topic_subject_key=subject.topics_in_subject_key
    except Exception :
        logging.exception("")
   
    if topic_subject_key==None:   
        
        topic_subject=Subject_Topics(subject_key=subject_key,topics_in_subject_key=topics_in_subject_key)
        topic_subject.put()    
        subject.topics_in_subject_key=topic_subject.key
        subject.put()
    else:
         
         topic_subject=topic_subject_key.get()
         topic_subject.topics_in_subject_key.extend(topics_in_subject_key)
         topic_subject.put()     
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

