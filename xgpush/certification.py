# 参见 https: // cloud.tencent.com / document / product / 548 / 41046
import base64
import hmac
from hashlib import sha256

from xgpush.constant import XG_SECRETKEY, XG_ACCESSID


class SignCertification():
    """签名认证"""

    def get_hex_hash(self, body, timeStamp):
        """
        2.通过 secretKey 作为密钥，对原始待签名字符串进行签名，生成得到签名：
        sign = Base64(HMAC_SHA256(待签名字符串, secretKey))
        :param body:
        :return:
        """
        unencrypt_sign = self.__get_unencrypt_sign(body, timeStamp)
        hashcode = hmac.new(XG_SECRETKEY.encode('utf-8'), unencrypt_sign.encode('utf-8'),
                            digestmod=sha256).hexdigest()
        return base64.b64encode(hashcode.encode('utf-8'))

    def __get_unencrypt_sign(self, body, timeStamp):
        """
        1.通过请求时间戳 + accessId + 请求 body 进行字符拼接，得到原始的待签名字符串：
        待签名字符串 = ${timeStamp} + ${accessId} + ${请求body}
        :param body:
        :return:
        """
        # 待加密字符串
        return timeStamp + XG_ACCESSID + body;


class AuthCertification():
    """Auth认证"""

    def get_auth_str(self):
        """
        拼接请求字符串
        生成算法为：base64(Access ID:SECRETKEY)，即对Access ID加上冒号，加上SECRETKEY拼装起来的字符串，再做base64转换。
        :return:
        """
        return base64.b64encode('{0}:{1}'.format(XG_ACCESSID, XG_SECRETKEY).encode('utf-8')).decode('utf-8')
