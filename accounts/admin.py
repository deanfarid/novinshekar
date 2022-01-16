from django.contrib import admin
from .models import Comment, users,ProfileModel,MyWishList
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


admin.site.register(users)
admin.site.register(Comment)
admin.site.register(MyWishList)

@admin.register(ProfileModel)
class ProfileModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
	list_display = ['user','name']
    
	# def get_created_jalali(self, obj):
	# 	return datetime2jalali(obj.birthday)


