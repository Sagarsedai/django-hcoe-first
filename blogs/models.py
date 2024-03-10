from django.db import models
import uuid
from tinymce import models as tmc_model


class BlogTag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Blog Tag"
        verbose_name_plural = "Blog Tag(s)"

    def __str__(self) -> str:
        return self.name


class BlogAuthors(models.Model):
    author = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Blog Author"
        verbose_name_plural = "Blog Author(s)"

    def __str__(self) -> str:
        return self.author


class Blog(models.Model):

    title = models.CharField(max_length=255)

    sub_title = models.CharField(max_length=500, null=True, blank=True)

    image = models.ImageField()
    description = tmc_model.HTMLField()

    tag = models.ForeignKey(
        BlogTag,
        on_delete=models.PROTECT,
        related_name="blogs",
    )

    authors = models.ManyToManyField(
        BlogAuthors,
        blank=True,
        related_name="authors_blogs",
    )

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog(s)"

    def __str__(self) -> str:
        return self.title
