from django.forms import ModelForm, Form, TextInput
from rbac import models


class RoleForm(ModelForm):
    class Meta:
        model = models.Role
        fields = ["title"]
        widgets = {
            "title": TextInput(attrs={"class": "form-control"})
        }