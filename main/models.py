from django.db import models


class Tag(models.Model):
    tag_name = models.CharField('Tag name', max_length=50, blank=True)

    def __str__(self):
        return self.tag_name


class Scope(models.Model):
    scope_name = models.CharField('name', max_length=50)
    description = models.CharField('description', max_length=200)
    tags = models.ManyToManyField(Tag)

    def has_scope(self):
        return self.scope_name is not None

    def __str__(self):
        return self.scope_name


class TagToApprove(models.Model):
    tag_app_name = models.CharField('Tag name', max_length=50, blank=True)
    comment = models.ForeignKey(Scope, related_name='comment', on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.tag_app_name


class University(models.Model):
    title = models.CharField('name', max_length=100)
    link = models.CharField('link', max_length=500, default='', blank=True)

    def has_scope(self):
        return self.title is not None

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField('title', max_length=200)
    code = models.CharField('code', max_length=50, blank=True, default='')
    university = models.ForeignKey(University, related_name='university', on_delete=models.CASCADE, null=True)
    description = models.CharField('description', max_length=500,  default='')
    link = models.CharField('link', max_length=500, default='', blank=True)
    tag_1 = models.ForeignKey(Tag, related_name='tag_1', on_delete=models.CASCADE, null=True)
    tag_2 = models.ForeignKey(Tag, related_name='tag_2', on_delete=models.CASCADE, null=True)
    tag_3 = models.ForeignKey(Tag, related_name='tag_3', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
