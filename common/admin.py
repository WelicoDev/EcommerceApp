from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
admin.site.unregister(Group)

admin.site.site_header = "OnlineShop Admin"
admin.site.site_title = "OnlineShop Admin Portal"
admin.site.index_title = "Welcome OnlineShop Admin Portel"
admin.site.empty_value_display = "Not available"