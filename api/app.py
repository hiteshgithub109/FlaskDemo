#Flask APP Routing
from flask import Flask, render_template, request, redirect, url_for, jsonify
#Create a simple flask application
app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return "<h1>Flask APP is running and this is home page</h1>"

@app.route("/index", methods=['GET'])
def index():
    return "<h1>Flask APP is running and this is index page</h1>"

#Variable Rules: giving parameter to the success page
@app.route("/success/<int:score>")
def success(score):
    # try toggling the comments in both the below lines and note the difference and also remove str() before the score concatenation
    # return f"The person has passed and the score is: {score}"
    return "The person has passed and the score is: " + str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return f"The person has failed and the score is: {score}"
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == "GET":
        return render_template('form.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
        average = (maths + science + history)/3
        res = ""
        if average >= 50:
            res = "success"
        else:
            res = "fail"
        # return render_template('form.html', score = average)
        return redirect(url_for(res, score=average))
    
# to see the result of this function go to postman give url as http://127.0.0.1:5000/api select body>raw>json and then write the json script with a and b keys and then click on send, you will be able to see the output if your server(this script) is running
@app.route("/api",methods=['POST'])
def calculateSum():
    data = request.get_json()
    data_dict = dict(data)
    a_val = data_dict['a']
    b_val = data_dict['b']
    return jsonify(a_val+b_val)
if __name__ == '__main__':
    app.run(debug=True)