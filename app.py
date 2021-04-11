from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Length
import pyrebase

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

config = {
  "apiKey": "AIzaSyDsxuOBeNP8ke-I8BV4PHWHAEAmYP4N_sU",
  "authDomain": "interest-driven-learning.firebaseapp.com",
  "databaseURL": "https://interest-driven-learning-default-rtdb.firebaseio.com",
  "storageBucket": "interest-driven-learning.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

class userSignInForm(FlaskForm): 

    # test = StringField("Hello this is a test input")
    key = StringField( 'Key', [DataRequired()])
    submit = SubmitField('Continue')

class logoutForm(FlaskForm):

    submit = SubmitField('Log Out and Complete Study')

class interestForm(FlaskForm):

    interestChoice = SelectField("Of the provided topics, which interests you the most?",[DataRequired()], choices=[('reading', 'Reading'), ('gaming', 'Playing Video Games'), ('music', 'Playing Or Listening To Music'), ('sports', 'Playing Or Watching Sports'), ('cooking', 'Cooking')])
    readingRate = RadioField("Reading",[DataRequired()], choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)])
    gamingRate = RadioField("Gaming",[DataRequired()], choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)])
    musicRate = RadioField("Music", [DataRequired()],choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)])
    sportsRate = RadioField("Sports", [DataRequired()],choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)])
    cookingRate = RadioField("Cooking",[DataRequired()], choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)])
    submit = SubmitField('Continue')

class superpositionQuiz(FlaskForm):
        
    question1 = RadioField("What is superposition?", [DataRequired()], choices=[(1, 'A. The ability of a particle to amplify or diminish'), (2, 'B. The ability of a particle to exist in multiple states at different times'), (3, 'C. The ability of a particle to exist in the same state at different times'), (4, 'D. The ability for a particle to exist in multiple states at the same time')])
    question2 = RadioField("What advantage does quantum computing offer over classic computing?", [DataRequired()], choices=[(1, 'A. It allows faster processing of zeroes and ones'), (2, 'B. It supports additional binary numbers'), (3, 'C. It can process multiple states in parallel'), (4, 'D. It can run calculations on a remote computer')])
    # question3 = StringField("Please write a brief summary of the science concept discussed in the video.", [DataRequired()])

    submit = SubmitField('Submit Quiz & Continue', render_kw={"onclick": "writeNewPost()"})

class restAPIQuiz(FlaskForm):
        
    question1 = RadioField("What is REST?", [DataRequired()], choices=[(1, 'A. A software used to build websites'), (2, 'B. A design concept used on top of UDP'), (3, 'C. A design concept used on top of HTTP'), (4, 'D. A programming paradigm used on top of JavaScript')])
    question2 = RadioField("Which of the following is not an architectural REST constraint?", [DataRequired()], choices=[(1, 'A. Client-Server'), (2, 'B. Stateless'), (3, 'C. Serverless'), (4, 'D. Layered System')])
    # question3 = StringField("Please write a brief summary of the science concept discussed in the video.", [DataRequired()])

    submit = SubmitField('Submit Quiz & Continue')

class dnsHarvestingQuiz(FlaskForm):
        
    question1 = RadioField("What is Domain Name Service (DNS)?", [DataRequired()], choices=[(1, 'A. A way to set the name of a domain you own'), (2, 'B. A way to translate domain names to IP addresses'), (3, 'C. A way to translate IP addresses to domain names'), (4, 'D. A way to transfer data from one domain to another')])
    question2 = RadioField("Q2. Which one of the following tools does not provide useful information for DNS harvesting?", [DataRequired()], choices=[(1, 'A. nslookup'), (2, 'B. dig'), (3, 'C. WHOIS'), (4, 'D. ipconfig')])
    # question3 = StringField("Please write a brief summary of the science concept discussed in the video.", [DataRequired()])

    submit = SubmitField('Submit Quiz & Continue')

class entaglementQuiz(FlaskForm):
        
    question1 = RadioField("What is entanglement?", [DataRequired()], choices=[(1, 'A. The phenomenon that occurs when two distinct particles collide and entangle with each other'), (2, 'B. The phenomenon that occurs when two particles respond to each other, even when they have no physical connection between them'), (3, 'C. The phenomenon that occurs when two particles react and form a new particle'), (4, 'D. The phenomenon that occurs when two particles interfere with each other')])
    question2 = RadioField("In entanglement, what relationship do the particles have?", [DataRequired()], choices=[(1, 'A. The particles are identical to each other'), (2, 'B. The particles are complements of each other'), (3, 'C. The particles are physically close to each other'), (4, 'D. The particles are in a continual state of motion')])
    # question3 = StringField("Please write a brief summary of the science concept discussed in the video.", [DataRequired()])

    submit = SubmitField('Submit Quiz & Continue')


class cryptographyQuiz(FlaskForm):
        
    question1 = RadioField("What is cryptography?", [DataRequired()], choices=[(1, 'A. Converting cleartext to ciphertext'), (2, 'B. Converting ciphertext to cleartext'), (3, 'C. Converting cleartext to ciphertext, and back to cleartext'), (4, 'D. Converting ciphertext to cleartext, and back to ciphertext')])
    question2 = RadioField("What is the difference between symmetric and asymmetric cryptography?", [DataRequired()], choices=[(1, 'A. Symmetric cryptography can use one or two keys to encrypt and decrypt data'), (2, 'B. Symmetric cryptography uses the same key to encrypt and decrypt data'), (3, 'C. Asymmetric cryptography only uses the RSA protocol'), (4, 'D. Asymmetric cryptography uses the same key to encrypt and decrypt data')])
    # question3 = StringField("Please write a brief summary of the science concept discussed in the video.", [DataRequired()])

    submit = SubmitField('Submit Quiz & Continue')

class cloudQuiz(FlaskForm):
        
    question1 = RadioField("What are the three cloud computing models?", [DataRequired()], choices=[(1, 'A. Infrastructure as a service, Processing as a service, Software as a service'), (2, 'B. Platform as a service, Storage as a service, Software as a service'), (3, 'C. Software as a service, Storage as a service, Infrastructure as a service'), (4, 'D. Software as a service, Infrastructure as a service, Platform as a service')])
    question2 = RadioField("Which of the following is true about Platform as a Service (PaaS)?", [DataRequired()], choices=[(1, 'A. The user needs to manage the platform and applications'), (2, 'B. The user needs to manage the applications only'), (3, 'C. The user needs to manage the platform only'), (4, 'D. The user does not need to manage anything')])
    # question3 = StringField("Please write a brief summary of the science concept discussed in the video.", [DataRequired()])

    submit = SubmitField('Submit Quiz & Continue')

class timerForm(FlaskForm):

    totalTime = StringField("Total Time")



@app.route("/", methods=['GET', 'POST'])
def demographics():

    session['superposition'] = False
    session['restAPI'] = False
    session['dns'] = False
    session['entanglement'] = False
    session['cryptography'] = False
    session['cloud'] = False

    form = userSignInForm()

    if form.validate_on_submit():
        check = db.child(form.key.data).get()
        if check.val() is not None:
            x = check.val()['confirmation']
            print(x)

            if x == 1:
                # user_name = form.key.data
                session['username'] = form.key.data
                session['start'] = db.child(session['username']).get().val()['start']
                print(session['start'])
                form.key.data = ''
                return redirect(url_for('interest_form'))
            else: 
                print(x)
                return render_template("demographics.html", form=form, error=True) 
        else: 
            return render_template("demographics.html", form=form, error=True) 

    return render_template("demographics.html", form=form, error=False) 

@app.route("/interest-form", methods=['GET', 'POST'])
def interest_form():  

    if 'username' in session:
        print(session['username'])

        notify = False

        form = interestForm()
        
        if form.validate_on_submit():
            print("validate")
            interestChoice = form.interestChoice.data
            # interest_choice = interestChoice # for use to pull lessons from database
            session['interest'] = form.interestChoice.data
            readingRate = form.readingRate.data
            gamingRate = form.gamingRate.data
            musicRate = form.musicRate.data
            sportsRate = form.sportsRate.data
            cookingRate = form.cookingRate.data

            i = {
                "interestChoice": interestChoice
            }
            
            db.child(session['username']).update(i)

            data = {
                "readingRate": readingRate,
                "gamingRate": gamingRate,
                "musicRate": musicRate,
                "sportsRate": sportsRate,
                "cookingRate": cookingRate
            }

            db.child(session['username']).child('interests').update(data)
            notify = False
            return redirect(url_for('study_intro'))
        elif request.method == 'POST':
            print("not validate")
            notify = True
            return render_template("interest-form.html", form=form, notify=notify)

        return render_template("interest-form.html", form=form, notify=notify) 
    else:
        return redirect(url_for('demographics'))

@app.route("/part1")
def study_intro():

    if 'username' in session:
        return render_template("study-intro.html", start=session['start'])
    else:
        return redirect(url_for('demographics'))

@app.route("/part2")
def study_break():
    if 'username' in session:
        return render_template("study-break.html", start=session['start'])
    else:
        return redirect(url_for('demographics'))

@app.route("/survey1")
def survey_exp():
    return render_template("survey-exp.html", start=session['start'])

@app.route("/survey2")
def survey_con():
    return render_template("survey-con.html", start=session['start'])

@app.route("/superposition", methods=['GET', 'POST'])
def superposition():

    if 'username' in session:

        form = superpositionQuiz()
        question1 = False
        question2 = False
        # question3 = False

        superLesson = db.child("lessons").child("superposition").child(session['interest']).get().val()
        one_liner = superLesson['one-liner']
        lesson = superLesson['lesson']

        if form.validate_on_submit():

            data = {
                "superpositionQ1": form.question1.data,
                "superpositionQ2": form.question2.data,
                # "superpositionQ3": form.question3.data
            }

            db.child(session['username']).child('experimental').child('superposition').update(data)
            session['superposition'] = True
            session['superpositionData'] = data

            return redirect(url_for('restAPI'))

        if not session['superposition']:
            return render_template("superposition.html", interest=session['interest'], user=session['username'], form=form, sec1=session['superposition'], sec2=session['restAPI'], sec3=session['dns'], one_liner=one_liner, lesson=lesson) # pass lessons and show more into the html 
        else: 
            return render_template("superposition.html", user=session['username'], form=form, sec1=session['superposition'], sec2=session['restAPI'], sec3=session['dns'], one_liner=one_liner, lesson=lesson, formData=session['superpositionData']) # pass lessons and show more into the html 

            
    else:
        return redirect(url_for('demographics'))

@app.route("/restAPI", methods=['GET', 'POST'])
def restAPI():

    if 'username' in session:

        form = restAPIQuiz()

        question1 = False
        question2 = False
        # question3 = False

        restAPILesson = db.child("lessons").child("restapi").child(session['interest']).get().val()
        one_liner = restAPILesson['one-liner']
        lesson = restAPILesson['lesson']

        if form.validate_on_submit():
        
            data = {
                "restQ1": form.question1.data,
                "restQ2": form.question2.data,
                # "restQ3": form.question3.data
            }

            db.child(session['username']).child('experimental').child('restAPI').update(data)
            session['restAPI'] = True

            return redirect(url_for('dnsHarvesting'))

        return render_template("restapi.html", form=form, interest=session['interest'], user=session['username'], sec1=session['superposition'], sec2=session['restAPI'], sec3=session['dns'], one_liner=one_liner, lesson=lesson)
    else:
        return redirect(url_for('demographics'))

@app.route("/DNSHarvesting", methods=['GET', 'POST'])
def dnsHarvesting():

    if 'username' in session:
        form = dnsHarvestingQuiz()

        question1 = False
        question2 = False
        # question3 = False

        dnsLesson = db.child("lessons").child("dns").child(session['interest']).get().val()
        one_liner = dnsLesson['one-liner']
        lesson = dnsLesson['lesson']

        if form.validate_on_submit():

            data = {
                "dnsQ1": form.question1.data,
                "dnsQ2": form.question2.data,
                # "dnsQ3": form.question3.data
            }

            db.child(session['username']).child('experimental').child('dns').update(data)
            session['dns'] = True

            return redirect(url_for('survey_exp'))
            # if session['start'] == 'e':
            #     return redirect(url_for('survey_exp'))
            #     # return redirect(url_for('study_break'))
            # elif session['start'] == 'c':
            #     return redirect(url_for('final_page'))


        return render_template("dns-harvesting.html", form=form, user=session['username'], interest=session['interest'], sec1=session['superposition'], sec2=session['restAPI'], sec3=session['dns'], one_liner=one_liner, lesson=lesson)
    else:
        return redirect(url_for('demographics'))

@app.route("/entanglement", methods=['GET', 'POST'])
def entanglement():

    if 'username' in session:

        form = entaglementQuiz()

        question1 = False
        question2 = False
        # question3 = False

        if form.validate_on_submit():

            data = {
                "entanglementQ1": form.question1.data,
                "entanglementQ2": form.question2.data,
                # "entanglementQ3": form.question3.data
            }

            db.child(session['username']).child('control').child('entanglement').update(data)
            session['entanglement'] = True

            return redirect(url_for('cryptography'))

        return render_template("entanglement.html", form=form, user=session['username'], sec1=session['entanglement'], sec2=session['cryptography'], sec3=session['cloud']) # pass lessons and show more into the html 
    else:
        return redirect(url_for('demographics'))


@app.route("/cryptography", methods=['GET', 'POST'])
def cryptography():

    if 'username' in session:

        form = cryptographyQuiz()

        question1 = False
        question2 = False
        # question3 = False

        if form.validate_on_submit():
        
            data = {
                "cryptographyQ1": form.question1.data,
                "cryptographyQ2": form.question2.data,
                # "cryptographyQ3": form.question3.data
            }

            db.child(session['username']).child('control').child('cryptography').update(data)
            session['cryptography'] = True

            return redirect(url_for('cloud'))

        return render_template("cryptography.html", form=form, user=session['username'], sec1=session['entanglement'], sec2=session['cryptography'], sec3=session['cloud'])
    else:
        return redirect(url_for('demographics'))

@app.route("/cloud", methods=['GET', 'POST'])
def cloud():

    if 'username' in session:
        form = cloudQuiz()

        question1 = False
        question2 = False
        # question3 = False

        if form.validate_on_submit():

            data = {
                "cloudQ1": form.question1.data,
                "cloudQ2": form.question2.data,
                # "cloudQ3": form.question3.data
            }

            db.child(session['username']).child('control').child('cloud').update(data)
            session['cloud'] = True

            return redirect(url_for('survey_con'))
            # if session['start'] == 'e':
            #     return redirect(url_for('final_page'))
            # elif session['start'] == 'c':
            #     return redirect(url_for('study_break'))

        return render_template("cloud.html", form=form, user=session['username'],  sec1=session['entanglement'], sec2=session['cryptography'], sec3=session['cloud'])
    else:
        return redirect(url_for('demographics'))


@app.route("/thank-you", methods=['GET', 'POST'])
def final_page():
    if 'username' in session:
        session.pop('username', None)
        session.pop('interest', None)
        session.pop('superposition', None)
        session.pop('restAPI', None)
        session.pop('dns', None)
        session.pop('entanglement', None)
        session.pop('cryptography', None)
        session.pop('cloud', None)
        return render_template("final-page.html")
    else:
        return redirect(url_for('demographics'))

@app.route("/goodbye")
def goodbye():
    return render_template("goodbye.html")


if __name__ == "__main__":    
    app.run()
