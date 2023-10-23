from flask import Flask,render_template,request,redirect,url_for,jsonify

## create simple flask app
app=Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "welcome the channel"


@app.route("/index",methods=["GET"])
def index():
    return "welcome the index page"

##variable rule
@app.route("/success/<int:score>")
def success(score):
    return "the person has passed and the score is " + str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "the person has failed and the score is " + str(score)

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
        maths=float(request.form['Maths'])
        science=float(request.form['Science'])
        history=float(request.form['History'])

        average_marks=(maths+science+history)/3

        if average_marks>=50:
            res='success'
        else:
            res='fail'
        
        return redirect(url_for(res,score=average_marks))

       ## return render_template('form.html',score=average_marks)


@app.route('/api',methods=['POST'])
def calculate_sum():
    data=request.get_json()
    a_val=float(dict(data)['a'])
    b_val=float(dict(data)['b'])

    return jsonify(a_val+b_val)




if __name__=="__main__":
    app.run(debug=True)