import sys
import datetime 
class Constant:
    STUDENT=100
    SCHOOL=200
    TEACHER=300
    STATE=3
    QUESTION=4
    USER_TYPE="type"
    USER_ENTITY="entity"
    LAST_LOGIN="lastlogin"
    #TOPIC=5
    ASSESSMENT=6
    NAME_ALIAS='N'
    QUESTION_TYPE_SINGLE=0
    QUESTION_TYPE_MULTIPLE=1
    NO_STUDENT_LEVEL_UPTO_25=0
    NO_STUDENT_LEVEL_UPTO_50=1
    NO_STUDENT_LEVEL_UPTO_75=2
    NO_STUDENT_LEVEL_UPTO_100=3
    STATE_IN_TOPIC=0
    STATE_OF_TOPIC=1
    STATE_INVALID=-1
    STATE_CONTAINED_TOPICS="contains_topic_keys"
    SEX_MALE=0
    SEX_FEMALE=1
    ADDRESS_TYPE_HOME=0
    ADDRESS_TYPE_WORK=1
    ADDRESS_TYPE_OTHER=2
    ERROR_BAD_VALUE=-1
    ERROR_FAILED_QUERY=-2
    ERROR_INCONSISTENT_STATE=-3
    ERROR_OPERATION_FAIL=-4
    ERROR_NO_DATA_FOUND=-5
    ERROR_INVALID_USER=-6
    UPDATION_SUCCESSFULL=0
    MAX_MARKS=100
    
    

class Subject_Name:
    TYPE_CLASS=0
    TYPE_GLOBAL=1
    SUB_MATHS="Mathematics"
    SUB_ENGLISH="English"
    SUB_GEOLOGY="Geology"
    SUB__SCIENCE="Science"
    SUB_VEDIC = "Vedic Maths"

'''class Topic:
    TOPIC_ADDITION="Addition"
    TOPIC_SUBSTRACTION="Substraction"'''
    
    
class States:
    state_city = {'UP' : ["Meerut","Ghaziabad"],'Karnataka' : ["Bengaluru","Hydrabad"]}
    
class Class:
    CLASS_V=5
    CLASS_VI=6

class Section:
    SECTION_A="A"

class UserType:
    STUDENT="Student"
    TEACHER="Teacher"
    SCHOOL="School"

    
class Default:
    date=datetime.datetime(int(2000),int(8),int(8),int(8),int(8),int(8))   
    
    
