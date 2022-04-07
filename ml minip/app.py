from flask import Flask, render_template, request
import pickle
import numpy as np
model = pickle.load(open('travelo.pkl', 'rb'))

app = Flask(__name__)

@app.route('/',methods=['POST'])
def helloworld():
    return render_template('MyTrip.html')

@app.route('/MyTrip_predict',methods=['POST'])
def insurance():
    Age=request.form['Age']
    MonthlyIncome=request.form['Monthly Income']

    arr = np.array([[Age,MonthlyIncome]])

    pred = model.predict(arr)

    return render_template('next.html', data=pred)



if __name__=='__main__':
    app.run(port=3000,debug=True)