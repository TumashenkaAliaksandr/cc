from django.contrib import admin
from .models import CompanyInfo, MoreServices, SliderService, SliderServicePhoto, Contractor, ProfessionalApplication, \
    Profile


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'logo')
    search_fields = ('name', 'phone', 'email')


class ServicePhotoInline(admin.TabularInline):
    model = SliderServicePhoto
    extra = 3  # количество дополнительных фото по умолчанию

@admin.register(SliderService)
class SliderServiceAdmin(admin.ModelAdmin):
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



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'phone',
        'city'
    )


@admin.register(ProfessionalApplication)
class ProfessionalApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'application_type',
        'company_name',
        'profession',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
        'application_type'
    )


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'company_name',
        'profession',
        'rating',
        'approved'
    )
