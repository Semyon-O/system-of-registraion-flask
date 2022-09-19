from flask import (
    Flask,
    flash,
    render_template,
    request
)

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=["post", "get"])
def route_login_page():
    print(request.form.get("username"))
    print(request.form.get("password"))
    flash("Successful")
    return render_template("index.html")


@app.route("/login", methods=["get", "post"])
def controller_login_pae():
    print(request)
    if request.method == "POST":
        print(request.form.get("username"))
        print(request.form.get("password"))
        return "post"
    return "Success"

@app.route("/main_page")
def route_main_page():
    return render_template("main_page.html")


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
