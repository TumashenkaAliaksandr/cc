from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class CompanyInfo(models.Model):
    name = models.CharField("Company Name", max_length=255)
    phone = models.CharField("Phone Number", max_length=50)
    email = models.EmailField("Email Address")
    logo = models.ImageField("Logo", upload_to="logo", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company Info"
        verbose_name_plural = "Company Info"


class SliderService(models.Model):
    title = models.CharField("Service Title", max_length=255)
    description = models.TextField("Description")
    price = models.DecimalField("Price", max_digits=10, decimal_places=2, null=True, blank=True)
    main_photo = models.ImageField("Main Photo", upload_to='services/main_photos/')

    def __str__(self):
        return self.title

class SliderServicePhoto(models.Model):
    service = models.ForeignKey(SliderService, on_delete=models.CASCADE, related_name='additional_photos')
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

    icon = models.ImageField(
        upload_to="services/icons/",
        blank=True,
        null=True,
        verbose_name="Иконка"
    )

    like = models.CharField(
        max_length=20,
        default="🤍",
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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    photo = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


class ProfessionalApplication(models.Model):
    TYPE_CHOICES = (
        ('individual', 'Individual'),
        ('company', 'Company'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    application_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    company_name = models.CharField(
        max_length=255,
        blank=True
    )

    profession = models.CharField(
        max_length=255,
        blank=True
    )

    description = models.TextField()

    service_area = models.CharField(
        max_length=255
    )

    status = models.CharField(
        max_length=20,
        default='pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

class Contractor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    company_name = models.CharField(
        max_length=255,
        blank=True
    )

    profession = models.CharField(
        max_length=255
    )

    description = models.TextField()

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=5.0
    )

    approved = models.BooleanField(
        default=False
    )