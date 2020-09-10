from django.db import models
from django.utils import timezone

from genre.models import Genre

from user.models import TMAuthor

class TMSeries(models.Model):
    series_id = models.AutoField(primary_key=True)
    series_title = models.CharField(max_length=30)
    introduce = models.CharField(max_length=1000, null=True, blank=True)
    paid_subscription = models.BooleanField(default=False)
    series_genre = models.ManyToManyField(Genre, related_name='series_genre')
    last_uploaded_date = models.DateTimeField(default = timezone.now)
    tomag_num_total = models.PositiveIntegerField()     #토막글 수 종합
    heart_num_total = models.PositiveIntegerField()     #공감 수
    comment_num_total = models.PositiveIntegerField()   #댓글 수 종합
    views_num_total = models.PositiveIntegerField()     #조회 수 종합
    writer = models.ForeignKey(TMAuthor, on_delete=models.CASCADE)

    def __str__(self):
        return self.series_title

class TMText(models.Model):
    text_id = models.AutoField(primary_key=True)
    text_title = models.CharField(max_length=30)
    main_sentence = models.CharField(max_length=200, null=True, blank=True)
    content = models.CharField(max_length=5000)
    text_genre =  models.ManyToManyField(Genre, related_name='text_genre')
    heart_num = models.PositiveIntegerField()     #공감 수
    comment_num = models.PositiveIntegerField()   #댓글 수
    views_num = models.PositiveIntegerField()     #조회 수
    date_of_write = models.DateField(default = timezone.now)
    writer = models.ForeignKey(TMAuthor, on_delete=models.CASCADE)
    series = models.ForeignKey(TMSeries, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text_title