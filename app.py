from flask import Flask, render_template, url_for, request, redirect, jsonify, make_response, json

import vicipher

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pltext = request.form['plaintext']
        key = request.form['key']
        print(pltext, key)
        ciphertext = vicipher.encrypt(pltext, key)
        decryptext = vicipher.decrypt(ciphertext, key)
        return render_template('encrp.html',
                               ciphertext=ciphertext,
                               plaintext=pltext,
                               key=key,
                               decryptext=decryptext)

    return render_template('index.html')


@app.route('/encrpd', methods=['POST', 'GET'])
def encrp():
    if 'cit' in request.form:
        ciphertext = request.form['cit']
        key = request.form['key1']
        print(ciphertext, key)
        decrptedtext = vicipher.decrypt(ciphertext, key)
        return render_template('decrpt.html', key=key, deplain=decrptedtext)
    else:
        return render_template('decrpt.html')


if __name__ == "__main__":
    app.run(debug=True)
