from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from configparser import ConfigParser
from validators import is_valid_name, is_valid_address, is_valid_phone, is_valid_email

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submission', methods=['POST'])
def submission():

    # Get text data
    name = request.form.get("name")
    dob = request.form.get("dob")
    spouse_name = request.form.get("s_name")
    spouse_dob = request.form.get("s_dob")
    address = request.form.get("address")
    phone_number = request.form.get("phone")
    email = request.form.get("email")

    # Validation
    has_error = False
    
    if not is_valid_name(name):
        flash("Invalid format for 'name' field. Accepted characters are A-Z, a-z, hyphens, spaces, and apostrophes.")
        has_error = True
    
    if not is_valid_name(spouse_name, allow_empty=True):
        flash("Invalid format for 'spouse's  name' field. If you leave this field blank, make sure nothing is entered into the box. Accepted characters are A-Z, a-z, hyphens, spaces, and apostrophes.")
        has_error = True

    if not is_valid_address(address):
        flash("Invalid address. Please try again.")
        has_error = True
    
    if not is_valid_phone(phone_number):
        flash("Invalid phone number format. Please try again.")
        has_error = True

    if not is_valid_email(email):
        flash("Invalid email. Please try again.")
        has_error = True
    
    if has_error:
        return redirect(url_for('index'))
    
    # Get image data
    img1 = request.files.get("img1")
    img2 = request.files.get("img2")
    img3 = request.files.get("img3")
    img4 = request.files.get("img4")
    img5 = request.files.get("img5")

    # .ini file used to store sensitive info
    config = ConfigParser()
    config.read('config.ini') #----------------------- CHANGE THIS
    to_address = config['INFO']['email']
    from_address = config['INFO']['email']
    psw = config['INFO']['password']
    host = config['INFO']['host']
    port = config['INFO']['port']

    # Create email body
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = "NEW CUSTOMER INFORMATION"

    fields = [
        ("Name", name),
        ("Date of birth", dob),
        ("Spouse's name", spouse_name),
        ("Spouse's date of birth", spouse_dob),
        ("Address", address),
        ("Phone number", phone_number),
        ("Email", email)
    ]
    lines = [f"{label}: {response}" for label, response in fields if response]
    body = "\n".join(lines)
    full = f"Here is the data from your customer:\n\n{body}"

    msg.attach(MIMEText(full, 'plain'))
    
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
    attach_file(img5)

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