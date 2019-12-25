from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Question, Choice

import logging
logger = logging.getLogger('common')


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    choises = Choice.objects.select_related('question').all()
    logger.info(choises)
    for c in choises:
        logger.info([c, c.question])


    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
                pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    # question = Question.objects.filter(id=1).first()
    # logger.info(question)
    # choises = question.choice_set.filter(id=1).all()
    # logger.info(choises)
    

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
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

def related_check(request):
    # # choises = Choice.objects.all()
    choises = Choice.objects.all().select_related('question')
    for c in choises:
        logger.info([c, c.question])

    # # qs = Question.objects.all()
    qs = Question.objects.all().prefetch_related('choice_set')
    for q in qs:
        logger.info([q, q.choice_set.all()[0].note])

    from django.db.models import Prefetch
    qs = Question.objects.all().prefetch_related(
        Prefetch('choice_set', queryset=Choice.objects.filter(id__gt=0)))
    for q in qs:
        logger.info([q, q.choice_set.all()[0].note])

    return render(request, 'polls/related_check.html')
