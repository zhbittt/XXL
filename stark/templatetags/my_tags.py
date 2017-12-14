from django import template

register = template.Library()

@register.inclusion_tag('stark/list.html')
def show_list(*args,**kwargs):
    data_list = kwargs["data_list"]
    header_list = kwargs["header_list"]
    return {"data_list":data_list,"header_list":header_list}
