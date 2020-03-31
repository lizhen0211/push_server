import json
import time

import requests

from xgpush.body import AndroidMessageBody
from xgpush.certification import SignCertification, AuthCertification
from xgpush.constant import XG_ACCESSID


def single_push_by_auth_certification():
    """单推 测试Auth认证"""
    auth_certification = AuthCertification()
    auth_str = auth_certification.get_auth_str()
    print(auth_str)

    url = 'https://api.tpns.tencent.com/v3/push/app'
    headers = {'Authorization': 'Basic {0}'.format(auth_str)}
    # 单推token
    token_list = ['01d670e91eebc202b0dffc5ab2a4ce52c3ab']
    single_push_body = AndroidMessageBody.get_single_push_body_dict(token_list)
    r = requests.post(url, json=single_push_body, headers=headers)
    print(r.text)


def single_push_by_sign_certification():
    """单推 测试签名认证"""
    url = 'https://api.tpns.tencent.com/v3/push/app'
    # 单推token
    token_list = ['01d670e91eebc202b0dffc5ab2a4ce52c3ab']
    single_push_body = AndroidMessageBody.get_single_push_body_dict(token_list)
    json_push_body = json.dumps(single_push_body)
    timeStamp = str(int(time.time()))
    sign_certification = SignCertification()
    sign = sign_certification.get_hex_hash(json_push_body, timeStamp)

    headers = {'Sign': sign, 'AccessId': XG_ACCESSID, 'TimeStamp': timeStamp}

    r = requests.post(url, json=single_push_body, headers=headers)
    print(r.text)


def multupy_push_by_auth_certification():
    """群推 测试Auth认证"""
    auth_certification = AuthCertification()
    auth_str = auth_certification.get_auth_str()

    url = 'https://api.tpns.tencent.com/v3/push/app'
    headers = {'Authorization': 'Basic {0}'.format(auth_str)}
    # 单推token
    token_list = ['01d670e91eebc202b0dffc5ab2a4ce52c3ab', '078c593c80fe9f872271e5d86f53bce4df17']
    _multupy_push_body = AndroidMessageBody.get_multupy_push_body_dict(token_list)
    r = requests.post(url, json=_multupy_push_body, headers=headers)
    print(r.text)


def multupy_push_by_sign_certification():
    """群推 测试签名认证"""
    url = 'https://api.tpns.tencent.com/v3/push/app'
    # 单推token
    token_list = ['01d670e91eebc202b0dffc5ab2a4ce52c3ab', '078c593c80fe9f872271e5d86f53bce4df17']
    multupy_push_body = AndroidMessageBody.get_multupy_push_body_dict(token_list)
    json_push_body = json.dumps(multupy_push_body)
    timeStamp = str(int(time.time()))
    sign_certification = SignCertification()
    sign = sign_certification.get_hex_hash(json_push_body, timeStamp)

    headers = {'Sign': sign, 'AccessId': XG_ACCESSID, 'TimeStamp': timeStamp}

    r = requests.post(url, json=multupy_push_body, headers=headers)
    print(r.text)


if '__main__' == __name__:
    """单推 测试签名认证"""
    # single_push_by_sign_certification()

    """单推 测试Auth认证"""
    # single_push_by_auth_certification()

    """群推 测试Auth认证"""
    # multupy_push_by_auth_certification()

    """群推 测试签名认证"""
    multupy_push_by_sign_certification()
