# -*- coding: utf-8 -*-
import requests
import subprocess
# from functools import partial
import json
# subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
# import execjs
import time

cookies = {
    '_xmLog': 'h5&0a7fb2fd-ee95-480c-a827-7d50a14df224&process.env.sdkVersion',
    'xm-page-viewid': 'ximalaya-mobile',
    'wfp': 'ACMyMzBmMjQ2YTBjNDk4ZGQ1wnF2a9nNXqp4bXdlYl9t',
    'Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070': '1725894472',
    'Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070': '1725894472',
    'HMACCOUNT': 'BA51EFD0C63D01A7',
    'trackType': 'web',
    'x_xmly_traffic': 'utm_source%3A%26utm_medium%3A%26utm_campaign%3A%26utm_content%3A%26utm_term%3A%26utm_from%3A',
    'impl': 'passport.ximalaya.com.web',
    's&e': 'd9d739335f8c013cad121e5e40c28e15',
    's&a': '%1ER%0BXYZLTO%01W%04^RL%04%1B%0F^U_%06N%06N[%08UV%06JVVZYOYVWT@G^XUZWW@R',
    'fds_otp': '5372227307329413477',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': '_xmLog=h5&0a7fb2fd-ee95-480c-a827-7d50a14df224&process.env.sdkVersion; xm-page-viewid=ximalaya-mobile; wfp=ACMyMzBmMjQ2YTBjNDk4ZGQ1wnF2a9nNXqp4bXdlYl9t; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1725894472; Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1725894472; HMACCOUNT=BA51EFD0C63D01A7; trackType=web; x_xmly_traffic=utm_source%3A%26utm_medium%3A%26utm_campaign%3A%26utm_content%3A%26utm_term%3A%26utm_from%3A; impl=passport.ximalaya.com.web; s&e=d9d739335f8c013cad121e5e40c28e15; s&a=%1ER%0BXYZLTO%01W%04^RL%04%1B%0F^U_%06N%06N[%08UV%06JVVZYOYVWT@G^XUZWW@R; fds_otp=5372227307329413477',
    'Origin': 'https://passport.ximalaya.com',
    'Referer': 'https://passport.ximalaya.com/page/web/login?fromUri=https%3A%2F%2Fstudio.ximalaya.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def get_encrypted_pwd(account):
    encrypted_account = subprocess.check_output(f'node "./02 account_pwd.js" {account}', shell=True).decode('utf-8').strip()
    return encrypted_account



def get_nonce():
    t = int(time.time() * 1000)
    url = f'https://passport.ximalaya.com/web/nonce/{t}'
    response = requests.get(url=url, cookies=cookies, headers=headers)
    nonce = response.json().get('nonce')
    return nonce


def get_signature(account, password, nonce):
    signature = subprocess.check_output(f'node "./07 signature.js" {account} {password} {nonce}', shell=True).decode('utf-8').strip()
    return signature


def spider_login(encrypted_account, encrypted_pwd, nonce, signature):
    params = {
        'fromUri': 'https%3A%2F%2Fstudio.ximalaya.com',
    }
    data = {
        'account': encrypted_account,
        'password': encrypted_pwd,
        'nonce': nonce,
        'signature': signature,
        'fromUri': 'https%3A%2F%2Fstudio.ximalaya.com',
        'fdsOtp': '',
    }
    json_data = json.dumps(data, separators=(',', ':'))
    response = requests.post(
        'https://passport.ximalaya.com/web/login/pwd/v2',
        params=params,
        cookies=cookies,
        headers=headers,
        data=json_data,
    )
    print(response.text)


def main(account, password):
    encrypted_account = get_encrypted_pwd(account)
    encrypted_pwd = get_encrypted_pwd(password)
    print("enc_account:", encrypted_account)
    print("enc_password:", encrypted_pwd)
    nonce = get_nonce()
    # nonce = "0-4BF3DA2F55805f0f5ac7805f87e053a4da1fa5f4d5f4fc60b7041fbda5e891"
    signature = get_signature(encrypted_account, encrypted_pwd, nonce)
    print('signature--->', signature)
    spider_login(encrypted_account, encrypted_pwd, nonce, signature)


if __name__ == '__main__':
    account = '15100326608'
    password = '123456'
    main(account, password)
