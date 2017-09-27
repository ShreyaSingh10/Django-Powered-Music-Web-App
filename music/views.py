from django.shortcuts import render
from django.http import Http404
#from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Album #only displaying the Albums n not the songs

# Create your views here.
def index(request):
	all_albums = Album.objects.all() #connects to DB looks at Albums table
	# and gets us all the albums
	#template = loader.get_template('music/index.html')
	#context = {'all_albums':all_albums}
	#return render(request, 'music/index.html', context)
	return render(request, 'music/index.html', {'all_albums':all_albums})
	#we pass the request ,the file path to thar template and the context that
	#is the data/info template needs


	#return HttpResponse(template.render(context, request))
	#now we want to loop through a ll the albums
	#html=''
	#for album in all_albums:
		#url='/music/' + str(album.id) +'/'
		#html += '<a href="' + url + '">' + album.album_title + '</a><br>'

	

	#return HttpResponse(html)


def detail(request, album_id):
	try:
		album = Album.objects.get(pk=album_id)
	except Album.DoesNotExist:
		raise Http404("Album does not exist")
	return render(request, 'music/detail.html', {'album': album})
	#return render("<h2>Details for Album id: " + str(album_id) + "</h2>")	

