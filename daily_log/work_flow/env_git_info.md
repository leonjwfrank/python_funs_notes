# git服务器建立
	ubuntu 20  官方安装说明 https://about.gitlab.com/install/#ubuntu
	注意: 在安装时，最后一步 https 如果没有域名可用，或者不需要使用加密https协议，需要替换域名为ip地址
	sudo EXTERNAL_URL="https://gitlab.example.com" apt-get install gitlab-ee
	替换为
	sudo EXTERNAL_URL="http://192.168.136.130" apt-get install gitlab-ee

	# 如果安装完成后，gitlab服务器仍然不能工作
	sudo gitlab-ctl restart
	# 配置和启用外部ip地址访问服务，编辑配置,并重启服务
	sudo vim /etc/gitlab/gitlab.rb
		external_url "http://192.168.10.1"
	sudo gitlab-ctl reconfigure 

	# 相对路径的禁用
	sudo gitlab-ctl restart unicorn

	# 登录并设置密码

	# 生成ssh密钥对 RSA算法 至少2048位，-C标志带有带引号的注释，例如电子邮件地址，是标记SSH密钥的一种可选方式
	ssh-keygen -t rsa -b 4096 -C "autocommsky@gmail.com"

	# 更新密钥
	ssh-keygen -p -f /path/to/ssh_key

	# 设置密钥
		在web界面。 用户头像--设置--ssh密钥，将生成的公钥pub添加到页面
		在git ssh 客户端添加私钥地址
		设置ssh代理环境
		eval $(ssh-agent -s)
		添加(如果ssh产生私钥在当前目录)
		ssh-add ./id_rsa
## 调试
	综合安装的调试指令 sudo gitlab-rails console
	启动控制台后添加日志监控 ActiveRecord::Base.logger = Logger.new(STDOUT)
## gitlab 服务器添加和管理用户
	run: alertmanager:

	run: gitaly: 

	run: gitlab-exporter: 

	run: gitlab-workhorse:
	run: grafana: 
	run: logrotate: 
	run: nginx: 
	run: node-exporter: 
	run: postgres-exporter: 
	run: postgresql: 
	run: prometheus: 
	run: puma: 
	run: redis:
	run: redis-exporter: 
	run: sidekiq: 


## 语言设置
	用户登录后，在右上角 设置--用户设置--偏好设置

## CI/CD 持续集成，持续发布
	安装gitrunner参考链接:	
	https://docs.gitlab.com/runner/install/linux-manually.html
	注册gitrunner，绑定gitlab地址url，token和执行者
	注册参考文档
	https://docs.gitlab.com/runner/register/index.html#docker
		在gitlab服务器的设置-CICD-展开可以查到当前gitlab服务的
		url:http://192.168.136.130
		token:Qi1yC28qsoFVzQtRyaus

	continue delopy， comtinue intergration
	Step 1:  add .gitlab-ci.yml in the root folder of your project/repo
	Step 2: git commit and git push to git repo
	Step 3: Create Gitlab runner for the project   # 本机配置失败#  需要安装，注册runner到你的gitlab服务器 http://192.168.136.130
	Step 4: Start the runner
	Step 5: Make any change in the project -> commit -> push

	# gitlab runner 注册
	sudo gitlab-runner register --config /tmp/test-config.toml --template-config /tmp/test-config.template.toml --non-interactive --url http://192.168.136.130 --registration-token "your gitlab token" --name test-runner --tag-list bash,test --locked --paused --executor shell

	或者
	sudo gitlab-runner start   # 一步步配置
	--url http://192.168.136.130 
	--registration-token "your gitlab token" 
	--name test-runner 
	--tag-list bash,test 
	--locked 
	--paused 
	--executor shell
	# 总结
	yml文件放在项目的根目录下，格式也正确，runner也注册成功跑起来了但是项目CICD中没有用户的项目提交记录。

# stash  
    代码写到一半需要切到另一个分支修复bug获取拉去其他合作者的代码合并做测试，这时便可以使用git stash未完成代码放到stash栈中
    stash list  列出stash所有记录
    stash apply  将某个记录取出
    stash clear  清空stash栈
# git cherry-pick
	当多人在不同分支开发一个版本时，经常会有A分支的合作者 debug B分支合作者B的某次或多次提交，这时git cherry-pick值得拥有。
	文件日志
	git blame -L 201,208 filename
	git blame -L 242,250 component/select_dealar.py

# 从本地分支对远程创建分支
    git clone  ...
    git checkout master
    git checkout -b newb
    git push origin newb:newb    # origin为远程分仓库名， 冒号前为远程仓库的分支名，后为本地分支名
    # 报错
    	git push origin newb:newb
		fatal: 'origin' does not appear to be a git repository
		fatal: Could not read from remote repository.
	# git remote -v  # 查看没有名称为 origin的远程分支，添加你的远程仓库地址为origin
	git remote add origin git@192.168.136.130:root/dev_wss.git

	# 再次查看 git remote -v 已有远程分支名
		master  git@192.168.136.130:root/dev_wss.git (fetch)
		master  git@192.168.136.130:root/dev_wss.git (push)
		origin  git@192.168.136.130:root/dev_wss.git (fetch)
		origin  git@192.168.136.130:root/dev_wss.git (push)
	# 再次修改推送，成功
	git add README.md
	git commit -am 'start edit'
	## edit file 
	git add README.md
	git commit -am 'done edit'
	## 推送
	$ git push origin newb:newb

		Counting objects: 3, done.
		Delta compression using up to 8 threads.
		Compressing objects: 100% (2/2), done.
		Writing objects: 100% (3/3), 275 bytes | 0 bytes/s, done.
		Total 3 (delta 1), reused 0 (delta 0)
		remote:
		remote: To create a merge request for newb, visit:
		remote:   http://192.168.136.130/root/dev_wss/-/merge_requests/new?merge_request%5Bsource_branch%5D=newb
		remote:
		To git@192.168.136.130:root/dev_wss.git
		   e13bd36..aaaa3f5  newb -> newb

	


# git --all
	所有仓库

# 密钥创建步骤
	ssh-keygen -o -t ras -C "example@www.com" -b 4096
	passphrase ssk@123456
	修改
	ssh-keygen -p -o -f <keyname>
	{
		merge:
		Merge 将branch分支合并到delvelop，将在develop留下一个提交记录
		git checkout feature_branch
		git merge maste
		或 git merge masgter geature_branch
	}
	{
	rebase 
		rebase 可以替代merge方法，rebase将在分支产生一条提交记录
		git checkout feature_branch
		git rebase master
	}
	{
		log
		显示分支，time， author
		git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset%s%Cgreen(%cr)&Cgreen(%cr)%C(bold blue)<%an>%Creset' --abbrev-commit
	}

	{指纹对比
		ssh-keygen -| -E md5 -f ~/.ssh/id_rsa.pub}


# 密码问题
	1，在git目录检查编辑 .git/config的origin部分
	2, 在备份修改后，重新配置ssh密钥，不要设置passparse
	3, 重新拉取远程目录
	4, 重新指定私钥
		设置ssh代理环境
		eval $(ssh-agent -s)
		添加(如果ssh产生私钥在当前目录)
		ssh-add ./id_rsa
# gitlab push 失败
	1,首先看提示origin是否存在，如果不存在则添加
	git remote add origin 'url'
    
    也可以直接通过仓库的git url来提交，而不使用别名
    git push -u "url"  master    # 即url 所属仓库的 master分支
    2, 尝试以下方法
	git push origin/new_two_sg
	error:Please make sure you have the corent access rights
	and the repository exists
	默认只push default是simple模式要求两边分支同名，而upstream模式则不做这个要求

	修改为; git config --global push default upstream
	如有远程分支
	*sg_new  52db1e1[origin/new_two_sg:ahead 1] test diff name branch
	提交时需要指定head 格式
	git push <remote> HEAD:<up-stream-branch-name>
	git push origin 52db1e1:new_two_sg
	或使用本地分支名 与 远程分支名
	git push origin sg_new new_two_sg
	git push origin sg_new new_two  # sg_new:new_two   ,如果冒号后远程分支不存在，则不创建


# gitlab rebase 与 merge 的使用场景
    比如在master分支，执行以下指令:
    git rebase newb    # fast-forward 结果看起来像是直线发展了。保留了原来的提交结构，而不是包含所有合并更改的合并提交
    git merge newb     # 自动合并提交分支，包括所有合并更改的合并提交。
	两个指令都可以快速将newb分支的内容合并到master



