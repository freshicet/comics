from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.http import Http404

def index(request): 
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")

def webcomiclist(request):
	from webcomicupdate import updateforFP
	from webcomicupdate import updateforTAY
	from webcomicupdate import updateforGG
	from webcomicupdate import updateforLAD
	from webcomicupdate import updateforMT
	from webcomicupdate import updateforQV
	from webcomicupdate import updateforSAW
	from webcomicupdate import updateforxkcd
	from webcomicupdate import updateforBS
	from webcomicupdate import updateforpbf
	from webcomicupdate import updateforCC
	from webcomicupdate import updateforD_C
	from webcomicupdate import updateforTA
	from webcomicupdate import updateforSMBC
	from webcomicupdate import updateforAC
	from webcomicupdateforWM import updateforWM
	return render_to_response('webcomiclist.html',{'updateforFP': updateforFP,'updateforTAY': updateforTAY
	,'updateforGG': updateforGG,'updateforLAD': updateforLAD,'updateforMT': updateforMT
	,'updateforQV': updateforQV,'updateforSAW': updateforSAW,'updateforxkcd': updateforxkcd
	,'updateforBS': updateforBS,'updateforpbf': updateforpbf,'updateforCC': updateforCC
	,'updateforWM': updateforWM,'updateforD_C': updateforD_C,'updateforTA': updateforTA
	,'updateforSMBC': updateforSMBC,'updateforAC': updateforAC})

def webcomiclistsection(request):
	if 'q' in request.GET:
		q = request.GET['q']
		if q == 'Flaky_pastry':
			from FP import comicTitle,comicURL,homepage,title
		if q == 'the_awkward_yeti':
			from webcomicTAY import comicTitle,comicURL,homepage,title
		if q == 'girl_genius':
			from GG import comicTitle,comicURL,homepage,title
		if q == 'lack_a_daisy':
			from webcomicLad import comicTitle,comicURL,homepage,title
		if q == 'mega_tokyo':
			from webcomicMT import comicTitle,comicURL,homepage,title
		if q == 'quantum_vibe':
			from webcomicQV import comicTitle,comicURL,homepage,title
		if q == 'sandra_and_woo':
			from webcomicSAW import comicTitle,comicURL,homepage,title
		if q == 'xkcd':
			from webcomicxkcd import comicTitle,comicURL,homepage,title
		if q == 'Dinosaur_Comics':
			from webcomicDC import comicTitle,comicURL,homepage,title	
		if q == 'butter_safe':
			from webcomicBS import comicTitle,comicURL,homepage,title
		if q == 'the_perry_bible_fellowship':
			from webcomicpbf import comicTitle,comicURL,homepage,title
		if q == 'cardboard_crack':
			from webcomicCC import comicTitle,comicURL,homepage,title
		if q == 'Wonder_mark':
			from webcomicWM import comicTitle,comicURL,homepage,title
		if q == 'The_Abominable':
			from webcomicTA import comicTitle,comicURL,homepage,title
		if q == 'Saturday_Morning_Breakfast_Cereal':
			from webcomicSMBC import comicTitle,comicURL,homepage,title
		if q == 'Axe_Cop':
			from webcomicAC import comicTitle,comicURL,homepage,title			
		return render_to_response('webcomiclistsection.html',{'comicTitle': comicTitle,'comicURL': comicURL,'homepage': homepage,'title': title})
	
def email(request):
    return render(request,"email.html")

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response