from django.core.exceptions import ValidationError
from django.contrib import admin
from accounts.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'phone', 'website')

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-phone', 'user')
        return queryset

    user_info.short_description = 'Info'

    def save_model(self, request, obj, form, change):
        if not change and UserProfile.objects.filter(user=obj.user).exists():
            raise ValidationError(f"User '{obj.user}' already has a profile.")
        super().save_model(request, obj, form, change)


admin.site.register(UserProfile, UserProfileAdmin)
