from django.contrib import admin

# Register your models here.

from .models import SubletGender, SubletListing, SubletOwnerInfo, SubletPlace, Subtenant, LegalFee, ImageModel


class SubletListingAdmin(admin.ModelAdmin):
    change_list_template = 'admin/subletlisting/subletlisting.html'


admin.site.register(SubletGender)
admin.site.register(SubletListing, SubletListingAdmin)
admin.site.register(SubletOwnerInfo)
admin.site.register(Subtenant)
admin.site.register(SubletPlace)
admin.site.register(LegalFee)
admin.site.register(ImageModel)
