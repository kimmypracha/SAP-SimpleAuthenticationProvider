from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("POSTGRES_URI")
db = SQLAlchemy(app)

class UserID(db.Model):
    __tablename__ = "userid"
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(255))
    def __init__(self, p_uid, p_username, p_password):
        self.uid = p_uid
        self.username = p_username
        self.password = p_password

@app.route('/signup',methods=["POST"])
def reg():
    if request.method == "POST":
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        uid = db.session.query(UserID).count()
        print("Here is commit data:")
        print(username, password)
        if not db.session.query(UserID).filter(UserID.username == username).count():
            newUser = UserID(uid,username,password)
            db.session.add(newUser)
            db.session.commit()
            return {
                "status" : 200,
                "message" : "Account Signup successfully!"
            }
        return {
            "status" : 400,
            "message" : "The username is already exists!"
        }

@app.route('/signin',methods=["POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        res = db.session.query(UserID).filter(UserID.username == username).all()
        if len(res) == 0:
            return {
                "status" : 400,
                "message" : "Invalid username or password"
            }
        else:
            print("Here is a result:")
            print(res[0].password, password)
            if res[0].password == password:
                return {
                    "status" : 200,
                    "message" : "Login successfully",
                    "uid" : res[0].uid
                }
            else:
                return {
                    "status" : 400,
                    "message" : "Invalid username or password"
                }
if __name__ == "main":
    app.run(debug=True)

#What we have to do now is only install and try to create the db and test it! 