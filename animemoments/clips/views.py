from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import AnimeSeries, Season, Episode
from subscription.models import Subscription

@login_required
def Clips(request):
    if request.COOKIES.get('login_success'):
        anime_series = AnimeSeries.objects.all()
        subscription_subscription = Subscription.objects.filter(user=request.user)
        return render(request, 'clips/Clips.html', {
            'anime_series': anime_series,
            'subscription_subscription': subscription_subscription
        })
    else:
        return redirect('land')

@login_required
def anime_seasons(request, series_id):
    subscription_subscription = Subscription.objects.filter(user=request.user)
    series = get_object_or_404(AnimeSeries, id=series_id)
    clips_season = Season.objects.filter(series=series).order_by('number')

    multiple_seasons = clips_season.count() > 1

    return render(request, 'clips/anime_seasons.html', {
        'subscription_subscription': subscription_subscription,
        'clips_season': clips_season,
        'series': series,
        'multiple_seasons': multiple_seasons
    })

@login_required
def season_episodes(request, series_id, season_id):
    subscriptions = Subscription.objects.filter(user=request.user)
    season = get_object_or_404(Season, pk=season_id, series__id=series_id)
    episodes = Episode.objects.filter(season=season)

    return render(request, 'clips/episode_detail.html', {
        'season': season,
        'episodes': episodes,
        'subscriptions': subscriptions
    })