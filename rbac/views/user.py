"""
用户管理
"""
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from rbac import models
from rbac.forms.user import UserForm, UpdateUserForm, UpdatePwdForm


def user_list(request):
    """
    角色列表
    :return:
    """
    user_queryset = models.UserInfo.objects.all()
    return render(request, "rbac/user_list.html", {'roles': user_queryset})


def user_add(request):
    """
    添加角色
    :param request:
    :return:
    """
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('rbac:user_list'))
    elif request.method == 'GET':
        form = UserForm()

    return render( request, 'rbac/role_chenge.html', {"form": form} )


def user_edit(request, pk):
    """
    编辑角色
    :param request:
    :param pk:
    :return:
    """
    obj = models.UserInfo.objects.filter(id=pk).first()
    if not obj:
        return HttpResponse("角色不存在")
    form = UpdateUserForm(instance=obj)
    if request.method == "POST":
        form = UpdateUserForm(instance=obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('rbac:user_list'))

    return render( request, 'rbac/role_chenge.html', {"form": form} )


def update_pwd(request, pk):
    """
    修改密码
    :param request:
    :param pk:
    :return:
    """
    obj = models.UserInfo.objects.filter(id=pk).first()
    if not obj:
        return HttpResponse("角色不存在")
    form = UpdatePwdForm(instance=obj)
    if request.method == "POST":
        form = UpdatePwdForm(instance=obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('rbac:user_list'))

    return render( request, 'rbac/role_chenge.html', {"form": form} )


def user_delete(request, pk):
    """
    删除角色
    :param request:
    :param pk:
    :return:
    """
    url = reverse("rbac:user_list")
    if request.method == "POST":
        models.UserInfo.objects.filter(pk=pk).delete()
        return redirect(url)
    return render(request, "rbac/delete.html", {"cancel_url": url})