from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    # title, body, show, datetime, image

    PUBLIC = 'public'
    PRIVATE = 'private'
    MY = 'my'

    SHOW_TYPES = [
        (PUBLIC, 'PUBLIC'),
        (PRIVATE, 'PRIVATE'),
        (MY, 'MY')
    ]

    title = models.CharField(max_length = 40, help_text="제목")
    body = models.TextField(help_text="포스트 본문 내용")
    show = models.CharField(max_length = 10, choices=SHOW_TYPES, default=PUBLIC, help_text="비공개 여부")
    datetime = models.DateTimeField(default = timezone.now)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null= True, related_name='comments')
    comment_contents = models.CharField(max_length=200)
    comment_writer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']