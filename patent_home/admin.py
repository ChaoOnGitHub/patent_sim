from django.contrib import admin
from patent_home.models import ClaimText,LSIModel
# Register your models here.

class PatentClaimAdmin(admin.ModelAdmin):
    list_display    =('patent_Num','claim','sim_patent','run_date')
    list_filter     =('patent_Num','run_date')
    date_hierarchy  ='run_date'


class ModelAdmin(admin.ModelAdmin):
    list_display    =('run_date',)
    list_filter     =('run_date',)
    date_hierarchy = 'run_date'

admin.site.register(ClaimText,PatentClaimAdmin)
admin.site.register(LSIModel,ModelAdmin)

