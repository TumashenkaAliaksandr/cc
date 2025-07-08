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
