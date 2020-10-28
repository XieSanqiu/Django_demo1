from django.contrib import admin

from TestModel.models import Test, Contact, Tag

# Register your models here.

class TagInline(admin.TabularInline):
    model = Tag

class ContractAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')  # list显示更多属性

    search_fields = ('name',)  #增加搜索栏

    inlines = [TagInline]  # 内联显示

    # fields = ('name', 'email')  #自定义表单，只显示部分属性
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )  #属性分块显示

admin.site.register(Contact, ContractAdmin)
# admin.site.register([Test, Tag]) #为了内联显示
admin.site.register([Test])
