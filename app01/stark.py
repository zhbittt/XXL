from app01 import models
from stark.service import v1
from django.conf.urls import url
from django.http import HttpResponse
from django.utils.safestring import mark_safe
class AuthorConfig(v1.StarkConfig):

    #自定义添加额外的url
    def extra_url(self):
        url_list=[
            url(r'^xxxx/',self.fun),
        ]
        return url_list
    #额外添加的url，对应的函数
    def fun(self):
        return HttpResponse("额外添加的url")


    #自定义查询字段
    list_display = [ 'id', "username", "password"]

    #有无添加按钮的权限
    # show_add_btn = True

    #自定义从那个字段搜索
    show_query_field=True
    query_field = ["username__contains","password__contains"]

    show_actions=True

    #自定义actions
    def multi_del(self,requset):
        pk_list = requset.POST.getlist('pk')
        self.model_class.objects.filter(pk__in=pk_list).delete()
    multi_del.short_desc='批量删除'

    def multi_init(self, requset):
        pk_list = requset.POST.getlist('pk')
    multi_init.short_desc='初始化'

    list_acions=[multi_del,multi_init]

    comb_filter = [
        v1.FilterOption('username',),
        v1.FilterOption('password',),
    ]



class BookConfig(v1.StarkConfig):
    list_display = ['id',"title","content","publish_time","author"]

class PublishConfig(v1.StarkConfig):
    list_display = ["id","title","addr"]

v1.site.registry(models.Author,AuthorConfig)
v1.site.registry(models.Book,BookConfig)
v1.site.registry(models.Publish,PublishConfig)
