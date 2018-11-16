from django.shortcuts import render, redirect
from django.http import HttpResponse
from axf.models import Category, Child, Product
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
    return render(request, "mine/mine.html")
