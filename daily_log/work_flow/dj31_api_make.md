
#1， linux 环境及项目创建
   安装python3，django
   apt install python3 && pip install django ~=3.1.0
   make code && cd code
   make library && library
   django-admin startproject config .   # 初始化项目
    
   # 文件解释

	    __init__.py # 创建初期为空文件，有此文件的 文件夹被视为一个 python包
		asgi.py  # 异步网关服务接口
		settings.py # 包含项目的所有配置
		urls.py  # 顶层 页面路由 控制
		wsgi.py #  代表Web服务器网关接口 并帮助 Django服务最终的网页
		manage.py # 执行各种Django命令，例如运行本地Web服务器或创建新应用。

	# 如果远程开发，需要添加 本地机器ip 或域名到允许列表
	    config/setting.py  # ALLOWED_HOSTS = ["127.0.0.1"]
	python manage.py migrate   # 环境创建
	python manage.py runserver 0.0.0.0:1999   # 在1999端口启动服务

	python manage.py startapp books    # 创建一个app 应用
	# 文件解释，创建的应用books 包含6个文件
		admin.py # 内置的Django 应用程序Admin的配置文件
		apps.py # 是应用本身的配置文件
	    migrations/ #目录存储迁移文件以进行数据库更改
		models.py #  定义数据库模型的地方
		tests.py # 应用测试文件
        views.py # 处理Web应用程序的请求/响应逻辑的地方

#2， 将app 构建为整体web应用
	# 1，在config/setting 添加新的app到配置项 INSTALLED_APPS configuration
	# 2，数据库，视图，连接，模板  数据库创建及管理员 
	    books/models.py
	    from django.db import models

		# Create your models here.
		class Book(models.Model):
		    title = models.CharField(max_length=250)
		    subtitle = models.CharField(max_length=250)
		    author = models.CharField(max_length=100)
		    isbn = models.CharField(max_length=13)
		    def __str__(self):
		        return self.title

	   编辑模型models.py后 执行更新  
	   python manage.py makemigrations books && python manage.py migrate
      管理员创建
      python manage.py createsuperuser
         username: admin
         password: admin123

	# 3, 配置注册应用程序
		from .models import Book
		admin.site.register(Book)
    
      配置注册后需要重启服务
      python manage.py runserver 0.0.0.0:1999   # 在1999端口启动服务
    
    #在/admin 管理页面创建一本书，
     通常将其显示为网页，表示 创建4个文件 
     books/views,# 控制如何显示 数据库中的数据，如果是列表形式则使用默认的ListView
     config/urls, # 用户访问页面时，将首先与此互动 
     books/urls  # 与config/urls 互动后 将到达这里，使用BookListView 在此视图文件中，Book模型与ListView一起使用以列出所有书籍
     books/template 
       # 最后一步是创建我们的模板文件，以控制实际网页上的布局。
		我们已经在视图中将其名称指定为book_list.html。它有两个选择位置：默认情况下，Django模板加载器会在位置：books/templates/books/book_list.html。
		我们也可以创建一个单独的改为在项目级别的模板目录中更新我们的config/settings.py文件以指向该目录


     # 代码
     cat books/views.py
		from django.shortcuts import render

		# Create your views here.
		from django.views.generic import ListView
		from .models import Book
		class BookListView(ListView):
		    model = Book
		    template_name = 'book_list.html'

     config/urls.py
     	from django.contrib import admin   # 如果用户访问 路由 /admin/ 则访问这个默认app admin
		from django.urls import path, include #include 将使用自定义的app books
		urlpatterns = [
		    path('admin/', admin.site.urls),
		    path('', include('books.urls')),  # 根路径为 books 路由
		]

	cat books/urls.py
		from django.urls import path
		from .views import BookListView

		urlpatterns = [
		    path('', BookListView.as_view(), name='home'),
		]
	
	vim books/templates/books/book_list.html
    
		<h1>All books</h1>
		{% for book in object_list %}
		<ul><li>Title: {{ book.title }}</li> 
		<li>Subtitle: {{ book.subtitle }}</li> 
		<li>Author: {{ book.author }}</li> 
		<li>ISBN: {{ book.isbn }}</li>
		</ul>
		{% endfor %}

	# 重启服务，并访问根路径将列出所有图书 http://127.0.0.1:1999/	



#3， 创建api服务
	
	安装 库 pip install djangorestframework~=3.11.0

	api 返回的数据为json格式， 我们的API将公开一系列端点，该端点在JSON中列出所有书籍。
	所以据此需要新的URL路由，新的视图，新的序列化文件  URL   view   serializer file。
	可以通过多种方式来组织这些文件，但是我的首选方法是创建专用的api应用
	这样可以保证扩展性。即使我们将来添加更多应用，每个应用仍可以包含专用网页所需的模型，视图，模板和url
	整个项目将保存在专用的api应用程序中的  API专用文件
	创建 api 应用
	python manage.py startapp api

	注册应用
	INSTALLED_APPS = ['api.apps.ApiConfig',
    				'books.apps.BooksConfig',   # 如果添加了这一行，就不能再添加 books，相互冲突
    				...
    				'books'   # 与之上的'books.apps.BooksConfig'冲突
    				]
    没有数据库改动，就不需要执行 python manage.py makemigrations  && python manage.py migrate

    # api应用的urls
    定义顶层路由 路径 形如： api/

    config/urls.py  添加路径 # 
		urlpatterns = [path('api/', include('api.urls')), ...# new]

	api/urls.py # 添加路径
		from django.urls import path
		from .views import BookAPIView
		urlpatterns = [
			path('', BookAPIView.as_view()),
		]	

	# api 应用的 Views 将依赖 django-restframwork的 内建视图
	内建rest视图故意模仿传统Django基于类的通用视图的格式，但是它们并不一样
	为了在调用api视图时，不至于混淆框架视图文件views.py， 
		# api/views.py
		from rest_framework import generics   # class of views,
		from books.models import Book        # 
		from .serializers import BookSerializer  # 序列化处理
		class BookAPIView(generics.ListAPIView):
			queryset = Book.objects.all()
			serializer_class = BookSerializer

    # 序列化处理，创建serializers.py
    touch api/serializers.py
	    from rest_framework import serializers
		from books.models import Book
		class BookSerializer(serializers.ModelSerializer):
			class Meta:
				model = Book
				fields = ('title', 'subtitle', 'author', 'isbn')


	# 访问
	指令：curl 127.0.0.1:1999/api/
	通过url 127.0.0.1:1999/api/ 。 可以发现有一个此页面中内置的许多功能，比如可视化


#4 后端Todo API 与 React 前端配合  

     清晰的看见 后端api 与 react融合
#4.1
     后端环境初始化，如果需要在新建的backend 虚拟化环境进行操作，重新安装django，否则django-admin 无效
     pip install install django~=3.1.0
     django-admin startproject config .
 
     python manage.py startapp todos
     python manage.py migrate

     # 注册到全局配置
     config/setting.py
     	# Local
		INSTALLED_APPS = ['todos', # new]

     创建models
     # todos/models.py
		from django.db import models
		class Todo(models.Model):
			title = models.CharField(max_length=200)
			body = models.TextField()
			def __str__(self):
				return self.title
	
	# 更新库,创建迁移。
	# 生成的单个迁移文件将包含两个应用程序上的数据。这只会增加调试难度。尽量减少迁移
	python manage.py makemigrations todos
	python manage.py makemigrations  # 不指定app时，将迁移所有有改动的app
	python manage.py migrate  

	如果我们进入管理员不会立即显示我们的Todos应用程序。我们需要更改todos/admin.py文件如下
	创建3个todos，然后为它们创建 web 页面，这需要新建 urls，views，templates

	# 注册应用
	INSTALLED_APPS = [ # 3rd party
					'rest_framework',
					'todos', 
						]

	# 设置权限为 允许全部
	隐式设计默认设置是为了使开发人员可以进入并开始在本地快速工作开发环境。但是，默认设置不适用于生产。所以
	通常，我们会在项目过程中对它们进行一些更改
	# new
	REST_FRAMEWORK = { 'DEFAULT_PERMISSION_CLASSES': [
				'rest_framework.permissions.AllowAny', ] }

	AllowAny是其中之一，这意味着当我们显式设置它时，与上面的操作一样，其效果与没有DEFAULT_PERMISSION_CLASSES配置的情况完全相同 。
	
	后端api服务 需要三个部分 urls.py, views.py, and serializers.py
	不需要 template

##4.2 urls, views, serializers
	
	全局urls
	# config/urls.py
		from django.contrib import admin
		from django.urls import include, path # new
			urlpatterns = [
				path('admin/', admin.site.urls),
				path('api/', include('todos.urls')), # new
				]
	应用app的 路由配置
	# todos/urls.py
		from django.urls import path
		from .views import ListTodo, DetailTodo
		urlpatterns = [
				path('<int:pk>/', DetailTodo.as_view()),
				path('', ListTodo.as_view()),
		]

	# 我们引用的还有两个尚未创建的视图：ListTodo和DetailTodo。
	但是，路由已完成。空字符串''处将有所有待办事项的列表，其他api/上的单词。每个待办事项都将在其主键上可用，这是一个值Django会在每个数据库表中自动设置。第一个条目是1，第二个条目是2，依此类推。因此，我们的第一个待办事项最终将位于API端点api/1/

	现在，我们需要将模型中的数据转换为JSON，在URL上输出。因此，我们需要一个序列化器
	restful框架有强大的内建序列化类 serializers  

    # todos/serializers.py
		from rest_framework import serializers
		from .models import Todo
		class TodoSerializer(serializers.ModelSerializer):
			class Meta:
				model = Todo
				fields = ('id', 'title', 'body',)

    我们正在指定要使用的模型以及具体的我们要公开的字段。请记住，id是由Django自动创建的，因此我们没有
    必须在我们的Todo模型中定义它，但是我们将在细节视图中使用它。

    # Views
    views.py 在 django中 是将数据发送到 templates，在rest框架中 其值将被发送到序列化操作类中
    Django REST Framework视图的语法故意与常规Django视图非常相似就像常规Django一样，Django REST Framework附带了通用视图以供通用案件。这就是我们在这里使用的。

    我们将使用两个视图来展示数据 ListAPIView  显示所有的 todos ，  
    RetrieveAPIView显示单个实例

    这里有重复每个视图的queryset和serializer_class的代码，即使扩展的通用视图是不同的。
    在 后面，我们将学习解决该问题的视图集和路由器，并允许我们使用更少的代码来创建相同的API视图和URL 

    ## 调用api

##4.3 跨域资源共享 CORS  Cross-Origin Resource Sharing
	当用户从不同站点或 同一个站点的不同位置访问时，需要配置此项。否则造成访问错误。
	比如mysite.com vs yousite.cn, 或者 localhost:2000 vs localhost:3000

	启用配置：
	使用django-rest-framwork 中间件 django-cors-headers
	    1.在全局配置文件中添加相关配置即可。
	    config/settings.py
	    添加corsheaders 到 INSTALLED_APPS
	    # 在MIDDLEWARE的CommonMiddleWare上方添加CorsMiddleware
	      这个位置很重要，因为加载是从上到下加载
	    2，创建白名单：
	    CORS_ORIGIN_WHITELIST

##4.4 小结
	从传统Django需要的唯一组件是models.py文件，urls.py路由。 views.py和serializers.py文件完全是Django REST Framework

	重要的是 通过配置  CORS headers 白名单只允许两个域访问我们的api，这是新手最简单重要的方式。
	然后添加一点Django REST Framework的序列化器和视图提供的魔力。

#5 前端 Node	

	首先，将React应用配置为我们的前端。 
	新建一个控制台界面，linux 下载并安装 node
	curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
	或者 wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash

	command -v nvm  # 激活命令行
	重启命令行控制台界面 即可完成安装

	# 安装React 并安装项目 
	我们将使用出色的npm-create-react-app包来快速启动一个新的React项目。这将生成我们的项目样板并通过一个命令安装所需的依赖项！
	npm使管理和安装多个软件包变得非常简单。 这是在本地安装软件包的一种改进方法，无需安装污染全局名称空间。这是安装React的推荐方法以及我们将使用的方法
    
    apt install npm   # 40M 上下
    npx create-react-app frontend  # 在todo目录创建前端app
    进入frontend 并启动应用
    $ cd frontend
	$ npm start

	# 在前端app构造模拟数据

		import React, { Component } from 'react';
		const list = [ {
		    "id":1,
		    "title":"1st todo",
		    "body":"Learn Django properly."
		    },
		    {
		    "id":2,
		    "title":"Second item",
		    "body":"Learn Python."
		    },
		        {
		    "id":3,
		    "title":"Learn HTTP",
		    "body":"It's important."
		   } ]

	将列表加载到组件的状态，然后使用JavaScript数组方法map()显示所有项目.可以复制代码，只需要看到如何与api配合工作


		class App extends Component {
		    constructor(props) {
		        super(props);
		        this.state = { list };
		}

		render() {
		    return (
		            <div>
		            {this.state.list.map(item => (
		             <div key={item.id}>
		                    <h1>{item.title}</h1>
		                    <p>{item.body}</p>
		                    </div>
		        ))}
		            </div>
		     );
		    } }
		export default App;

	我们已将列表加载到App组件的状态中，然后使用map遍历每个组件列表中的项目，显示每个项目的标题和正文。我们还添加了ID作为密钥，这是一个反应特定的要求；该ID由Django自动添加到我们每个数据库字段中。
    
    注意：如果在前端看见js错误，只需要重新安装npm
    该修复程序通常是npm-install，然后尝试重新启动npm。如果这样不起作用，则删除您的node_modules文件夹并运行npm install。这样就可以在99％的时间内解决问题。欢迎使用现代JavaScript。 :)

##5.1 连接前后端  # 有bug
	使用 django api 替换 mock 数据
	发出HTTP请求的两种流行方法：内置FetchAPI或axios它带有几个附加功能。在此示例中，我们将使用axios。使用Control-c停止运行的应用程序。然后安装axios

	在前端安装 axios， 用于前端发起request 请求
	npm install axios

	如果axios 安装失败，使用 内置的fetch
	//src/App.js
	import React, { Component } from 'react';
	//import axios from 'axios'; // new
	class App extends Component {
		state = {
			todos: []
		};
	// new
	componentDidMount() {
	this.getTodos();
	}
	// new
	getTodos() {
	fetch('http://127.0.0.1:2000/api/')
	.then(response )
	.then(data => this.setState({ totalReactPackages: data.total }));
	//.catch(err => {
	//console.log(err);
	//})
	//);
	}
	render() {
		return ( <div> {this.state.todos.map(item => (
		<div key={item.id}> <h1>{item.title}</h1> <span>{item.body}</span> </div>
		))}
		</div>
		);
	} }
	export default App;

##5.2 小结
  前后端分离将增强web站点的灵活性。
  接下来增强我们的API，使其支持多个HTTP动作，例如POST（添加新待办事项），PUT（更新现有的待办事项）和DELETE（删除待办事项）

  然后我们将构建一个健壮的Blog API，该API支持完整的CRUD（创建-读取-更新-删除）功能，随后再向其中添加用户身份验证，以便用户可以登录，注销，然后通过我们的API注册帐户。


# 6 扩展api功能 -blog api，
	# 新建posts 应用
       python manage.py startapp posts

	# 在全局setting注册
	  INSTALLED_APPS = ['posts.apps.PostsConfig', # blog api]

    # 在全局路由 注册 posts路由
      urlpatterns = [path('api/v1/', include('posts.urls')), # new]

    # App配置， 模型 models.py, 5个字段
        # posts/models.py
		from django.db import models
		from django.contrib.auth.models import User
		class Post(models.Model):
		    author = models.ForeignKey(User, on_delete=models.CASCADE)
		    title = models.CharField(max_length=50)
		    body = models.TextField()
		    created_at = models.DateTimeField(auto_now_add=True)
		    updated_at = models.DateTimeField(auto_now=True)
		    def __str__(self):
		        return self.title

    # App配置，在默认管理app中注册
    from .models import Post
	# Register your models here.

	admin.site.register(Post)

	PostsApp 路由配置，在app的 urls中，用户访问全局urls后，将被导向这里
		# posts/urls.py
		from django.urls import path
		from .views import PostList, PostDetail

		urlpatterns = [
		    path('<int:pk>/', PostDetail.as_view()),
		    path('', PostList.as_view()),
		]

    # PostsApp 序列化操作， 接口返回数据 Json 字段
    序列化程序不仅可以将数据转换为JSON，还可以指定要包含或包含哪些字段,但是我们不想包含updated_at字段。
    Django_REST_Framework强大的序列化程序类使控制变得非常简单。我们创建了一个PostSerializer，并在其中指定了一个Meta类包括哪些字段并明确设置要使用的模型。有很多方法可以自定义序列化程序.

        # posts/serializers.py
		from rest_framework import serializers
		from .models import Post
		class PostSerializer(serializers.ModelSerializer):
		    class Meta:
		        fields = ('id', 'author', 'title', 'body', 'created_at',)
		        model = Post

	# PostsApp 视图配置，Views.py将 数据转发到 序列化模块.
	ListCreateAPIView，它类似于我们之前使用的ListAPIView，但允许写。我们还希望使各个博客文章可供阅读，更新或删除。确实，为此提供了一个内置的通用Django_REST_Framework视图用途：RetrieveUpdateDestroyAPIView。  我们要做的就是更新我们的通用视图以从根本上改变给定API端点的行为。所有这些功能都是可用的，经过测试的并且可以正常使用。不必在这里重新发明轮子。 此时api通过views视图的更改已经具有 CRUD功能。
		# posts/views.py
		from rest_framework import generics
		from .models import Post
		from .serializers import PostSerializer

		class PostList(generics.ListCreateAPIView):  # 可读写的视图
		    queryset = Post.objects.all()
		    serializer_class = PostSerializer

		class PostDetail(generics.RetrieveUpdateDestroyAPIView):  # 可更新，删除的视图
		    queryset = Post.objects.all()
		    serializer_class = PostSerializer

    # 测试模块
	    # posts/tests.py
		from django.test import TestCase
		from django.contrib.auth.models import User
		from .models import Post

		class BlogTests(TestCase):
		    @classmethod
		    def setUpTestData(cls):
		        # Create a user
		        testuser1 = User.objects.create_user(
		            username='testuser1', password='abc123')
		        testuser1.save()
		        # Create a blog post
		        test_post = Post.objects.create(
		            author=testuser1, title='Blog title', body='Body content...')
		        test_post.save()

		    def test_blog_content(self):
		        post = Post.objects.get(id=1)
		        author = f'{post.author}'
		        title = f'{post.title}'
		        body = f'{post.body}'
		        self.assertEqual(author, 'testuser1')
		        self.assertEqual(title, 'Blog title')
		        self.assertEqual(body, 'Body content...')

    # 迁移并重启服务
    python manage.py makemigrations posts &&  python manage.py migrate && python manage.py runserver 0.0.0.0:2000

	始终对API（v1/，v2/等）进行版本控制，因为更改API的各个使用者也可能需要一些时间才能更新。那您可以在一段时间内支持API v1的方式，同时还启动新的，更新的v2并避免破坏依赖您API后端的其他应用。
    
    一个项目中有多个应用，创建专用的api应用可能更有意义将所有其他API网址路由都包含进去。但是对于像这样的基础项目，我宁愿避免仅用于路由的api应用。如有需要，我们随时可以添加一个.

#7  查看和编辑权限 Permissions
    安全性是任何网站的重要组成部分，但对于Web API而言则至关重要。现在rest_framework 有out-of-the-box 权限可以应用于项目水平，视图层 或 个人模型 （ project-level, a view-level，individual model level.）
    
    创建一个用户，并赋予它不同权限。

    在 127.0.0.1:2000/admin/  添加一个用户(user)  用户名/密码： testuser/user.123  其他不做操作，保存后转跳至用户列表。
    今后，无论何时我们想在用户帐户之间切换时，都需要跳到Django管理员，退出一个帐户，然后登录另一个帐户。每次。然后切换回到我们的API端点。

    Django REST Framework具有单行设置来添加登录并直接注销到可操作的API。

    在项目级别的urls.py文件中，添加一个包含rest_framework.urls的新URL路由。使用 api-auth 匹配

	    # config/urls.py
		from django.contrib import admin
		from django.urls import include, path
		urlpatterns = [
			path('admin/', admin.site.urls),
			path('api/v1/', include('posts.urls')),
			path('api-auth/', include('rest_framework.urls')), # new
		]
    访问http://127.0.0.1:8000/api/v1/上的可浏览API。有一个细微的变化：右上角的用户名旁边是一个向下的箭头，点击可以发现 logout 登出按钮。
    登出后 被重定向到Django REST Framework的登录页面，使用新用户 testuser登录。 

    登录后可以发现，所有api都没有进行权限限制，可以被任何人使用。 即使登出testuser 也一样。 任何用户都可以查看删除修改文章。 

    项目级别： 这是因为 “发布列表”端点以及“详细列表”端点，
    是我们之前在config/settings.py中将项目的项目级别权限设置为AllowAny。
    
    我们可以在多个层次操作权限
     this—project-level, view-level,   object-level—but
    
    # 视图权限 这里有两个视图，让我们为它们都添加权限。
    from rest_framework import generics, permissions #权限
    每个视图类都增加权限属性。
	    class PostList(generics.ListCreateAPIView):
	    	permission_classes = (permissions.IsAuthenticated,) # new 只有登录的用户可以查看
	    	...
	    class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    		permission_classes = (permissions.IsAuthenticated,) # new 只有登录的用户可以查看
    		...

    刷新可浏览的API，网址为http://127.0.0.1:8000/api/v1/。看看发生了什么,此时后台将返回 403 拒绝消息
    	HTTP 403 Forbidden
		Allow: GET, POST, HEAD, OPTIONS
		Content-Type: application/json
		Vary: Accept

		{
		    "detail": "Authentication credentials were not provided."
		}
    
    向每个视图添加专用的Permission_classes如果要在整个API上设置相同的权限设置，则重复此操作。最好一次更改我们的权限（最好是在项目级别）。

#7.1   # 项目权限限制
   在项目级别设置严格的权限策略，并根据需要在视图级别放宽策略。这这就是我们要做的。
   Django_REST_Framework随附了许多内置的项目级,我们可以使用的设置
    • AllowAny - #任何用户，无论是否登录，全部权限。
	• IsAuthenticated  -  #仅认证，注册 登录的用户
	• IsAdminUser  -  #仅管理员，超级用户
	• IsAuthenticatedOrReadOnly - #未经授权的用户可以查看任何页面，但只有认证用户可以编辑新建删除。

  这四个设置中的任何一个都需要更新DEFAULT_PERMISSION_CLASSES，然后设置和刷新我们的网络浏览器。

#7.2 自定义权限 Custom permissions
    只希望特定博客帖子的作者能够对其进行编辑或删除；否则博客文章应为只读。
    超级用户帐户应具有对帐户的完整CRUD访问权限 ，但常规用户testuser只可编辑自己的。

    代码内部，Django REST Framework依赖于BasePermission类，所有其他每个任务类权限都从该BasePermission类继承。这意味着内置的权限设置（例如AllowAny，IsAuthenticated，其他自定义是将其扩展)。

    由于我们的需求是 任何人都可以查看，但是只有管理员和作者可以编辑。将重载 has_object_permission方法。
    如果请求包含HTTP SAFE_METHODS中包含动词（一个包含GET，OPTIONS和HEAD的元组），那么它是有只读的许可被授予
	    # posts/permissions.py
		from rest_framework import permissions
		class IsAuthorOrReadOnly(permissions.BasePermission):
			def has_object_permission(self, request, view, obj):
				# Read-only permissions are allowed for any request
				if request.method in permissions.SAFE_METHODS:
					return True
				# Write permissions are only allowed to the author of a post
				return obj.author == request.user

   关于创建，删除或编辑功能 在这种情况下，我们检查对象的作者是否匹配，这是我们的博客文章obj.author与发出请求request.user的用户匹配。
   回到views.py文件中，我们应该导入IsAuthorOrReadOnly，然后我们可以添加Permission_PostDetail的类
  
   请注意，通用视图将仅检查对象级权限以获取检索到的视图。一个模型实例。如果您需要对列表视图进行对象级过滤-对于以下内容的集合实例-您需要过滤的方法实现： https://www.django-rest-framework.org/api-guide/filtering/#overriding-the-initial-queryset
   设置严格的项目级别权限策略的想法，这样只有经过身份验证的用户才能查看API。然后根据需要在特定API上更方便地访问视图级别或自定义权限端点。


#8 用户认证
   User Authentication
   第7章我们更新了API权限，也称为授权。在本章我们将实现身份验证，这是用户可以注册的过程，新用户的登录登出控制等
   传统的整体式Django网站认证中，认证更为简单，涉及基于会话的Cookie模式，我们将在下面进行回顾。但是使用API​​会有些棘手。请记住，HTTP是无状态协议，因此没有内置的方式可以记住用户是否从一个请求到下一个请求进行了身份验证。每次用户请求受限资源时，必须验证自己。
 
   解决方案是在每个HTTP请求中传递唯一的标识符。令人困惑的是此标识符的形式不是公认的方法，它可能需要多个形式。 Django REST Framework随附了四个不同的内置身份验证选项：基本，会话，令牌和默认值。而且还有更多的第三方软件包可提供额外的JSON Web令牌（JWT）等功能。
   审查每种方法的弊端，然后为我们的Blog API做出明智的选择。到最后，我们将已创建用于注册，登录和注销的API端点。

##8.1 基础认证 Base Authentication
   之前发送批准的身份验证凭据授予访问权限。 大致交互流程如下：
	    1. 客户端发起HTTP请求 
		2. 服务器使用HTTP响应进行响应，该HTTP响应包含401（未授权）状态代码和WWW-Authenticate HTTP标头，其中包含有关如何授权的详细信息
		3. 客户端通过Authorization HTTP标头发送回凭据
		4. 服务器检查凭据并以200 OK或403 Forbidden状态代码响应
   批准访问后，客户端将发送带有Authorization HTTP标头的所有以后的请求证书。图示过程如下：
		   Client                     Server
		 
		 GET / HTTP/1.1 ---->
		
		                <--------HTTP/1.1 401 Unauthorized WWW-Authenticate: Basic
		               
		 GET / HTTP/1.1
		Authorization:
		 Basic d3N2OnBhc3N3b3JkMTIz          
		 ------------->
		                     <------ HTTP/1.1 200 OK
	 请注意，发送的授权凭证是未加密的，
	 如<username>:<password> wsv:password123的base64编码后为  d3N2OnBhc3N3b3JkMTIz.
    
     这种方法的主要优点是简单。但是有几个主要缺点。
      首先，对于每个单个请求，服务器都必须查找并验证用户名和密码，效率低下。
           最好先查找一次，然后传递一些令牌表示该用户已获批准的一种。
      其次，用户凭据以明文形式传递，而不是通过互联网完全加密。这是非常不安全的，任何未加密的互联网数据都可以轻松被抓取和使用。

      最后，这种方法 通常用于https加密传输 。

##8.2 会话认证 
    Session Authentication
    Django使用会话和Cookie的组合认证。在较高级别上，客户端使用其身份验证凭据（用户名&密码），然后从存储的服务器接收会话ID作为Cookie。然后，此会话ID将在以后的每个HTTP请求的标头中传递。
    传递会话ID后，服务器将使用它来查找包含所有内容的会话对象给定用户的可用信息，包括凭据。
	这种方法是有状态的，因为必须在两台服务器（会话对象）和客户端（会话ID）。

	基本流程如下：
	   1，用户键入登录凭据（用户名，密码）
	   2，服务器校验凭据是否正确并生产一个会话对象 并 存储在数据库
	   3，服务器发送客户端 会话ID，并不是session 对象本身，sessin本身作为cookie存储在浏览器
	   4，将来所有 此会话的请求，其HTTP header都将包含 session ID， 如果经数据库校验通过，请求将被允许。
       5，一旦用户登出一个应用，会话ID将被同时在服务器和客户端摧毁。
       6，如果用户稍后再次登录，新的会话将产生并作为 cookie 存储在客户端。

     Django_REST_Framework中的默认设置实际上是使用Django的 身份验证和会话身份验证组合。 session ID通过后将在HTTP header中传递于每一个请求。

     优点是，由于用户凭据仅发送一次，因此它更加有效和安全。
		并非在每个请求/响应周期中都像基本身份验证中那样。 
		服务器不必每次都验证用户的凭据，只需匹配会话ID到快速查找的会话对象。
     缺点是， 首先，会话ID仅在登录已执行的浏览器中有效；它不能跨多个域工作。
	     这是一个明显的问题，当一个API需要支持多个前端很麻烦，例如网站和移动应用程序。
	     第二，会话对象必须保持最新，这在具有多个站点的大型站点中可能是一个挑战。您如何在每个服务器上保持会话对象的准确性？
	     第三，对于每个单独的请求，即使是不需要身份验证的请求，都会发送Cookie 效率低下。
	  通常不建议对任何API使用基于会话的身份验证方案，如果将有多个前端，网页和APP。

##	令牌认证 Token Authentication  
    第三种主要方法（以及我们将在BlogAPI中实现的一种方法）是使用令牌验证。由于单页网页的兴起，这是近年来最流行的方法应用程序。
    基于令牌的身份验证是无状态的：客户端将初始用户凭据发送至服务器生成唯一的令牌，然后由客户端将其存储为cookie或本地储存。然后，此令牌在每个传入HTTP请求的标头和服务器中传递使用它来验证用户已通过身份验证。服务器本身不保留用户记录，以及令牌是否有效。

    Cookies vs localStorage
	Cookies用于读取服务器端信息。它们较小（4KB），并随每个HTTP请求自动发送。 LocalStorage专为客户端信息而设计。它更大（5120KB），默认情况下，每个HTTP请求都不会发送其内容。

	Cookie和localStorage中存储的令牌很容易受到XSS攻击。
	目前最佳做法是使用httpOnly和Securecookie标志将令牌存储在cookie中。

	让我们看一下此 挑战/响应流 （ challenge/response）中的实际HTTP消息的简单版本。注意HTTP标头WWW-Authenticate指定在响应中使用的令牌的使用授权标头请求。
	示意图表 Diagram
		Client 					Server
       -------->
       GET / HTTP/1.1
                     <----------- HTTP/1.1 401 Unauthorized WWW-Authenticate: Token
      ---------->
      GET / HTTP/1.1
     Authorization: 
     Token 401f7ac837da42b97f613d789819ff93537bee6a
                     <--------- 
                     HTTP/1.1 200 OK

     这种方法有很多好处。由于令牌存储在客户端上，因此扩展维护最新会话对象的大型服务器不再是问题。
     令牌可以共享在多个前端之间：相同的令牌可以代表网站上的用户，并且相同用户在移动应用上。
     主要局限性 ：相同的会话ID不能在不同的前端之间共享

     缺点：
        潜在的不利因素是令牌可能会变得很大。令牌包含所有用户信息，不仅是ID，
     还有会话ID /会话对象的设置。由于令牌是根据每个请求发送的，管理其大小可能会成为性能问题。             
         令牌的实施方式也可能有很大不同。
    Django_REST_Framework  令牌内建库 TokenAuthentication  是很基础的，不支持设置令牌到期，这是可以添加的安全性改进。它也只会产生一个令牌，因此网站上的用户以及后来的移动应用程序都将使用相同的令牌。
    由于有关用户的信息存储在本地，这需要更新两组客户信息 因此可能导致维护和维护方面的问题。

    可以添加到Django的令牌的增强版本可以通过多个第三方程序包的REST框架。 JWT有很多好处，包括生成唯一客户端令牌和令牌到期的能力。它们可以在服务器生成或第三方服务（如Auth）。而且JWT可以被加密，这使得它们可以更安全地通过不安全的HTTP连接发送。

    对于大多数Web API而言，最安全的选择是使用基于令牌的身份验证方案。JWTs是不错的，是现代的补充，尽管它们需要其他配置。最后，在这里我们将使用内置的TokenAuthentication。

    # Default Authentication
    第一步是配置我们的新身份验证设置。 Django REST框架来了具有许多隐式设置的设置。
    例如，DEFAULT_PERMISSION_CLASSES在我们将其更新为IsAuthenticated之前，将其设置为AllowAny。 明确config/setting默认认证配置如下
	    	REST_FRAMEWORK = { 'DEFAULT_PERMISSION_CLASSES': [
				'rest_framework.permissions.IsAuthenticated', ],
		    'DEFAULT_AUTHENTICATION_CLASSES': [ # new
				'rest_framework.authentication.SessionAuthentication', 'rest_framework.authentication.BasicAuthentication'],
				}
    
    要同时使用两种方法，答案是它们有不同的用途。会话用于 提供可浏览的API以及登录和注销该API的能力。 BasicAuthentication用于传递API本身的HTTP标头中的会话ID。


    # 实现令牌认证
    1，设置DEFAULT_AUTHENTICATION_CLASSES   TokenAuthentication
		# config/settings.py
		REST_FRAMEWORK = { 'DEFAULT_PERMISSION_CLASSES': [
		'rest_framework.permissions.IsAuthenticated',
		],
		'DEFAULT_AUTHENTICATION_CLASSES': [
		'rest_framework.authentication.SessionAuthentication', 'rest_framework.authentication.TokenAuthentication', # new
		],}
    2，添加token认证到 全局 setting设置 INSTALLED_APPS
    	'rest_framework.authtoken', # new
    3， 我们对INSTALLED_APPS进行了更改，因此我们需要同步数据库
        pythn manager.py migrate
    4, 使用superuser 管理员
       你会看到那里现在顶部的“令牌”部分。确保您使用超级用户帐户登录后才能有 token 使用权

    由于几乎所有的API需要此功能，因此有几个优秀且经过测试的第三方可以满足 token的创建和管理功能。
## api 接口认证
    dj-rest-auth   # 开箱即用log in, log out, and password 重置 .

    安装 pip install dj-rest-auth
    # 全局路由 配置
       添加 path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')), # new

    重启服务 python manager.py runserver 0.0.0.0:2000

    现在可以访问api的认证接口
    http://127.0.0.1:2000/api/v1/dj-rest-auth/login/
    http://127.0.0.1:2000/api/v1/dj-rest-auth/logout/
    http://127.0.0.1:2000/api/v1/dj-rest-auth/password/reset/   
    http://127.0.0.1:2000/api/v1/dj-rest-auth/password/reset/confirm

    # 接口用户注册
    传统Django不附带用于用户注册的内置视图或URL，DjangoRESTFramework也没有。这就表示我们需要从头开始编写自己的代码；考虑到问题的严重性，这种方法有些冒险–和可能带来安全隐患。

 	django-allauth #第三方包用于将 其他各大网站 FB，twitter，ins的用户接入到该接口。

 	## 安装
 	pip install django-allauth~=0.42.0

 	全局配置添加
 	    django.contrib.sites
		allauth
		allauth.account
		allauth.socialaccount
		dj_rest_auth.registration
    配置添加如下：
    # config/settings.py
		INSTALLED_APPS = [
         'dj_rest_auth.registration', # new
		
		'django.contrib.sites', # new
		'allauth', # new
		'allauth.account', # new
		'allauth.socialaccount', # new
		'posts', ]

		EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # new
		SITE_ID = 1 # new

	电子邮件配置需要电子邮件后端配置，因为默认情况下，当有新用户登录时，将发送一封电子邮件注册，要求他们确认其帐户。与其设置电子邮件服务器，不如说我们将使用console.EmailBackend设置将电子邮件输出到控制台。
    SITE_ID是内置Django“站点”框架的一部分，这是一种来自同一Django项目的网站 承载多个站点的方法 。
    显然，我们只有一个网站在这里工作 但是django-allauth使用sites框架，因此我们必须指定一个默认设置。
  
    # 编辑生效的视图
    # config/urls.py
		from django.contrib import admin
		from django.urls import include, path
		urlpatterns = [
			path('admin/', admin.site.urls),
			path('api/v1/', include('posts.urls')),
			path('api-auth/', include('rest_framework.urls')),
			path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
			path('api/v1/dj-rest-auth/registration/', # new
		          include('dj_rest_auth.registration.urls')),
		]

	访问并注册api：  apiuser/api.123456
	     http://127.0.0.1:2000/api/v1/dj-rest-auth/registration/
	注册接口将返回
	    POST /api/v1/dj-rest-auth/registration/
		HTTP 201 Created
		Allow: POST, OPTIONS
		Content-Type: application/json
		Vary: Accept

		{
		    "key": "70d423eede3500e4a764a01e6c6ed7d916938a78"
		}
    返回值键是此新用户的身份验证令牌。您查看命令行控制台，则django-allauth将自动生成一封电子邮件。
    可以更新此默认文本，并添加具有其他配置的电子邮件SMTP服务器
     控制台的输出，因为我们没有配置邮件服务器，所以输出到了控制台
		     Content-Type: text/plain; charset="utf-8"
		MIME-Version: 1.0
		Content-Transfer-Encoding: 7bit
		Subject: [example.com] Please Confirm Your E-mail Address
		From: webmaster@localhost
		To: apiuser@gmail.com
		Date: Sat, 08 May 2021 04:34:35 -0000
		Message-ID: <162044847553.377968.13115344862963186126@usercom>

		Hello from example.com!

		You're receiving this e-mail because user apiuser has given yours as an e-mail address to connect their account.

		To confirm this is correct, go to http://127.0.0.1:2000/api/v1/dj-rest-auth/registration/account-confirm-email/MQ:1lfEfj:-piJC3WMRmCiehWdQZJ96eh7gKAosFmUd8_oOsOWaMg/

		Thank you from example.com!
		example.com

	然后通过管理员账户登录 http://127.0.0.1:2000/admin/ 即可看见api注册的新的token用户

## 旧用户的token添加
	一旦我们通过API使用任一帐户登录，令牌都会自动添加并可用。比如使用admin在api登录也将对admin产生token
	apiuser/api.123456
	http://127.0.0.1:2000/api/v1/dj-rest-auth/login/

	页面将返回
		POST /api/v1/dj-rest-auth/login/
	HTTP 200 OK
	Allow: POST, OPTIONS
	Content-Type: application/json
	Vary: Accept

	{"key": "70d423eede3500e4a764a01e6c6ed7d916938a78"}
	


	在我们的前端框架中，我们需要捕获并存储此令牌。传统上，这在客户端上操作，无论是在本地存储localStorage中还是作为缓存cookie，然后所有以后的请求 都包括标头中的令牌作为对用户进行身份验证的一种方式。 选择前端很重要。
	
	建构Web API时，用户身份验证是最难掌握的领域之一。没有整体结构的好处，我们作为开发人员必须深刻理解和理解。
	适当配置我们的HTTP请求/响应周期。Django REST Framework对此过程提供了很多内置支持，如内建TokenAuthentication
	
	但是，开发人员必须配置其他区域，例如用户注册 和 专用网址/视图 urls/views 本身，使用第三方框架来减少工作量
	dj-rest-auth & django-allauth


#9， 视图集和路由集 Viewsets and Routers
	viewsets   # rest_framework 的api视图开发工具
 	routers   # rest_framework的 api 路由开发工具
 	它们是视图和URL之上的附加抽象层。首要的好处是单个视图集可以替换多个相关视图。而且路由器可以自动为开发人员生成网址。在具有多个端点的大型项目中，这意味着开发人员可以编写更少的代码。可以说，对于有经验的开发人员来说也更好理解。

 	看看如何从视图和URL切换到视图集，路由器可以实现相同的功能，而所需的功能要少得多代码。
 	config/urls.py 现有的路由
	 	admin/      #
		api/
		api/v1/
		api-auth/
		api/v1/dj-rest-auth/
		api/v1/dj-rest-auth/registration/
		api-auth/
		api/v1/dj-rest-auth/
		api/v1/dj-rest-auth/registration/

 	前两个端点是我们创建的，而dj-rest-auth提供了另外五个端点。
 	现在让我们添加两个附加端点以列出所有用户和单个用户。这是一个共同的特征，在许多API开发中有这个需求，这将使我们更加清楚为什么将我们的视图和URL重构为视图集和路由器可以说得通。
 	传统的Django有一个内置的User模型类，我们在认证一章的前面的版本中已经使用过。因此，我们不需要创建新的数据库模型。相反，我们只是需要连接新的端点。此过程始终涉及以下三个步骤
 	    新的 serializer 类
 	    新的 views 视图集
 	    为每个端点的新的 URL 路由集

 	修改serializers，添加新的 用户类
    	# posts/serializers.py
		from django.contrib.auth import get_user_model # new
		from rest_framework import serializers
		from .models import Post
		class PostSerializer(serializers.ModelSerializer):
			class Meta:
				model = Post
				fields = ('id', 'author', 'title', 'body', 'created_at',)
		class UserSerializer(serializers.ModelSerializer): # new
			class Meta:
				model = get_user_model()
				fields = ('id', 'username',)

    这里将使用了get_user_model来引用User模型，在Django中，实际上有三种不同的方式来引用User模型。
	通过使用get_user_model，我们可以确保我们引用的是正确的用户模型，无论它是否是默认用户或自定义用户模型，通常在新的Django项目中定义。
	然后，我们需要为每个端点定义视图。首先将UserSerializer添加到列表中
    最后 创建列出所有用户的UserList类和UserDetail类
    提供单个用户的详细视图。就像我们的帖子视图一样，
    在这里我们可以使用ListCreateAPIView和RetrieveUpdateDestroyAPIView。
    我们还需要参考用户通过get_user_model进行建模，以便将其导入到第一行。

    修改视图
    	# posts/views.py
		from django.contrib.auth import get_user_model # new
		from .serializers import PostSerializer, UserSerializer # new

		class UserList(generics.ListCreateAPIView): # new
			queryset = get_user_model().objects.all()
			serializer_class = UserSerializer
		class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
			queryset = get_user_model().objects.all()
			serializer_class = UserSerializer

    ”视图和“用户”视图都具有完全相同的queryset和serializer_class。也许可以通过某种方式将它们组合在一起保存代码。

    修改 posts/urls.py 应用路由
    urlpatterns = [path('users/', UserList.as_view()), # new
			path('users/<int:pk>/', UserDetail.as_view()), # new
			...]


	确保本地服务器仍在运行，并跳至可浏览的API.

		http://127.0.0.1:2000/api/v1/users/

#9.1  视图集 Viewsets
    视图集是一种将多个相关视图的逻辑组合到单个类中的方法。其他换句话说，一个视图集可以替换多个视图。目前，我们有四个视图：两个用于博客文章和两个给用户。我们可以使用两个视图集来模仿相同的功能：一个用于博客帖子和一个供用户使用.
    代码
	    # posts/views.py
		from django.contrib.auth import get_user_model
		from rest_framework import viewsets # new
		from .models import Post
		from .permissions import IsAuthorOrReadOnly
		from .serializers import PostSerializer, UserSerializer
		class PostViewSet(viewsets.ModelViewSet): # new
			permission_classes = (IsAuthorOrReadOnly,)
			queryset = Post.objects.all()
			serializer_class = PostSerializer

		class UserViewSet(viewsets.ModelViewSet): # new
			queryset = get_user_model().objects.all()
			serializer_class = UserSerializer

	它既提供了列表视图又提供了为我们提供详细视图。而且我们不再对于每个视图都重复相同的queryset和serializer_class。
    现在服务停止了，因为缺少路由。 接下来配置路由
#9.2 路由集    # Routers
    路由集直接与视图集一起使用，以自动为我们生成URL模式。我们目前posts/urls.py文件具有四个URL模式：两个用于博客文章，两个用于用户。我们可以 不用为每个视图集采用一条路线。因此，使用两个路由而不是四个URL路由模式。
    
     SimpleRouter  与 DefaultRouter
    我们将使用SimpleRouter，但也可以创建自定义路由器以获得更多高级功能。
    # posts/urls.py
	from django.urls import path
	from rest_framework.routers import SimpleRouter
	from .views import UserViewSet, PostViewSet
		router = SimpleRouter()
		router.register('users', UserViewSet, basename='users')
		router.register('', PostViewSet, basename='posts')
		urlpatterns = router.urls

	重启服务，查看效果
	python manager.py runserver 0.0.0.0:2000

	可以看到现在称为“用户实例”而不是“用户详细信息”，并且内置了一个附加的“删除”选项到ModelViewSet。
	可以自定义视图集，但这是一个重要的折衷，以换取更少的编写空间带有视图集的代码是默认设置，可能需要一些其他配置才能匹配您想要的。
	但是，如果我们使用超级用户帐户（该博客文章的作者）登录，那么我们就拥有完整的读写编辑删除权限。

	视图集和路由器集是功能强大的抽象，可减少我们作为开发人员必须写的重复代码量。但是，这种简洁性是以牺牲初始学习曲线为代价的。会感觉头疼几次使用视图集和路由器而不是视图和URL模式，这很奇怪。
	最终，何时向项目添加视图集和路由器的决定是非常主观的。一个好的经验法则是从视图和URL开始。如果您发现API随着复杂性的增长而增长，自己一遍又一遍地重复相同的端点模式，然后查看视图集并路由器。在此之前，请保持简单。


#10 模式和文档
	现在已经完成了API，我们需要一种方法来快速记录其功能，并且准确地给别人。毕竟，在大多数公司和团队中，使用API​​的开发人员与最初构建它的开发人员不同。这对我们来说幸运的是，有自动工具可以处理。
	schema是机器可读的文档，概述了所有可用的API端点，URL和支持的HTTP动词（GET，POST，PUT，DELETE等）。
	将文档简化为人类易于阅读和使用的架构。在这里，我们将添加一个模式添加到Blog项目中，然后添加两种不同的文档编制方法。到最后我们将实现一种自动化的方式来记录我们的 API 当前和将来的 任何变化。
   
    已有的大致api列表
    |Endpoint |HTTP Verb|
	|--------------------------------------|---------|
	|/ 									|GET |
	|/:pk/ 								|GET |
	|users/ 							|GET |
	|users/:pk/ 						|GET |
	|/rest-auth/registration 			|POST |
	|/rest-auth/login 					|POST |
	|/rest-auth/logout 					|GET |
	|/rest-auth/password/rest_framework |POST |
	|/rest-auth/password/reset/confirm  |POST |

#10.1 模式 Schemas

	#django rest framework 已经切换到OpenAPI模式
	第一步是同时安装PyYAML和uritemplate PyYAML 这将改变我们的架构，转换为OpenAPI格式是基于YAML的，而uritemplate将参数添加到URL路径。

   接下来，我们可以选择：生成静态模式或动态模式。如果您的API不会经常更改，因此可以定期生成静态模式并从静态服务器提供服务档案以取得强大效能但是，
   如果您的API确实经常更改，则可以考虑动态选项。我们将在此处实现两者。
    安装依赖包
    pip install pyyaml==5.3.1 uritemplate==3.0.1
	首先，是使用generatechema管理命令的静态模式方法。我们可以将结果输出到文件： openapi-schema.yml.

	# 静态方法：
	 python manage.py generateschema > openapi-schema.yml
	如果您打开该文件，则该文件会很长，而且不友好。但是对于电脑来说，这是完美的格式化。
	对于动态方法，通过在顶部导入get_schema_view来更新config/urls.py
	然后在openapi创建专用路径。标题，描述和版本可以是根据需要定制。
	修改全局配置 config/url.py
		from rest_framework.schemas import get_schema_view # 模板静态处理api
			...
			path('openapi', get_schema_view( # new
		        title="Blog API",
		        description="A sample API for learning DRF",
		        version="1.0.0"), name='openapi-schema'),
		    ]

	现在访问 http://127.0.0.1:2000/openapi， 以查看变化，可以看到不太友好。
    

    # 动态方法  翻译api 为文档给其他开发者
    Django REST框架还带有内置的API文档功能，可翻译，对其他开发人员而言，将架构转换为更友好的格式。
    或者使用第三方包 drf-yasg， 它有更多功能。 这里将使用第三方包 drf-yasg
    ## 1,安装：pip install install drf-yasg==1.17.1
    ## 2,注册，使用第三方包都需要注册，不要忘记注册第三方包，否则运行时可能找不到该功能：
       # config/settings.py
		INSTALLED_APPS = ['drf_yasg', # new]

    ## 3, 更新urls.py 路由
    第三步，更新我们的项目级别的urls.py文件。 我们可以替换DRF，从drf_yasg中获取get_schema_view以及导入openapi。我们还将添加DRF并允许使用其他选项。
	schema_view变量已更新，并包含其他字段，例如terms_of_service联系人和许可。然后在我们的urlpatterns下，为Swagger和ReDoc添加路径

	    # config/urls.py
	    ... #其他导入不变
	    from rest_framework import permissions # new
		from drf_yasg.views import get_schema_view # new
		from drf_yasg import openapi # new

		schema_view = get_schema_view( # new
			openapi.Info(
			title="Blog API",
			default_version="v1",
			description="A sample API for learning DRF",
			terms_of_service="https://www.google.com/policies/terms/",
			contact=openapi.Contact(email="hello@example.com"),
			license=openapi.License(name="BSD License"),
			),
			public=True,
			permission_classes=(permissions.AllowAny,),
			)
        ... # 其他配置不变
    
    访问http://127.0.0.1:2000/swagger/  和 http://127.0.0.1:2000/redoc/
    他们非常全面，并阐明了更多可以取决于API的需求.

    文档是任何API的重要组成部分。通常，这是开发人员的第一件事在团队内部还是在开源项目中查看。得益于自动化工具
    我们通过第三方库的使用 仅需要少量的配置 旧可以确保您的API拥有准确的最新文档
    Django REST框架。在三个不同项目的过程中-库API，Todo API和博客API-我们从头开始逐步构建更复杂的Web API。
    在此过程的每一步中，Django REST框架都提供了内置功能，使我们更轻松。
    官方文档(https://www.django-rest-framework.org/)是进一步探索的绝佳资源。现在您已经掌握了基本知识.

    关于测试：
    传统的Django测试可以而且应该可应用于任何Web API项目，但Django REST中还有一整套工具仅用于测试API请求的框架。


    下一步是实现官方DRF教程  中介绍的pastebin API。我为此编写了更新的初学者指南，其中包含分步说明。
	第三方包对于Django REST Framework开发至关重要，而对于Django本身。完整清单可以在Django Packages(https://djangopackages.org/)上找到，也可以在Github上的awesome-django.






