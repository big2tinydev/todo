from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime
from django.contrib.auth.models import User

now = datetime.now() # current date and time
time = now.strftime("%H:%M:%S")


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    location = models.CharField(max_length=30, blank=True, null=True)
    employee_number = models.IntegerField()
    work_shift = models.IntegerField(default=2)

    class Meta:
        ordering = ['user']
        verbose_name_plural = "User Profiles"
        verbose_name = "User Profile"

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)



class Account(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Accounts"
        verbose_name = "Account"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Account, self).save(*args, **kwargs)

