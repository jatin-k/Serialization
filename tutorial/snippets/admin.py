from django.contrib import admin
from snippets.models import NewUser

# Register your models here.
admin.site.register(NewUser)

class SnippetAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'city']
