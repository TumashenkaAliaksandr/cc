from django.contrib import admin
from .models import CompanyInfo, ServicePhoto, Service, MoreServices


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')


class ServicePhotoInline(admin.TabularInline):
    model = ServicePhoto
    extra = 3  # количество дополнительных фото по умолчанию

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    inlines = [ServicePhotoInline]


@admin.register(MoreServices)
class MoreServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_active",
        "sort_order",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "short_description",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    list_editable = (
        "is_active",
        "sort_order",
    )
