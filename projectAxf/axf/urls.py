
from django.conf.urls import url
from axf import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', views.login),
    url(r'^home/$', views.home),
    url(r'^market/(\w+)/(\w+)/(\w+)/$', views.market),
    url(r'^cart/$', views.cart),
    url(r'^mine/$', views.mine),
    url(r'^verifyCode/$', views.verifyCode),
    url(r'^upImage/$', views.upImage),
    url(r'^quit/$', views.quit),

]
