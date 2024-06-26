from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Категория товаров",
        help_text="Введите название категории",
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание", help_text="Опишите категорию"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание", help_text="Опишите продукт"
    )
    # manufactured_at = models.DateField(
    #     blank=True, null=True, verbose_name="Дата производства", help_text="Введите дату производства"
    # )
    image = models.ImageField(
        upload_to="photo", blank=True, null=True, verbose_name="Загрузите фото продукта"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.FloatField(verbose_name="Цена продукта в руб.")
    created_at = models.DateField(
        blank=True, null=True, verbose_name="Дата создания (записи в БД)"
    )
    updated_at = models.DateField(
        blank=True, null=True, verbose_name="Дата последнего изменения (записи в БД)"
    )
    in_stock = models.BooleanField(default=True)
    owner = models.ForeignKey(User,
                              verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL
                              )

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price", "created_at", "updated_at"]
        permissions = [
            ('can_change_in_stock', 'Can change in stock'),
            ('can_edit_description', 'Can edit description'),
            ('can_edit_category', 'Can edit category')
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт', related_name='prod')
    version_number = models.IntegerField(verbose_name="номер версии")
    name = models.CharField(verbose_name="название версии")
    is_active = models.BooleanField(verbose_name="активная версия")

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
