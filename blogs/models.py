from django.db import models
import uuid


class BlogTag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Blog Tag"
        verbose_name_plural = "Blog Tag(s)"

    def __str__(self) -> str:
        return self.name


class Blog(models.Model):

    title = models.CharField(max_length=255)

    sub_title = models.CharField(max_length=500, null=True, blank=True)

    image = models.ImageField()
    description = models.TextField()

    tag = models.ForeignKey(
        BlogTag,
        on_delete=models.PROTECT,
        related_name="blogs",
    )

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog(s)"

    def __str__(self) -> str:
        return self.title
