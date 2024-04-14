from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from markdown2 import markdown
from .models import MarkdownContent, Image, Paper
from .form import ImageForm
from .tools import ImageSaver
from django.views import generic
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import uuid
from django.core.files.storage import default_storage
import hashlib


def render_markdown_from_database(request, markdown_id):
    markdown_instance = MarkdownContent.objects.get(pk=markdown_id)
    html_content = markdown(markdown_instance.markdown_content)
    return render(request, 'cyberpoligon/render_markdown.html', {'html_content': html_content})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            image_saver = ImageSaver(request.FILES['image'])  
            image_saver.save()
            return redirect('image_list')  # Перенаправление на страницу со списком изображений
    else:
        form = ImageForm()
    return render(request, 'cyberpoligon/upload_image.html', {'form': form})

def image_list(request):
    images = Image.objects.all()
    return render(request, 'cyberpoligon/image_list.html', {'images': images})

def paper_list(request):
    papers = Paper.objects.all()
    return render(request, 'cyberpoligon/paper_list.html', {'papers': papers})

def show_paper(request, paper_id):
    paper = Paper.objects.get(pk=paper_id)
    title = paper.title
    html_content = markdown(paper.content)
    return render(request, 'cyberpoligon/show_paper.html', {'title': title, 'html_content': html_content})
