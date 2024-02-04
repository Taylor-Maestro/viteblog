######################################################################
# 获取所有Blob对象存储
# import requests

# url = "http://nexusapi.com:8081/service/rest/v1/blobstores"

# headers = {
#     "Accept": "application/json",
#     "Authorization": "Basic YWRtaW46YWRtaW4xMjM="
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)

######################################################################
# 创建Blob对象存储
# import requests

# url = "http://nexusapi.com:8081/service/rest/v1/blobstores/file"

# payload = {
#     "path": "blobpath",
#     "name": "blobname"
# }
# headers = {
#     "Accept": "application/json",
#     "Content-Type": "application/json",
#     "content-type": "application/json",
#     "Authorization": "Basic YWRtaW46YWRtaW4xMjM="
# }

# response = requests.request("POST", url, json=payload, headers=headers)

# print(response.text)

######################################################################
# 创建yum-proxy代理仓库
# import requests

# url = "http://nexusapi.com:8081/service/rest/v1/repositories/yum/proxy"

# payload = {
#     "name": "yum-proxy",
#     "online": True,
#     "storage": {
#         "blobStoreName": "default",
#         "strictContentTypeValidation": True
#     },
#     "proxy": {
#         "remoteUrl": "https://mirrors.tuna.tsinghua.edu.cn/centos",
#         "contentMaxAge": 1440,
#         "metadataMaxAge": 1440
#     },
#     "negativeCache": {
#         "enabled": True,
#         "timeToLive": 1440
#     },
#     "httpClient": {
#         "blocked": False,
#         "autoBlock": True,
#         "connection": {
#             "retries": 0,
#             "userAgentSuffix": "Email: yourname@email.com",
#             "timeout": 60,
#             "enableCircularRedirects": False,
#             "enableCookies": False,
#             "useTrustStore": False
#         }
#     }
# }
# headers = {
#     "Accept": "application/json",
#     "Content-Type": "application/json",
#     "content-type": "application/json",
#     "Authorization": "Basic YWRtaW46YWRtaW4xMjM="
# }

# response = requests.request("POST", url, json=payload, headers=headers)

# print(response.text)


######################################################################
# 创建pypi-proxy代理仓库
import requests

url = "http://nexusapi.com:8081/service/rest/v1/repositories/pypi/proxy"

payload = {
    "name": "pypi-proxy",
    "online": True,
    "storage": {
        "blobStoreName": "default",
        "strictContentTypeValidation": True
    },
    "proxy": {
        "remoteUrl": "https://pypi.tuna.tsinghua.edu.cn",
        "contentMaxAge": 1440,
        "metadataMaxAge": 1440
    },
    "negativeCache": {
        "enabled": True,
        "timeToLive": 1440
    },
    "httpClient": {
        "blocked": False,
        "autoBlock": True,
        "connection": {
            "retries": 0,
            "userAgentSuffix": "Email: yourname@email.com",
            "timeout": 60,
            "enableCircularRedirects": False,
            "enableCookies": False,
            "useTrustStore": False
        }
    }
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "content-type": "application/json",
    "Authorization": "Basic YWRtaW46YWRtaW4xMjM="
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
print(response.status_code)