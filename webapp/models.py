from django.db import models

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
