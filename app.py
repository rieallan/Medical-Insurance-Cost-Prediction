from flask import Flask,request,render_template,send_file
from prediction import Predictions,PredictionFile
import shutil
import os
import sys



sys.path.append("..")


des = os.path.abspath('templates')

app = Flask(__name__)


@app.route("/")  
def intro():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
def predict():
    if request.method =='POST':
        try:

            age = int(request.form.get("age"))
            sex = request.form.get("sex")
            bmi = float(request.form.get("bmi"))
            child = int(request.form.get("child"))
            smoke = request.form.get("smoke")
            reg = request.form.get("reg")

            p = Predictions(age,sex,bmi,child,smoke,reg)
            predic = p.predict()

            return render_template('results.html',predic=predic)
    
    
        except Exception as e:

            print("The exception has raised",e)
            return "Something went wrong :("

    else:
        return render_template('index.html')




@app.route('/predictfile',methods=['POST'])
def pred_files():
    
    if request.method =='POST':

        try:

            csvfile = request.files["csvfile"].read()
            

            f = PredictionFile(csvfile)
            pfile = f.predictfile()

            dest = os.path.join(des, 'newcsv.csv')

            if os.path.exists(dest):
                os.remove(dest)
                pfile.to_csv(os.path.join(des,'newcsv.csv'))
                

            else:
                pfile.to_csv(os.path.join(des,'newcsv.csv'))

            return render_template('resultfiles.html')

        except Exception as e:

            print("The exception has raised",e)
            return "Something went wrong :(",e
    else:
        return render_template('index.html')


@app.route('/downloads/newcsv',methods=['GET','POST'])
def download_file():
    
    file_path = des + '/' + "newcsv.csv"
    return send_file(file_path)


if __name__ == '__main__':

    app.run(host='127.0.0.1',port=7000,debug=True)
    app.run(debug=True)