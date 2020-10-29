# tcpdump 基础教程

本教程将向您展示如何以各种方式隔离流量（从IP，端口，协议到应用程序层流量），以确保您尽快找到所需的信息。

tcpdump 是每个人都应该学习的工具，作为数据包分析的基础。
基本沟通
通过IP查找流量
按来源和/或目的地过滤
显示网络流量
显示港口流量
按协议显示流量
显示IPv6流量
使用端口范围查找流量
根据数据包大小查找流量
写入文件
隔离TCP标志
查找HTTP用户代理
查找明文HTTP GET
查找HTTP主机
查找HTTP Cookie
查找SSH连接
查找DNS流量
查找FTP流量
查找明文密码
查找带有恶意比特的数据包
使用apt install tcpdump（Ubuntu）或yum install tcpdump（Redhat / Centos）安装tcpdump
让我们从一个基本命令开始，该命令将使我们获得HTTPS流量：

tcpdump -nn S X 端口 443

04：45：40.573686 IP 78.149.209.110.27782 > 172.30.0.144。443：标志[。]，ack
278239097，胜利28，选项[nop，nop，TS val 939752277 ecr 1208058112]，长度0
    0x0000：   4500 0034 0014 0000 2e06 c005 4e8e d16e E..4 ........ N..n 
    0x0010：   ac1e 0090 6c86 01bb 8e0a b73e 1095 9779 .... l ......> .. .y 
    0x0020：   8010 001c d202 0000 0101 080a 3803 7b55 ............ 8. {U 
    0x0030：   4801 8100
你可以用一个单一的数据包-c 1，或ñ与数量-c n。
这显示了一些HTTPS流量，在输出的右侧部分显示了一个十六进制显示（alas，它已加密）。请记住，如果有疑问，请使用您感兴趣的端口运行上面的命令，并且应该在途中。

例子
PacketWizard™并不是真正的商标，但应该是。

准备运行TCPDUMP的从业人员

现在您已经可以获得基本的流量，下面逐步介绍在网络，安全性或任何类型的PacketWizard™工作期间可能需要的大量示例。
接口上的所有内容
通过查看影响界面的内容，只需查看发生了什么。

或使用获取所有接口-i any。
tcpdump -i eth0

通过IP查找流量
最常见的查询之一，使用host，您可以看到往返于1.1.1.1的流量。

表达式类型：

host，net，和port。

方向：

src和dst。

类型：

host，net，和port。

协议：

tcp，udp，icmp，等等。
tcpdump 主机 1.1.1.1

06：20：25.593207 IP 172.30.0.144.39270> one.one.one.one。域：
12790+ A？google.com。
（28）06：20：25.594510 IP one.one.one.one。域 > 172.30.0.144.39270：
12790 1/0/0 A 172.217.15.78（44）
按源和/或目标过滤
如果您只想查看一个方向或另一个方向的路况，可以使用src和dst。

tcpdump src 1.1.1.1
tcpdump dst 1.0.0.1

通过网络查找数据包
要查找去往或来自特定网络或子网的数据包，请使用该net选项。

您也可以将其与src和dst选项结合使用。
tcpdump 净 1.2.3.0/24

使用十六进制输出获取数据包内容
当您想查看有问题的数据包的内容时，十六进制输出很有用，当您隔离一些候选者进行更仔细的检查时，通常最好使用十六进制输出。

tcpdump -c 1 -X icmp


单个ICMP数据包（十六进制可见）

显示与特定端口相关的流量
常用选项：：

-nn不解析主机名或端口名。

-S：获取整个数据包。

-X：获取十六进制输出。
您可以通过使用port选项以及端口号找到特定的端口流量。

tcpdump 端口 3389
tcpdump src 端口 1025

显示一种协议的流量
如果您正在寻找一种特定类型的流量，则可以使用tcp，udp，icmp以及许多其他流量。

tcpdump icmp

仅显示IP6流量
您还可以使用协议选项查找所有IP6流量。

tcpdump ip6

使用端口范围查找流量
您还可以使用一系列端口来查找流量。

tcpdump portrange 21-23

根据数据包大小查找流量
如果要查找特定大小的数据包，则可以使用这些选项。您可以使用数学期望的更少，更大或与其相关的符号。

tcpdump 减去 32
tcpdump 大于 64
tcpdump <= 128

读取/写入捕获到文件（pcap）
将数据包捕获保存到文件中以供将来分析通常很有用。这些文件被称为PCAP（PEE-cap）文件，它们可以由数百种不同的应用程序处理，包括网络分析仪，入侵检测系统，当然还有它们tcpdump本身。在这里，我们使用开关将文件写入名为capture_file的文件-w。

tcpdump 端口 80 -w capture_file

您可以使用-r开关读取PCAP文件。注意，在读取文件时，可以在tcpdump中使用所有常规命令。您仅受以下事实的限制：您无法捕获和处理文件中不存在的内容。

tcpdump -r capture_file

高级
现在，我们已经通过一些示例了解了基础知识可以做什么，下面让我们看一些更高级的内容。

更多的选择
这里有一些其他方法可以调整通话方式tcpdump。

-X：以十六进制和ascii两种格式显示数据包的内容。
-XX：与相同-X，但还会显示以太网标头。
-D ：显示可用接口列表
-l ：行可读输出（用于保存时查看或发送至其他命令）
-q ：输出内容不那么冗长（更安静）。
-t ：提供人类可读的时间戳输出。
-tttt ：提供最大的人类可读时间戳输出。
-i eth0 ：在eth0接口上监听。
-vv ：详细输出（更多的v提供更多输出）。
-c：仅获取x个数据包，然后停止。
-s：以字节为单位定义捕获的快照长度（大小）。使用-s0得到的一切，除非你是有意捕捉少。
-S ：打印绝对序列号。
-e ：也获取以太网头。
-q ：显示较少的协议信息。
-E ：通过提供加密密钥来解密IPSEC通信。
一切都取决于组合
能够单独完成这些事情的功能很强大，但是真正的魔力在于tcpdump能够以创造性的方式组合选项以准确隔离您要查找的内容。可以通过三种方式进行组合，如果您完全学习了编程，那么它们将对您非常熟悉。

与
and或&&
或
or或||
除
not或!
原始输出视图
使用此组合可查看详细的输出，不解析主机名或端口号，使用绝对序列号并显示人类可读的时间戳。

tcpdump -tt nn vv S

以下是一些组合命令的示例。

来自特定IP并发往特定端口
让我们找到从10.5.2.3到端口3389上任何主机的所有流量。

tcpdump -nnvvS src 10.5.2.3 和 dst端口3389

从一个网络到另一个
让我们看一下所有来自192.168.xx并进入10.x或172.16.xx网络的流量，并且我们显示的十六进制输出没有主机名解析，并且具有额外的冗长程度。

tcpdump -nvX src网192.168.0.0/16 和 dst网10.0.0.0/8 或 172.16.0.0/16

到特定IP的非ICMP流量
这将向我们显示去往192.168.0.2而不是 ICMP的所有流量。

tcpdump dst 192.168.0.2 和 src net 而 不是icmp

来自不在特定端口上的主机的流量
这将向我们显示来自不是SSH流量的主机的所有流量（假设使用默认端口）。

tcpdump -vv src mars 而 不是 dst port 22

如您所见，您可以构建查询以查找所需的任何内容。关键是要首先弄清楚正是你要找的是什么，然后建立语法流量的特定类型的隔离。

请记住，在构建复杂的查询时，可能必须使用单引号将选项分组。使用单引号来指示tcpdump忽略某些特殊字符，在这种情况下，在“（）”括号下面。同样的技术可以使用其他表现形式，例如被用于组host，port，net等。

tcpdump'src 10.0.2.4和 （dst端口3389或22）'

隔离TCP标志
您还可以使用过滤器隔离设置了特定TCP标志的数据包。

隔离TCP RST标志。
下面的过滤器可以找到这些各种数据包，因为它tcp[13]查看TCP报头中的偏移量13，数字表示字节中的位置，并且！= 0表示所讨论的标志设置为1，即它处于打开状态。
tcpdump的'TCP [13]＆ 4！= 0 '
tcpdump的'TCP [tcpflags] == TCP-RST '

隔离TCP SYN标志。
tcpdump的'TCP [13]＆ 2！= 0 '
tcpdump的'TCP [tcpflags] == TCP-SYN '

隔离同时设置了SYN和ACK标志的数据包。
tcpdump'tcp [13] = 18 '

tcpdump的标志字段输出中仅显示PSH，RST，SYN和FIN标志。显示了URG和ACK，但它们显示在输出中的其他位置，而不是标志字段中。
隔离TCP URG标志。
tcpdump的'TCP [13]＆ 32！= 0 '
tcpdump的'TCP [tcpflags] == TCP-URG '

隔离TCP ACK标志。
tcpdump的'TCP [13]＆ 16！= 0 '
tcpdump的'TCP [tcpflags] == TCP-ACK '

隔离TCP PSH标志。
tcpdump的'TCP [13]＆ 8！= 0 '
tcpdump的'TCP [tcpflags] == TCP-PSH '

隔离TCP FIN标志。
tcpdump的'TCP [13]＆ 1！= 0 '
tcpdump的'TCP [tcpflags] == TCP-鳍 '

日常食谱示例
由于tcpdump可以输出ASCII格式的内容，因此您可以使用它使用其他命令行工具（例如）来搜索明文内容grep。
最后，既然我们不了解这一理论，那么这里有许多快速食谱可用于捕获各种流量。

SYN和RST集
tcpdump'tcp [13] = 6'

查找HTTP用户代理
该-l开关可让您在捕获流量时查看其流量，并在发送至这类命令时提供帮助grep。
tcpdump -vvAls0 | grep '用户代理：'

明文GET请求
tcpdump -vvAls0 | grep'GET '

查找HTTP主机头
tcpdump -vvAls0 | grep '主机：'

查找HTTP Cookie
tcpdump -vvAls0 | grep'Set -Cookie | Host：| Cookie：'

查找SSH连接
无论连接进入哪个端口，此命令都可以工作，因为它会收到标语响应。

tcpdump的'TCP [（TCP [12] >> 2）：4] = 0x5353482D'

查找DNS流量
tcpdump -vvAs0 端口 53

查找FTP流量
tcpdump -vvAs0 端口 ftp或ftp-data

查找NTP流量
tcpdump -vvAs0 端口 123

查找明文密码
tcpdump 端口http或端口ftp或端口smtp或端口imap或端口pop3或端口telnet -lA | egrep -i -B5'pass = | pwd = | log = | login = | user = |用户名= | pw = | passw = | passwd = | password = | pass：| user：|用户名：|密码：|登录名： |通过|用户'

使用恶意比特查找流量
IP标头中有一个永远不会被合法应用程序设置的位，我们称之为“邪恶位”。这是一个有趣的过滤器，用于查找已切换到的数据包。

tcpdump'ip [6]＆128！= 0 '

也请查看我的其他教程。

摘要
这是外卖。

tcpdump对于任何想要进入网络或信息安全的人来说，它是一个有价值的工具。
它与流量交互的原始方式，加上它在检查数据包方面提供的精度，使其成为学习TCP / IP的最佳工具。
像Wireshark这样的协议分析器很棒，但是如果您想真正掌握Packet-fu，则必须tcpdump首先与之兼容。
好的，这本入门书应该使您变得更强大，但是手册页对于最高级和一次性的使用场景应该总是很方便的。我真的希望这对您有用，如果您有任何疑问，请随时与我联系。

笔记
我目前（有点）在tcpdump上为No Starch Press写一本书。
领先的形象来自securitywizardry.com。
一些隔离滤波器是从sébastienwains借来的。
感谢hackertarget.com上的Peter启发了新的目录（简化），并感谢2018年7月添加的其他一些更高级别的协议过滤器。
对于TCP标志字谜是：ü nskilled 甲 ttackers p酯[r eal 小号 ecurity ˚f olk。


参考:
    https://danielmiessler.com/study/tcpdump/