import random

from PIL import Image
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from axf.models import Category, Child, Product, AxfUser
from django.core.cache import cache
import uuid
from django.contrib.auth import logout
import os
import io
from axf.views_func import upfileIimgBytes, upfileImgLocal
# Create your views here.


def index(request):
    # return HttpResponse("welcome\r to axf!")
    return render(request, "common/base.html")

def home(request):
    return render(request, "home/home.html")
def market(request, gid, cid, sid):
    # 获取商品组信息 按sort字段排序
    categories = Category.objects.all().order_by("sort")
    # 获取商品子组信息
    childs = Child.objects.filter(category_id=gid)
    # 获得该组元素对应的商品信息
    products = Product.objects.filter(category_id=gid)
    # 获取子组元素对应的商品信息
    if cid != "0":
        products = products.filter(child_id=cid)
    if sid == "1":
        products = products.order_by("sort")
    elif sid == "2":
        products = products.order_by("price")
    elif sid == "3":
        products = products.order_by("-price")
    return render(request, "market/market.html",
                  {"categories": categories, "childs": childs, "products": products, "gid": gid, "cid": cid})
def cart(request):
    return render(request, "cart/cart.html")

def mine(request):
    phone = request.session.get("phone")
    user = None
    if phone:
        user = AxfUser.objects.get(pk=phone)
    return render(request, "mine/mine.html", {"phone": phone, "user": user})


def login(request):
    # 如果是未登录页面 返回login页面
    if request.method == "GET":
        path = request.GET.get("from")
        return render(request, "mine/login.html", {"path": path})
    else:
        # 拿到手机号码 判断redis中是否存在
        phone = request.POST.get("phone")
        newTokenValue = str(uuid.uuid4())
        # 判断redis中手机号是否存在
        if cache.get(phone):
            # 用户存在(手机号和tokenValue在)
            user = AxfUser.objects.get(pk=phone)
            user.token = newTokenValue
            # 重定向到原来界面
            # 为什么是GET而不是POST
            userUrl = "/" + request.GET.get("from") + "/"

        else:
            # 不存在则创建用户
            user = AxfUser.create(phone, newTokenValue, None)
            # 重定向到upImage
            userUrl = "/upImage/"
        user.save()
        # 状态保持, 手机号存到session中
        request.session["phone"] = phone
        # 同步到redis缓存
        cache.set(phone, newTokenValue)
        # 将newTokenValue写入cookie
        response = redirect(userUrl)
        response.set_cookie("token", newTokenValue)
        return response

# 将图片写成byte文件上传到阿里云的oss中
def upImage(request):
    if request.method == "GET":
        return render(request, "mine/upImage.html")
    else:
        for key in request.FILES:
            files = request.FILES.getlist(key)
            for file in files:
                fileName = str(uuid.uuid4()) + ".jpg"
                imgage = Image.open(file)
                # 这一步可以放到celery 中
                imgByte = io.BytesIO()
                imgage.save(imgByte, "png")
                url = upfileIimgBytes(fileName, imgByte.getvalue())
                # 找到当前用户
                phone = request.session.get("phone")
                user = AxfUser.objects.get(pk=phone)
                # usr的图片存储网址
                user.img = url
                user.save()
        return redirect("/mine/")

# 用短信发送验证码
def verifyCode(request):
    string = '1234567890'
    # 随机选取6个值作为验证码
    rand_str = ''
    for i in range(0, 6):
        rand_str += str(random.randrange(0, len(string)))
    # 使用阿里云发短信
    # 得到要接收验证码的手机号
    """
    # 得到前端传递来的data：{"phone": $("#phone").val()}中key值phone对应的键值：要接收验证码的手机号
    phone = request.GET.get("phone")
    text = "您的验证码是：%s。请不要把验证码泄露给其他人。" % rand_str
    send_sms(text, phone)
    """
    # 验证码存储到session中
    request.session["verifyCode"] = rand_str
    # 返回JsonResponse 数据给前端
    return JsonResponse({"error": 0, "data": {"verifyCode": rand_str}})


def quit(request):
    logout(request)
    response = redirect("/mine/")
    response.delete_cookie("token")
    return response



"""
# 上传到阿里云本地静态文件中,再上传到阿里云的oss中
def upImage(request):
    if request.method == "GET":
        return render(request, "mine/upImage.html")
    else:
        for key in request.FILES:
            files = request.FILES.getlist(key)
            for file in files:
                fileName = str(uuid.uuid4()) + ".jpg"
                filePath = os.path.join(settings.MEDIA_ROOT, fileName)
                with open(filePath, "wb") as fp:
                    for info in file.chunks():
                        fp.write(info)
                url = upfileImgLocal(fileName, filePath)
                # 找到当前用户
                phone = request.session.get("phone")
                user = AxfUser.objects.get(pk=phone)
                # usr的图片存储网址
                user.img = url
                user.save()
        return redirect("/mine/")
"""
