from django import forms
from .models import MarkdownContent, Image, Paper
from .tools import ImageSaver

class MarkdownContentForm(forms.ModelForm):
    class Meta:
        model = MarkdownContent
        fields = ['title', 'markdown_content']


class ImageForm(forms.ModelForm):
    # class Meta:
    #     model = Image
    #     fields = ['file_name', 'image']
    class Meta:
        model = Image
        fields = ['image']

    def save(self, commit=True):
        image_instance = super().save(commit=False)
        image_file = self.cleaned_data['image']
        image_saver = ImageSaver(image_file)  # Создаем экземпляр ImageSaver
        image_instance = image_saver.save()    # Вызываем метод save() ImageSaver для сохранения изображения
        if commit:
            image_instance.save()
        return image_instance

class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = ['title', 'title', 'content', 'author']