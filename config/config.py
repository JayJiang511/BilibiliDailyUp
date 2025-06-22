"""
The config for this script, you can read the description in README.md
"""

LIKE_OR_NOT = True
# 投币时是否点赞

USE_ENVIRONMENT_VARIABLE = True
# 从环境变量中读取CK 确保已经设置环境变量BILIBILI 只支持单个账号

COIN_OR_NOT = True
# 是否投币

COIN_NUM = -1
# 投币数量 -1为完成所有也就是如果你已经投过1次那就只会投4次
# 如果不是 -1 则指定投币数量范围1-5

SILVER2COIN_OR_NOT = True
# 是否将银瓜子兑换为硬币


STRICT_MODE = True
# 是否开启严格模式，严格模式会保证至少5次成功投币，因为官方投币API存在缺陷，会有投币成功但是返回失败的情况
# 默认开启严格模式，如果关闭则只会投币5次，无论成功失败，会出现少投币的情况，因为可能失败，但是不会造成浪费硬币的情况，自行选择
NUM_MODE = False
# 该模式与严格模式互斥,开启此模式,投币只会投COIN_NUM次,无论成功失败

UID_LIST = ['473837611', '1131457022', '433587902', '2026561407', '50329118']
# 投币UP主的ID号,如果不修改，默认将用上面这个列表里的,可以选择自己喜欢的UP主
# 获取UID的方法见README.md

COOKIE_LIST = [
buvid3=4E9A88EC-4D42-B097-D5AA-BF90BBFBFFC040004infoc; b_nut=1744143440; _uuid=DA2E11010E-103E3-267F-C43C-8F34CD2106CD371537infoc; enable_web_push=DISABLE; enable_feed_channel=ENABLE; buvid4=34361D6A-6EC4-32D9-F338-3C6AF3DCB15041672-025040820-AtKSaKPJ4Zt08EyrTaEZqA%3D%3D; rpdid=|(uR)m~u|k)R0J'u~RRuRJlYJ; DedeUserID=3461569495173335; DedeUserID__ckMd5=5b1e7cafee152dfb; hit-dyn-v2=1; buvid_fp_plain=undefined; LIVE_BUVID=AUTO7917452335374594; CURRENT_QUALITY=80; bp_t_offset_3461569495173335=1071686424450826240; SESSDATA=5d098847%2C1764185617%2Ce40ef%2A51CjD_aJQYfysyEWz734AXsXZZNfUUGHjmeNrqZefHvJ9Rz5WDNlNRh5oYCfuyQ0dmw0oSVmhSTTBpZHFRZFNtSnp1bS1xcTRDcU1GZzhpTjNiY0oxY3ZBWHBpZVVVMm5kS2E3MnFXUS1JR3BmRllKemJabmU3TlBTYnk4RmhlYXFyN0UzNFV4bjV3IIEC; bili_jct=b1c3e80e7182938dd0ac877ec770c945; header_theme_version=OPEN; theme-tip-show=SHOWED; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTA3MDU0MzIsImlhdCI6MTc1MDQ0NjE3MiwicGx0IjotMX0.Zv92RyGsh2i5dTH4txTwzYnm7Atgsz_vJICoeyTq9JY; bili_ticket_expires=1750705372; fingerprint=59eb1afd7b5ceabf7eb47b0b8017b4fc; buvid_fp=1152b7110326e8a50cebb8b660a8e069; b_lsid=BBE3109BA_19796D22539; home_feed_column=5; browser_resolution=1865-956; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; sid=6ijmfw26; CURRENT_FNVAL=4048; perf_dv6Tr4n=1; theme_style=ligh
    r""
]
# Bilibili的COOKIE获取的方法见README.md 支持多账号

PUSH_OR_NOT = False
TOKEN = ''
# PUSH PLUS的TOKEN 官网为https://www.pushplus.plus

WECHAT_PUST_OR_NOT = True
# 默认关闭企业微信推送

WECHAT_ID = ""
# 企业ID
WECHAT_SECRET = ""
# 企业应用secret
WECHAT_APP_ID = ""
# 企业应用的id
# 企业应用推送 文档https://developer.work.weixin.qq.com/document/path/90236

SERVER_PUSH_OR_NOT = False
SERVER_KEY = ""
# 是否开启sever酱,有填写则推送,空字符串则不推送 https://sct.ftqq.com/sendkey获取key
