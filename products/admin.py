from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.FishingProducts)
class AdminProduct(admin.ModelAdmin):

    readonly_fields= ('jcreated', 'jupdated',)
    list_display = ('name','jcreated','jupdated',)
    actions = ['discount_30']

    def discount_30(self, request, queryset):
        from math import ceil
        discount = 30  # percentage

        for product in queryset:
            """ Set a discount of 30% to selected products """
            multiplier = discount / 100.  # discount / 100 in python 3
            old_price = product.price
            new_price = ceil(old_price - (old_price * multiplier))
            product.price_discounted = new_price
            product.save(update_fields=['price_discounted'])
    discount_30.short_description = 'Set 30%% discount'
    
admin.site.register(models.Dicty)
admin.site.register(models.KeyVal)
admin.site.register(models.feedback)
admin.site.register(models.Images)
admin.site.register(models.Categury)
admin.site.register(models.mainpageimages)
@admin.register(models.MiniCategury)
class AdminCategory(admin.ModelAdmin):
    list_display = ('title','parent',)

# admin.site.register(models.MiniCategury)

admin.site.register(models.Tags)
admin.site.register(models.PriceField)



