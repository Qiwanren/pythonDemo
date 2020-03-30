import hmac
import hashlib
import base64


def jm_sha256(key, value):
    """
    sha256加密
    return:加密结果转成16进制字符串形式
    """
    hsobj = hashlib.sha256(key.encode("utf-8"))
    hsobj.update(value.encode("utf-8"))
    return hsobj.hexdigest()


print(jm_sha256("snsd", "我是sha256加密"))
# 1c1b963b4af90a0685d071a281af8d721451763765be160664cb83d6da6c1d3b


def jm_md5(key, value):
    """
    md5加密
    return:加密结果转成16进制字符串形式
    """
    hsobj = hashlib.md5(key.encode("utf-8"))
    hsobj.update(value.encode("utf-8"))
    return hsobj.hexdigest()


print(jm_sha256("snsd", "我是md5加密"))
# fed0ad1f56d4fc52017a7bf32561845444eec1cdae7065ea8f6b37abf076756b


def hmac_sha256(key, value):
    """
    hmacsha256加密
    return:加密结果转成16进制字符串形式
    """
    message = value.encode('utf-8')
    return hmac.new(key.encode('utf-8'), message, digestmod=hashlib.sha256).hexdigest()


print(hmac_sha256("snsd", "我是hmacsha256加密"))
# db8b895abc88a59cf8776a233ee1457c7239380347ef4dca8e48bc88433167eb


def hmac_md5(key, value):
    """
    hmacmd5加密
    return:加密结果转成16进制字符串形式
    """
    message = value.encode('utf-8')
    return hmac.new(key.encode('utf-8'), message, digestmod=hashlib.md5).hexdigest()


print(jm_sha256("snsd", "我是hmacmd5加密"))
# e2f8b511b75e5955d251b601494c392fe536b860ff6f1fa8f2157bc88cff9b59


def base_64(value):
    """
    base64加密
    return:加密结果转成16进制字符串形式
    """
    return base64.b64encode(value.encode('utf-8')).decode('utf-8')


print(base_64('xiaofeiji'))
# eGlhb2ZlaWpp