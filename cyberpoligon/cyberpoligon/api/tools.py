import hashlib
import uuid
from django.core.files.storage import default_storage
from django.utils.text import slugify
from .models import Image

class ImageSaver:
    def __init__(self, file):
        self.file = file

    def save(self):
        self.img = self.__find_by_md5_hash()
        if self.img is not None:
            return self.img

        # Генерация уникального имени файла с использованием UUID
        file_extension = self.file.name.split('.')[-1]
        file_name = f"{uuid.uuid4()}.{file_extension}"

        self.img = Image(
            id=str(uuid.uuid4()),
            file_name=file_name,
            mime_type=self.file.content_type,
            md5_hash=self.md5_hash
        )

        with default_storage.open(file_name, 'wb+') as destination:
            for chunk in self.file.chunks():
                destination.write(chunk)

        self.img.save()
        return self.img

    def __find_by_md5_hash(self):
        self.md5_hash = hashlib.md5(self.file.read()).hexdigest()
        self.file.seek(0)
        return Image.objects.filter(md5_hash=self.md5_hash).first()
