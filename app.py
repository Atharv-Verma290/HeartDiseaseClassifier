from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

def process_class(predicted_class):
   if predicted_class == 0:
      return "No Heart Disease"
   if predicted_class == 1:
      return "Heart Disease"


@app.route('/', methods = ['POST', 'GET'])
def index():
  if request.method == "POST":
    age = int(request.form.get('age'))
    sex = int(request.form.get('sex'))
    chest_pain_type = int(request.form.get('chest_pain_type'))
    resting_bp_s = int(request.form.get('resting_bp_s'))
    cholestrol = int(request.form.get('cholestrol'))

    blood_sugar = int(request.form.get('blood_sugar'))
    if(blood_sugar > 120):
       blood_sugar = 1
    else:
       blood_sugar = 0

    resting_ecg = int(request.form.get('resting_ecg'))
    max_heart_rate = int(request.form.get('max_heart_rate'))
    exercise_angina = int(request.form.get('exercise_angina'))
    oldpeak = float(request.form.get('oldpeak'))
    st_slope = int(request.form.get('ST_slope'))
    
    input_data = [sex,age,chest_pain_type,resting_bp_s,cholestrol,blood_sugar,resting_ecg,max_heart_rate,exercise_angina,oldpeak,st_slope]
    input_data = np.array(input_data)
    input_data = input_data.reshape(1,-1)
    print(input_data.shape)

    #checking the retreived values
    print(f"sex:",sex)
    print(f"age:", age)
    print(f"chest_pain:", chest_pain_type)
    print(f"resting_bp_s:", resting_bp_s)
    print(f"cholestrol:", cholestrol)
    print(f"blood_sugar:", blood_sugar)
    print(f"resting_ecg:", resting_ecg)
    print(f"max_heart_rate:", max_heart_rate)
    print(f"exercise_angina:", exercise_angina)
    print(f"oldpeak:", oldpeak)
    print(f"ST_slope:", st_slope)

    print(input_data.shape)
    classifier = joblib.load("classifier.joblib")
    predicted_class = int(classifier.predict(input_data))
    print(predicted_class)

    return render_template('result.html',predicted_class = process_class(predicted_class))
  else:
    return render_template('homepage.html')


if __name__ == '__main__':
    app.run(debug=True)
