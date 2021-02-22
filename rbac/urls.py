from django.conf.urls import re_path
from django.contrib import admin
from rbac.views import role, user, menu

urlpatterns = [
    # 权限管理
    re_path(r'^role/list/', role.role_list, name="role_list"),
    re_path(r'^role/add/', role.role_add, name="role_add"),
    re_path(r'^role/eidt/(?P<pk>\d+)/$', role.role_edit, name="role_edit"),
    re_path(r'^role/delete/(?P<pk>\d+)/$', role.role_delete, name="role_delete"),
    # 用户管理
    re_path(r'^user/list/', user.user_list, name="user_list"),
    re_path(r'^user/add/', user.user_add, name="user_add"),
    re_path(r'^user/eidt/(?P<pk>\d+)/$', user.user_edit, name="user_edit"),
    re_path(r'^update/pwd/(?P<pk>\d+)/$', user.update_pwd, name="update_pwd"),
    re_path(r'^user/delete/(?P<pk>\d+)/$', user.user_delete, name="user_delete"),
    # 菜单管理
    re_path(r'^menu/list/', menu.menu_list, name="menu_list"),
    re_path(r'^menu/add/', menu.menu_add, name="menu_add"),
    re_path(r'^menu/edit/(?P<pk>\d+)/$', menu.menu_edit, name="menu_edit"),
    re_path(r'^menu/del/(?P<pk>\d+)/$', menu.menu_del, name="menu_del"),
    # 二级菜单
    re_path(r'^second/add/(?P<pk>\d+)/$', menu.second_add, name="second_add"),

]
