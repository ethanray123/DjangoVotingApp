from django.views.generic import DetailView, ListView
from .models import Candidate, PartyList, Position, User, Vote
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


class HomeView(ListView):
    model = Position
    template_name = "home.html"
    context_object_name = "positions"


class IndependentView(ListView):
    model = Position
    template_name = "position/independent.html"
    context_object_name = "positions"


class PartyView(ListView):
    model = PartyList
    template_name = "position/party.html"
    context_object_name = "parties"


class CandidateView(DetailView):
    model = Candidate
    template_name = "position/candidate.html"
    context_object_name = "candidate"


def vote(request, candidate_id):
    voter = request.user
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    if (
        not candidate.is_voted(voter) and
            not candidate.position.is_voted(voter)):
        Vote.objects.create(owner=voter, candidate=candidate)
        message = "Vote Successfully Registered"
    else:
        message = "Cannot Vote! Vote Has Already Been Casted"

    # redisplay the individual voting form.
    # add a Vote instance with:
    # -the current user as the owner and
    # -the candidate voted as the candidate

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return render(
        request, 'position/vote.html',
        {
            'message': message,
        })
