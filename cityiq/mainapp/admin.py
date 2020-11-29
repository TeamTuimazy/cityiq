from django.contrib import admin
from .models import *


class IndexIQAdmin(admin.ModelAdmin):
    readonly_fields=(
        'direction1',
        'direction2',
        'direction3',
        'direction4',
        'direction5',
        'direction6',
        'direction7',
        'direction8',
        'direction9',
        'direction10',
        'index_iq',
    )


admin.site.register(City)
admin.site.register(IndexIQ, IndexIQAdmin)
admin.site.register(HistoryIndexIQ)