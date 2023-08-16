from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

FAI =Flask(__name__)
@FAI.route('/htmlform',methods=['GET','POST'])
def htmlform():
    if request.method == 'POST':
        fd = request.form
        return str(fd)
    return render_template('htmlform.html')

class NameForm(Form):
    name = StringField(validators=[DataRequired()])
    submit = SubmitField()

@FAI.route('/webform',methods = ['GET',"POST"])
def webform():
    NF = NameForm()
    if request.method == 'POST':
        NFD = NameForm(request.form)
        if NFD.validate():
            return NFD.data
    return render_template('webform.html',NF = NF)

if __name__ == '__main__':
    FAI.run(debug=True)
