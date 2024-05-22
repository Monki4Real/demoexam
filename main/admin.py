from django.contrib import admin
from .models import User, Statement

class StatementAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'user', 'date_time']
    list_filter = ['status']
    search_fields = ['title', 'body']
    actions = ['accept_statements', 'reject_statements']

    def accept_statements(self, request, queryset):
        queryset.update(status='Accepted')

    def reject_statements(self, request, queryset):
        queryset.update(status='Rejected')

admin.site.register(Statement, StatementAdmin)

admin.site.register(User)

