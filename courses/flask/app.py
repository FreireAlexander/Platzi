from flask import Flask, render_template
from markupsafe import escape

app = Flask("Web App")

user_1 = {
    'name': 'Freire',
    'surname': 'Palomino',
    'role': 'administrator', 
    'id': 1001123456,
    'acount': 0,
    'badges': ['python', 'java', 'c++']
}
users=[
    user_1, 
    {
        'name': 'Alexander',
        'surname': 'Palma',
        'role': 'Chief Leader', 
        'id': 1009923456,
        'acount': 0,
        'badges': ['python', 'java', 'Linux']
    }
]

@app.route("/home/<userName>")
def personalPage(userName):
    notFound = {
        'name': 'NOT FOUND',
        'surname': '',
        'role': '', 
        'id': None,
        'acount': None,
        'badges': []
    }
    res = None
    for user in users: 
        if str(user['name']).lower() == str(userName).lower():
            res = user
    
    if res:
        return render_template('personalPage.html', user=res)
    else:
        return render_template('personalPage.html', user=notFound)


@app.route('/team')
def teamPage():
    return render_template('teamPage.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
