from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form, EmailField, PasswordInput, CharField, widgets
from rbac import models


class UserForm( ModelForm ):
    wid_02 = widgets.PasswordInput()
    wid_01 = widgets.TextInput()
    r_password = CharField(widget=wid_02, label="确认密码")
    email = EmailField(widget=wid_01, label="邮箱")

    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "r_password", "email"]
        widgets = {
            "password": PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'

    def clean_r_password(self):
        """
        检查密码是否一致
        :return:
        """
        password = self.cleaned_data.get( 'password' )
        r_password = self.cleaned_data.get( 'r_password' )
        if password != r_password:
            raise ValidationError( "两次密码不一致" )
        return r_password


class UpdateUserForm( ModelForm ):
    wid_01 = widgets.TextInput()
    email = EmailField(widget=wid_01, label="邮箱")

    class Meta:
        model = models.UserInfo
        fields = ["name", "email"]

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        for name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'


class UpdatePwdForm( ModelForm ):
    wid_02 = widgets.PasswordInput()
    r_password = CharField(widget=wid_02, label="确认密码")
    password = CharField(widget=wid_02, label="密码")

    class Meta:
        model = models.UserInfo
        fields = ["password", "r_password"]

    def __init__(self, *args, **kwargs):
        super(UpdatePwdForm, self).__init__(*args, **kwargs)
        for name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'

    def clean_r_password(self):
        """
        检查密码是否一致
        :return:
        """
        password = self.cleaned_data.get( 'password' )
        r_password = self.cleaned_data.get( 'r_password' )
        if password != r_password:
            raise ValidationError( "两次密码不一致" )
        return r_password
