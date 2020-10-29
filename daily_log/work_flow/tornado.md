# tornado
	提供一个简易的web框架，支持异步高并发
	RequestHandler,Application
	启动一个服务的步骤和过程
		1，主业务函数，一般继承自 web.RequestHandler
		2, 缓存数据服务器 redis
		3, 绑定缓存服务器到主业务函数服务器
		4, 注册主业务函数到handlers， 类型为列表，列表元素0:路径， 1:函数名 2:函数需要的参数
		5,注册到web.Application
	method2:
		define

		1, define 注册函数
		2，options提交和获取函数

#1，tornado 路由，访问不同路径设置方式
	class MainHandler(web.RequestHandler):
		def get(self):
			self.write('hello,world')
	if __name__ == "__main__":
		app = tornado.web.application([(r'/', MainHandler)])
		app.listen(8800)
		ioloop.IOLoop.current().start()

# flask 
	flask 路由使用blueprint方式
	app = Flask(__name__)
	app.route('/', 'POST')
	def ret_index():
		return 'index.html'
	if __name__ == "__main__":
		app.run(host='0.0.0.0',port=8801)


# request and response method
	tirnado 相应请求时通过继承 web.RequestHandler的weite方法响应
	获取参数 self.get_argument(), self.set_cookie(), self.get_cookie()
	响应self.write()
	flask 响应请求时，通过jinjia2模板， 修改其中的部分内容来交互和响应
	获取参数通过request向下变量的形式
	响应通过return，也可以返回字符串，模板文件或其他response对象

	tornado
		class MainHandler(web.RequestHandler):
			def get(self):
				self.write('Hello, world!')
	flask from flask import Flask, request, redirect, url_for
	app = Flask(__name__)
	@app.route('/login', method=['GET','POST'])
	def login():
		if request.method == 'POST':
			return redirect(url_for('index'))
		return "Hello, World"

tornado 
	cookie 来自tornado继承类 tornado.web.RequestHandler
	1, set_cookie   #key, value 分别为需要设置的关键字与值
	2, set_secure_cookie  # 安全cookie设置
	3, 重写RequestHandler的get和post方法，并计数访问次数

# ----------------------------
flask 通过session上下文变量方式呈现
	导入session 包，from flask import session
	session['name'] = request.form['name']   # 从前端html接收name字段值
	session.pop('name'， 'Jack')  #删除name为Jack的session

# -------------------------
	1， 如果API涉及规范为RESTful，考虑使用token
	2，如果API被不同终端使用，cookies受限，推荐token
	3， 如果SPA， 服务端没有渲染，推荐token
	4，其他情况可以使用 cookies 和session

# --------------------------
## 模板
   tornado 没有第三方模板，只有自立模板，UI模块，可以组件化html模板内容

   flask绑定jinjia2模板


