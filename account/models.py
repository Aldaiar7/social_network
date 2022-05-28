from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.forms import CharField
from django.utils import timezone
from django.utils.text import slugify

from phonenumber_field.modelfields import PhoneNumberField

from mptt.models import MPTTModel, TreeForeignKey

from .managers import UserProfileManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_birth = models.DateField()
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone', 'email', 'date_birth', 'first_name', 'second_name']
    
    


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user'
    )
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        user = User.objects.get(pk=self.user_id)
        self.slug = slugify(user.username)
        super(Profile, self).save(*args, **kwargs)

    

class Status(models.Model):
    status = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
    )



class Subsctiption(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sub_follower')
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sub_following')
    created = models.DateTimeField(auto_now_add=True)

  


class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='message_sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='message_receiver')
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)

   


class Reccomendation(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    


class ProfileReccomendation(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    recommendation = models.ForeignKey(Reccomendation, on_delete=models.CASCADE)


class Mark(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class ProfileMark(models.Model):
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

   


class Comment(MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    
    class MPTTMeta:
        order_insertion_by = ['-created']
    
    def children(self):
        return Comment.objects.filter(parent=self)
    
    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
    
 


class Repost(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)