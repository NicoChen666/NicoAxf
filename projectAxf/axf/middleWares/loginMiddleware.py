from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.core.cache import cache

class LoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        #在点击购物车页面时判断
        if request.path in ["/cart/"]:
            #验证是否登录
            phone = request.session.get("phone")
            path = request.GET.get("from")
            if not phone:
                #没有状态保持，说明未登录
                return redirect("/login/?from=%s" % path)
            #获取缓存
            token1 = cache.get(phone)
            token2 = request.COOKIES.get("token")
            if token1 != token2:
                return redirect("/login/?from=%s" % path)
            return None
