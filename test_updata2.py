from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # 1. 准备数据
    article_title_1 = "我的第一篇笔记"
    article_title_2 = "我的第二篇笔记"

    # 2. 使用多行 f-string (f"""...""") 来构建 HTML
    # f-string 允许你用 {变量名} 的方式直接在字符串中嵌入变量
    # <!DOCTYPE html> 是一个文档类型声明 (Document Type Declaration)。它告诉浏览器，当前页面使用的是 HTML5 规范。务必写上，否则版本会乱，后面加 CSS 布局会有很多坑
    html_context = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Second Brain</title>
    </head>
    <body>
        <h1>My Second Brain</h1>
        
        <div>
            <h2>{article_title_1}</h2>
            <h2>{article_title_2}</h2>
        </div>
    
    </body>
    </html>
    """
    
    return html_context

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)