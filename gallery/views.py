from django.shortcuts import render, get_object_or_404
from .models import GalleryAlbum


def gallery_list(request):
    albums = GalleryAlbum.objects.filter(is_published=True)
    return render(request, 'gallery/list.html', {'albums': albums})


def gallery_album(request, pk):
    album = get_object_or_404(GalleryAlbum, pk=pk, is_published=True)
    photos = album.photos.all()
    return render(request, 'gallery/album.html', {'album': album, 'photos': photos})



