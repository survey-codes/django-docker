import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.CharField(primary_key=True, default="Empty", editable=False, max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def disable(self):
        self.is_active = False
        self.save()

    class Meta:
        abstract = True
