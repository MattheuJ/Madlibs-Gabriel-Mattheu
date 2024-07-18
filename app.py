from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def mablibsApp():
    return render_template('index.html')






#print(f"On one {y}, a man named {name} went to {placeList[random.randint(0,2)]}. 
#      He's retired now, but he {job} for a living, and made ${income} a year. 
#      Now, in his freetime, he likes to dress up as a {dressUpList[random.randint(0,2)]}. 
#      He likes to go to {dressUpList[random.randint(0,2)]} coneventions, which are always hosted in {placeList[random.randint(0,2)]} for some reason. 
#      Last year, at one of the conventions, he was arrested because he {arrest} another convestion goer becuase they were dressed as a {dressUpList[random.randint(0,2)]}.")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)