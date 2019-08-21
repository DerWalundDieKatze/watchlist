from flask import Flask

app = Flask(__name__)  # 实例引入的flask对象


@app.route('/')             # 使用url装饰器绑定url
def hello():
    return 'Welcome to My Watchlist!'
