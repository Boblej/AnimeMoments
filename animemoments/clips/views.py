from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import AnimeSeries, Season, Episode

@login_required
def Clips(request):
    if request.COOKIES.get('login_success'):
        anime_series = AnimeSeries.objects.all()
        return render(request, 'clips/Clips.html', {'anime_series': anime_series}, )
    else:
        return redirect('land')

def anime_seasons(request, series_id):
    anime_series = get_object_or_404(AnimeSeries, pk=series_id)
    seasons = Season.objects.filter(series=anime_series)
    return render(request, 'anime_seasons.html', {'anime_series': anime_series, 'seasons': seasons})

def season_episodes(request, season_id):
    season = get_object_or_404(Season, pk=season_id)
    episodes = Episode.objects.filter(season=season)
    return render(request, 'season_episodes.html', {'season': season, 'episodes': episodes})