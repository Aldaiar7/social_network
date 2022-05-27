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
    created = models.DateTimeField(editable=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone']

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        return super(User, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user'
    )
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user__username)
        super(Profile, self).save(*args, **kwargs)


class Status(models.Model):
    status = models.TextField()
    created = models.DateTimeField(editable=False)
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(User, self).save(*args, **kwargs)


class Subsctiption(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sub_follower')
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sub_following')
    created = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(User, self).save(*args, **kwargs)


class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='message_sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='message_receiver')
    created = models.DateTimeField(editable=False)
    message = models.TextField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(User, self).save(*args, **kwargs)


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField()
    created = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(User, self).save(*args, **kwargs)


class Description(models.Model):
    description = models.TextField()
    created = models.DateTimeField(editable=False)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(User, self).save(*args, **kwargs)


class Reccomendation(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(User, self).save(*args, **kwargs)


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
    created = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(User, self).save(*args, **kwargs)


class Comment(MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(editable=False)
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
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(User, self).save(*args, **kwargs)


class Repost(models.Model):
    created = models.DateTimeField(editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)