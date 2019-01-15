from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    # 这里是demo，实际这么返回响应字符串是不规范的
    return '<h1>Hello World!</h1>'
if __name__ == '__main__':
    app.run(debug=True)