from django.contrib import admin

# Register your models here.

from .models import SubletGender, SubletListing, SubletOwnerInfo, SubletPlace, Subtenant, LegalFee, ImageModel

admin.site.register(SubletGender)
admin.site.register(SubletListing)
admin.site.register(SubletOwnerInfo)
admin.site.register(Subtenant)
admin.site.register(SubletPlace)
admin.site.register(LegalFee)
admin.site.register(ImageModel)