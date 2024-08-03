from django.contrib import admin
from .models import AnimeSeries, Season, Episode

class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1

class SeasonInline(admin.TabularInline):
    model = Season
    extra = 1

@admin.register(AnimeSeries)
class AnimeSeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_url')
    search_fields = ('title',)
    inlines = [SeasonInline]

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('series', 'number',)
    search_fields = ('series__title', 'number',)
    list_filter = ('series',)
    inlines = [EpisodeInline]

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('season', 'number', 'title', 'url')
    search_fields = ('season__series__title', 'season__number', 'number', 'title', 'url')
    list_filter = ('season__series', 'season',)

