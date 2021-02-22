#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf import settings


def init_permission(current_user, request):
    """
    用户权限的初始化，二级菜单
    :param current_user: 当前用户对象
    :param request: 请求相关所有数据
    :return:
    """
    # 2. 权限信息初始化
    # 根据当前用户信息获取此用户所拥有的所有权限，并放入session。
    # 当前用户所有权限
    permission_queryset = current_user.roles.filter(permissions__isnull=False).values("permissions__url",
                                                                                      "permissions__title",
                                                                                      "permissions__id",
                                                                                      "permissions__pid",
                                                                                      "permissions__name",
                                                                                      "permissions__pid__title",
                                                                                      "permissions__pid__url",
                                                                                      "permissions__meun_id",
                                                                                      "permissions__meun__title",
                                                                                      "permissions__meun__icon",
                                                                                      ).distinct()
    menu_dict = {}
    permission_dict = {}
    for item in permission_queryset:
        meun_id = item['permissions__meun_id']
        url = item['permissions__url']
        node = {
                    'id': item["permissions__id"],
                    "title": item['permissions__title'],
                    "url": url
                }
        permission_dict[item['permissions__name']] = {
                                'id': item["permissions__id"],
                                'url': url,
                                'pid': item["permissions__pid"],
                                'p_title': item["permissions__pid__title"],
                                'title': item["permissions__title"],
                                'p_url': item["permissions__pid__url"],
                                'url': item["permissions__url"]
                                }

        if meun_id:
            if not menu_dict.get(meun_id):
                menu_dict[meun_id] = {
                    "title": item['permissions__meun__title'],
                    "icon": item["permissions__meun__icon"],
                    "children": [node]
                }
            else:
                menu_dict[meun_id]["children"].append(node)

    # 获取权限中所有的URL
    # permission_list = []
    # for item in permission_queryset:
    #     permission_list.append(item['permissions__url'])

    # permission_list = [item['permissions__url'] for item in permission_queryset]
    request.session[settings.MEUN_SESSION_KEY] = menu_dict
    request.session[settings.PERMISSION_SESSION_KEY] = permission_dict
