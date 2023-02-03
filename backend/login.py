from flask import *

app = Flask(__name__)


# @app.route("/registration")
# def reg():
#     return "Registration Page"

@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login", methods = ["POST"])
def login():
    if request.method == 'POST':
        #接收用户名和密码
        name = request.form["user"]
        pwd = request.form["password"]
        #若用户名及密码正确，跳转welcome.html页面
        #两组数据进入数据库检验，返回存在/不存在 
        # if name == 'lexi' and pwd == '123': 
        if getmessage(name, pwd):
            return render_template("welcome.html")
        else:
            return render_template("404.html")
    else:
        return render_template("404.html")



if __name__ == '__main__': #只有在run(not import) main.py的时候才会执行下一行
    app.run() 
