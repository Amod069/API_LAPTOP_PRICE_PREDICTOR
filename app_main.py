
from flask import Flask,request,jsonify
import pickle
import sklearn
import numpy as np
model=pickle.load(open('pipe.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def home():
    return 'PLEASE ADD "/predict" in url to access the api'
@app.route('/predict',methods=['POST'])
def predict():
    company=request.form.get('company')
    type=request.form.get('type')
    ram = request.form.get('ram')
    weight = request.form.get('weight')
    touchscreen = request.form.get('touchscreen')
    ips = request.form.get('ips')
    screensize = request.form.get('screensize')
    resolution = request.form.get('resolution')
    cpubrand = request.form.get('cpubrand')
    hdd = request.form.get('hdd')
    ssd = request.form.get('ssd')
    gpubrand = request.form.get('gpubrand')
    os = request.form.get('os')
    if touchscreen=='YES':
        touchscreen=1
    else:
        touchscreen = 0
    if ips=='YES':
        ips=1
    else:
        ips = 0

    ppi= None
    X_res=int(resolution.split('x')[0])
    Y_res=int(resolution.split('x')[1])
    ppi=(((X_res**2)+(Y_res**2))**0.5)/float(screensize)

    query=np.array([company,type,ram,weight,touchscreen,ips,ppi,cpubrand,hdd,ssd,gpubrand,os])
    query = query.reshape(1,12)
    PREDICTED= str(round(int(np.exp(model.predict(query)))))
    return jsonify({"PRICES": "PREDICTED PRICE IS " +PREDICTED})


if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0')
