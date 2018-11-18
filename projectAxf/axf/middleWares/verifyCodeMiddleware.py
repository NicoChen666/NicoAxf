from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class VerifyCodeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/login/" and request.method == "POST":
            verifyCodePost = request.POST.get("verifyCode")
            verifyCodeSession = request.session.get("verifyCode")
            # phonePost = request.POST.get("phone")
            # phoneSession = request.session.get("phone")
            # 验证码不一样 或者手机号不一样
            if verifyCodePost != verifyCodeSession:
                # 重定向到注册页面(可以试试反向解析）
                return redirect("/login/")
            # 验证码一样 请求继续执行
            return None
