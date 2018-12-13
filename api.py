from flask import Flask, jsonify, abort, make_response,render_template,url_for,request,redirect

# Flaskクラスのインスタンスを作成
# __name__は現在のファイルのモジュール名
api = Flask(__name__)

@api.route("/")
def index():
    return render_template('index.html')
# GETの実装
@api.route('/get', methods=['GET'])
def get():
    result = { "greeting": 'hello flask' }
    return make_response(jsonify(result))

@api.route('/posttest',methods = ['POST'])
def posttest():
    print(request.form.getlist('num'))
    print(request.form['action'])
    ans = 0
    for i in request.form.getlist('num'):
        if str.isdecimal(i):
          ans += int(i)
        else:
          return render_template('index.html',message = "数字を入力してください")
    return render_template('kotae.html',kotae = ans)


# エラーハンドリング
@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.run()
