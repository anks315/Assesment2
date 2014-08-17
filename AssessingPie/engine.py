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
    def __init__(self,questionstuple,prob):
        self.questionstuple = questionstuple
        self.prob = prob

class  UserBuffer:
    def __init__(self):
        self.count=0
        self.initializebuffer()
        self.states = [State((-1,),0.25),State((0,),0.25),State((0,1),0.25),State((0,1,2),0.25)]
        self.questions = {0:Question(3,0.75,'Add 3 and 5',8), 1:Question(2,0.50,'Add 29 + 35',64), 2:Question(1,0.25,'Divide and find quotient 58 by 9',6),}
        self.minquestion = 1
        self.maxprobstate = 0

    def initializequestions:

    def initializebuffer(self):
        state_db =Query.get_states_of_topic("Number  System")
        initialprob = 1/state_db.__len__()
        self.states.append(State((-1),initialprob))
        for tempstate in state_db:
            questiontuple = tuple(Query.get_questions_of_state(tempstate.key))
            self.states.append(State(questiontuple,initialprob))



usersdict ={}
previousmin=-1

def setcount(userid):
    usersdict[userid].count+=1

def getcount(userid):
    return usersdict[userid].count

def maxstate(userid) :
    return  usersdict[userid].maxprobstate

def nextquestion(userid) :
    return usersdict[userid].minquestion

def update(userid,correct):

    global previousmin

    previousmin = usersdict[userid].minquestion
    usersdict[userid].questions[usersdict[userid].minquestion].probsum=3.00
    count =-1
    if correct==True:
        numstate = usersdict[userid].questions[usersdict[userid].minquestion].num_states
        subtractamount = (numstate * 0.1)/ (len(usersdict[userid].states)-numstate)

        usersdict[userid].minquestion=-1

        for state in usersdict[userid].states:
            count+=1

            if previousmin in state.questionstuple:
                state.prob+=0.1
                if usersdict[userid]. states[usersdict[userid].maxprobstate].prob < state.prob:
                    usersdict[userid].maxprobstate=count
                for ques in state.questionstuple:
                    if ques!=-1:
                        usersdict[userid].questions[ques].probsum+=0.1
                        if usersdict[userid].minquestion==-1:
                            usersdict[userid].minquestion =ques
                        if abs(usersdict[userid].questions[usersdict[userid].minquestion].probsum - 0.5) > abs(usersdict[userid].questions[ques].probsum - 0.5):
                            usersdict[userid].minquestion=ques
            else:
                state.prob-=subtractamount
                for quest in state.questionstuple:
                    if quest!=-1:
                        if usersdict[userid].minquestion==-1:
                            usersdict[userid].minquestion =quest
                        usersdict[userid].questions[quest].probsum-=subtractamount
                        if abs(usersdict[userid].questions[usersdict[userid].minquestion].probsum - 0.5) > abs(usersdict[userid].questions[quest].probsum - 0.5):
                            usersdict[userid].minquestion=quest
    else:
        numstate = usersdict[userid].questions[usersdict[userid].minquestion].num_states
        addamount = (numstate * 0.1)/ (len(usersdict[userid].states)-numstate)

        usersdict[userid].minquestion=-1
        for state in usersdict[userid].states:
            count+=1
            if previousmin in state.questionstuple:
                state.prob-=0.1
                for ques in state.questionstuple:
                    if ques!=-1:
                        usersdict[userid].questions[ques].probsum-=0.1
                        if usersdict[userid].minquestion==-1:
                            usersdict[userid].minquestion =ques
                        if abs(usersdict[userid].questions[usersdict[userid].minquestion].probsum - 0.5) > abs(usersdict[userid].questions[ques].probsum - 0.5):
                            usersdict[userid].minquestion=ques
            else:
                state.prob+=addamount
                if(usersdict[userid].states[usersdict[userid].maxprobstate].prob < state.prob):
                    usersdict[userid].maxprobstate=count

                for quest in state.questionstuple:
                    if quest!=-1:
                        usersdict[userid].questions[quest].probsum+=addamount
                        if usersdict[userid].minquestion==-1:
                            usersdict[userid].minquestion =quest
                        if abs(usersdict[userid].questions[usersdict[userid].minquestion].probsum - 0.5) > abs(usersdict[userid].questions[quest].probsum - 0.5):
                            usersdict[userid].minquestion=quest