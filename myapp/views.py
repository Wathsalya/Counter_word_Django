import operator

from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

class MyView(View):

    def get(self, request, *args, **kwargs):
      #  context ={ 'name':'Wathslaya', 'age'  : 25,  'country'  :'Srilanka'
        return render(request,'index.html' )

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	word_dictionary = {}
	for word in wordlist:
		if word in word_dictionary:
			#increase the frequency
			word_dictionary[word] += 1
		else:
			# add the word to the dictionary
			word_dictionary[word] = 1
	# word_dictionary.items convert the dict into list
	sorted_words = sorted(word_dictionary.items(),key=operator.itemgetter(1), reverse = True)
	print(sorted_words)

	return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist),'word_dictionary':word_dictionary,'sorted':sorted_words})


