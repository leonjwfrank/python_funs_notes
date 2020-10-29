# TLS/SSL  
	两点之间加密，包括，客户端/服务器， 服务器/服务器， 客户端/客户端
	服务器/客户端协商
		为了进行SSL / TLS协商，系统管理员必须准备至少2个文件：  私钥和证书。当从证书颁发机构（例如DigiCert Trust Services）请求时，必须创建一个附加文件。此文件称为  从私有密钥生成的证书签名请求。生成文件的过程取决于将使用文件进行加密的软件

	大多数客户端信任从证书颁发机构请求的证书，但是可能需要在服务器安装称为中间证书颁发机构证书。
	取决于服务器软件。通常不需要在客户端应用程序或浏览器上安装中间或根证书


# 标准SSL握手
	使用RSA 密钥交换算法时的标准SSL握手
	1，client hello， 
		服务器使用SSL与客户端进行通信所需信息。包括SSL 版本，密码设置，特定会话数据。
	2，server hello
		服务器使用SSL与客户端进行通信所需信息。包括SSL 版本，密码设置，特定会话数据。
	3，身份验证和预掌握密码
		客户端验证服务器证书。 exp: 通用名称/日期/颁发者。 
		客户端（取决于密码）为会话创建主密码。使用服务器公钥加密。
		将加密的主密码发送到服务器。
    4，解密和主密钥
    	服务器使用私钥解密主密码。
    	服务器与客户端均执行步骤以生成具有商定密码的主密钥。
    5，使用会话密钥加密。
    	客户端/服务器都交换信息，以通知将来的消息将被加密。

    简单过程见本文中的 Sample_code_used in SSL_handshake.pdf

# 证书的区别，客户端证书与服务端证书
	客户端证书
		标识客户端或用户。 向服务器验证客户端并准确确定其身份。

	服务器证书
		服务器或SSL证书，通常颁发给所有者的主机名(如XX-SERVER-01)或域名(www.example.com)。
		用于验证站点的所有者。
		Web浏览器访问服务器，并验证SSL服务器证书真实(由证书颁发机构验证)。
		比如电子商务网站。

		如何获取:
			网站运营商通过向签名请求证书提供者(证书颁发机构)提出申请来获得证书。一个电子文档，字符格式的字符串。
			包括所有基本信息:网站名称。联系电子邮件地址。公司信息等。
			颁证机构对请求进行签名，产生一个公共证书，该证书将提供给连接到该网站的任何web浏览器。DNS解析？
			比如颁证机构在发布证书前，将向公共域名注册商核对电子邮件地址是否与证书请求中提供的一致。

			此外，配置网站来确定任何希望连接的用户都需要提供客户端证书以及有效用户名和密码。
			这就是启用双重认证。 “您知道的东西，您拥有的东西。”

			证书时匿名的终结。 但是可以保证信任。


# 从HTTP移植到HTTPS
	
	使用这些步骤来帮助您计划，方便您的网站迁移
	1，从安全角度评估你的网站；
		准备一个当前HTTP的URL列表，把他们映射到HTTPS网站相应位置。 
		并验证所有外部脚本和图像都可以与HTTPS一起使用。
	2，充分发挥网站备份功能。
		更改你的网站任何内容时，都应该备份你的网站。向托管服务商和运营商了解备份内容。
	3，选择正确的证书。
		 Obtain an SSL/TLS certificate from a reputable certificate authority like Letencripty, who can offer guidance and technical 
		support as a part of enabling HTTPS for your website.
		选择信誉良好的 TLS/SSL 证书服务商。 类似于Letencripty，他们可以提供指导和技能支持。这些都作为启用网站加密的一部分。
	4， 安装和测试证书
		Ensure your SSL certificates are properly installed. Symantec offers a free tool called CryptoReport that allows you to test 
		your SSL/TLS certificates and view any browser warnings.
		确认你的SSL 证书被适当的安装了。 赛门铁克提供一个免费工具https://ssltools.digicert.com/checker/，这允许你测试你的TLS/SSL证书，并查看任何浏览器警告。
	5，删除混合内容
		Replace all HTTP references with HTTPS pointers. If you don’t remove mixed content, some pages will not be displayed, “Not Secure” warnings may appear in browser windows and your entire site will be less secure.
		HTTP到 HTTPS 全部的映射完成后，如果你不删除HTTP相关的这些混合内容，一些页面将不被显示。 不安全的警告将永远存在一些站点，导致整个站点安全性降低。

	6， 保持证书合规
		Stay compliant by keeping your website updated with the latest security requirements and standards. Check the CA/Browser Forum and NIST for SSL/TLS standards, and PCI if your site accepts payments.
		保持你站点合乎于 最新的 安全规范和标准。 检查 证书和浏览器论坛 以及NIST（SSL/TLS）标准(https://csrc.nist.gov/News/2019/nist-publishes-sp-800-52-revision-2)，以及PCI 如果你的站点选择的付款方式。

	7, 重定向HTTP从HTTPS流量
		Ensure that all instances of HTTP traffic are redirected to HTTPS. Set up 301 redirects to notify search engines of your new HTTPS address.
		确保所有HTTP实例重定向到HTTPS， 设301重定向错误码并提示用户访问你的新的HTTPS站点。

	8，实施自动扫描系统
		Identify non-compliant elements and third-party content. Replace unsecured content with safer alternatives. Where possible, use verified and accountable third-party technology

		识别不合规定的元素和第三方内容。 替换不安全的内容，转而使用安全内容/如果可能，使用检验后的的和认证的第三方技术。
	9，使用HTTPOnly 和 安全缓存设置去保证 黑客无法破坏你的站点
		Use both the “HttpOnly” and “Secure” cookie settings to 
		ensure that hackers can’t break into your website.

	10，实施HTTP严格的传输协议。
		IMPLEMENT HTTP STRICT TRANSPORT SECURITY
		HTTP Strict Transport Security (HSTS) is a standard that protects your website visitors by ensuring they are connected over HTTPS. Make sure that all connections are only accessible via HTTPS and include HSTS in the HTTP response reader.
		HTTPS安全传输协议，是确保你的所有访问者都可以通过HTTPS来访问你站点的所有内容。 保证所有内容都在HTTPS访问并在HTTP响应。

# 量子加密安全
量子后密码学
为量子安全的未来做准备
几乎所有的数字通信都由三种加密系统保护：公钥加密，数字签名和密钥交换。

在当今的公钥基础结构中，这些系统是使用RSA或ECC非对称密码算法实现的。RSA和ECC密码学依赖一种称为计算硬度的假设，即理论数问题（例如整数分解或离散对数问题）没有有效解决方案的假设。但是，这些假设基于经典计算机的处理能力。

1994年，Peter Shor证明了使用功能强大的量子计算机和特定的算法（后来称为Shor's算法）可以很容易地打破依赖于计算硬度假设的非对称算法。实际上，具有足够量子位和电路深度的量子计算机可以立即破解非对称算法。ASC X9量子计算风险研究小组发布的一项研究估算了这些确切要求。

算法	所需的逻辑量子位	所需电路深度
RSA-2048	4700	8 10 ^ 9
ECC NIST P-256	2330	1.3 10 ^ 11 2

大多数专家估计，在未来20年内，将构建具有所需量子比特和电路深度的足够强大的量子计算机，以破解RSA和ECC密钥。
量子计算机对非对称密码算法构成了最大的威胁。这意味着用于对证书进行数字签名和处理初始SSL / TLS握手的密码系统都是潜在的攻击媒介。
但是AES这类的对称加密算法似乎可以抵抗量子加密攻击。  从AES-128到AES-256 这是因为对称密钥基于伪随机字符串，并且需要使用蛮力攻击或利用某种已知的漏洞来破坏加密，而不是使用算法（例如，Shor算法）来破坏非对称密钥密码学。

信任链
量子计算机构成的最危险的攻击媒介可能是数字证书使用的信任链（证书链）。RSA和ECC非对称密码算法用于信任链的每个级别中-根证书对自身和中间证书进行签名，而中间证书对最终实体证书进行签名

如果量子计算机能够计算中间证书或根证书的私钥，那么构建PKI的基础将崩溃。通过访问私钥，威胁参与者可以颁发欺诈性证书，这些证书在浏览器中将自动被信任。而且与最终实体证书不同，替换根证书绝非易事。


#  词汇
##	SSL词汇表


256位加密 256-bit encryption
Process of scrambling an electronic document using an algorithm whose key is 256 bits in length. The longer the key, the stronger it is.
使用密钥长度为256位的算法对电子文档进行加扰的过程。密钥越长，密钥越强。

A

非对称密码学  Asymmetric cryptography
These are ciphers that imply a pair of 2 keys during the encryption and decryption processes. In the world of SSL and TLS, we call them public and private keys.
这些密码在加密和解密过程中暗示一对2个密钥。在SSL和TLS的世界中，我们称它们为公钥和私钥。

C

证书签名请求（CSR）Certificate signing request (CSR)
Machine-readable form of a DigiCert certificate application. A CSR usually contains the public key and distinguished name of the requester.
DigiCert证书申请的机器可读形式。CSR通常包含请求者的公钥和专有名称。

认证机构（CA） Certification authority (CA)
Entity authorized to issue, suspend, renew, or revoke certificates under a CPS (Certification Practice Statement). CAs are identied by a distinguished name on all certificates and CRLs they issue. A Certification Authority must publicize its public key, or provide a certificate from a higher level CA attesting to the validity of its public key if it is subordinate to a Primary certification authority. DigiCert is a Primary certification authority (PCA)
根据CPS（认证实践声明）被授权发行，暂停，更新或吊销证书的实体。在颁发的所有证书和CRL上，CA均以可分辨的名称标识。证书颁发机构必须公开其公钥，或者如果它隶属于主证书颁发机构，则必须提供更高级别的CA证明其公钥的有效性的证书。DigiCert是主要的证书颁发机构（PCA）。

密码套件 Cipher suite
This is a set of key exchanges protocols which includes the authentication, encryption and message authentication algorithms used within SSL protocols.
这是一组密钥交换协议，其中包括SSL协议中使用的身份验证，加密和消息身份验证算法。

通用名（CN） Common name (CN)
Attribute value within the distinguished name of a certificate. For SSL certificates, the common name is the DNS host name of the site to be secured. For Software Publisher Certificates, the common name is the organization name.
证书的专有名称中的属性值。对于SSL证书，通用名称是要保护的站点的DNS主机名。对于Software Publisher Certificates，通用名称是组织名称。

连接错误 Connection error
When security issues preventing a secure session to start are flagged up while trying to access a site.
尝试访问站点时，会标记出阻止安全会话启动的安全问题。

d

Domain Validation (DV) SSL Certificates    域验证（DV）SSL证书
The most basic level of SSL certificate, only domain name ownership is validated before the certificate is issued.
最基本的SSL证书级别，在颁发证书之前仅验证域名所有权。


E
Elliptic Curve Cryptography (ECC)   椭圆曲线密码学（ECC）
Creates encryption keys based on the idea of using points on a curve to dene the public/private key pair. It is extremely difficult to break using the brute force methods often employed by hackers and offers a faster solution with less computing power than pure RSA chain encryption.
基于使用曲线上的点定义公钥/私钥对的想法来创建加密密钥。使用黑客经常使用的暴力破解方法很难破解，并且提供了一种比纯RSA链加密更快的解决方案，并且计算能力更低。

加密  Encryption
Process of transforming readable (plaintext) data into an unintelligible form (ciphertext) so that the original data either cannot be recovered (one-way encryption) or cannot be recovered without using an inverse decryption process (two-way encryption).
将可读（纯文本）数据转换为难以理解的形式（密文）的过程，这样原始数据要么无法恢复（单向加密），要么无法恢复因为无反向解密过程（双向加密）。

Extended Validation (EV) SSL Certificates    扩展验证（EV）SSL证书
The most comprehensive form of secure certificate which validates domain, require very strict authentication of the company and highlights it in the address bar.
安全证书的最全面形式，用于验证域，要求对公司进行非常严格的身份验证，并在地址栏中突出显示该证书。

K
密钥交换 Key change
This is the way users and server securely establish a pre-master secret for a session.
这是用户和服务器安全地建立会话的主控机密的方式。

M

Master secret   主密钥
The key material used for generation of encryption keys, MAC secrets and initialization vectors.
用于生成加密密钥，MAC机密和初始化向量的密钥材料。

Message Authentication Code (MAC)   消息验证码（MAC）
A one way hash function arranged over a message and a secret.
一种安排在消息和机密之上的单向哈希函数。

Ø

Organization Validation (OV) SSL Certificates   组织验证（OV）SSL证书
A type of SSL certificate that validates ownership of the domain and the existence of the organization behind it.
一种SSL证书，用于验证域的所有权以及域背后组织的存在。

P


Pre-master secret    预主密钥预告
The key material used for the master secret derivation.
用于主密钥推导的密钥材料。


Public key infrastructure (PKI)    公钥基础结构（PKI）
Architecture, organization, techniques, practices, and procedures that collectively support the implementation and operation of a certificate-based public key cryptographic system. The PKI consists of systems that collaborate to provide and implement the public key cryptographic system, and possibly other related services.
共同支持基于证书的公钥密码系统的实现和操作的体系结构，组织，技术，实践和过程。PKI由协作提供和实现公钥密码系统以及可能其他相关服务的系统组成。

S

Secure servers    安全服务器
Server that protects host web pages using SSL or TLS. When a secure server is in use, the server is authenticated to the user. In addition, user information is encrypted by the user's web browser's SSL protocol before being sent across the Internet. Information can only be decrypted by the host site that requested it.
使用SSL或TLS保护主机网页的服务器。使用安全服务器时，服务器将向用户验证身份。此外，在通过Internet发送之前，用户信息已通过用户的Web浏览器的SSL协议加密。信息只能由请求它的主机站点解密。

SAN (Subject Alternative Name) SSL certificates  SAN（主题备用名称）SSL证书
Type of certificate which allows multiple domains to be secured with one SSL certificate.
允许使用一个SSL证书保护多个域的证书类型。

SSL协议
Stands for secure sockets layer. Protocol for web browsers and servers that allows for the authentication, encryption and decryption of data sent over the Internet.
代表安全套接字层。Web浏览器和服务器的协议，允许对通过Internet发送的数据进行身份验证，加密和解密。

SSL certificate    SSL证书
Server certificate that enables authentication of the server to the user, as well as enabling encryption of data transferred between the server and the user. SSL certificates are sold and issued directly by DigiCert, and through the DigiCert PKI Platform for SSL Center.
服务器证书，用于对用户进行服务器身份验证，并对服务器和用户之间传输的数据进行加密。SSL证书由颁证机构(如DigiCert，Let'sEncryption)直接销售和颁发，并通过DigiCert PKI SSL Center平台提供。

SSL Handshake    SSL握手
A protocol used within SSL for the purpose of security negotiation.
SSL中用于安全协商的协议。

对称加密
Encryption method that imply the same key is used both during the encryption and decryption processes.
在加密和解密过程中都使用暗示相同密钥的加密方法。


TCP协议
Transmission control protocol, one of the main protocols in any network.
传输控制协议，任何网络中的主要协议之一。


Wildcard SSL certificates 	通配符SSL证书
Type of certificate used to secure multiple subdomains.
用于保护多个子域的证书的类型。

