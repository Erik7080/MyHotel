from django.contrib import admin

from .models import ExtraCategory, RoomType, DiscountedPacks, Extra

admin.site.register(ExtraCategory)
admin.site.register(RoomType)
admin.site.register(DiscountedPacks)
admin.site.register(Extra)
