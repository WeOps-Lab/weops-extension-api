# -*- coding: utf-8 -*-
"""Django project settings
"""

try:
    from core.settings import settings

    APP_CODE = settings.weops_app_id
    SECRET_KEY = settings.weops_app_token
    COMPONENT_SYSTEM_HOST = settings.bk_paas_host
    DEFAULT_BK_API_VER = settings.default_bk_api_ver
    ADMIN_USER = settings.admin_username
except Exception:
    APP_CODE = ""
    SECRET_KEY = ""
    COMPONENT_SYSTEM_HOST = ""
    DEFAULT_BK_API_VER = "v2"
    ADMIN_USER = "admin"

CLIENT_ENABLE_SIGNATURE = False
