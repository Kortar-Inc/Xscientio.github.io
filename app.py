from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS  # Import CORS from flask_cors

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:62765", "https://xsciento.com"]}}) # Enable CORS for all routes

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Update with your SMTP port
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'kortar.inc@gmail.com'
app.config['MAIL_PASSWORD'] = 'ddou nhxd yyuk ukwj'
app.config['MAIL_DEFAULT_SENDER'] = 'kortar.inc@gmail.com'

mail = Mail(app)

@app.route('/', methods=['POST'])
def send_email():
    data = request.json
    recipient_email = data.get('recipient_email')
    subject = data.get('subject')
    body = data.get('body')

    try:
        # Create a messagegunicorn
        message = Message(subject=subject, recipients=[recipient_email], body=body)

        # Send the email
        mail.send(message)

        return jsonify({'success': True, 'message': 'Email sent successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
