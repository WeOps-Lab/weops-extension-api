# WeOps-Extension-Api
![](https://wedoc.canway.net/imgs/img/嘉为蓝鲸.jpg)

WeOps-Extension-Api是一个无状态的API服务，为上层应用提供扩展能力的Restful服务.

## 优势
- 无状态
    - 使用restful API方式对接，所有资源均可uri定位，单原子无依赖其他原子能力
    
- 可集成
    - 可直接集成蓝鲸SaaS或其他外部开放API,进行数据处理
    
- 可调试
    - 支持swagger文档展示及在线调试
    
- 高效
    - 拥有开发标准及内置核心模块,可快速开发一个Restful API
    

    



## 依赖库文档

* Uvicorn: https://www.uvicorn.org/
* FastAPI: https://fastapi.tiangolo.com/
* Python-DotEnv: https://saurabh-kumar.com/python-dotenv/
* requests: https://requests.readthedocs.io/en/latest/
* fastapi-utils: https://fastapi-utils.davidmontague.xyz/
* Pydantic: https://pydantic-docs.helpmanual.io/



## 开始使用

1. 环境安装

> 可使用pipenv,virtualenv,anaconda,此处仅演示anaconda

```shell
# 创建3.6虚拟环境
conda create --name weops_extension_api python=3.6
# 进入虚拟环境
conda activate weops_extension_api

# 安装环境所需pip包
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# 安装pre-commit
pip install pre-commit
pre-commit install --allow-missing-config
pre-commit install --hook-type commit-msg --allow-missing-config

```

2.配置开发环境变量
> 开发配置.env文件,环境变量大写且=两侧无空格
> 可配置参数可参考server/core/settings 下Settings

```shell
APP_HOST=127.0.0.1
APP_PORT=8081
ENV=dev
```

> 如果需对接蓝鲸相关Saas,则配置BK_PAAS_HOST=http://paas.your.com/
> 
> 如果需关闭请求日志记录,默认开启,则配置ENABLE_REQUESTS_LOG=false


3.启动服务

```shell
# 启动fastapi进程
python main.py
```

4.查看docs
> [AutoMate API Docs](http://127.0.0.1:8081/docs)


## 目录结构
```markdown
├── Dockerfile  
├── LICENSE
├── Makefile
├── Readme.md
├── core            
│   ├── __init__.py
│   ├── bk_api_utils  
│   │   ├── __init__.py
│   │   └── main.py 
│   ├── bootstrap.py   
│   ├── exception      
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── handlers.py
│   ├── http_schemas      
│   │   ├── __init__.py
│   │   └── common_response_schema.py
│   ├── init.py
│   ├── logger
│   │   ├── __init__.py
│   │   ├── conf.py
│   │   ├── handlers.py
│   │   └── main.py
│   ├── readme.md
│   ├── service
│   │   ├── __init__.py
│   │   └── base.py
│   ├── settings.py
│   └── utils
│       ├── __init__.py
│       ├── autodiscover.py
│       ├── clean_items.py
│       ├── common.py
│       ├── crypto_utils.py
│       ├── patch.py
│       ├── performance.py
│       ├── threadpool.py
│       └── vault.py
├── docs
│   ├── assert
│   ├── imgs
│   └── 开发规范.md
├── logs
│   ├── error.log
│   └── weops_extension_api.log
├── main.py
├── pyproject.toml
├── requirements.txt
├── scripts
│   ├── check_commit_message.py
│   ├── check_migrate
│   │   ├── check_migrate.py
│   │   ├── field_library.csv
│   │   └── field_library.json
│   └── check_requirements.py
├── server
│   ├── __init__.py
│   ├── apps
│   │   ├── __init__.py
│   │   └── example
│   ├── libs
│   │   └── __init__.py
│   └── utils
│       ├── __init__.py

```





