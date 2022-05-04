from flask import Flask, flash, render_template, request, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY']="secretkey"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=True

debug = DebugToolbarExtension(app)

responses = []
@app.route('/')
def show_starting_page():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('survey.html', title=title, instructions=instructions)

@app.route('/begin', methods=['POST'])
def begin_survey():
    return redirect('question/0')

@app.route('/question/<int:id>')
def show_question(id):
    questions = satisfaction_survey.questions[id]
    return render_template('question.html', question=questions)

@app.route('/answer', methods=['POST'])
def submit_answer_1():   
    return redirect("/question/2")

@app.route('/answer', methods=['POST'])
def submit_answer_2():    
    return redirect("/question/3")