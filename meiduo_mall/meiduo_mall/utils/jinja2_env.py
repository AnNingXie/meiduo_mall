from jinja2 import Environment
from django.urls import reverse
from django.contrib.staticfiles.storage import staticfiles_storage

def jinja2_environment(**options):
    # jinja2的环境
    # 创建环境对象
    env = Environment(**options)

    # 自定义语法 {{ static('静态文件相对路径') }}  {{ url('路由的命名空间') }}
    env_dict = {
        'static': staticfiles_storage.url, # 获取静态文件的前缀
        'url': reverse  # 做重定向 反向解析
    }
    env.globals.update(env_dict)
    
    # 返回环境对象
    return env
