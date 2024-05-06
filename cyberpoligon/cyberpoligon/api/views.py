import hashlib
import json
import uuid
import time
from django.conf import settings
from django.core.files.storage import default_storage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from markdown2 import markdown

from .form import ImageForm
from .models import Image, MarkdownContent, Paper
from .tools import ImageSaver


def render_markdown_from_database(request, markdown_id):
    markdown_instance = MarkdownContent.objects.get(pk=markdown_id)
    html_content = markdown(markdown_instance.markdown_content)
    return render(
        request, "cyberpoligon/render_markdown.html", {"html_content": html_content}
    )


def upload_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            image_saver = ImageSaver(request.FILES["image"])
            image_saver.save()
            return redirect(
                "image_list"
            )  # Перенаправление на страницу со списком изображений
    else:
        form = ImageForm()
    return render(request, "cyberpoligon/upload_image.html", {"form": form})


def image_list(request):
    images = Image.objects.all()
    return render(request, "cyberpoligon/image_list.html", {"images": images})


def paper_list(request):
    papers = Paper.objects.all()
    return render(request, "cyberpoligon/paper_list.html", {"papers": papers})


def show_paper(request, paper_id):
    paper = Paper.objects.get(pk=paper_id)
    title = paper.title
    html_content = markdown(paper.content)
    return render(
        request,
        "cyberpoligon/show_paper.html",
        {"title": title, "html_content": html_content},
    )


@csrf_exempt
def submit_view(request):
    if request.method == "POST":
        # Получение JSON данных из запроса
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError as e:
            return JsonResponse(
                {
                    "status": "error",
                    "message": "Ошибка разбора JSON: {}".format(str(e)),
                },
                status=400,
            )

        # Сохранение JSON данных в файл
        try:
            with open("JSON/%Y%m%d-%H%M%S.json", "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            return JsonResponse(
                {
                    "status": "error",
                    "message": "Ошибка сохранения данных в файл: {}".format(str(e)),
                },
                status=500,
            )

        return JsonResponse({"status": "success"})
    else:
        return JsonResponse(
            {"status": "error", "message": "Метод не поддерживается"}, status=405
        )
