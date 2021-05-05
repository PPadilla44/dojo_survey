from flask import Flask, render_template, redirect, request
app = Flask(__name__)
@app.route("/")
def show_form():
    return render_template("index.html")
@app.route("/result", methods=['POST'])
def show_result():
    print(request.form)
    form_name = request.form['name']
    form_location = request.form['location']
    form_language = request.form['language']
    form_comment = request.form['comment']
    form_radio  = request.form['mood']
    form_check = request.form.getlist('breakfast')
    return render_template("result.html", form_name=form_name, form_location=form_location, form_language=form_language, form_comment=form_comment, form_radio = form_radio, form_check=form_check)
if __name__ == "__main__":
    app.run(debug=True)