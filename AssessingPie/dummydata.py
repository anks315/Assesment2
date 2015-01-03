from google.appengine.ext import ndb
import Query
import logging
import datetime
import time

from Constant import Constant,UserType,Subject_Name
import Constant
from Query import addSubject, addTopic   
from models import QuestionInstance,State_Questions,Topic_States,Question,State,Address,Teacher,Class,\
    Assessment_Record
from models import School,Student,UserInfo,Subject,Assessment,Student_Assessments
from  models import Topic_Questions,State_Questions,Topic_States,Subject_Topics
from models import Topic,User,Subject 

def fill():
    try:
            flush()
            address1=Query.addAddress(type=Constant.Constant.ADDRESS_TYPE_HOME,state="UP",city="Meerut",street="12")
            school=Query.addSchool("CVSchool", address1)
            time.sleep(15)
            ankit_user=Query.addUserInfo("Ankit","Bhatia",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            kavya_user=Query.addUserInfo("Kavya","Singh",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "kavya@gmail.com", 7667654766)
            prajjwal_user=Query.addUserInfo("Prajjwal","Ojha",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "prajjwal@gmail.com", 87654766)
            shiv_user=Query.addUserInfo("Shiv","Sahay",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            
            
            sarthaj_user=Query.addUserInfo("Sarthak","Tiwari",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "vivek@gmail.com", 8787877)
            mishika_user=Query.addUserInfo("Mishika","Singh",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "kavya@gmail.com", 7667654766)
            prasoon_user=Query.addUserInfo("Prasoon","Garg",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_MALE, address1, "prajjwal@gmail.com", 87654766)
            pravesh_user=Query.addUserInfo("Pravesh","Sahay",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
   
            
            
            vijay_user=Query.addUserInfo("Vijay","Mehta",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            sulabh_user=Query.addUserInfo("Sulabj","Jain",datetime.datetime(int(2009),int(8),int(6),int(23),int(12),int(8)),Constant.Constant.SEX_FEMALE, address1, "8778", 654766)
            #userinfo7=Query.addUserInfo("Smriti","Arora",datetime.datetime.now(),Constant.SEX_FEMALE, address1, "8778", 654766)
            #userinfo8=Query.addUserInfo("Samarath","Tiwari",datetime.datetime.now(),Constant.SEX_FEMALE, address1, "8778", 654766)
            
            
            student_vivek=Query.addStudent("Ankit_Bhatia",ankit_user, school.key,'password')
            student_kavya=Query.addStudent("Kavya_Singh",kavya_user, school.key,'pwd')
            student_prajjwal=Query.addStudent("Prajjwal_Ojha",prajjwal_user, school.key,'pwd')
            student_shiv=Query.addStudent("Shiv_Sahay",shiv_user, school.key,'pwd')
            
            
            student_sarthak=Query.addStudent("Sarthak_Tiwari",sarthaj_user, school.key,'pwd')
            student_mishika=Query.addStudent("Mishika_Singh",mishika_user, school.key,'pwd')
            student_prasoon=Query.addStudent("Prasoon_Garg", prasoon_user,school.key,'pwd')
            student_pravesh=Query.addStudent("Pravesh_Sahay",pravesh_user, school.key,'pwd')
            #teacher1=Query.addTeacher("teacher1", userinfo1, school.key)
            
            
            
            class_VA=Query.addClass(name="Class_V",school_key= school.key,section_details="A",year_session="2013-2014")  #to be changed
            class_VIB=Query.addClass(name="Class_VI",school_key= school.key,section_details="B",year_session="2013-2014")  #to be changed
            
            
            
            
            Query.assign_students_to_class(class_VA.key, [student_vivek.key])
            Query.assign_students_to_class(class_VA.key, [student_sarthak.key,student_mishika.key,student_prasoon.key,student_pravesh.key])

            
            
            
            
            
            
            teacher_vijay=Query.addTeacher("Vijay_Mehta",vijay_user, school.key,"password")
            teacher_sulabh=Query.addTeacher("Sulabj_Jain" ,sulabh_user, school.key,"")
            
          
            
            
            a=Query.assign_classes_to_teacher(teacher_vijay.key,[class_VA.key])
            Query.assign_classes_to_teacher(teacher_vijay.key,[class_VA.key])
            
            
            
            SUB_maths=Query.addSubject(Constant.Subject_Name.TYPE_CLASS, Constant.Subject_Name.SUB_MATHS,school.key,class_VA.key)
            #subject2=Query.addSubject(Subject.TYPE_CLASS, Subject.SUB_SCIENCE,school.key,class1.key)
            SUB_english=Query.addSubject(Constant.Subject_Name.TYPE_CLASS, Constant.Subject_Name.SUB_ENGLISH,school.key,class_VA.key)
            SUB_vedic = Query.addSubject(Constant.Subject_Name.TYPE_GLOBAL, Constant.Subject_Name.SUB_VEDIC,school.key,class_VA.key)
            #subject4=Query.addSubject(Subject.TYPE_CLASS, Subject.SUB_GEOLOGY,school.key,class1.key)

            a=Query.assign_subjects_to_class(class_VA.key, [SUB_maths.key])
            a=Query.assign_subjects_to_class(class_VA.key, [SUB_english.key])
            a=Query.assign_subjects_to_class(class_VA.key, [SUB_vedic.key])
            
            
            Query.assign_subjects_to_teacher(teacher_vijay.key,[SUB_maths.key])
            a=Query.assign_subjects_to_teacher(teacher_vijay.key,[SUB_english.key])
            a=Query.assign_subjects_to_teacher(teacher_vijay.key,[SUB_vedic.key])

           
            ##Query.login("Suraj_Singh", "pwd")
            
            
            
            
            topic_number=Query.addTopic(school_key=school.key,name="Know Your Numbers", prerequisite_topics=[],subject_key=SUB_maths.key,types=["Comparing Numbers","Numbers Formation","Arrangement_Ascending"])
            topic_trig=Query.addTopic(school_key=school.key,name="Trigonimetric_Ratio", prerequisite_topics=[topic_number.key],subject_key=SUB_maths.key,types=["type1","type2","type3"])
            topic_height=Query.addTopic(school_key=school.key,name="Height & Distance", prerequisite_topics=[topic_trig.key,topic_number.key],subject_key=SUB_maths.key,types=["type1","type2","type3"])
            topic_circle=Query.addTopic(school_key=school.key,name="Circle_operation", prerequisite_topics=[topic_number.key],subject_key=SUB_maths.key,types=["type1","type2","type3"])
           
            
            
            
            topic_part=Query.addTopic(school_key=school.key,name="Part of Speech", prerequisite_topics=[],subject_key=SUB_english.key,types=["type1","type2","type3"])
            topic_tenses=Query.addTopic(school_key=school.key,name="Tenses", prerequisite_topics=[],subject_key=SUB_english.key,types=["type1","type2","type3"])
            topic_sentences=Query.addTopic(school_key=school.key,name="Sentences", prerequisite_topics=[topic_part.key],subject_key=SUB_english.key,types=["type1","type2","type3"])
            topic_voices=Query.addTopic(school_key=school.key,name="Voices", prerequisite_topics=[topic_sentences.key,topic_part.key],subject_key=SUB_english.key,types=["type1","type2","type3"])
            #topic5=Query.addTopic(school_key=school.key,name="Ellipse ", prerequisite_topics=[topic.key],subject_key=subject1.key)
            
            
            topic_chap_one=Query.addTopic(school_key=school.key,name="Basic Concept of Vedic Maths", prerequisite_topics=[],subject_key=SUB_vedic.key,types=["Base of A Number","Complement with zero in between","Complement with zero at end","Complement with decimal in between"])
            topic_chap_two=Query.addTopic(school_key=school.key,name="Subtraction at a Look", prerequisite_topics=[topic_chap_one.key],subject_key=SUB_vedic.key,types=["Subtraction from base","Subtraction from bigger base","Subtraction from multiple of base","Subtraction with same number of digit","General Subtraction"])
            topic_chap_three=Query.addTopic(school_key=school.key,name="Multiplication with 99999...", prerequisite_topics=[topic_chap_one.key],subject_key=SUB_vedic.key,types=["Multiplication of 999.. with same number of digit","Multiplication of 999.. with less number of digit","Multiplication of 999.. with greater number of digit"])
            topic_chap_four=Query.addTopic(school_key=school.key,name="Magic with 11", prerequisite_topics=[topic_chap_one.key],subject_key=SUB_vedic.key,types=["Multipyling with 11","Multiplying with 1111.."])
            topic_chap_five=Query.addTopic(school_key=school.key,name="Multiplying with 12(without using 12)", prerequisite_topics=[topic_chap_one.key],subject_key=SUB_vedic.key,types=["Multiply with 12","Multiply with 112","Multiply with 1112"])
            


            questioninstance_number1=Query.addQuestionInstance(problem_statement="Sum of of 2 and 3 ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["5"],school_key=school.key)
            
            questioninstance_number2=Query.addQuestionInstance(problem_statement="Sum of 222+30  ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["252"],school_key=school.key)
            #questioninstance_number3=Query.addQuestionInstance(problem_statement="Which one is greatest ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["1902","1920","9201","9021","9210"], answers=["9210"],school_key=school.key)

            #questioninstance_number4=Query.addQuestionInstance(problem_statement="Which one is smallest ?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["1902","1920","9201","9021","9210"], answers=["9210"],school_key=school.key)

            questioninstance_number3=Query.addQuestionInstance(problem_statement="quotient of 58 by 9", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=[], answers=["6"],school_key=school.key)


            questioninstance_base_one=Query.addQuestionInstance(problem_statement="Whether 2900 is base or not? y or n ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["n"],school_key=school.key,url="")
            questioninstance_complement_zeroinbetween = Query.addQuestionInstance(problem_statement="Find Complement of 3049 ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["6941"],school_key=school.key,url="")
            questioninstance_complement_zeroatend = Query.addQuestionInstance(problem_statement="Find Complement of 3420", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["6580"],school_key=school.key,url="")
            questioninstance_complement_decimalinbetween = Query.addQuestionInstance(problem_statement="Find Complement of 437.26", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["437.26"],school_key=school.key,url="")

            question_base_one=Query.addQuestion(questioninstance_base_one,school.key)
            question_complement_zeroinbetween=Query.addQuestion(questioninstance_complement_zeroinbetween,school.key)
            question_complement_zeroatend=Query.addQuestion(questioninstance_complement_zeroatend,school.key)
            question_complement_decimalinbetween=Query.addQuestion(questioninstance_complement_decimalinbetween,school.key)


            Query.assign_questions_to_topic(topic_chap_one.key,[question_base_one.key],school.key,"Base of A Number")
            Query.assign_questions_to_topic(topic_chap_one.key,[question_complement_zeroinbetween.key],school.key,"Complement with zero in between")
            Query.assign_questions_to_topic(topic_chap_one.key,[question_complement_zeroatend.key],school.key,"Complement with zero at end")
            Query.assign_questions_to_topic(topic_chap_one.key,[question_complement_decimalinbetween.key],school.key,"Complement with decimal in between")
            '''
            state_chapone_one=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapone_two=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapone_three = Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapone_four = Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapone_five=  Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapone_six = Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapone_seven = Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapone_eight = Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            '''
         #   Query.assign_questions_to_state(state_chapone_one.key, [question_base_one.key],school.key)
          #  Query.assign_questions_to_state(state_chapone_two.key, [question_base_one.key,question_complement_zeroinbetween.key],school.key)
           # Query.assign_questions_to_state(state_chapone_three.key, [question_base_one.key,question_complement_decimalinbetween.key],school.key)
           # Query.assign_questions_to_state(state_chapone_four.key, [question_base_one.key,question_complement_zeroatend.key],school.key)
           # Query.assign_questions_to_state(state_chapone_five.key, [question_base_one.key,question_complement_zeroinbetween.key,question_complement_decimalinbetween.key],school.key)
           # Query.assign_questions_to_state(state_chapone_six.key, [question_base_one.key,question_complement_zeroinbetween.key,question_complement_zeroatend.key],school.key)
           # Query.assign_questions_to_state(state_chapone_seven.key, [question_base_one.key,question_complement_zeroatend.key,question_complement_decimalinbetween.key],school.key)
            #Query.assign_questions_to_state(state_chapone_eight.key, [question_base_one.key,question_complement_zeroatend.key,question_complement_decimalinbetween.key,question_complement_zeroinbetween.key],school.key)

            Query.map_state_to_topic_type(topic_chap_one.key, {1:["Base of A Number"],2:["Base of A Number","Complement with zero in between"],3:["Base of A Number","Complement with zero in between","Complement with zero at end"],4:["Base of A Number","Complement with zero in between","Complement with zero at end","Complement with decimal in between"]},school.key)

            #Query.assign_states_to_topic(topic_chap_one.key,[state_chapone_one.key,state_chapone_two.key,state_chapone_six.key,state_chapone_eight.key],school.key)



            '''
            questioninstance_subtractionfrombase=Query.addQuestionInstance(problem_statement="10000-3246=? ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["6754"],school_key=school.key,url="")
            questioninstance_subtractionfrombiggerbase=Query.addQuestionInstance(problem_statement="10000-23=? ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["9977"],school_key=school.key,url="")
            questioninstance_subtractionfrommultipleofbase=Query.addQuestionInstance(problem_statement="5000-248=? ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["752"],school_key=school.key,url="")
            questioninstance_subtractionsamenumberofdigit=Query.addQuestionInstance(problem_statement="9000-5246=? ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["3754"],school_key=school.key,url="")
            questioninstance_general_subtraction=Query.addQuestionInstance(problem_statement="96247-28519=? ", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["67728"],school_key=school.key,url="")

            question_subtractionfrombase=Query.addQuestion(questioninstance_subtractionfrombase,school.key)
            question_subtractionfrombiggerbase=Query.addQuestion(questioninstance_subtractionfrombiggerbase,school.key)
            question_subtractionfrommultipleofbase=Query.addQuestion(questioninstance_subtractionfrommultipleofbase,school.key)
            question_subtractionsamenumberofdigit=Query.addQuestion(questioninstance_subtractionsamenumberofdigit,school.key)
            question_general_subtraction=Query.addQuestion(questioninstance_general_subtraction,school.key)


            Query.assign_questions_to_topic(topic_chap_two.key,[question_subtractionfrombase.key,question_subtractionfrombiggerbase.key,question_subtractionfrommultipleofbase.key,question_subtractionsamenumberofdigit.key,question_general_subtraction.key],school.key,"type1")

            state_chaptwo_one=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chaptwo_two=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chaptwo_three=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chaptwo_four=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chaptwo_five=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chaptwo_six=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chaptwo_seven=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chaptwo_eight=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chaptwo_nine=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)



            Query.assign_questions_to_state(state_chaptwo_one.key, [question_subtractionfrombase.key],school.key)
            Query.assign_questions_to_state(state_chaptwo_two.key, [question_general_subtraction.key],school.key)
            Query.assign_questions_to_state(state_chaptwo_three.key, [question_subtractionfrombase.key,question_general_subtraction.key],school.key)
            Query.assign_questions_to_state(state_chaptwo_four.key, [question_subtractionfrombase.key,question_subtractionfrombiggerbase.key],school.key)
            Query.assign_questions_to_state(state_chaptwo_five.key, [question_subtractionfrombase.key,question_subtractionfrombiggerbase.key,question_subtractionfrommultipleofbase.key],school.key)
            Query.assign_questions_to_state(state_chaptwo_six.key, [question_subtractionfrombase.key,question_subtractionfrombiggerbase.key,question_subtractionfrommultipleofbase.key,question_subtractionsamenumberofdigit.key],school.key)
            Query.assign_questions_to_state(state_chaptwo_seven.key, [question_subtractionfrombase.key,question_general_subtraction.key,question_subtractionfrombiggerbase.key],school.key)
            Query.assign_questions_to_state(state_chaptwo_eight.key, [question_subtractionfrombase.key,question_general_subtraction.key,question_subtractionfrombiggerbase.key,question_subtractionfrommultipleofbase.key],school.key)
            Query.assign_questions_to_state(state_chaptwo_nine.key, [question_subtractionfrombase.key,question_general_subtraction.key,question_subtractionfrombiggerbase.key,question_subtractionsamenumberofdigit.key,question_subtractionfrommultipleofbase.key],school.key)


            Query.assign_states_to_topic(topic_chap_two.key, [state_chaptwo_one.key,state_chaptwo_two.key,state_chaptwo_three.key,state_chaptwo_four.key,state_chaptwo_five.key,state_chaptwo_six.key,state_chaptwo_seven.key,state_chaptwo_eight.key,state_chaptwo_nine.key],school.key)




            questioninstance_multiplication999=Query.addQuestionInstance(problem_statement="389 * 999=?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["388611"],school_key=school.key,url="")
            questioninstance_multiplication999less=Query.addQuestionInstance(problem_statement="243 * 9999=?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["2429757"],school_key=school.key,url="")
            questioninstance_multiplication999greater=Query.addQuestionInstance(problem_statement="7428 * 99=?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["735372"],school_key=school.key,url="")

            question_multiplication999=Query.addQuestion(questioninstance_multiplication999,school.key)
            question_multiplication999less=Query.addQuestion(questioninstance_multiplication999less,school.key)
            question_multiplication999greater=Query.addQuestion(questioninstance_multiplication999greater,school.key)

            Query.assign_questions_to_topic(topic_chap_three.key,[question_multiplication999.key,question_multiplication999less.key,question_multiplication999greater.key],school.key,"type1")

            state_chapthree_one=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapthree_two=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapthree_three=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)


            Query.assign_questions_to_state(state_chapthree_one.key, [question_multiplication999.key],school.key)
            Query.assign_questions_to_state(state_chapthree_two.key, [question_multiplication999.key,question_multiplication999less.key],school.key)
            Query.assign_questions_to_state(state_chapthree_three.key, [question_multiplication999.key,question_multiplication999less.key,question_multiplication999greater.key],school.key)

            Query.assign_states_to_topic(topic_chap_three.key, [state_chapthree_one.key,state_chapthree_two.key,state_chapthree_three.key],school.key)



            questioninstance_magicwith11=Query.addQuestionInstance(problem_statement="4573 * 11=?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["50303"],school_key=school.key,url="")
            questioninstance_magicwith1111=Query.addQuestionInstance(problem_statement="2473 * 1111=?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["2747503"],school_key=school.key,url="")

            question_magicwith11=Query.addQuestion(questioninstance_magicwith11,school.key)
            question_magicwith1111=Query.addQuestion(questioninstance_magicwith1111,school.key)


            Query.assign_questions_to_topic(topic_chap_four.key,[question_magicwith11.key,question_magicwith1111.key],school.key,"type1")

            state_chapfour_one=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapfour_two=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)

            Query.assign_questions_to_state(state_chapfour_one.key, [question_magicwith11.key],school.key)
            Query.assign_questions_to_state(state_chapfour_two.key, [question_magicwith11.key,question_magicwith1111.key],school.key)

            Query.assign_states_to_topic(topic_chap_four.key, [state_chapfour_one.key,state_chapfour_two.key],school.key)



            questioninstance_multiplywith12=Query.addQuestionInstance(problem_statement="3785 * 12=?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["45420"],school_key=school.key,url="")
            questioninstance_multiplywith112=Query.addQuestionInstance(problem_statement="432 * 112=?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["48384"],school_key=school.key,url="")
            questioninstance_multiplywith1112=Query.addQuestionInstance(problem_statement="5321 * 1112=?", type=Constant.Constant.QUESTION_TYPE_SINGLE, choices=["yes","no"], answers=["5916952"],school_key=school.key,url="")


            question_multiplywith12=Query.addQuestion(questioninstance_multiplywith12,school.key)
            question_multiplywith112=Query.addQuestion(questioninstance_multiplywith112,school.key)
            question_multiplywith1112=Query.addQuestion(questioninstance_multiplywith1112,school.key)

            Query.assign_questions_to_topic(topic_chap_five.key,[question_multiplywith12.key,question_multiplywith112.key,question_multiplywith1112.key],school.key,"type1")

            state_chapfive_one=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapfive_two=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)
            state_chapfive_three=Query.addState(type=Constant.Constant.STATE_IN_TOPIC,school_key=school.key)


            Query.assign_questions_to_state(state_chapfive_one.key, [question_multiplywith12.key],school.key)
            Query.assign_questions_to_state(state_chapfive_two.key, [question_multiplywith12.key,question_multiplywith112.key],school.key)
            Query.assign_questions_to_state(state_chapfive_three.key, [question_multiplywith12.key,question_multiplywith112.key,question_multiplywith1112.key],school.key)

            Query.assign_states_to_topic(topic_chap_five.key, [state_chapfive_one.key,state_chapfive_two.key,state_chapfive_three.key],school.key)


            '''
            assessment1=Query.addAssessment(name="Vedic Maths :1",list_topic_key=[topic_chap_one.key,topic_chap_two.key,topic_chap_three.key,topic_chap_four.key,topic_chap_five.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime(int(2014),int(11),int(12),int(23),int(12),int(8)),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)

            assessment2=Query.addAssessment(name="Vedic Maths :2",list_topic_key=[topic_chap_one.key],school_key=school.key,date=datetime.datetime.now(),due_date=datetime.datetime(int(2014),int(11),int(12),int(23),int(12),int(8)),published=True,teacher_key=teacher_vijay.key,class_key=class_VA.key)

            
            
            a=Query.get_global_subjects(school.key)
            a=Query.get_subject_details_by_student(student_vivek.key);

            #a=Query.update_assessment_detail_of_student(total_score=50,topic_scores=[20,40,20,21,56],student_key= student_vivek.key,assessment_key= assessment1.key, current_state_key=[state_chapfive_one.key,state_chapfive_two.key,state_chapfive_three.key,state_chapfive_three.key,state_chapfive_three.key], next_state_key=[state_chapfive_one.key,state_chapfive_two.key,state_chapfive_three.key,state_chapfive_three.key,state_chapfive_three.key] \
            #                                          , next_question_key=[question_multiplywith12.key,question_general_subtraction.key,question_multiplywith12.key,question_multiplywith12.key,question_multiplywith12.key], school_key=school.key, completion_date=datetime.datetime(int(2014),int(8),int(8),int(8),int(8),int(8)))
            
            
            
            a=Query.get_mastery_by_subject_sc(SUB_vedic.key, student_vivek.key)
            b=Query.get_assessment_score_of_student(student_vivek.key,assessment1.key)
            a=Query.get_assessment_next_states_of_student(student_vivek.key,assessment1.key)
            a=Query.get_assessment_next_questions_of_student(student_vivek.key,assessment1.key)
            a=Query.get_assessment_scores_of_student(student_vivek.key,assessment1.key)
            a=Query.get_pending_assessments_by_subject(student_vivek.key,SUB_vedic.key)
            a=Query.get_learning_progress(student_vivek.key,SUB_vedic.key)
            b=Query.get_recent_assessment_score_of_student(student_vivek.key,SUB_vedic.key)
            a=Query.get_recent_assessment_next_states_of_student(student_vivek.key,SUB_vedic.key)
            a=Query.get_recent_assessment_topic_scores_of_student(student_vivek.key,SUB_vedic.key)
            a=Query.get_recent_assessment_next_questions_of_student(student_vivek.key,SUB_vedic.key)
            return str(a)+str(b)


    except Exception :
            logging.exception("")
            return Constant.Constant.ERROR_OPERATION_FAIL



def flush():
    ndb.delete_multi(School.query().fetch(keys_only=True)) 
    ndb.delete_multi(QuestionInstance.query().fetch(keys_only=True))
    ndb.delete_multi(State_Questions.query().fetch(keys_only=True))
    ndb.delete_multi(Topic_States.query().fetch(keys_only=True))
    ndb.delete_multi(Question.query().fetch(keys_only=True))
    ndb.delete_multi(State.query().fetch(keys_only=True))
    ndb.delete_multi(Address.query().fetch(keys_only=True))
    ndb.delete_multi(Teacher.query().fetch(keys_only=True))
    ndb.delete_multi(Class.query().fetch(keys_only=True))
    ndb.delete_multi(Assessment_Record.query().fetch(keys_only=True))
    ndb.delete_multi(Student.query().fetch(keys_only=True))
    ndb.delete_multi(UserInfo.query().fetch(keys_only=True))
    ndb.delete_multi(Student_Assessments.query().fetch(keys_only=True))
    ndb.delete_multi(Assessment.query().fetch(keys_only=True))
    ndb.delete_multi(Subject.query().fetch(keys_only=True))
    ndb.delete_multi(Topic_Questions.query().fetch(keys_only=True))
    ndb.delete_multi(State_Questions.query().fetch(keys_only=True))
    ndb.delete_multi(Topic_States.query().fetch(keys_only=True))
    ndb.delete_multi(Subject_Topics.query().fetch(keys_only=True))
    ndb.delete_multi(Student_Assessments.query().fetch(keys_only=True))
    ndb.delete_multi(Topic.query().fetch(keys_only=True))
    ndb.delete_multi(User.query().fetch(keys_only=True))
    ndb.delete_multi(Assessment_Record.query().fetch(keys_only=True))
    