from django import forms
from .models import (
    Profile,
    ProfessionalApplication
)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = (
            'photo',
            'phone',
            'city'
        )


class ProfessionalApplicationForm(forms.ModelForm):
    class Meta:
        model = ProfessionalApplication

        fields = (
            'application_type',
            'company_name',
            'profession',
            'description',
            'service_area'
        )

        widgets = {
            'description': forms.Textarea(
                attrs={'rows': 5}
            )
        }
