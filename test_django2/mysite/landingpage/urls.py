from django.contrib import admin
from django.urls import path
from main.views import index, mentor, mentee, board, about, new, postcreate, result, recommend, comment #views.py에 index라는 함수 매칭
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('mentor/',mentor),
    # path('mentor/<int:pk>/'),
    path('mentee/',mentee),
    path('board/',board),
    path('board/new/',new),
    path('about/',about),
    path('postcreate/',postcreate),
    path('result/', result),
    path('mentor/recommend', recommend),
    path('mentor/recommend/comment', comment),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
