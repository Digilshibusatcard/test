from django.contrib import admin
from .models import RawPayload

@admin.register(RawPayload)
class RawPayloadAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'payload_preview')  # Display timestamp and payload preview
    search_fields = ('payload',)  # Enable search on the payload field

    def payload_preview(self, obj):
        return obj.payload[:50]  # Display first 50 characters of the payload
    payload_preview.short_description = 'Payload Preview'  # Set column header
