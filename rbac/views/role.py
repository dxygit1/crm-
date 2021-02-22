"""
角色管理
"""
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from rbac import models
from rbac.forms.role import RoleForm


def role_list(request):
    """
    角色列表
    :return:
    """
    role_queryset = models.Role.objects.all()
    return render(request, "rbac/role_list.html", {'roles': role_queryset})


def role_add(request):
    """
    添加角色
    :param request:
    :return:
    """
    form = RoleForm()
    if request.method == "POST":
        form = RoleForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('rbac:role_list'))

    return render( request, 'rbac/role_chenge.html', {"form": form} )


def role_edit(request, pk):
    """
    编辑角色
    :param request:
    :param pk:
    :return:
    """
    obj = models.Role.objects.filter(id=pk).first()
    if not obj:
        return HttpResponse("角色不存在")
    form = RoleForm( instance=obj )
    if request.method == "POST":
        form = RoleForm(instance=obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('rbac:role_list'))

    return render( request, 'rbac/role_chenge.html', {"form": form} )


def role_delete(request, pk):
    """
    删除角色
    :param request:
    :param pk:
    :return:
    """
    url = reverse("rbac:role_list")
    if request.method == "POST":
        models.Role.objects.filter(pk=pk).delete()
        return redirect(url)
    return render(request, "rbac/delete.html", {"cancel_url": url})