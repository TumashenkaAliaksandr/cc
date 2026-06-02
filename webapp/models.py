from django.db import models
from django.urls import reverse


class CompanyInfo(models.Model):
    name = models.CharField("Company Name", max_length=255)
    phone = models.CharField("Phone Number", max_length=50)
    email = models.EmailField("Email Address")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company Info"
        verbose_name_plural = "Company Info"


class Service(models.Model):
    title = models.CharField("Service Title", max_length=255)
    description = models.TextField("Description")
    price = models.DecimalField("Price", max_digits=10, decimal_places=2, null=True, blank=True)
    main_photo = models.ImageField("Main Photo", upload_to='services/main_photos/')

    def __str__(self):
        return self.title

class ServicePhoto(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='additional_photos')
    photo = models.ImageField("Additional Photo", upload_to='services/additional_photos/')
    alt_text = models.CharField("Alt Text", max_length=255, blank=True)

    def __str__(self):
        return f"Photo for {self.service.title}"


class MoreServices(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название услуги"
    )

    slug = models.SlugField(
        unique=True,
        verbose_name="Slug"
    )

    image = models.ImageField(
        upload_to="services/",
        verbose_name="Изображение"
    )

    icon = models.CharField(
        max_length=20,
        default="🛒",
        blank=True,
        verbose_name="Иконка"
    )

    short_description = models.TextField(
        verbose_name="Краткое описание"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Активна"
    )

    sort_order = models.PositiveIntegerField(
        default=0,
        verbose_name="Сортировка"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["sort_order", "name"]
        verbose_name = "More Service"
        verbose_name_plural = "More services"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "service_detail",
            kwargs={"slug": self.slug}
        )
