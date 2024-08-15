from django.contrib import admin
from .models import Client, Project

admin.site.register(Client)
admin.site.register(Project)





# from django.contrib import admin
# from .models import Client, Project, User

# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ('client_name', 'created_by', 'created_at', 'updated_at')
#     search_fields = ('client_name',)

# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('project_name', 'client', 'created_by', 'created_at')
#     search_fields = ('project_name', 'client__client_name')
#     filter_horizontal = ('users',)

# @admin.register(User)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'phone_number', 'address')
#     search_fields = ('user__username',)
