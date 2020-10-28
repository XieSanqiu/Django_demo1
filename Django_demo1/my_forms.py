from django import forms
from django.core.exceptions import ValidationError
from app01 import models

class EmpForm(forms.Form):
    # label：输入框前面的文本信息。
    # error_message：自定义显示的错误信息，属性值是字典， 其中 required 为设置不能为空时显示的错误信息的 key。
    name = forms.CharField(min_length=4, label="姓名", error_messages={"min_length": "你太短了", "required": "该字段不能为空!"})
    age = forms.IntegerField(label="年龄")
    salary = forms.DecimalField(label="工资")

class EmpForm2(forms.Form):
    name = forms.CharField(min_length=5, label="姓名", error_messages={"required": "该字段不能为空!",
                                                                     "min_length": "用户名太短。"})
    age = forms.IntegerField(label="年龄")
    salary = forms.DecimalField(max_digits=5, decimal_places=2, label="工资")
    r_salary = forms.DecimalField(max_digits=5, decimal_places=2, label="请再输入工资")


    def clean_name(self):  # 局部钩子
        val = self.cleaned_data.get("name")


        if val.isdigit():
            raise ValidationError("用户名不能是纯数字")
        # elif models.Emp.objects.filter(name=val):
        #     raise ValidationError("用户名已存在！")
        else:
            return val

    def clean(self):  # 全局钩子 确认两次输入的工资是否一致。
        val = self.cleaned_data.get("salary")
        r_val = self.cleaned_data.get("r_salary")


        if val == r_val:
            return self.cleaned_data
        else:
            raise ValidationError("请确认工资是否一致。")