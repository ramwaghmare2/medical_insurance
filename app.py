import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from utils import MedicalInsurence

########### Initialize the flask app #############
app = Flask(__name__)

########## Homepage #############
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods = ['POST','GET'])
def get_insurence_charges():
    if request.method == 'POST':
        data = request.form
        age = eval(data['age'])
        sex = data['sex']
        bmi = eval(data['bmi'])
        children = eval(data['children'])
        smoker = data['smoker']
        region = data['region']

        print("age, sex, bmi,children,smoker, region",age, sex, bmi,children,smoker, region)
        med_ins = MedicalInsurence(age, sex, bmi,children,smoker, region)
        charges = med_ins.get_predicted_charges()
        return render_template("index.html", charges=charges)
        #return jsonify({"Result": f"Predicted Medical Insurence Charges are : {charges}"})

    else:
        age = eval(request.args.get('age'))
        sex = request.args.get('sex')
        bmi = eval(request.args.get('bmi'))
        children = eval(request.args.get('children'))
        smoker = request.args.get('smoker')
        region = request.args.get('region')

        print("age, sex, bmi,children,smoker, region",age, sex, bmi,children,smoker, region)
        med_ins = MedicalInsurence(age, sex, bmi,children,smoker, region)
        charges = med_ins.get_predicted_charges()
        return render_template("index.html", charges=charges)
        #return jsonify({"Result": f"Predicted Medical Insurence Charges are : {charges}"})

if __name__ == "__main__":
    app.run(debug=True)
