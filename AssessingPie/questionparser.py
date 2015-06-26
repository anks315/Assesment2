__author__ = 'ankur'

import  gspread;
import logging

def login():
    gc =  gspread.login('anks.315@gmail.com', 'ankurjain')
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1Kp_AGK2JW2Yghz0euOHBgxBgP1FW0aPdyxXSiVsDGmE/edit#gid=1399864160')
    worksheet = sh.get_worksheet(0)
    val = worksheet.cell(1, 1).value
    logging.info("worksheet")
    logging.info(val)
