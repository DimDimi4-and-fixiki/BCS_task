from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Block

# Register your models here.


class BLockAdmin(admin.ModelAdmin):
    # Admin logic for Block table
    list_display = ('height', 'hash', 'number_of_transactions')
    search_fields = ("height__startswith", )


admin.site.site_header = "Admin Panel"  # changes header

admin.site.register(Block, BLockAdmin)  # Adds Block table to the panel
admin.site.unregister(Group)  # Removes Groups
admin.site.unregister(User)  # Removes Users
