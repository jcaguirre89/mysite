from django.contrib import admin
from .models import PlayRecord
# Register your models here.

class PlayRecordAdmin(admin.ModelAdmin):
    fields = ['id', 'strategy_ror', 'play_time']
    
admin.site.register(PlayRecord)