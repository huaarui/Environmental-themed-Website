

from django.db import models
from django.utils import timezone


class ForumPost(models.Model): # 定义论坛帖子模型
    # 定义帖子标题，最大长度为200
    title = models.CharField(max_length=200)
    # 定义帖子内容，使用TextField类型
    content = models.TextField()
    # 定义帖子创建时间，使用DateTimeField类型，auto_now_add=True表示在创建时自动添加当前时间
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment on {self.post.title}"
