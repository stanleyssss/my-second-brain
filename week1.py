from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return """
     <h1>欢迎来到我的第二大脑</h1>
     <p>这是一个记录我所有想法和学习笔记的地方。</p>
     <p>去看看我的其他页面吧：</p>
     <a href="/about">关于我</a>
     <br> <!-- 这个br标签是用来换行的 -->
     <a href="/goals">我的学习目标</a>
     """


@app.route('/about')
def about_page():
    return "About me"


@app.route('/goals')
def goal_page():
    return "My goals"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)