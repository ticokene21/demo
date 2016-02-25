from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .forms import *

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = Choice.objects.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

#########################################################################################################
# INSERT, DELETE, UPDATE


def insert_question(request):
	form = QuestionForm()
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/polls/')
	else:
		form = QuestionForm()
	
	return render(request, 'polls/insert.html',{'form':form})
	 
def delete_question(request,question_id):
	question = Question.objects.get(pk = question_id)
	question.delete()
	return HttpResponseRedirect('/polls/')	

def edit_question(request,question_id):
	form = QuestionForm()
	question = Question.objects.get(pk = question_id)
	if request.method == 'POST':
		form = QuestionForm(request.POST or None,instance=question)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/polls/')
	else:
		form = QuestionForm()

	return render(request,'polls/edit.html',{'form':form})

