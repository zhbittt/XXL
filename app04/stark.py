from stark.service import v1
from app04 import  models

class UserInfoStarkConfig(v1.StarkConfig):

    def display_gender(self,obj=None,is_header=None):
        if is_header:
            return "性别"
        return obj.get_gender_display()

    def display_depart(self,obj=None,is_header=None):
        if is_header:
            return "部门"
        return obj.depart.caption

    def display_roles(self,obj=None,is_header=None):
        if is_header:
            return "角色"
        role_list=[]
        for x in obj.roles.all():
            role_list.append(x.title)
        return ",".join(role_list)

    list_display = ["id", "name", "email", display_gender,display_depart,display_roles]

    comb_filter = [
        v1.FilterOption('gender',is_choice=True),
        v1.FilterOption('depart',),
        v1.FilterOption('roles',True),
    ]

    query_field =["id__contains","name__contains","email__contains","depart__caption__contains"]
    show_actions = True
    show_query_field = True

    #自定义action
    # def multi_find(self):
    #     print("multi_find")
    # multi_find.short_desc = '查找'
    # list_acions = [multi_find]



v1.site.registry(models.UserInfo,UserInfoStarkConfig)
v1.site.registry(models.Role)
v1.site.registry(models.Department)
