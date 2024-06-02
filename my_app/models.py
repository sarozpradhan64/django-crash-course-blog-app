from django.db import models

STATUS_CHOICES = (('draft', 'DRAFT'), ('published', 'PUBLISHED'))

class Blog(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    content = models.TextField()
    is_featured = models.BooleanField(default=False, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True)
    publish_date = models.DateField()

    def __str__(self):
        return self.title+" by: "+self.author

    class Meta:
        ordering = ["id"]

