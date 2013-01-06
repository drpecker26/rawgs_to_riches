import market
from flask import Flask, session, render_template, request, redirect, url_for, flash
app = Flask(__name__)

@app.route('/')
def index():
    player = None
    if 'username' in session and session['username'] in market.players: # TODO: this should be two separate cases
        player = market.players[session['username']]
    return render_template('index.html', player=player)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if not username: # empty string is not allowed
            flash('Invalid username.')
            return redirect(url_for('login'))
        try:
            market.add_player(username)
        except KeyError:
            flash('That username is already taken.')
            return redirect(url_for('login'))
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    # request.method == 'GET'
    if 'username' in session: # already logged in
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
