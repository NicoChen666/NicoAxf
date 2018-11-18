import oss2
from django.conf import settings


#将阿里云本地文件上传到阿里云的oss中
def upfileImgLocal(imgKey, imgPath):
    auth = oss2.Auth('LTAId5fbxTNHSEmG', 'zJ7lnFKouqQXJGhVYfZ3nirNfQsVpU')
    bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com', 'nicoaxf')
    bucket.put_object_from_file(imgKey, imgPath)
    # 生成url
    style = 'image/resize,m_fixed,w_100,h_100'
    url = bucket.sign_url('GET', imgKey, 60 * 60 * 24 * 300, params={'x-oss-process': style})
    return url

# 上传到阿里云的oss中
def upfileIimgBytes(imgKey, imgBytes):
    # 阿里云oss 配置
    auth = oss2.Auth('LTAId5fbxTNHSEmG', 'zJ7lnFKouqQXJGhVYfZ3nirNfQsVpU')
    bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com', 'nicoaxf')
    bucket.put_object(imgKey, imgBytes)
    # 生成url
    style = 'image/resize,m_fixed,w_100,h_100'
    url = bucket.sign_url('GET', imgKey, 60 * 60 * 24 * 300, params={'x-oss-process': style})
    return url