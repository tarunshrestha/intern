from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte= timezone.now())
    


class ResultsView(generic.DetailView):
    model = Question
    template_name = "results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
         selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
         return render(request,
                        'detail.html',
                        {
                             'question':question,
                             'error_message':'You didnot choose any choice. '
                        }
                       )
    else:
         selected_choice.votes=F("votes") + 1
         selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# Old code:

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return render(request, 'index.html' ,context)

# def detail(request, question_id):
#         question = get_object_or_404(Question, pk=question_id)
#         return render(request, 'detail.html', {'question':question})

# def result(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/result.html', {'question':question})


