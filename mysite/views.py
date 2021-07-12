from django.shortcuts import render
from django.http import HttpResponse
from pytube import YouTube
def youtube(request):
    return render(request,'youtube.html')

def downloadVideo(request):
    link =  request.POST.get('link')
    print(link)
    video=YouTube(link)
    stream =video.streams.get_highest_resolution()
    stream.download()
    return render(request, 'youtube.html')