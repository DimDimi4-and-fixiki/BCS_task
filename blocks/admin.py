from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Block

# Register your models here.


class BLockAdmin(admin.ModelAdmin):
    list_display = ('height', 'hash')


admin.site.site_header = "Admin Panel"

admin.site.register(Block, BLockAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
