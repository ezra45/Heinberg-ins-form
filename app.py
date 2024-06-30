from flask import Flask, render_template, request, redirect, url_for
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from configparser import ConfigParser

# .ini file used to store sensitive info
config = ConfigParser()
config.read('config.ini') #----------------------- CHANGE THIS
to_address = config['INFO']['email']
from_address = config['INFO']['email']
psw = config['INFO']['password']
host = config['INFO']['host']
port = config['INFO']['port']

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submission', methods=['POST'])
def submission():

    # Get text data
    name = request.form.get("name")
    spouse_name = request.form.get("s_name")
    address = request.form.get("address")
    phone_number = request.form.get("phone")
    email = request.form.get("email")
    
    # Get image data
    img1 = request.files.get("img1")
    img2 = request.files.get("img2")
    img3 = request.files.get("img3")
    img4 = request.files.get("img4")

    # Create email body
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = "Test Email"

    body = f"""\
    This is a test email. Here is the data from your customer:
        
    Name: {name}
    Spouse's name: {spouse_name}
    Address: {address}
    Phone number: {phone_number}
    Email: {email}
    """
    msg.attach(MIMEText(body, 'plain'))
    
    # Function for attaching files to the email
    def attach_file(file):
        if file:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={file.filename}')
            msg.attach(part)

    # Attaching image uploads
    attach_file(img1)
    attach_file(img2)
    attach_file(img3)
    attach_file(img4)

    # Sending mail
    server = smtplib.SMTP(host, port)
    server.starttls()
    server.login(from_address, psw)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()

    return redirect(url_for("thanks"))

@app.route('/thanks')
def thanks():
    return render_template("thanks.html")

if __name__ == '__main__':
    app.run(debug=True) #----------------------- CHANGE THIS