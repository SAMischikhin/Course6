from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.timezone import now

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    description = models.CharField(max_length=500, null=True, blank=True)
    is_published = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(default=now)
    image = models.ImageField(upload_to="image/", null=True, blank=True)

class Comment(models.Model):
    text = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(default=now)

