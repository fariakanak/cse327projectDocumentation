from django.contrib import admin
from hrm.models import *
from . import models
# Register your models here.

admin.site.register(User)
admin.site.register(Dept)
admin.site.register(Document)
admin.site.register(Team)

class AdminArea(admin.AdminSite):
    site_header = 'Admin Area'
    login_template = 'registration/login.html'
admin_site = AdminArea(name='AdminArea')

admin_site.register(models.User)