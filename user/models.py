from django.db import models
from django.contrib.auth.models import User
from main.models import Scope

DEFAULT_EXAM_ID = 1


class Subj(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    main_sphere = models.ForeignKey(Scope, related_name='main_sphere', on_delete=models.CASCADE, blank=True, default=DEFAULT_EXAM_ID)
    off_sphere = models.ForeignKey(Scope, related_name='off_sphere', on_delete=models.CASCADE, blank=True, default=DEFAULT_EXAM_ID)

    def __str__(self):
        return self.user.first_name
