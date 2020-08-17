from django.contrib import admin
from .models import Post, Question,Choice, Mentor, Board

admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Mentor)
admin.site.register(Board)
