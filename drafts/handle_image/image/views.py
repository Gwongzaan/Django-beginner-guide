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


@login_required()
def list_image(request):
    images = Image.objects.filter(user=request.user)
    return render(request, "image/list_images.html", {"images": images})


@login_required()
@require_POST
@csrf_exempt
def del_image(request):
    image_id = request.POST["image_id"]
    try:
        image = Image.objects.get(id=image_id)
        image.delete()
        return JsonResponse({"status": "1"})
    except:
        return JsonResponse({"status": "2"})
