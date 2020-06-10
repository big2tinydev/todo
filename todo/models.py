from datetime import datetime

from django.db import models
from django.template.defaultfilters import slugify

now = datetime.now()  # current date and time
time = now.strftime("%H:%M:%S")


class Image(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(default="assets/default.png", blank=True)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Images"
        verbose_name = "Image"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Image, self).save(*args, **kwargs)


class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    task = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        ordering = ['task']
        verbose_name_plural = "Tasks"
        verbose_name = "Task"

    def __str__(self):
        return self.task

    def save(self, *args, **kwargs):
        self.slug = slugify(self.task)
        super(Todo, self).save(*args, **kwargs)


class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    task = models.ForeignKey(Todo, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Projects"
        verbose_name = "Project"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)
