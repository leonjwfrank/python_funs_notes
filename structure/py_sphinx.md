### 一, 在sphinx中展示漂亮的文档

1, 环境准备:

已安装python,

pip install  sphinx sphinx-autobuild

2, 已安装sphinx

​	1,  新建文档工作目录如 ../notes/base_md  

​	2, 进入此目录 sphinx-quickstart 

​	3, 选择配置方式, 如分离源目录和构建目录, 展示作者和项目名称, 设置默认显示语言等

3, 选择是否使用window command file make, 在文档编辑后可快速生成发布

4, 使用 make html 生成文档（需要进入make.bat所在目录，如..notes/base_md）.

5,  编辑文档,

 	5.1 在index中插入链接

​		.. _a link:

​	5.2  插入图片

​		.. image:: ../build/html/_static/clouds_night.png

​	5.3 支持.md 等解析

​               安装 recommonmark.parser:   pip install recommonmark

```python
from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']
```

​	5.4  尾注

​	.. rubric:: Footnotes

​	5.4  支持在移动端展示