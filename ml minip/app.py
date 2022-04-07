from msilib.schema import Property
from flask import Flask, render_template, request
import pickle
import numpy as np
model = pickle.load(open('travelo.pkl', 'rb'))

app = Flask(__name__)

@app.route('/',methods=['GET'])
def helloworld():
    return render_template('MyTrip.html')

@app.route('/next_predict',methods=['POST'])
def travel():
    CustomerId=request.form['CustomerId']
    ProdTaken=request.form['ProdTaken']
    Age=request.form['Age']
    HowwasCustomerContacted=request.form['How was Customer Contacted']
    CityTire=request.form['City Tire']
    PitchDuration=request.form['Pitch Duration']
    occupation=request.form['occupation']
    gender=request.form['gender']
    NoofTravellers=request.form['No of Travellers']
    Product=request.form['Product']
    PropertyRatings=request.form['Property Ratings']
    MaritalStatus=request.form['Marital Status']
    NoofTripsperYear=request.form['No of Trips per Year']
    Passport=request.form['Passport']
    PitchRatings=request.form['Pitch Ratings']
    Car=request.form['Car']
    NoofChildren=request.form['No of Children']
    designation=request.form['designation']
    MonthlyIncome=request.form['Monthly Income']

    arr = np.array([[CustomerId,ProdTaken,Age,HowwasCustomerContacted,CityTire,PitchDuration,occupation,gender,NoofTravellers,Product,PropertyRatings,MaritalStatus,Passport,PitchRatings,Car,NoofChildren,designation,MonthlyIncome,NoofTripsperYear]])

    pred = model.predict(arr)

    return render_template('next.html', data=pred)



if __name__=='__main__':
    app.run(port=3000,debug=True)