from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('bank_web.html')
    
@app.route('/main_page', methods=['GET', 'POST'])
def main_page():
    return render_template('main_page.html')