from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    
def count(request):
    full_text = request.GET['fulltext']

    wordlist = full_text.split()

    worddict = {}

    for word in wordlist:
        if word in worddict:
            #Increase
            worddict[word] += 1
        
        else:
            #Add to the dictionary
            worddict[word] = 1

    sortedwords = sorted(worddict.items(), 
    key=operator.itemgetter(1),
    reverse=True)

    return render(request, 'count.html', 
    {'full_text':full_text, 
    'count':len(wordlist), 
    'sortedwords':sortedwords})
