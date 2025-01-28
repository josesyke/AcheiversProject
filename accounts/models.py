from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='London')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image/', blank=True, null=True)

        # Add the default objects manager
    objects = models.Manager()


    # Custom manager for filtering profiles in London
    london = UserProfileManager()

    def __str__(self):
        return self.user.username

    # Optional static method for creating profiles manually
    @staticmethod
    def create_profile(user):
        return UserProfile.objects.create(user=user)


# Signal to create a profile when a user is created
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
