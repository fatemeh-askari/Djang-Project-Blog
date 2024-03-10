from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        PUBLISHED = 'PB', 'Published'

    class PublishedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=Post.Status.PUBLISHED)

    title = models.CharField(max_length=300, verbose_name='title')
    slug = models.SlugField(max_length=300,verbose_name='slug')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='author')
    image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True, null=True, verbose_name='image')
    body = models.TextField(verbose_name='text')
    publish = models.DateTimeField(default=timezone.now, verbose_name='publish')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='updated')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name='status')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)
        indexes = [
            models.Index(fields=['title'])
        ]
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80, verbose_name='name')
    email = models.EmailField()
    body = models.TextField(verbose_name='text')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'comment by {self.name} on {self.post}'


class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=80)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    answer_admin = models.TextField(null=True, blank=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']
        verbose_name = "Contact us"
        verbose_name_plural = "Contact us"

    def __str__(self):
        return f'{self.name} by {self.email} on {self.subject}'


class Project(models.Model):
    title = models.CharField(max_length=80, verbose_name='project title')
    employer = models.CharField(max_length=80, verbose_name='employer')
    image = models.ImageField(upload_to='projects/', null=True, blank=True, verbose_name='project image')
    video = models.FileField(upload_to='videos/', verbose_name='video file', null=True, blank=True)
    date = models.CharField(max_length=80, verbose_name='date published project')
    language = models.CharField(max_length=100, verbose_name='project language')
    preview = models.URLField(verbose_name='project preview')

    def __str__(self):
        return f'{self.title} for {self.employer}'
