from django.contrib import admin
from .models import Theatre, Equipment, Request, UserProfile
from django.utils.html import format_html

# Register your models here.
@admin.register(Theatre)
class TheatreAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'division', 'rvp', 'region')
    search_fields = ('name', 'region', 'rvp')

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'item_number', 'price', 'photo_preview')
    readonly_fields = ['photo_preview']
    search_fields = ('make', 'model')

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('{}', obj.photo.url)
        return "No photo available"
    photo_preview.short_description = "Photo Preview"


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'theatre', 'equipment', 'approval_status', 'request_date')
    list_filter = ('approval_status', 'request_date')
    search_fields = ('requisition_number', 'po_number')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'theatre')
    search_fields = ('user__username', 'theatre__name')
    list_filter = ('theatre',)
