from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/', methods = ['GET','POST'])
def mablibsApp():
    return render_template('index.html',url=url_for('madlibscompleted'))

@app.route('/completed', methods = ['GET', 'POST'])
def madlibscompleted():
    if request.method == 'POST':
        dayoftheweek = request.form['dayoftheweek']
        name = request.form['name']
        place1 = request.form['place1']
        pasttenseverb1 = request.form['pasttenseverb1']
        income = request.form['income']
        noun1 = request.form['noun1']
        place2 = request.form['place2']
        pasttenseverb2 = request.form['pasttenseverb2']
        noun2 = request.form['noun2']
    return render_template('completed.html',url=url_for('madlibscompleted'), dayoftheweek=dayoftheweek, name=name, place1=place1, pasttenseverb1=pasttenseverb1, income=income, noun1=noun1, place2=place2, pasttenceverb2=pasttenseverb2, noun2=noun2)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)    