from flask import Flask
import flask


app=Flask(__name__)

@app.route('/',methods=['POST'])
def data_get():
    try:
        # get请求，用flask.request.args.get ,post请求用form.gets
        # 或者统一用flask.request.values.get
        id = flask.request.form.get('id') if 'id' in flask.request.form else ''
        password = flask.request.form.get('password')if 'password' in flask.request.form else ''
        str1 = id +',' + password
        return str1
    except Exception as err:
        return str(err)
    
if __name__ == "__main__":
    app.run()