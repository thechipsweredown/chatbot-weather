from flask import session

location = session['location'];
time = session['time'];
weather = session['weather'];

def is_yes_no_question(message):
    # check whether message is yes no question
    pass
