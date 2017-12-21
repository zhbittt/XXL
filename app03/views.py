from django.shortcuts import render

'''
分页
'''
context=[]
for x in range(1,1023):
    context.append('host-%s.com'%x)

# from until.pager import Pagination
from until.pager1 import Pagination
def host(request):
    request.encoding
    pager_obj = Pagination(request.GET.get("page"),len(context),request.path_info)
    context_list = context[pager_obj.start:pager_obj.end]
    page_html_list=pager_obj.page_html()
    return render(request,'host.html',{"context_list":context_list,"page_html_list":page_html_list})