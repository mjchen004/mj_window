from flask import Flask,url_for

app = Flask(__name__)
@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login ABC'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profileee'

#程式重新启动的时候执行
with app.test_request_context(): 
    print("执行test_request_context")
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', name='alice', password='12345'))
    print(url_for('profile', username='alice tan'))