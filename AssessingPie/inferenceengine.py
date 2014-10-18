from AssessingPie.models import UserInfo

__author__ = 'ankur'
import logging
import Query
from models import UserInfo, User,Teacher
from gaesessions import get_current_session
import models
import Constant
import datetime
import time
class Question:
    def __init__(self,key,typeid,questionstring):
        self.key=key
        self.typeid = typeid
        self.questionstring = questionstring

class TypeCache:
    def __init__(self):
        self.typelist ={}

    def addtype(self,key,typeid,questionstring):
         self.typelist[typeid] =Question(key,typeid,questionstring)

    def gettype(self,typeid):
        return self.typelist[typeid].questionstring

    def gettypekey(self,typeid):
        return self.typelist[typeid].key

    def getlength(self):
        return len(self.typelist)

class SurmiseRelation:
    def __init__(self,userbuffer):
        self.surmisecache = {}
        loopvar = userbuffer.typeCache.getlength()-1
        while loopvar >= 0:
            self.surmisecache[loopvar] = []
            loopvar-=1



    def addstate(self,typeid,state):
        self.surmisecache[typeid].append(state)

    def getstates(self,typeid):
        return  self.surmisecache.get(typeid)

    def removestate(self,typeid,state):
        self.surmisecache[typeid].remove(state)

    def addstateifnotcontained(self,typeid,state):
        contained=0
        for tempstate in self.surmisecache[typeid]:
            if state.issubset(tempstate):
                self.removestate(typeid,tempstate)
            if tempstate.issubset(state):
                contained=1
        if contained==0:
            SurmiseRelation.addstate(self,typeid,state)


class BlockCache:
    def __init__(self):
        self.blockcache={}

    def initializeblock(self,blocknumber):
         self.blockcache[blocknumber]={}

    def setimplicationtrue(self,blocknumber,queryid):
        self.blockcache[blocknumber][queryid]=1

    def setimplicationfalse(self,blocknumber,queryid):
        self.blockcache[blocknumber][queryid]=2

    def getimplication(self,blocknumber,queryid):
        return  self.blockcache[blocknumber].get(queryid,-1)


def createsurmise(userbuffer):

    numques=userbuffer.typeCache.getlength()
    for x in range(0,numques):
        tempset=set()
        for y in range(0,numques):
            implication=userbuffer.blockCache.getimplication(0,numques*x+y)
            if implication is not None and implication == 2:
                tempset.add(y)

        if len(tempset)>0:
            insertintosurmise(userbuffer,tempset)

def insertintosurmise(userbuffer,tempset):
    for x in tempset:
        tempstatelist = userbuffer.surmiseRelation.getstates(x)
        if tempstatelist is None:
            userbuffer.surmiseRelation.addstate(x,tempset)
        else:

            tobeadded=1
            for state in tempstatelist:
                if tempset.issubset(state):
                    userbuffer.surmiseRelation.removestate(x,state)
                    userbuffer.surmiseRelation.addstate(x,tempset)
                    tobeadded=0
                    break
                else:
                    if state.issubset(tempset):
                        tobeadded=0
                        break

            if tobeadded==1:
                userbuffer.surmiseRelation.addstate(x,tempset)

def prepareblock(userbuffer,blocknumber):
    userbuffer.blockCache.initializeblock(blocknumber)

def passedhstest(userbuffer,block,antecedent,implication):
    passed=True
    numoftypes=userbuffer.typeCache.getlength()
    for questiontype in range(0,numoftypes):
        tempstatelist = userbuffer.surmiseRelation.getstates(questiontype)
        for state in tempstatelist:
            if implication in state and set(antecedent).intersection(state)==set([questiontype]):
                passed=False
                return passed
    return passed

def collectsurmisestate(userbuffer,antecedent):
    addlist=[]
    for questiontype in antecedent:
        tempstatelist = userbuffer.surmiseRelation.getstates(questiontype)
        for state in tempstatelist:
            if set(antecedent).intersection(state)==set([questiontype]):
                addlist.append(state)
    return addlist

def updatesurmise(userbuffer,antecedent,implication):
    addlist = collectsurmisestate(userbuffer,antecedent)
    numtype = userbuffer.typeCache.getlength()
    for questiontype in range(0,numtype):
        tempstatelist=userbuffer.surmiseRelation.getstates(questiontype)
        for state in tempstatelist:
            if implication in state and set(antecedent).intersection(state)==set():
                for addstate in addlist:
                    addstate=addstate.union(state)
                    userbuffer.surmiseRelation.removestate(questiontype,state)
                    userbuffer.surmiseRelation.addstateifnotcontained(questiontype,addstate)


def infertrue(userbuffer,block,antecedentid,antecedent):
    numquestiontype=userbuffer.typeCache.getlength()
    implication=antecedentid % numquestiontype
    for questiontype in range(0,numquestiontype):
        implicationvalue=userbuffer.blockCache.getimplication(0,numquestiontype*implication+questiontype)
        if implicationvalue is not None and implicationvalue==1:
            if block != questiontype:
                if block>0 and passedhstest(userbuffer,block,antecedent,questiontype):
                    updatesurmise(userbuffer,antecedent,questiontype)
                userbuffer.blockCache.setimplicationtrue(block,antecedentid-implication+questiontype)
        else:
            if implicationvalue is not None and implicationvalue==1:
                if block != questiontype:
                    userbuffer.blockCache.setimplicationtrue(block,antecedentid-implication+questiontype)





class InferenceBuffer:
    def __init__(self,topickey):
        self.typeCache = TypeCache()
        question_db = Query.get_questions_of_topic(topickey)

        typeid=-1
        for tempques in question_db:
            typeid+=1
            questionstring=tempques.instance.problem_statement
            key = tempques.key
            self.typeCache.addtype(key,typeid,questionstring)

        self.surmiseRelation = SurmiseRelation(self)
        self.blockCache = BlockCache()
        self.blockCache = BlockCache()

def generatestates(userbuffer,topickey,schoolkey):
    logging.error("entered g")
    statesgen =[]
    numoftype = userbuffer.typeCache.getlength()
    for questiontype in range(0,numoftype):
        surmiselist = userbuffer.surmiseRelation.getstates(questiontype)
        for surmisestate in surmiselist:
            tobeaddedlist =[]
            tobeaddedlist.append(surmisestate)
            for state in statesgen:
                tobeaddedlist.append(surmisestate.union(state))
            for stateadd in tobeaddedlist:
                if stateadd not in statesgen:
                 statesgen.append(stateadd)
    stateall = set()
    num = numoftype-1
    while num >= 0:
        stateall.add(num)
        logging.error(userbuffer.typeCache.gettype(num))
        num-=1
    logging.error(stateall)
    if stateall not in statesgen:
        statesgen.append(stateall)
        tobeaddedlist=[]
    queryreadydict = {}
    statenum =0
    for stateset in statesgen:
        templist = []
        for items in stateset:
            templist.append(userbuffer.typeCache.gettypekey(items))
        queryreadydict[statenum]=templist
        statenum+=1
    session = get_current_session()
    logging.error(queryreadydict)
    #user_name = User.query((User.username == 'Vijay_Mehta')).get()
    teacher = Teacher.query(Teacher.username == 'Vijay_Mehta',ancestor=schoolkey).get()
    logging.info('@@@@@@@@@@@@@@@@@@@@@@'+str(teacher))
    #Query.map_state_to_questions_dummy(queryreadydict,session['schoolkey'])
    Query.map_state_to_questions(topickey,queryreadydict,schoolkey)
    count=topickey.get().assessment_count
    count+=1
    class_v=(teacher.classes_under_teacher)[0]
    #teacher=UserInfo.query()
    assessment1=Query.addAssessment(name="Know Your Numbers : "+str(count),list_topic_key=[topickey],school_key=schoolkey,date=datetime.datetime.now(),due_date=datetime.datetime(int(2014),int(11),int(12),int(23),int(12),int(8)),published=True,teacher_key=teacher.key,class_key=class_v)
    a=Query.get_states_of_topic(topickey)
