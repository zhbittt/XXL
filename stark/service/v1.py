from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render

class StarkConfig(object):
    def __init__(self,model_class,site):
        self.model_class = model_class
        self.site= site

    list_display=[]
    def get_urls(self):
        # 给正则表达式定义个别名，name = 应用名_表名_对应操作 例：name = app01_Author_add

        nametuple =(self.model_class._meta.app_label,self.model_class._meta.model_name)

        url_patterns =[
            url(r'^$',self.changelist_view,name="%s_%s"%nametuple),
            url(r'^add/$',self.add_view,name="%s_%s_add"%nametuple),
            url(r'^(\d+)/change/$',self.change_view,name="%s_%s_change"%nametuple),
            url(r'^(\d+)/delete/$',self.delete_view,name="%s_%s_delete"%nametuple),
        ]
        return url_patterns

    @property
    def urls(self):
        return self.get_urls()

    #忘记添加request
    def changelist_view(self,request):
        '''
        列表显示
        '''
        if not self.list_display:
            self.list_display=[ x.name for x in self.model_class._meta.fields]

        #查询表的所有数据
        obj_list=self.model_class.objects.all()
        print(self.model_class,obj_list)

        '''
            [
                [id,usernmae,password],
                [id,username,password],
            ]
        '''
        #####返回列表
        # header_data_list=[]
        # for header_name in self.list_display:
        #     if isinstance(header_name,str):
        #         field_verbose_name=self.model_class._meta.get_field(header_name).verbose_name
        #     else:
        #         field_verbose_name=header_name(self,is_header=True)
        #     header_data_list.append(field_verbose_name)
        #####使用yield返回
        def header_data():
            for header_name in self.list_display:
                if isinstance(header_name, str):
                    field_verbose_name = self.model_class._meta.get_field(header_name).verbose_name
                else:
                    field_verbose_name = header_name(self, is_header=True)
                yield field_verbose_name

        ######返回列表
        # new_data_list=[]
        # for obj in obj_list:
        #     temp =[]
        #     print(obj)
        #     for field_name in self.list_display:
        #         print(field_name,type(field_name))
        #         if isinstance(field_name,str):
        #             val = getattr(obj,field_name)
        #         else:
        #             val = field_name(self,obj)
        #         temp.append(val)
        #     new_data_list.append(temp)
        ######使用yield返回
        def data_list():
            for obj in obj_list:
                print("obj-----",obj)
                def inner(obj):
                    for field_name in self.list_display:
                        print(field_name, type(field_name))
                        if isinstance(field_name, str):
                            val = getattr(obj, field_name)
                        else:
                            val = field_name(self, obj)
                        yield val
                yield inner(obj)

        # return render(request, 'stark/changelist_view.html',{"data_list":new_data_list,"header_list":header_data_list})
        return render(request, 'stark/changelist_view.html',{"data_list":data_list(),"header_list":header_data()})

    def add_view(self,request):
        '''
        添加
        '''
        return HttpResponse("添加")

    def change_view(self,request,nid):
        '''
        修改
        '''
        return HttpResponse("修改")

    def delete_view(self,request,nid):
        '''
        删除
        '''
        return HttpResponse("删除")


class StarkSite(object):

    def __init__(self):
        self._registry = {}

    def registry(self,model_class,stark_config_class=None):
        if not stark_config_class:
            stark_config_class = StarkConfig
        self._registry[model_class]=stark_config_class(model_class,self)#self是site对象

    def get_urls(self):

        url_patterns = []
        for model_class,start_config_obj in self._registry.items():
            # model_class._meta.app_label   获取应用名
            # model_class._meta.model_name   获取表名
            # model_class._meta.g

            url_patterns +=[
                url(r'^%s/%s/'% (model_class._meta.app_label, model_class._meta.model_name),
                    (start_config_obj.urls, None, None))
            ]

        return url_patterns

    @property
    def urls(self):
        return  self.get_urls(),None,None

site = StarkSite()
