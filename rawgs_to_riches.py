import market
from flask import Flask, session, render_template, request, redirect, url_for, flash
app = Flask(__name__)

# Sam's first comment

@app.route('/')
def index():
    """the homepage"""
    player = None
    if 'username' in session:
        if session['username'] not in market.players:
            flash('Invalid username. You have been logged out')
            return redirect(url_for('logout'))
        player = market.players[session['username']]
    return render_template('index.html', player=player)

@app.route('/update', methods=['GET', 'POST'])
def update():
    """update a player's info"""
    if 'username' not in session:
        flash('You must log in first.')
        return redirect(url_for('login'))
    if session['username'] not in market.players:
        flash('Invalid username. You have been logged out')
        return redirect(url_for('logout'))
    player = market.players[session['username']]
    try:
        player.update(**{field: int(request.form[field]) for field in ['rawg_demand', 'rawg_price', 'rig_supply', 'rig_price']})
    except ValueError as e:
        flash(e.message)
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if not username: # empty string is not allowed
            flash('Invalid username.')
            return redirect(url_for('login'))
        if username in market.players:
            flash('That username is already taken.')
            return redirect(url_for('login'))
        else:
            market.add_player(username)
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

# Build in a troubleshooting page.
@app.route('/troubleshoot')
def troubleshoot():
    wholemarket = market
    return render_template('troubleshoot.html',market = wholemarket)


if __name__ == '__main__':
    import os
    app.secret_key = os.urandom(24)
    app.debug = True
    app.run()
