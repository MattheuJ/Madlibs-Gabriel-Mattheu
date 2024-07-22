from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/', methods = ['GET','POST'])
def mablibsApp():
    if request.method == 'POST':
        dayoftheweek = request.form['dayoftheweek']
        noun1 = request.form['noun1']
        place1 = request.form['place1']
        pasttencever1 = request.form['pasttenceverb1']
        income = request.form['income']
        noun2 = request.form['noun2']
        place2 = request.form['place2']
        pasttenceverb2 = request.form['pasttenceverb2']
    return render_template('index.html')
    "On one {day of the week}"





#print(f"On one {y}, a man named {name} went to {placeList[random.randint(0,2)]}. 
#      He's retired now, but he {job} for a living, and made ${income} a year. 
#      Now, in his freetime, he likes to dress up as a {dressUpList[random.randint(0,2)]}. 
#      He likes to go to {dressUpList[random.randint(0,2)]} coneventions, which are always hosted in {placeList[random.randint(0,2)]} for some reason. 
#      Last year, at one of the conventions, he was arrested because he {arrest} another convestion goer becuase they were dressed as a {dressUpList[random.randint(0,2)]}.")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)