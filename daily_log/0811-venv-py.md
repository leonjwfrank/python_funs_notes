venv-虚拟环境
	virtualenv是一个非常流行的工具，可为Python库创建隔离的Python环境。如果您不熟悉此工具，我强烈建议您学习它，因为它是非常有用的工具，在本答案的其余部分中，我将对其进行比较。

	它的工作方式是在目录（例如：）中安装一堆文件env/，然后修改PATH环境变量以在其之前添加自定义bin目录（例如：）env/bin/。在完全相同的副本python或python3二进制文件放在这个目录中，但是Python编程寻找相对于其路径优先库，环境中的目录。它不是Python标准库的一部分，但受到PyPA（Python包装管理局）的正式认可。激活后，您可以使用在虚拟环境中安装软件包pip。

	pyenv用于隔离Python版本。例如，您可能想针对Python 2.7、3.6、3.7和3.8测试代码，因此需要一种在它们之间切换的方法。一旦被激活，它的前缀PATH与环境变量~/.pyenv/shims，那里有专用的文件相匹配的Python命令（python，pip）。这些不是Python附带命令的副本。它们是特殊的脚本，它们根据PYENV_VERSION环境变量，.python-version文件或~/.pyenv/version文件来动态地决定要运行哪个版本的Python 。pyenv还可以使用命令简化下载和安装多个Python版本的过程pyenv install。

	pyenv-virtualenv是一个插件pyenv由同一作者的pyenv，允许你使用pyenv和virtualenv在同一时间方便。但是，如果您使用的是Python 3.3或更高版本，请pyenv-virtualenv尝试运行python -m venv它（如果有），而不是virtualenv。如果您不希望使用便利功能，则可以在不使用的情况下一起使用virtualenv和。pyenvpyenv-virtualenv

	virtualenvwrapper是virtualenv（参见docs）的一组扩展。它为您提供诸如mkvirtualenv，的命令，lssitepackages尤其是workon在不同virtualenv目录之间切换时。如果要多个virtualenv目录，此工具特别有用。

	pyenv-virtualenvwrapper是pyenv与作者相同的插件pyenv，可以方便地集成virtualenvwrapper到pyenv。

	pipenv旨在结合Pipfile，pip并virtualenv为在命令行一个命令。该virtualenv目录通常放置在中~/.local/share/virtualenvs/XXX，XXX是项目目录路径的哈希值。这与不同virtualenv，后者的目录通常位于当前工作目录中。pipenv是指在开发Python应用程序（而不是库）时使用。还有的替代物pipenv，例如poetry，我将不在此处列出，因为此问题仅与名称相似的软件包有关。

标准库：
	pyvenv是Python 3随附的脚本，但在Python 3.6中已弃用，因为它存在问题（更不用说混乱的名称了）。在Python 3.6及更高版本中，确切的等效项是python3 -m venv。

	venv是Python 3随附的软件包，您可以使用它运行python3 -m venv（尽管出于某些原因，某些发行版将其分成了单独的发行版软件包，例如python3-venv在Ubuntu / Debian上）。它的作用与相同virtualenv，但仅具有部分功能（请参见此处的比较）。virtualenv继续比受欢迎venv，尤其是因为前者同时支持Python 2和3。


## 实践

	启动虚拟环境
	py > 3.3
	 python3 -m venv v-env
	 或者
	 virtualenv v-env
	source v-env/bin/activate   # 激活

	“Pillow”的常用图形库的部署包，使用 --target选项在新的项目本地 package中安装Pillow
	 pip install --target ./package Pillow
	停止虚拟环境
	deactivate 或 ctrl + d



