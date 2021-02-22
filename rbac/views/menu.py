"""
菜单权限管理
"""
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from rbac import models
from rbac.forms.menu import MenuForm, SecondMenuForm


def menu_list(request):
    """
    权限列表
    :return:
    """
    menu_queryset = models.Menu.objects.all()
    mid = request.GET.get("mid")
    sid = request.GET.get("sid")
    menu_er = models.Permission.objects.filter( menu_id=mid ) if mid else []
    return render(request, "rbac/menu_list.html", {'roles': menu_queryset, "mid": mid, "sid": sid, "menu_er": menu_er})


def menu_add(request):
    """
    添加一级菜单
    :param request:
    :return:
    """
    form = MenuForm()
    if request.method == "POST":
        form = MenuForm(data=request.POST)
        if form.is_valid():
            form.save()
            base_url = reverse('rbac:menu_list')
            old_par = request.GET.get("_filter")
            return redirect("%s?%s" % (base_url, old_par))

    return render( request, 'rbac/role_chenge.html', {"form": form} )


def menu_edit(request, pk):
    """
    编辑一级菜单
    :param request:
    :param pk:
    :return:
    """
    obj = models.Menu.objects.filter(id=pk).first()
    if not obj:
        return HttpResponse("角色不存在")
    form = MenuForm( instance=obj )
    if request.method == "POST":
        form = MenuForm(instance=obj, data=request.POST)
        if form.is_valid():
            form.save()
            base_url = reverse( 'rbac:menu_list' )
            old_par = request.GET.get( "_filter" )
            return redirect( "%s?%s" % (base_url, old_par) )

    return render( request, 'rbac/role_chenge.html', {"form": form} )


def menu_del(request, pk):
    """
    删除一级菜单
    :param request:
    :param pk:
    :return:
    """
    base_url = reverse( 'rbac:menu_list' )
    old_par = request.GET.get("_filter" )
    url = "%s?%s" % (base_url, old_par)
    if request.method == "POST":
        models.Menu.objects.filter(pk=pk).delete()
        # a = models.Menu.objects.filter(pk=pk).delete()

        return redirect(url)

    return render(request, "rbac/delete.html", {"cancel_url": url})


def second_add(request, pk):
    """
    添加二级菜单
    :param pk: 获取当前选中的一级菜单（用于默认选中）
    :param request:
    :return:
    """
    menu_obj = models.Menu.objects.filter(pk=pk).first()
    form = SecondMenuForm(initial={"menu": menu_obj})
    if request.method == "POST":
        form = SecondMenuForm(data=request.POST)
        if form.is_valid():
            form.save()
            base_url = reverse('rbac:menu_list')
            old_par = request.GET.get("_filter")
            return redirect("%s?%s" % (base_url, old_par))

    return render( request, 'rbac/role_chenge.html', {"form": form} )



