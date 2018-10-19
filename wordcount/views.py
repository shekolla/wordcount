
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request,'home.html',{'shekollasai':'the king'})

def counts(request):

	main_words= request.GET['fulltext']
	each_words = main_words.replace(',',' ').replace('.',' ').split()
	dict_words = {}
	for word in each_words:
		dict_words[word] = dict_words.get(word,0) + 1
	words_list = sorted(dict_words.items(), key=operator.itemgetter(1), reverse=True)
	return render(request, 'counts.html',{'words_list':words_list, 'words_len':len(each_words), 'original':main_words})