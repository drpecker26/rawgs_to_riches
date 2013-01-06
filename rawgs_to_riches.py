from flask import Flask, session, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', username=session['username'] if 'username' in session else None)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    import os
    app.secret_key = os.urandom(24)
    app.debug = True
    app.run()
