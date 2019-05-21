from .models import Location, Cycle, Dropcycle, Pickcycle
from django.contrib import admin


class cycleAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'owner', 'rent', 'rating', 'picked_times')
    list_filter = ('name', 'model',)
    search_fields = ('name', 'model', 'owner', 'rent', 'rating', 'picked_times', 'is_picked')


class pickAdmin(admin.ModelAdmin):
    list_display = ('cycle_id', 'picked_by', 'pick_date')
    list_filter = ('cycle_id', 'picked_by',)
    search_fields = ('cycle_id', 'picked_by', 'pick_date')


class dropAdmin(admin.ModelAdmin):
    list_display = ('pick_id', 'drop_date')
    list_filter = ('pick_id', 'drop_date',)
    search_fields = ('pick_id', 'drop_date')


class locationAdmin(admin.ModelAdmin):
    list_display = ('area', 'near_by', 'cycle_id')
    list_filter = ('cycle_id', 'area',)
    search_fields = ('cycle_id', 'area')


admin.site.register(Cycle, cycleAdmin)
admin.site.register(Location, locationAdmin)
admin.site.register(Pickcycle, pickAdmin)
admin.site.register(Dropcycle, dropAdmin)


admin.site.site_header = 'GREEN-CITY Admin'
admin.site.index_title = 'GREEN-CITY Dashboard'
admin.site.site_title = 'Administrator'
