# -*- coding: utf-8 -*-
import json
import requests
import subprocess
import re
import time
from hashlib import sha256

timer = int(time.time() * 1000)


def get_h5st(p):
    js_file = './02 京东.js'
    ret = subprocess.run(['node', js_file, json.dumps(p)], capture_output=True, text=True, encoding='utf-8')
    # print(ret.stdout)  # 打印标准输出
    # print(ret.stderr)  # 打印标准错误输出
    return re.search(":::(?P<h5st>.*?):::", ret.stdout).group('h5st')


cookies = {
    '__jdv': '143920055|direct|-|none|-|1725469038503',
    '__jdu': '17254690385012015302450',
    'shshshfpa': '54074622-fa38-63ff-5f68-e8f15dabe96e-1725469162',
    'shshshfpx': '54074622-fa38-63ff-5f68-e8f15dabe96e-1725469162',
    'areaId': '7',
    'PCSYCityID': 'CN_310000_310100_0',
    'ipLoc-djd': '7-458-464-37568',
    'mba_muid': '17254690385012015302450',
    'jsavif': '1',
    'mba_sid': '1726119934811684758058003909.1',
    '3AB9D23F7A4B3CSS': 'jdd0365EHKN33YV53QJYTUYRWOSKFHJJYJP6CKYYMK634BEESF24X3Y4S4WABYNCMXYC6XTRUXPFAZIQUKMMOLO4ZVPBSXMAAAAMR4TB77LYAAAAACSBGUTC5POVLAIX',
    '_gia_d': '1',
    'wlfstk_smdl': 'nuvdwpijc7ao6vtn1g849c2qg3dx1sjp',
    'TrackID': '1MzrsWIfJcNnqy0ZRNFve22iOeLU1QNL1sdcA2N3Jj4v3vjuSWddijEIZjE1i3N1rOvB0KFuAHP-mXMRX0ujWNB29QNDEAcnt_43x7jan9Pg',
    'thor': 'B1385CA699BE29B12CDB513DE6BBFC6B64C79BD98AFBC69518AE155BC09CDE94A49333B75D94B40B075C576572B0FE0B2C7D2E02A5F5F5FA36E6D9A7F672087B3D9906005BE3986AEB74F8B7B5E1D20975F0AE75842F207FF923CA2096FFEC67FF7EFE9054A3D46F6C28B9DEACDE99D8A563B1E58FCF1B7F3954A92F99A585EF',
    'light_key': 'AASBKE7rOxgWQziEhC_QY6yahkBxQwE9XNOswKLk61AE6SLn9cJinqygdmK3ctLbVE1vp47Z',
    'pinId': 'leteGGkBL5U',
    'pin': 'vz437h',
    'unick': '8488ht9kyvzjvb',
    'ceshi3.com': '000',
    '_tp': 'M82tgnVBwuIXRL%2B4F1dywQ%3D%3D',
    '_pst': 'vz437h',
    '__jda': '143920055.17254690385012015302450.1725469039.1726117511.1726119934.6',
    '__jdb': '143920055.3.17254690385012015302450|6.1726119934',
    '__jdc': '143920055',
    'flash': '3_XTjcPUqPMT7ixPF5D37spKp3A-hLVeEk9Ctfwl5YVbW2E3Q3joPEz4wTqez30k6tH5Q8SAamCd-LimDLF7zrEuztlT6seisv_Ey6Siq2AqJU0q8yMqbcIamq7cztZIU-VPxeYPamTl_fjFS8OIn2_GDLo5_ifwS0wBzSLCwJ',
    'shshshfpb': 'BApXSy2bM5_RA8egyCH-NS-2hgYbmbVi0BmcHlk1q9xJ1MleqxYC2',
    '3AB9D23F7A4B3C9B': '65EHKN33YV53QJYTUYRWOSKFHJJYJP6CKYYMK634BEESF24X3Y4S4WABYNCMXYC6XTRUXPFAZIQUKMMOLO4ZVPBSXM',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'cookie': '__jdv=143920055|direct|-|none|-|1725469038503; __jdu=17254690385012015302450; shshshfpa=54074622-fa38-63ff-5f68-e8f15dabe96e-1725469162; shshshfpx=54074622-fa38-63ff-5f68-e8f15dabe96e-1725469162; areaId=7; PCSYCityID=CN_310000_310100_0; ipLoc-djd=7-458-464-37568; mba_muid=17254690385012015302450; jsavif=1; mba_sid=1726119934811684758058003909.1; 3AB9D23F7A4B3CSS=jdd0365EHKN33YV53QJYTUYRWOSKFHJJYJP6CKYYMK634BEESF24X3Y4S4WABYNCMXYC6XTRUXPFAZIQUKMMOLO4ZVPBSXMAAAAMR4TB77LYAAAAACSBGUTC5POVLAIX; _gia_d=1; wlfstk_smdl=nuvdwpijc7ao6vtn1g849c2qg3dx1sjp; TrackID=1MzrsWIfJcNnqy0ZRNFve22iOeLU1QNL1sdcA2N3Jj4v3vjuSWddijEIZjE1i3N1rOvB0KFuAHP-mXMRX0ujWNB29QNDEAcnt_43x7jan9Pg; thor=B1385CA699BE29B12CDB513DE6BBFC6B64C79BD98AFBC69518AE155BC09CDE94A49333B75D94B40B075C576572B0FE0B2C7D2E02A5F5F5FA36E6D9A7F672087B3D9906005BE3986AEB74F8B7B5E1D20975F0AE75842F207FF923CA2096FFEC67FF7EFE9054A3D46F6C28B9DEACDE99D8A563B1E58FCF1B7F3954A92F99A585EF; light_key=AASBKE7rOxgWQziEhC_QY6yahkBxQwE9XNOswKLk61AE6SLn9cJinqygdmK3ctLbVE1vp47Z; pinId=leteGGkBL5U; pin=vz437h; unick=8488ht9kyvzjvb; ceshi3.com=000; _tp=M82tgnVBwuIXRL%2B4F1dywQ%3D%3D; _pst=vz437h; __jda=143920055.17254690385012015302450.1725469039.1726117511.1726119934.6; __jdb=143920055.3.17254690385012015302450|6.1726119934; __jdc=143920055; flash=3_XTjcPUqPMT7ixPF5D37spKp3A-hLVeEk9Ctfwl5YVbW2E3Q3joPEz4wTqez30k6tH5Q8SAamCd-LimDLF7zrEuztlT6seisv_Ey6Siq2AqJU0q8yMqbcIamq7cztZIU-VPxeYPamTl_fjFS8OIn2_GDLo5_ifwS0wBzSLCwJ; shshshfpb=BApXSy2bM5_RA8egyCH-NS-2hgYbmbVi0BmcHlk1q9xJ1MleqxYC2; 3AB9D23F7A4B3C9B=65EHKN33YV53QJYTUYRWOSKFHJJYJP6CKYYMK634BEESF24X3Y4S4WABYNCMXYC6XTRUXPFAZIQUKMMOLO4ZVPBSXM',
    'origin': 'https://search.jd.com',
    'priority': 'u=1, i',
    'referer': 'https://search.jd.com/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-referer-page': 'https://search.jd.com/Search',
    'x-rp-client': 'h5_1.0.0',
}

params = {
    'appid': 'search-pc-java',
    'functionId': 'pc_search_s_new',
    'client': 'pc',
    'clientVersion': '1.0.0',
    't': str(timer),
    'body': '{"keyword":"手机","pvid":"d1d01d957303422e9ad99c677fd6f34c","isList":0,"page":"7","s":"176","click":"0","log_id":"1726120002045.4883","show_items":""}',
    'loginType': '3',
    'uuid': '143920055.17254690385012015302450.1725469039.1726117511.1726119934.6',
    'area': '7_458_464_37568',
    'h5st': '20240912134648731;yy9mz56nitgmyg96;f06cc;tk03wba721c1618ncRwwyNa7o8kZJcBjtb8CKWjbJusVSj40HFto1IuRIU6mGsT8usg-90Y4k-3sgJCV6uoNc0KpQj9y;404361000b48f0bcaea63a0af54a1a46;4.7;1726120008731;TKmWueWMdg5KB6xNnBpHvK0R0rsLTHSSbdSiFNUzVQA3gqk29xrabrbDHwlxBBs_Avne2Qsg2347P6RO2pnmGt38z0C1C480yGc-Ehzc64_uT1rYvfAdXrnc-4ufy2rN6VoW_znyQO_cgt7fm5aRQuGLxfEW3wAey-TCE77dOeaymjy6NoULN8G8dFTyFkr5XsinswtKcWuW5ZESsiS2rXRCNgjyEnKtcxmiJd-5v8MRt-ZTL27dz3JjTix4NtWF7CECTc2otOGFlOElkzUas15cwIrjGIJrnSTYgjLteNHqFkVybyfa3qGBQQjyCs9thY-SSvVccze2hgZD1u_eUIB9dZbFy82JnRK96Wzf3PTrjz4ntsdoJnA8ZIz_glsQr66_TGRgZT74HLAWTFgEX7QopDOw3x2qF4EQIJlwh3VivUrvifZwI7KcG4Hb_MWgOUMSTct4Glbcl9ETcr9EoSlO-ZBzZUindepKIIsEoLRn0vy6T6OU4IJEiwkvWUobblkCdine926J0EDkvnRlB5wI6utedXghCkPCXV-GsyO104dQuCtLpRmkFDuC6VykF1OWggE7nDk8PeheJO0dl8zjLad9Prk3hGJ0DQIeqffFGvzEemLTD52YgeDqWQHLXbk3;80f4424cd64828e51e23f92e8d7464e1',
    'x-api-eid-token': 'jdd0365EHKN33YV53QJYTUYRWOSKFHJJYJP6CKYYMK634BEESF24X3Y4S4WABYNCMXYC6XTRUXPFAZIQUKMMOLO4ZVPBSXMAAAAMR4TB77LYAAAAACSBGUTC5POVLAIX',
}
s = sha256()
s.update(params['body'].encode())

body = s.hexdigest()

params2 = {
    "appid": "search-pc-java",
    "functionId": "pc_search_s_new",
    "client": "pc",
    "clientVersion": "1.0.0",
    "t": timer,
    "body": body
}
h5st = get_h5st(params2)
print("h5st:::", h5st)
params['h5st'] = h5st

response = requests.get('https://api.m.jd.com/', params=params, cookies=cookies, headers=headers)
print(response.text)
