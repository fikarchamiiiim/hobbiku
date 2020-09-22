from django.contrib import admin
from .models import Menu,UserProfileInfo, Variation, Category

class MenuAdmin(admin.ModelAdmin):
    list_display = ('judulMenu','picMenu','hargaMenu','kuantitas','slug','timestamp','updated','active','category')
    date_hierarchy = ('updated')
    search_fields = ['judulMenu']

class UserAdmin(admin.ModelAdmin):
    list_display = ('user','alamat','Provinsi','Kota','Kecamatan','Kelurahan','profile_pic')
    search_fields = ['user']

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','category','title','updated','active')
    search_fields = ['product']


admin.site.register(Menu, MenuAdmin)
admin.site.register(UserProfileInfo, UserAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(Category)


