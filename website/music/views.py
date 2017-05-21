from django.http import Http404
from django.http import HttpResponse
from .models import  Album,Song
#from django.template import loader
from django.shortcuts import render, get_object_or_404
"""
def index(request):
    all_albums=Album.objects.all()
    html=''
    for album in all_albums:
        url='/music/'+str(album.id)+'/'
        html+='<a href="'+url+'">'+album.album_title + '</a><br>'
    return HttpResponse(html)
"""
"""
"""
def index(request):
    all_albums=Album.objects.all()
    #template=loader.get_template('music/index.html')
    context={
        'all_albums':all_albums,
    }
    #return HttpResponse(template.render(context,request))
    return render(request,'music/index.html',context)

def details(request,album_id):
    #return HttpResponse("<h2>Details for Album id:" + str(album_id)+"</h2>")
    album=get_object_or_404(Album,pk=album_id)
    return render(request, 'music/detail.html', {'album':album})

def favourite(request,album_id):
    #return HttpResponse("<h2>Details for Album id:" + str(album_id)+"</h2>")
    album=get_object_or_404(Album,pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
            return render(request, 'music/detail.html', {
                'album': album,
                'error_message': "You did not select a valid song"
            })
    else:
        selected_song.is_favourite= True
        selected_song.save()
        return render(request, 'music/detail.html', {'album':album})
