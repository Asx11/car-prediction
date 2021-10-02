
from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)  
model  = pickle.load(open('model.pkl', 'rb')) 
scalerX = pickle.load(open('scalerX.pkl', 'rb'))
scalery = pickle.load(open('scalery.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
    

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        wheelbase = float(request.form['wheelbase'])
        carlength = float(request.form['carlength'])
        carwidth = float(request.form['carwidth'])
        carheight = float(request.form['carheight'])
        curbweight = int(request.form['curbweight'])
        enginesize = int(request.form['enginesize'])
        boreratio = float(request.form['boreratio'])
        stroke = float(request.form['stroke'])
        compressionratio = float(request.form['compressionratio'])
        horsepower = int(request.form['horsepower'])
        peakrpm = int(request.form['peakrpm'])
        citympg = int(request.form['citympg'])
        highwaympg = int(request.form['highwaympg'])

        cylindernumber = request.form['cylindernumber']
        cylindernumber_two = 0
        cylindernumber_eight= 0
        cylindernumber_five= 0
        cylindernumber_four= 0
        cylindernumber_six= 0
        cylindernumber_three= 0
        cylindernumber_twelve= 0

        if cylindernumber == '2':
            cylindernumber_two = 1
        elif cylindernumber == '3' :
            cylindernumber_three= 1           
        elif cylindernumber == '4' :
            cylindernumber_four= 1
        elif cylindernumber == '5' :
            cylindernumber_five= 1 
        elif cylindernumber == '6' :
            cylindernumber_six= 1
        elif cylindernumber == '8' :
            cylindernumber_eight= 1
        else :
            cylindernumber_twelve= 1

        enginetype = request.form['enginetype']
        enginetype_dohc = 0
        enginetype_dohcv= 0
        enginetype_ohc= 0
        enginetype_ohcv= 0
        enginetype_ohcf= 0
        enginetype_rotor= 0
        enginetype_l= 0

        if enginetype == 'dohc':
            enginetype_dohc = 1
        elif enginetype == 'dohcv' :
            enginetype_dohcv= 1           
        elif enginetype == 'ohc' :
            enginetype_ohc= 1
        elif enginetype == 'ohcv' :
            enginetype_ohcv= 1 
        elif enginetype == 'ohcf' :
            enginetype_ohcf= 1
        elif enginetype == 'rotor' :
            enginetype_rotor= 1
        else :
            enginetype_l= 1

        fuelsystem = request.form['fuelsystem']
        fuelsystem_idi = 0
        fuelsystem_mfi = 0
        fuelsystem_1bbl = 0        
        fuelsystem_2bbl = 0
        fuelsystem_4bbl = 0
        fuelsystem_mpfi = 0
        fuelsystem_spdi = 0
        fuelsystem_spfi = 0
        
        if fuelsystem == 'idi':
            fuelsystem_idi = 1
        elif fuelsystem == 'mfi' :
            fuelsystem_mfi= 1           
        elif fuelsystem == '2bbl' :
            fuelsystem_2bbl = 1
        elif fuelsystem == '1bbl' :
            fuelsystem_1bbl = 1 
        elif fuelsystem == '4bbl' :
            fuelsystem_4bbl= 1
        elif fuelsystem == 'mpfi' :
            fuelsystem_mpfi= 1
        elif fuelsystem == 'spdi' :
            fuelsystem_spdi= 1
        else :
            fuelsystem_spfi == 1
        
        carbody = request.form['carbody']
        carbody_convertible= 0
        carbody_hardtop= 0
        carbody_hatchback= 0
        carbody_sedan= 0
        carbody_wagon= 0
       
        if carbody == 'convertible':
            carbody_convertible= 1           
        elif carbody == 'hardtop':
            carbody_hardtop= 1
        elif carbody == 'hatchback':
            carbody_hatchback= 1
        elif carbody == 'sedan':
            carbody_sedan= 1
        else:
            carbody_wagon= 1

        fueltype = request.form['fuelType']
        if fueltype == 'diesel':
            fueltype_diesel= 1
            fueltype_gas= 0
        else:
            fueltype_diesel= 0
            fueltype_gas= 1

        aspiration = request.form['aspiration']
        if aspiration == 'std':
            aspiration_std= 1
            aspiration_turbo= 0
        else:
            aspiration_std= 0
            aspiration_turbo= 1

        doornumber = request.form['doornumber']
        if doornumber == 'four':
            doornumber_four= 1
            doornumber_two= 0
        else:
            doornumber_four= 0
            doornumber_two= 1

        enginelocation = request.form['enginelocation']
        if enginelocation == 'four':
            enginelocation_front= 1
            enginelocation_rear= 0
        else:
            enginelocation_front= 0
            enginelocation_rear= 1

        drivewheel = request.form['drivewheel']
        if drivewheel == '4wd':
            drivewheel_4wd= 1
            drivewheel_fwd= 0
            drivewheel_rwd= 0
        
        elif drivewheel== 'fwd':
            drivewheel_4wd= 0
            drivewheel_fwd= 1
            drivewheel_rwd= 0
        else:
            drivewheel_4wd= 0
            drivewheel_fwd= 0
            drivewheel_rwd= 1
        

        
        categ = [fueltype_diesel, fueltype_gas, aspiration_std, aspiration_turbo, doornumber_four, 
        doornumber_two, carbody_convertible, carbody_hardtop, carbody_hatchback, carbody_sedan, carbody_wagon, drivewheel_4wd, 
        drivewheel_fwd, drivewheel_rwd,enginelocation_front, enginelocation_rear, enginetype_dohc,enginetype_dohcv, enginetype_l, 
        enginetype_ohc, enginetype_ohcf, enginetype_ohcv, enginetype_rotor, cylindernumber_eight,cylindernumber_five, 
        cylindernumber_four, cylindernumber_six, cylindernumber_three, cylindernumber_twelve, cylindernumber_two, fuelsystem_1bbl,
        fuelsystem_2bbl, fuelsystem_4bbl, fuelsystem_idi, fuelsystem_mfi, fuelsystem_mpfi,fuelsystem_spdi, fuelsystem_spfi]        
        
        num = [wheelbase, carlength, carwidth, carheight, curbweight,enginesize, boreratio, stroke, compressionratio, 
        horsepower, peakrpm, citympg, highwaympg]
        
        
        
        df_num=pd.Series(num)        
        df_categ=pd.DataFrame(categ)
        #scaler.fit(df_num.values.reshape(-1, 1))
        numscal=pd.DataFrame(scalerX.transform(df_num.values.reshape(1, -1)))
        input=pd.concat([df_categ.T,numscal],axis=1).values
       
        
    
        prediction = model.predict(input)       
        #numscal.insert(13,'price',prediction[0])
        #output = abs(scalery.inverse_transform(numscal)[:,13:][0][0]).round(2)
        output = abs(scalery.inverse_transform(prediction[0])).round(2)

        return render_template('index.html', prediction_text='We predict price at  {} '.format(output[0])) 
 

if __name__ == '__main__':
    app.run(debug=True)

