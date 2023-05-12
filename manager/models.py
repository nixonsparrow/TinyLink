from django.db import models
from django.shortcuts import redirect


class Link(models.Model):
    original = models.CharField(max_length=1024, null=False, blank=False)
    short = models.CharField(max_length=64, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def redirect(self):
        return redirect(self.original)
