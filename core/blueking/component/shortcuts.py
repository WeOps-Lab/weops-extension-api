# -*- coding: utf-8 -*-
import logging

from . import conf
from .client import ComponentClient

logger = logging.getLogger("component")

__all__ = [
    "get_client_by_admin",
    "get_client_by_user",
]


def get_client_by_user(username, **kwargs):
    """根据user实例返回一个client

    :param username:蓝鲸用户的用户名
    :returns: 一个初始化好的ComponentClient对象
    """

    common_args = {"bk_username": username}
    common_args.update(kwargs)
    return ComponentClient(conf.APP_CODE, conf.SECRET_KEY, common_args=common_args)


def get_client_by_admin(**kwargs):
    return get_client_by_user("admin", **kwargs)
