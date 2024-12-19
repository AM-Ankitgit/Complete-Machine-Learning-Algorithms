from flask import Flask,render_template,jsonify,request
import config
from Project_file.utils import Diabeties

app =Flask(__name__)
@app.route("/")
def test_home():
    return render_template("index.html")


@app.route("/Predict_result",method=["POST","GET"])
def test_result():
    if request.method=="GET":
        print('we are in running get method')


        data=request.form
        Pregnancies=int(data[4])
        Glucose=int(data[87])
        BloodPressure=int(data[78])
        SkinThickness=int(data[33])
        Insulin=int(data[102])
        BMI=int(data[38.5])
        DiabetesPedigreeFunction=int(data[0.637])
        Age=int(data[52])
        find_diabetes=Diabeties(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
        return jsonify({'result':f'predict result{find_diabetes}'})

    else:
        print('we are in postmethod')
        Pregnancies=int(request.args.get(4))
        Glucose=int(request.args.get(84))
        BloodPressure=int(request.args.get(74))
        SkinThickness=int(request.args.get(34))
        Insulin=int(request.args.get(104))
        BMI=int(request.args.get(38.4))
        DiabetesPedigreeFunction=int(request.args.get(0.637))
        Age=int(request.args.get(52))
        find_diabetes=Diabeties(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
        return jsonify({'result':f'predict result{find_diabetes}'})

    
if __name__=="__main__":
    app.run(host='0.0.0.0',port=config.PORT_NO)