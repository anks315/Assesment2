__author__ = 'ankur'
import logging
import models
import Query

class Question:
    def __init__(self,num_states,probsum,questionstring,answer):
        self.num_states = num_states
        self.probsum = probsum

        self.questionstring = questionstring
        self.answer = answer

class State :
    def __init__(self,questionstuple,prob,key):
        self.questionstuple = questionstuple
        self.prob = prob
        self.key=key


class  UserBuffer:
    def __init__(self,topickey):
        self.count=0

        self.states = {}
        self.questions = dict()
        self.minquestion = -1
        self.maxprobstate = 0
        self.maxprobsize=0
        self.initializebuffer(topickey)
        self.numstates=-1

    def initializebuffer(self,topickey):
        question_db = Query.get_questions_of_topic(topickey)
        state_db =Query.get_states_of_topic(topickey)
        self.numstates=len(state_db)
        type(state_db)
        initialprob = 1/float(len(state_db) + 1)
        previous_minquestion=-1
        for tempques in question_db:
            num_states = tempques.no_states_contained_in
            questionstring=tempques.instance.problem_statement
            answer = tempques.instance.answer
            if previous_minquestion==-1:
                previous_minquestion = abs(int(((len(state_db)+1)/2)-num_states))
                self.minquestion=tempques.key
            else:
                 if(abs(int((len(state_db)+1)/2)-num_states) < previous_minquestion):
                     self.minquestion = tempques.key

            self.questions[tempques.key]=Question(num_states,initialprob*num_states,questionstring,answer)



        self.states[0] =[State((-1,),initialprob,0)]
        for tempstate in state_db:

            questions = Query.get_questions_of_state(tempstate.key)

            queskeylist =[]
            logging.error(type(questions))


            for question in questions:
                queskeylist.append(question.key)
            questiontuple = tuple(queskeylist)
            key=tempstate.key
            size = len(questiontuple)
            temp = self.states.get(size)
            if temp is None:
                self.states[size]=[]
            self.states[size].append(State(questiontuple,initialprob,key))


readytolearn = {}
usersdict ={}
previousmin=-1
completedtopics = {}

def getnumquestions(userid):
    return len(usersdict[userid].questions)

def setcount(userid):
    usersdict[userid].count+=1

def getcount(userid):
    return usersdict[userid].count

def maxstate(userid) :
    return  usersdict[userid].maxprobstate

def maxstatesize(userid):
    return  usersdict[userid].maxprobsize

def nextquestion(userid) :
    return usersdict[userid].minquestion




def update(userid,correct):

    global previousmin

    previousmin = usersdict[userid].minquestion

    count =-1
    if correct==True:
        numstate = usersdict[userid].questions[usersdict[userid].minquestion].num_states
        subtractamount = (numstate * 0.1)/ (usersdict[userid].numstates-numstate)

        usersdict[userid].minquestion=-1
        for statesize in usersdict[userid].states:
            count=-1
            for state in usersdict[userid].states[statesize]:
                count+=1

                if previousmin in state.questionstuple:
                    increament = (1/(usersdict[userid].questions[previousmin].probsum))-1
                    g = (0.5*state.prob)*increament
                    state.prob+=g
                    if usersdict[userid]. states[usersdict[userid].maxprobstate][usersdict[userid].maxprobstate].prob < state.prob:
                        usersdict[userid].maxprobstate=count
                        usersdict[userid].maxprobsize=statesize
                    for ques in state.questionstuple:
                        if ques!=-1:
                            usersdict[userid].questions[ques].probsum+=g
                            if usersdict[userid].minquestion==-1:
                                usersdict[userid].minquestion =ques
                            if (ques!=previousmin and abs(usersdict[userid].questions[usersdict[userid].minquestion].probsum - 0.5) > abs(usersdict[userid].questions[ques].probsum - 0.5)):
                                usersdict[userid].minquestion=ques
                else:
                    g=0.5*state.prob
                    state.prob-=0.5*state.prob
                    for quest in state.questionstuple:
                        if quest!=-1:
                            if usersdict[userid].minquestion==-1:
                                usersdict[userid].minquestion =quest
                            usersdict[userid].questions[quest].probsum-=g
                            if (quest!=previousmin and abs(usersdict[userid].questions[usersdict[userid].minquestion].probsum - 0.5) > abs(usersdict[userid].questions[quest].probsum - 0.5)):
                                usersdict[userid].minquestion=quest
    else:
        numstate = usersdict[userid].questions[usersdict[userid].minquestion].num_states
        addamount = (numstate * 0.1)/ (usersdict[userid].numstates-numstate)

        usersdict[userid].minquestion=-1
        for statesize in usersdict[userid].states:
            count=-1
            for state in usersdict[userid].states[statesize]:
                count+=1
                if previousmin in state.questionstuple:
                    g=0.5*state.prob
                    state.prob-=0.5*state.prob
                    logging.error("decrement value")
                    logging.error(g)
                    for ques in state.questionstuple:
                        if ques!=-1:
                            usersdict[userid].questions[ques].probsum-=g
                            if usersdict[userid].minquestion==-1:
                                usersdict[userid].minquestion =ques
                            if (ques!=previousmin and abs(usersdict[userid].questions[usersdict[userid].minquestion].probsum - 0.5) > abs(usersdict[userid].questions[ques].probsum - 0.5)):
                                usersdict[userid].minquestion=ques
                else:
                    increament = (1/(1-(usersdict[userid].questions[previousmin].probsum)))-1
                    logging.error("hii imcreament value")

                    g = (0.5*state.prob)*increament
                    logging.error(g)
                    state.prob+=g
                    if(usersdict[userid].states[usersdict[userid].maxprobsize][usersdict[userid].maxprobstate].prob < state.prob):
                        usersdict[userid].maxprobstate=count
                        usersdict[userid].maxprobsize=statesize

                    for quest in state.questionstuple:
                        if quest!=-1:
                            usersdict[userid].questions[quest].probsum+=g
                            if usersdict[userid].minquestion==-1:
                                usersdict[userid].minquestion =quest
                                logging.error("entered min")
                            if (quest!=previousmin and abs(usersdict[userid].questions[usersdict[userid].minquestion].probsum - 0.5) > abs(usersdict[userid].questions[quest].probsum - 0.5)):
                                usersdict[userid].minquestion=quest
                                logging.error("entered min")
    usersdict[userid].questions[previousmin].probsum=50.00