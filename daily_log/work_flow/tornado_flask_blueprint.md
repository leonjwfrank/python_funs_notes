# BluePrint
	视图是一个应用对请求进行响应的函数。
	Flask可以通过模型把进来的请求URL匹配到对应的处理视图，视图返回数据，Flask把数据变成出去的响应。Flask也可以反过来，根据视图名称和参数生成URL
## 创建蓝图
	Blurprint是 组织一组相关视图及其他代码的方式。与把视图及其他代码直接注册到应用的方式不同，
	蓝图方式是 把视图和其他代码 注册到蓝图，然后在工厂函数中把蓝图注册到应用。

	Flaskr有两个蓝图，一个用于认证功能，另一个用于博客帖子管理。
	每个蓝图代码都在一个单独模块中。

### 创建一个api蓝图
	api = Blueprint('api', __name__, url_prefix='/api')

	# 绑定到函数
	@api.route('/posts/')
	def get_posts():
    	return 'posts api success'


