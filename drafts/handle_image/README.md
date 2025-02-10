collect images online

- startapp image

outline

- create app
- data model
- form
- function view
- URL config

```python


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
```

collect and manage images

```python


# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import ImageForm
from .models import Image


@login_required
@csrf_exempt
@require_POST
def upload_image(request):
    form = ImageForm(request.POST)

    if form.is_valid():
        try:
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return JsonResponse({"status": "1"})
        except:
            return JsonResponse({"status": "0"})
```

thumbnail image

[sorl-thrmbnail](https://github.com/jazzband/sorl-thumbnail)

displaying images

# ref

[imagefield](https://docs.djangoproject.com/en/5.1/ref/models/fields/#imagefield)
[discussion about thumbnail contribution for django ](https://docs.djangoproject.com/wiki/Thumbnails)
[jQuery](http://jquery.com)
[nodejs](https://nodejs.org/en)
[javascript](https://docs.djangoproject.com/en/5.1/internals/contributing/writing-code/javascript)
[django-jquery](https://pypi.python.org/pypi/django-jquery)
[Serialzing django objects](docs.djangoproject.com/en/5.1/topics/serialization)
