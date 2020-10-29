# Lambda 无需预置或管理服务器 即可运行代码，按使用时间计费
	只需上传代码，Lambda将处理运行和扩展高可用性代码所需的一切工作。 
	可以设置代码自动从其他AWS服务触发，或者直接从任何Web或移动应用程序调用。

	使用案例
	数据处理
		响应数据更改，系统状态变化或用户操作等触发器。 Lambda 可以由S3,DynamoDB,Kinesis,SNS, CloudWatch 等AWS服务直接触发，可以连接到现有EFS文件系统。 也可也通过AWS Step Functions编排到工作流程中。   
		构建各种实时的无服务器 数据处理系统。
	实时文件处理
		可以使用Amazon S3 触发AWS Lambda， 以便在上传数据后立即处理。
		可以直连到现有 Amazon EFS文件系统，支持大规模文件处理，进行大规模并行共享访问。
		如： Lambda 实时创建缩略图，视频代码转换，建立文件索引，处理日志，验证内容，聚合和筛选数据。
		比如可以使用Lambda来调整图片大小，来展示在不同的设备上。
		示例代码： https://github.com/aws-samples/lambda-refarch-fileprocessing
	实时数据流处理
		使用AWS Lambda 和 Amazon Kinesis 处理实时流数据。从而跟踪应用程序获得，处理事务处理顺序，分析单击数据流，整理数据，生成指标，筛选日志，建立索引，分析社交媒体。 遥测和计量 IoT设备数据。
		示例代码：https://github.com/aws-samples/lambda-refarch-streamprocessing

	机器学习
		使用AWS Lambda 将数据输入到机器学习模型前进行预处理，通过Lambda访问EFS，还可以提供模型进行大规模预测，无需预置和管理任何设施。
		AWS Lambda Serverless 机器学习训练和预测。

	后端
		使用AWS Lambda 构建无服务器后端，处理Web，移动，物联网IoT和第三方API请求，充分利用Lambda始终如一的高性能控制。
		如多内存配置，预配置并发，以便构建任何规模的延迟敏感应用。

    Web应用程序
    	通过AWS Lambda 与其他AWS服务结合，开发人员构建功能强大的Web应用程序。从而自动扩展和收缩，跨多个数据中心在高可用配置中运行，无需在可扩展，备份，多数据中心冗余方面做任何管理工作
    	示例代码：https://github.com/aws-samples/lambda-refarch-webapp

    IoT后端
    	使用 AWS Lambda 构建无服务器后端，以处理 Web、移动、物联网 (IoT) 和第 3 方 API 请求
    	示例代码：https://github.com/aws-samples/lambda-refarch-iotbackend
    移动后端
    	使用AWS Lambda 和 Amazon API Gateway 构建后端，以验证和处理API请求。
    	使用AWS Amplify轻松将后端与 IOS，Android，Web，React Native前端集成。
    	示例代码：https://github.com/aws-samples/lambda-refarch-mobilebackend
## lambda cli调用
	同步调用
		aws lambda invoke --function-name my-function --payload '{ "key": "value" }'
 response.json

 	异步调用
 	    aws lambda invoke --function-name my-function --invocation-type Event --payload
 '{ "key": "value" }' response.json
 	支持以下异步调用目标
 		• Amazon SQS – 标准 SQS 队列。
		• Amazon SNS – SNS 主题。
		• AWS Lambda – Lambda 函数。
		• Amazon EventBridge – EventBridge 事件总线。

	运行时
    AWS Lambda 运行时 (p. 117)是围绕不断进行维护和安全更新的操作系统、编程语言和软件库的组合构建
的。当安全更新不再支持某个运行时组件时，Lambda 将弃用该运行时

## X-Ray 跟踪-- web控制台 
	X-Ray 将处理这些数据以生成服务映射和可搜索的跟踪摘要
	AWS X-Ray 守护程序是在Lambda 环境中运行，并侦听包含分段和子分段的 UDP 流量的应用程序。它缓冲传入的数据并将其分批写入
	X-Ray，从而减少跟踪调用所需的处理和内存开销。

	lambda主动跟踪，为 my-function 的函数启用主动跟踪
	aws lambda update-function-configuration --function-name my-function \
--tracing-config Mode=Active

	AWS CloudFormation启用主动跟踪  P289
	对 AWS CloudFormation 模板中的 AWS::Lambda::Function 资源启用活动跟踪，请使用TracingConfig 属性。
	Example function-inline.yml – 跟踪配置


## 综合示例py--Blank函数
	Blank 函数示例应用程序是一个初学者应用程序，它演示 Lambda 中使用一个调用 Lambda API 的函数执行的常见操作。它显示日志记录、环境变量、AWS X-Ray 跟踪、层、单元测试和 AWS 开发工具包的使用情况。
		
	https://github.com/awsdocs/aws-lambda-developer-guide/tree/master/sample-apps/blank-python
	 一个 Python 函数，用于显示日志记录、环境变量、 AWS X-Ray 跟踪、层、单元测试和 AWS 开发工具包的使用情况



