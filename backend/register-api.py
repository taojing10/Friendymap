from flask import Flask, render_template, request, url_for


app = Flask(__name__)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        account = user.find_one({'username' : request.form['username']})

        if account:
            error = 'Account already exists !'
        elif not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not email:
            error = 'email is required.'


    return render_template('/register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)