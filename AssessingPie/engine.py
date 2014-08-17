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

        self.states = []
        self.questions = dict()
        self.minquestion = -1
        self.maxprobstate = 0
        self.initializebuffer()

    def initializebuffer(self):
        question_db = Query.get_questions_by_topic_name("Number  System")
        state_db =Query.get_states_by_topic_name("Number  System")
        type(state_db)
        initialprob = 1/float(len(state_db) + 1)
        previous_minquestion=-1
        for tempques in question_db:
            num_states = tempques.no_states_contained_in
            questionstring=tempques.instance.problem_statement
            answer = tempques.instance.answer
            if previous_minquestion==-1:
                previous_minquestion = abs(int((len(state_db)/2)-num_states))
                self.minquestion=tempques.key
            else:
                 if(abs(int(len(state_db)/2)-num_states) < previous_minquestion):
                     self.minquestion = tempques.key

            self.questions[tempques.key]=Question(num_states,initialprob*num_states,questionstring,answer)



        self.states.append(State((-1,),initialprob))
        for tempstate in state_db:

            questions = Query.get_questions_of_state(tempstate.key)
            queskeylist =[]
            for question in questions:
                queskeylist.append(question.key)
            questiontuple = tuple(queskeylist)
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