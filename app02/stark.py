from stark.service import v1
from app02 import models

v1.site.registry(models.UserInfo)
v1.site.registry(models.Role)