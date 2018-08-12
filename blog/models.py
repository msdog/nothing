from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField('标题', max_length = 70)
  body = models.TextField('内容', max_length=200, blank=True)
  created_time = models.DateTimeField('发布时间')

  class Mate:
    verbose_name = '文章'
    verbose_name_plural = '文章'
    
  def __str__(self): # 默认返回 在templates中渲染
    return self.body
