from flask import Flask, flash, render_template, request, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY']="secretkey"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=True

debug = DebugToolbarExtension(app)


@app.route('/')
def show_starting_page():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('survey.html', title=title, instructions=instructions)

@app.route('/begin', methods=['POST'])
def begin_survey():
    session['RESPONSES_KEY'] = [] 
    return redirect('question/0')

@app.route('/question/<int:id>')
def show_question(id):
    responses = session.get('RESPONSES_KEY', False)
    questions = satisfaction_survey.questions[id]
    if len(responses)!= id:
        flash('Please do not attempt to answer the questions out of order')
        return redirect(f'/question/{len(responses)}')
    
    return render_template('question.html', question=questions, id=id)

@app.route('/answer', methods=['POST'])
def submit_answer():
    choice = request.form['answer']
    responses = session['RESPONSES_KEY']
    responses.append(choice)
    session['RESPONSES_KEY'] = responses
    if len(responses) == len(satisfaction_survey.questions):
        return '<h1>Thank you for completing this survey</h1>'
    else:
        return redirect(f'question/{len(responses)}')

