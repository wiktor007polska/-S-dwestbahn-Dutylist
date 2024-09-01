from flask import Flask, request, redirect, url_for, session, render_template, flash

app = Flask(__name__)
app.secret_key = '742345123441'  # Replace with a strong, random secret key

# Dummy user credentials
User_Password = [
    ("Guest", "1234"),
    ("wiktor007polska", "SWB123"),
    ("Staff", "ILSWB2.6"),
    ("Finnisthebestname", "Calibra.01")
]

def check_credentials(username, password):
    return (username, password) in User_Password

@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("logged_in"):
        return redirect(url_for("main"))
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if check_credentials(username, password):
            session["logged_in"] = True
            session["username"] = username
            return redirect(url_for("main"))
        else:
            flash("Username or Password is incorrect.", "error")
    
    return render_template("index.html")

@app.route("/main", methods=["GET"])
def main():
    if not session.get("logged_in"):
        return redirect(url_for("index"))
    return render_template("main.html", username=session["username"])

@app.route("/logout", methods=["GET"])
def logout():
    session.pop("logged_in", None)
    session.pop("username", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
