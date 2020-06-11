from django.contrib import admin
#import admin_thumbnails
from django.utils.safestring import mark_safe

# Register your models here.
from .models import TeaStallProducts



# admin.site.register(TeaStallProduct)
# @admin_thumbnails.thumbnail('item_image', 'Thumbnail')


# @admin.register(TeaStallProduct)
# @admin_thumbnails.thumbnail('item_image')
class TeaStallProductAdmin(admin.ModelAdmin):
    site_header = "Sadguru's Amrit Tulya Tea Shop"
    # print('image_tag:',image_tag.url)
    list_display = ('item_name','item_description','price_value', 'image_tag')
    readonly_fields = ('image_tag',)

admin.site.register(TeaStallProducts, TeaStallProductAdmin)