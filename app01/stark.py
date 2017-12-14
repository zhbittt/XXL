from app01 import models
from stark.service import v1
from django.utils.safestring import mark_safe
class AuthorConfig(v1.StarkConfig):

    def check_box(self,obj=None,is_header=False):
        if is_header:
            return "选择"
        return mark_safe('<input type="checkbox">')

    def edit(self,obj=None,is_header=False):
        # from app01 import models
        # aaaa=models.Author._meta.fields
        # print(aaaa)
        # for x in aaaa:
        #     print("aaaaaaaaaaaaaaaa",x.name)

        if is_header:
            return "操作"
        return mark_safe('<a href="/stark/%s/%s/%s/change/">编辑</a>'%(self.model_class._meta.app_label,self.model_class._meta.model_name,obj.id))
    list_display = [check_box, 'id', "username", "password",edit]

class BookConfig(v1.StarkConfig):
    list_display = ['id',"title","contentt","publish_time","author_id"]

class PublishConfig(v1.StarkConfig):
    list_display = ["id","title","addr"]

v1.site.registry(models.Author,AuthorConfig)
v1.site.registry(models.Book,BookConfig)
v1.site.registry(models.Publish,PublishConfig)
