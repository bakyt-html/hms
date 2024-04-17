from django.conf.urls.static import static
from django.urls import path, include

from hms_prj import settings
from . import views
urlpatterns = [
    # path('', views.base_page),
    path('rooms/', views.room_list),
    path('', views.main_page),
    path('rooms/<int:room_id>/', views.room_detail)
    # path('', views.index)
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)