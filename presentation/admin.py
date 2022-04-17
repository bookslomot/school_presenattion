from django.contrib import admin

from presentation.models import Presentation


@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'description', )
    list_display_links = ('owner', 'title', )
    search_fields = ('owner', 'title', )
    ordering = ('owner', )
