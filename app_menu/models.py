from django.db import models


class TreeMenuCategory(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name="Name")
    verbose_name = models.CharField(max_length=255, blank=True, verbose_name="Verbose name")

    def __str__(self):
        return f"{self.verbose_name}"

    class Meta:
        verbose_name = 'Menu category'
        verbose_name_plural = 'Menu categories'


class TreeMenu(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name="Name")
    category = models.ForeignKey(
        TreeMenuCategory,
        on_delete=models.CASCADE,
        verbose_name="Category",
    )
    path = models.CharField(max_length=1000, blank=True, verbose_name="Link")
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=0,
        verbose_name="Parent element",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'
