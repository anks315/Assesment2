__author__ = 'ankur'

import  gspread;
import logging
import Query

def login():
    gc =  gspread.login('anks.315@gmail.com', 'ankurjain')
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1Kp_AGK2JW2Yghz0euOHBgxBgP1FW0aPdyxXSiVsDGmE/edit#gid=1399864160')

    worksheet = sh.get_worksheet(0)
    val = worksheet.cell(1, 1).value
    logging.info("worksheet")
    logging.info(val)
    schoolkey = Query.get_school_by_name("CvSchool");
    classdict = Query.get_class_of_school(schoolkey);
    classkey = classdict[className];
    subjectdict = Query.get_subject_details_of_class(classkey);
    subjectkey = subjectdict["subjectname"];
    topickeykey = Query.add_topic_from_excel(schoolkey,"demotopic",[],subjectkey,[],4);
    Query.addQuestion_from_excel(problem_statement,type,choices,answers,schoolkey,topickeykey)