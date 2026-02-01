from django.db import models
from django.utils.text import slugify
import uuid

# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=300, null=False, blank=False)
    slug = models.SlugField(max_length=300, null=False, blank=True, default="")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.slug

    def save(self):
        self.slug = slugify(self.title)
        super().save()
