from django.urls import path
from . import views

urlpatterns = [
    path('markdown/<int:markdown_id>/', views.render_markdown_from_database, name='render_markdown'),
    path('upload/', views.upload_image, name='upload_image'),  # Для загрузки изображений
    path('images/', views.image_list, name='image_list'),     # Для просмотра списка изображений
    # path('image/<int:image_id>/', views.image_detail, name='image_detail'),
    path('papers/', views.paper_list, name='paper_list'),     # Для просмотра списка статей
    path('papers/<int:paper_id>/', views.show_paper, name='show_paper'),

]