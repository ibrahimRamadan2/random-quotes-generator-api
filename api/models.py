from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Author(models.Model):
    name = models.CharField(_("Author Name"), max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"


class Quote(models.Model):
    quote = models.CharField(_("quote"), max_length=200)
    author = models.ForeignKey(Author,
                               related_name="qoutes",
                               on_delete=models.CASCADE)

    def __str__(self) -> str:

        return f"{self.author.name} quote {self.id}"


# generate Quotes
# hima = Author.objects.get(id=2)
# for i in range(10, 100):
#     Quote.objects.create(quote=f"Quote num {i}", author=hima)
