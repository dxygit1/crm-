from django import template
from django.conf import settings
from collections import OrderedDict

from django.urls import reverse

register = template.Library()


@register.inclusion_tag("rbac/static_meun.html")
def static_meun(request):
    """
    创建一级菜单
    :return:
    """
    meun_list = request.session.get(settings.MEUN_SESSION_KEY)
    url = request.path_info
    return {"meun_list": meun_list, "url": url}


@register.inclusion_tag("rbac/meun_meun.html")
def menu_meun(request):
    """
    创建二级菜单
    :return:
    """
    meun_dict = request.session.get(settings.MEUN_SESSION_KEY)
    pid = request.menu_pid
    # 对字典的key进行排序
    key_list = sorted(meun_dict)
    # 创建空的有序字典
    oreder_dict = OrderedDict()
    url = request.path_info
    for n in key_list:
        var = meun_dict[n]
        var["class"] = "hide"

        for key in var["children"]:
            if pid == key["id"]:
                var["class"] = ''
                key["class"] = "action"
        oreder_dict[n] = var

    return {"meun_dict": oreder_dict, "url": url}


@register.inclusion_tag("rbac/navigation.html")
def breadcrumb(request):

    return {"record_list": request.url_record}


@register.filter
def has_permission(request, name):
    """
    判断是否有权限
    :param request:
    :param name:
    :return:
    """
    if name in request.session[settings.PERMISSION_SESSION_KEY]:
        return True
    return False


@register.simple_tag
def menu_url(request, name, *args, **kwargs):
    """
    生成带有原搜索条件的url
    :param request:
    :param name:
    :return:
    """
    base_url = reverse(name, args=args, kwargs=kwargs)
    if not request.GET:
        return base_url
    from django.http import QueryDict
    queryct = QueryDict(mutable=True)
    queryct["filter"] = request.GET.urlencode()
    return "%s?_%s" % (base_url, queryct.urlencode())


