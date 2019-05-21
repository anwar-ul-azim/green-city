from django.contrib import admin
from .models import Profile, Verify


class userAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'date_of_birth', 'phone_number')
    list_filter = ('user', 'date_of_birth',)
    search_fields = ('user', 'phone_number')


class verifyAdmin(admin.ModelAdmin):
    list_display = ('user', 'nid', 'is_verified', 'is_verify_submit')
    list_filter = ('user', 'is_verify_submit',)
    search_fields = ('user', 'is_verified')


admin.site.register(Profile, userAdmin)
admin.site.register(Verify, verifyAdmin)
