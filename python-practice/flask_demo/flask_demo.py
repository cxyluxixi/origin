from flask import Flask,render_template,request,redirect,url_for,abort,make_response
import json
import requests



app = Flask(__name__)

# /hello?uname=123&pass=456
@app.route('/hello')
def hello_flask():
    print(request.args['uname'])
    print(request.args['pass'])
    return 'Hello,flask'

# 通过url <xxx> , 在我们实际输入url的时候，不需要输入<>,直接输入xxx
@app.route('/hello/<name>')
def hello(name):
    return 'hello,'+name

# post方法，先打开html，输入form数据，然后使用html里的按钮post
@app.route('/index')
def index():
    try:
        return render_template('xxx.html')

    except:
        return '网页不存在，404'

# 上面的html，跳转到/login，这里设置methods，多种方法都可以接收
@app.route('/login',methods=['GET','POST'])
def login():
    return '正在登陆'


# 返回页面，用render_template
@app.route('/page')
def return_page():
    print('返回一个页面')
    # 往页面里传信息，直接在render_template 后面传内容msg='context'，也就是**context
    # 然后在对应的html文件里，使用{{msg}} ，呈现内容
    # render_template(template_name_or_list, **context)
    return render_template('echarts.html',msg='用户名或密码错误')


# 向html里传数据，在html里使用jquery，ajax来访问这里的/data_page
@app.route('/data_page')
def data_page():
    name = ['a','b','c','d','e','f','g']
    number = [12,43,56,33,24,67,44]
    return json.dumps({'name':name,'number':number})



# 页面跳转，redirect,url_for
@app.route('/newpage')
def return_url():
    return redirect(url_for('return_page')) # 这里括号里写方法名

# 返回状态码，abort 
@app.route('/error')
def return_error():
    # abort()括号里直接写状态码，不用str
    abort(404)

# 修改response对象的参数，make_response
@app.route('/response')
def return_response():
    r = make_response('xxx')
    r.headers['Content-Type'] = 'text'
    return r

if __name__ == "__main__":
    # 用debug模式，调试，这样每次改了代码可以直接重启
    app.run(debug=1)