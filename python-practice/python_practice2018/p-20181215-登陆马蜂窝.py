import requests


def mafengwo_login():
    passport=input('输入用户名，邮箱或手机号')
    password = input('输入密码')
    print('start to login 马蜂窝')
    post_data = {
        'passport':passport,
        'password':password,
        'code':''
    }
    response = mafengwoSession.post('https://passport.mafengwo.cn/login/',data = post_data, headers= header)
    print(response.status_code)
    mafengwoSession.cookies.save()

def loginState():
    checkLogState = "http://www.mafengwo.cn/plan/route.php"
    loginRes = mafengwoSession.get(checkLogState,headers=header,allow_redirects = False) 
    if loginRes.status_code != 200:
        return False
    else:
        return True

if __name__ == "__main__":
    # python2 和 python3的兼容代码
    try:
        # python2 中
        import cookielib
        print(f"user cookielib in python2.")
    except:
        # python3 中
        from http.cookiejar import LWPCookieJar 
        print(f"user cookielib in python3.")
    # session代表某一次连接
    mafengwoSession = requests.session()
    # 因为原始的session.cookies 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法。
    mafengwoSession.cookies = LWPCookieJar(filename='mafengwoCookies.txt')

    header = {
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'referer':'https://passport.mafengwo.cn/',
    }
    try:
        mafengwoSession.cookies.load('mafengwoCookies.txt')
    except:
        mafengwo_login()
        mafengwoSession.cookies.load('mafengwoCookies.txt')
    isLogin = loginState()
    if isLogin == False:
        print('登陆失败，重新输入用户名和密码')
        mafengwo_login()
    else:
        print('登陆成功，保存cookie')
        resp = mafengwoSession.get("http://www.mafengwo.cn/plan/fav_type.php", headers = header, allow_redirects = False)
        mafengwoSession.cookies.save()
        print(resp.status_code)
    

