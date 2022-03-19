from flask import Flask, render_template, redirect, request, session, url_for
from db import Actions, config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sUpErSeCrEtKeY'
execute = Actions(config)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = request.form.to_dict()
    if 'name' in form and 'birthday' in form and 'gender' in form:
        session['name'] = name = form['name']
        session['birthday'] = birthday = form['birthday']
        session['gender'] = gender = form['gender']
        session['spot'] = spot = execute.new_spot()
        execute.new_entry(name, birthday, gender, spot)
        return redirect('/queue')

    return render_template('login.html')


@app.route('/queue')
def queue():
    name = session['name']
    session['spot'] = execute.get_spot(name)
    infront = execute.total_infront(name)
    if session['spot'] is not None:
        return render_template('queue.html', name=session['name'], spot=session['spot'][0], total_infront=infront)

    return render_template('queue.html', name=name, spot=1, total_infront=infront)


@app.route('/leave')
def leave():
    if 'name' in session:
        name = session['name']
        spot = session['spot']
        execute.leave(name, spot)
        for i in list(session.keys()):
            session.pop(i, None)

        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
