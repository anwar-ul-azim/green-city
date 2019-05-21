from django.contrib import admin
from .models import Payment, Transition, CashInOrOut


class paymentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'balance', 'earned', 'due')
    list_filter = ('owner', 'balance',)
    search_fields = ('owner', 'balance')


class transitionAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'amount', 'date')
    list_filter = ('sender', 'receiver','date',)
    search_fields = ('sender', 'receiver')


class cashAdmin(admin.ModelAdmin):
    list_display = ('client', 'cash_in', 'cash_out', 'date')
    list_filter = ('client', 'date',)
    search_fields = ('client', 'date')


admin.site.register(Payment, paymentAdmin)
admin.site.register(Transition, transitionAdmin) 
admin.site.register(CashInOrOut, cashAdmin)
