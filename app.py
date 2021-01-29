from flask import Flask,render_template,request
import requests

api_key = "143cb75595d71ef99f425fd491a93b9e"
url = "http://data.fixer.io/api/latest?access_key=" + api_key
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency") #USD
        secondCurrency = request.form.get("secondCurrency") #TRY
        amount = request.form.get("amount") #20
        
        response = requests.get(url) # GET requests atacak eğer çalışıyor ise 200 kodlu response dönecek
        app.logger.info(response)
        
        infos = response.json()
        
        
        firstValue = infos["rates"][firstCurrency] # rates içerisinde get request edilen değerin karşılığını almak için 
        secondValue = infos["rates"][secondCurrency]
        
        result = (secondValue / firstValue) * float(amount)
        
        currencyInfo = dict()
        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency 
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result
        app.logger.info(infos) 
        
        return render_template("index.html",info = currencyInfo)
    else:
        return render_template("index.html")
    

if __name__ == "__main__":
    app.run(debug=True)
    