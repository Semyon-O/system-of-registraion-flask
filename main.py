from flask import Flask, render_template, request, url_for, redirect
from modules.database import db, Models
from flask_login import LoginManager, login_user, login_required

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    id_user = db.session.query(Models.Users).get(user_id)
    db.session.close()
    return id_user


@app.route("/", methods=["post", "get"])
def route_login_page():
    return render_template("index.html")


@app.route("/registration", methods=["get", "post"])
def controller_login_page():
    if request.method == "POST":
        Name = request.form.get("fullname")
        Email = request.form.get("email")
        Password = request.form.get("password")
        db.session.add(
            Models.Users(name=Name, email=Email, password=Password)
        )
        db.session.commit()
        db.session.close()
        return render_template("index.html")
    return "error"


@app.route("/auth", methods=["post", "get"])
def controller_auth_page():
    if request.method == "POST":
        Name = request.form.get("username")
        Password = request.form.get("password")

        try:
            res: Models.Users = db.session.query(Models.Users).filter_by(name=Name).one()
            db.session.close()
        except:
            return "Нет такого пользователя ((("

        if res.password == Password:
            login_user(res)
            return redirect(url_for("main_page"))
        else:
            return "Invalid password"
    return redirect(url_for("route_login_page"))


@app.route("/auth/main_page/")
@login_required
def main_page():
    return render_template("main_page.html")


@app.route("/logout")
@login_required
def logout():
    pass




if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
