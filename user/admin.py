from django.contrib import admin


from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'email', 'created_at', 'is_active', 'is_staff')
    list_display_links = ('id', 'name', 'last_name', 'email')
    search_fields = ('id', 'name', 'last_name', 'email')
    list_filter = ('is_staff', 'is_active')
    ordering = ('name', )
    list_editable = ('is_active', 'is_staff')
