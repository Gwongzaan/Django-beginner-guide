from urllib import request

from django import forms
from django.core.files.base import ContentFile
from slugify import slugify

from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = (
            "title",
            "url",
            "description",
        )

    def clean_url(self):
        url = self.cleaned_data["url"]
        valid_extensions = [
            "jpg",
            "jpeg",
            "png",
        ]
        extension = url.rsplit(".", 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError("given URL does not match valid extensions")

        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super(ImageForm, self).save(commit=False)
        image_url = self.cleaned_data["url"]
        image_name = f'{slugify(image.title)}.{image_url.rsplit(".", 1)[1].lower()}'

        response = request.urlopen(image_url)

        image.image.save(image_name, ContentFile(response.read()), save=False)

        if commit:
            image.save()
        return image
