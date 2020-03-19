import tornado.web
import tornado.auth

class GoogleOAuth2LoginHandler(tornado.web.RequestHandler,
                               tornado.auth.GoogleOAuth2Mixin):
    """google 认证方式
    使用OAuth2的Google身份验证。

    为了使用，请向Google注册您的应用程序，然后复制
    与您的应用程序设置相关的参数。

    *转到http://console.developers.google.com上的Google Dev Console。
    *选择一个项目，或创建一个新项目。
    *在左侧边栏中，选择API和身份验证。
    *在API列表中，找到Google+ API服务并将其设置为ON。
    *在左侧边栏中，选择“凭据”。
    *在页面的OAuth部分中，选择创建新客户端ID。
    *将重定向URI设置为指向您的身份验证处理程序
    *将“客户端机密”和“客户端ID”复制为应用程序设置为
      ``{“ google_oauth”：{“密钥”：CLIENT_ID，“秘密”：CLIENT_SECRET}}``
    .. testcode::

            class GoogleOAuth2LoginHandler(tornado.web.RequestHandler,
                                           tornado.auth.GoogleOAuth2Mixin):
                async def get(self):
                    if self.get_argument('code', False):
                        access = await self.get_authenticated_user(
                            redirect_uri='http://your.site.com/auth/google',
                            code=self.get_argument('code'))
                        user = await self.oauth2_request(
                            "https://www.googleapis.com/oauth2/v1/userinfo",
                            access_token=access["access_token"])
                        # Save the user and access token with
                        # e.g. set_secure_cookie.
                    else:
                        await self.authorize_redirect(
                            redirect_uri='http://your.site.com/auth/google',
                            client_id=self.settings['google_oauth']['key'],
                            scope=['profile', 'email'],
                            response_type='code',
                            extra_params={'approval_prompt': 'auto'})

        .. testoutput::
           :hide:

    """
    async def get(self):
        if self.get_argument('code', False):
            user = await self.get_authenticated_user(
                redirect_uri='http://your.site.com/auth/google',
                code=self.get_argument('code'))
            # Save the user with e.g. set_secure_cookie
        else:
            await self.authorize_redirect(
                redirect_uri='http://your.site.com/auth/google',
                client_id=self.settings['google_oauth']['key'],
                scope=['profile', 'email'],
                response_type='code',
                extra_params={'approval_prompt': 'auto'})



class TwitterLoginHandler(tornado.web.RequestHandler,
                          tornado.auth.TwitterMixin):
    """
    twitter 认证
    Twitter OAuth身份验证。

    要通过Twitter进行身份验证，请使用进行注册
    Twitter，网址为http://twitter.com/apps。然后复制您的消费者密钥
    和应用程序的消费者秘密
    ~~ tornado.web.Application.settings```twitter_consumer_key``和
    ``twitter_consumer_secret``。在处理程序上使用此mixin
    您注册为应用程序的回调URL的URL。

    设置您的应用程序后，您可以像这样使用mixin
    使用Twitter验证用户身份并访问其流：

    .. testcode::

        class TwitterLoginHandler(tornado.web.RequestHandler,
                                  tornado.auth.TwitterMixin):
            async def get(self):
                if self.get_argument("oauth_token", None):
                    user = await self.get_authenticated_user()
                    # Save the user using e.g. set_secure_cookie()
                else:
                    await self.authorize_redirect()

    .. testoutput::
       :hide:

    〜OAuthMixin.get_authenticated_user返回的用户对象
    包括属性``username''，``name''，``access_token''，
    以及在上介绍的所有自定义Twitter用户属性
    https://dev.twitter.com/docs/api/1.1/get/users/show
    """
    async def get(self):
        if self.get_argument("oauth_token", None):
            user = await self.get_authenticated_user()
            # Save the user using e.g. set_secure_cookie()
        else:
            await self.authorize_redirect()

