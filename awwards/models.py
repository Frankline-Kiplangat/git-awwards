# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Profile(models.Model):
    """
    class containing projects' objects
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    profile_pic = models.ImageField( default = 'default.jpg',upload_to='profilepics/')
    bio = models.TextField(max_length=80, blank=True)
    contact = models.CharField(max_length =200,blank=True)

    def __str__(self):
        """
        function returns informal representations of the models' objects
        """
        return f'{self.user.username} Profile'

    def save_profile(self):
        """
        method saves entered profiles to the database
        """
        save()
    def update_profile(self, using=None, fields=None, **kwargs):
        """
        method updates saved profile
        """
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)

    def update_profile(self, using=None, fields=None, **kwargs):
        """
        method updates saved profile
        """
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)

    def delete_profile(self):
        """
        method deletes entered user profiles to the database
        """
        self.delete()


class Projects(models.Model):
    """
    class containing projects' description
    """
    project_name = models.CharField(max_length=50, blank=True)
    project_image = models.ImageField(blank=True, upload_to='projectimages/')
    description = models.TextField(max_length=300, blank=True)
    github_repo = models.CharField(max_length=150, blank=True)
    url = models.CharField(max_length=50, blank=True)
    project_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.project_name

    def save_projects(self):
        """
        method saves entered projects to the database
        """
        save()

    def update_projects(self, using=None, fields=None, **kwargs):
        """
        method updates saved projects
        """
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)

    @classmethod
    def get_projects(cls,project_search):
        project = cls.objects.filter(project_name__icontains=project_search)
        return project

    @property
    def project_image_url(self):
        if self.project_image and hasattr(self.project_image, 'url'):
            return self.project_image.url

    class Meta:
        ordering = ["-pk"]


    def delete_projects(self):
        """
        method deletes entered projects to the database
        """
        self.delete()
