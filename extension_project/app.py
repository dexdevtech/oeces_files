from flask import Flask, render_template, request, jsonify, redirect, url_for, session, send_file
from chat import get_response
from clustering import override_old_excel, cluster
from database_user import get_account
import zipfile
import json

app = Flask(__name__)
app.secret_key = 'helloworldhehe'

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] =  'no-store,no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
        if request.method == 'POST':
            user = request.form['name']
            password = request.form['password']
            if get_account(user, password):
                session['user'] = user
                return redirect(url_for('dashboard'))
        else:
            if 'user' in session:
                return redirect(url_for('dashboard'))
            return render_template('login.html')
        return render_template('login.html')

@app.post('/predict')
def predict():
    text = request.get_json().get('message')
    response = get_response(text)
    message = {'answer': response}
    return jsonify(message)

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/user')
def dashboard():
    if 'user' in session:
        user = session['user']
        return render_template('dashboard_.html', user=user)
    return redirect(url_for('login'))

@app.route('/terms')
def tnc():
    return render_template('tnc.html')

@app.route('/forgot-password')
def forgot_pass():
    return render_template('forgot_pass.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

# ROUTES IN DASHBOARD
@app.route('/traccar')
def traccar():
    return redirect('https://www.traccar.org/')

@app.route('/textit')
def textit():
    return redirect('https://textit.com/msg/')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    override_old_excel()
    cluster(file)

    return redirect(url_for('download_file'))


@app.route('/download')
def download_file():
    file_path1 = 'CLUSTER1.xlsx'  # Replace with the actual path to the file you want to serve for download
    file_path2 = 'CLUSTER2.xlsx'

    zip_filename = 'clusters.zip'
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(file_path1)
        zipf.write(file_path2)

    return send_file(zip_filename, as_attachment=True)

@app.route('/ticket')
def tickets():
    return redirect('https://docs.google.com/spreadsheets/d/1uSvBSBsGLVbyUOUo2_r--8SpI3fDGx1sqCXBPgssy6Q/edit#gid=0')

@app.route('/cluster-subscribers')
def cluster_subscribers():
    return render_template('cluster.html')

@app.route('/contacts')
def contacts():
    return redirect('https://docs.google.com/spreadsheets/d/1ei6CDCUw7Hia3bZh-yziPsD8PWUQBVNG/edit#gid=1750962503')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)












