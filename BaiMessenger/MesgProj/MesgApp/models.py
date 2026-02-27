from django.db import models
from django.conf import settings 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='images/avatars/', blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    @property
    def user_id(self):
        return self.user.id

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Chat(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def str(self):
        return self.name

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def str(self):
        return f"{self.sender}: {self.text[:20]}"

class GroupChat(models.Model):
    chat = models.OneToOneField(Chat, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='images/group_avatars/', blank=True, null=True)
    
    def str(self):
        return f"Group: {self.chat.name}"

