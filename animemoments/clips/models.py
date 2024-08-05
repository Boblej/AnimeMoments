from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify

class AnimeSeries(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Season(models.Model):
    series = models.ForeignKey(AnimeSeries, on_delete=models.CASCADE, related_name='seasons')
    number = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        unique_together = ('series', 'number')
        ordering = ['series', 'number']

    def __str__(self):
        return f'{self.series.title} - Season {self.number}'

class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='episodes')
    number = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    title = models.CharField(max_length=255)
    url = models.URLField()
    download_url = models.URLField(blank=True, null=True)

    class Meta:
        unique_together = ('season', 'number')
        ordering = ['season', 'number']

    def __str__(self):
        return f'{self.season.series.title} - Season {self.season.number} - Episode {self.number}: {self.title}'

    def get_embed_url(self):
        if "watch?v=" in self.url:
            return self.url.replace("watch?v=", "embed/")
        elif "youtu.be" in self.url:
            video_id = self.url.split('/')[-1]
            return f"https://www.youtube.com/embed/{video_id}"
        return self.url