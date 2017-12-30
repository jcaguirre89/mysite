from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'photos/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """ Return the last 5 published questions.
        Not including those set to be published in the future
        lte: Less Than or Equal to"""
        return Question.objects.filter(
                pub_date__lte=timezone.now()
                ).order_by('pub_date')[:5]


"""
there is also a get_list_or_404 which uses the models method filter instead
of get

#first, most basic version. note the try to check if question id exists
def detail(request, question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")  
    return render(request,
                  'photos/detail.html',
                  {'question': question})    

#second version, uses the get_object_or_404 shortcut
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,
                  'photos/detail.html',
                  {'question': question})
    
    
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,
                  'photos/results.html',
                  {'question': question})
"""

class DetailView(generic.DetailView):
    model = Question
    template_name = 'photos/detail.html'
    
    def get_queryset(self):
        """
        Excludes any question that isn't published yet
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'photos/results.html'



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #If selected choice exists, add it to DB and save, else redirect back
    #to question detail page
    #if voted succesfully, redirect to results page
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form
        return render(request,
                      'photos/detail.html',
                      {'question': question,
                       'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        #always return an HttpResponseRedirect after succesfully dealing
        #with POST data. this prevents data from being posted twice if a
        #user hits the back button.
        return HttpResponseRedirect(reverse('photos:results',
                                            args=(question.id,)))
        


        