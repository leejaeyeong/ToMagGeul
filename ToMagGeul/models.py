from django.db import models

from genre.models import Genre

from user.models import TMAuthor

class TMseries(models.Model):
    series_id = models.AutoField(primary_key=True)
    series_title = models.CharField(max_length=30)
    introduce = models.CharField(max_length=1000, null=True, blank=True)
    paid_subscription = models.BooleanField(default=False)
    foler_genre = models.ManyToManyField(Genre, related_name='foler_genre')
    last_uploaded_date = models.DateTimeField(default = timezone.now)
    tomag_num_total = models.PositiveIntegerField()     #토막글 수 종합
    heart_num_total = models.PositiveIntegerField()     #공감 수
    comment_num_total = models.PositiveIntegerField()   #댓글 수 종합
    views_num_total = models.PositiveIntegerField()
    writer = models.ForeignKey(TMAuthor)

    def __str__(self):
        return self.series_title