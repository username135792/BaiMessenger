from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Profile, Chat, Message, GroupChat

User = get_user_model()

class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ['avatar', 'description']

admin.site.unregister(User)
admin.site.register(User, type('CustomUserAdmin', (UserAdmin,), {'inlines': [ProfileInline]}))

admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(GroupChat)