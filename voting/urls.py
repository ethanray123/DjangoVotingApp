from django.urls import path
from . import views
# from django.contrib.auth.views import login


app_name = 'voting'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('independent/', views.IndependentView.as_view(), name='independent'),
    path('party/', views.PartyView.as_view(), name='party'),
    path('vote/candidate/<int:candidate_id>', views.vote, name='vote'),
    path('vote/party/<int:party_id>', views.voteParty, name='vote-party'),
    path('candidate/<int:candidate_id>', views.CandidateView.as_view(), name='candidate-detail'),
]
