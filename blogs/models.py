from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=255)

    sub_title = models.CharField(max_length=500, null=True, blank=True)

    image = models.ImageField()
    description = models.TextField()

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog(s)"

    def __str__(self) -> str:
        return self.title
