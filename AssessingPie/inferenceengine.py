__author__ = 'ankur'

class Question:
    def __init__(self,key,typeid,questionstring):
        self.key=key
        self.typeid = typeid
        self.questionstring = questionstring

class TypeCache:
    typelist ={}
    @staticmethod
    def addtype(key,typeid,questionstring):
         TypeCache.typelist[typeid] =Question(key,typeid,questionstring)
    @staticmethod
    def gettype(typeid):
        return TypeCache.typelist[typeid].questionstring
    @staticmethod
    def getlength():
        return len(TypeCache.typelist)

class SurmiseRelation:
    surmisecache = {}
    @staticmethod
    def intialize():
        loopvar = TypeCache.getlength()-1
        while loopvar >= 0:
            SurmiseRelation.surmisecache[loopvar] = []
            loopvar-=1
    @staticmethod
    def addstate(typeid,state):
        SurmiseRelation.surmisecache[typeid].append(state)
    @staticmethod
    def getstates(typeid):
        return  SurmiseRelation.surmisecache.get(typeid)
    @staticmethod
    def removestate(self,typeid,state):
        SurmiseRelation.surmisecache[typeid].remove(state)
    @staticmethod
    def addstateifnotcontained(typeid,state):
        contained=0
        for tempstate in SurmiseRelation.surmisecache[typeid]:
            if state.issubset(tempstate):
                SurmiseRelation.removestate(typeid,tempstate)
            if tempstate.issubset(state):
                contained=1
        if contained==0:
            SurmiseRelation.addstate(typeid,state)


class BlockCache:
    blockcache={}
    @staticmethod
    def initializeblock(blocknumber):
         BlockCache.blockcache[blocknumber]={}
    @staticmethod
    def setimplicationtrue(blocknumber,queryid):
        BlockCache.blockcache[blocknumber][queryid]=1
    @staticmethod
    def setimplicationfalse(blocknumber,queryid):
        BlockCache.blockcache[blocknumber][queryid]=2
    @staticmethod
    def getimplication(blocknumber,queryid):
        return  BlockCache.blockcache[blocknumber].get(queryid,-1)


def createsurmise():

    numques=TypeCache.getlength()
    for x in range(0,numques):
        tempset=set()
        for y in range(0,numques):
            implication=BlockCache.getimplication(0,numques*x+y)
            if implication is not None and implication == 2:
                tempset.add(y)

        if len(tempset)>0:
            insertintosurmise(tempset)

def insertintosurmise(tempset):
    for x in tempset:
        tempstatelist = SurmiseRelation.getstates(x)
        if tempstatelist is None:
            SurmiseRelation.addstate(x,tempset)
        else:

            tobeadded=1
            for state in tempstatelist:
                if tempset.issubset(state):
                    SurmiseRelation.removestate(x,state)
                    SurmiseRelation.addstate(x,tempset)
                    tobeadded=0
                    break
                else:
                    if state.issubset(tempset):
                        tobeadded=0
                        break

            if tobeadded==1:
                SurmiseRelation.addstate(x,tempset)

def prepareblock(blocknumber):
    BlockCache.initializeblock(blocknumber)

def passedhstest(block,antecedent,implication):
    passed=True
    numoftypes=TypeCache.getlength()
    for questiontype in range(0,numoftypes):
        tempstatelist = SurmiseRelation.getstates(questiontype)
        for state in tempstatelist:
            if implication in state and set(antecedent).intersection(state)==set([questiontype]):
                passed=False
                return passed
    return passed

def collectsurmisestate(antecedent):
    addlist=[]
    for questiontype in antecedent:
        tempstatelist = SurmiseRelation.getstates(questiontype)
        for state in tempstatelist:
            if set(antecedent).intersection(state)==set([questiontype]):
                addlist.append(state)
    return addlist

def updatesurmise(antecedent,implication):
    addlist = collectsurmisestate(antecedent)
    numtype = TypeCache.getlength()
    for questiontype in range(0,numtype):
        tempstatelist=SurmiseRelation.getstates(questiontype)
        for state in tempstatelist:
            if implication in state and set(antecedent).intersection(state)==set():
                for addstate in addlist:
                    addstate=addstate.union(state)
                    SurmiseRelation.removestate(questiontype,state)
                    SurmiseRelation.addstateifnotcontained(questiontype,addstate)


def infertrue(block,antecedentid,antecedent):
    numquestiontype=TypeCache.getlength()
    implication=antecedentid % numquestiontype
    for questiontype in range(0,numquestiontype):
        implicationvalue=BlockCache.getimplication(0,numquestiontype*implication+questiontype)
        if implicationvalue is not None and implicationvalue==1:
            if block != questiontype:
                if block>0 and passedhstest(block,antecedent,questiontype):
                    updatesurmise(antecedent,questiontype)
                BlockCache.setimplicationtrue(block,antecedentid-implication+questiontype)
        else:
            if implicationvalue is not None and implicationvalue==1:
                if block != questiontype:
                    BlockCache.setimplicationtrue(block,antecedentid-implication+questiontype)


def initializetypecache():
    TypeCache.addtype(0,0,"Simple addition")
    TypeCache.addtype(1,1,"Carry Over addition")
    TypeCache.addtype(2,2,"Division")