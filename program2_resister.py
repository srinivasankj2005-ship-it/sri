from flask import Flask,jsonify
import re

app = Flask(__name__)

def is_vaild_email(email):
    pattern= r'^[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z}{2,}$,
    return re.match(pattern,email)is not None
@app.route('/register',methods=['post'])
def register():
    data = request.get_json()
    name = data.get('name','')
    email = data.get('email','')
    if not name or not email:
        return jsonify({"sucess":False,"message": "Name and email are required"}),400
    if not is_valid_email(email):
        return jsonify({"sucess":False,"message": "Invaild email format"}),400
    return jsonify({"sucess":True,"message": f"User {name} registerd successfully with email {email}"}),400
    
    if __name__== '__main__':
        app.run(debug=True)
