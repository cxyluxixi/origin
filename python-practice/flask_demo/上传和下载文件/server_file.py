import flask 
from flask import Flask
import os

app = Flask(__name__)

@app.route('/download')
def file_get():
    if 'filename' not in flask.request.values:
        return '图片.jpg'

    else:
        data = b''
        try:
            filename = flask.request.values.get('filename')
            print(filename)
            # 这里的filename文件要和终端地址在同一个文件下，不然找不到filename图片文件
            if filename != '' and os.path.exists(filename):
                fileobj = open(filename,'rb')
                data = fileobj.read()
                fileobj.close()
        except Exception as err:
            data = str(err).encode()
        return data

@app.route('/upload',methods =['POST','GET'])
def upload_file():
    try:
        if 'filename' in flask.request.values:
            filename = flask.request.values.get('filename')
            data = flask.request.get_data()
            fileup = open('upload'+filename,'wb')
            fileup.write(data)
            fileup.close()
            return 'finish'
        else:
            return '没有按要求上传文件'
    except Exception as err:
        return str(err)



if __name__ == "__main__":
    app.run()