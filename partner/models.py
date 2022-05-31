from django.db import models
from django.contrib.auth.models import User
from main.models import TagToApprove, University


class Partner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    university = models.ForeignKey(University, related_name='vuz', on_delete=models.CASCADE, null=True)
    mobile = models.CharField(max_length=20, null=False)
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name
