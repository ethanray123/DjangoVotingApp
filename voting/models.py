from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count


class Position(models.Model):
    position_title = models.CharField(max_length=200)
    maximum_candidates = models.IntegerField(default=0)

    def __str__(self):
        return self.position_title

    def is_voted(self, voter):
        return voter.votes.filter(candidate__position=self).exists()

    @property
    def candidates(self):
        """
        Conditions when Displaying Candidates of a Position:

        - if current user has already voted for a candidate with
        that position, the user is prompted not to vote for this
        position

        """
        return self.candidate_infos.order_by("user__last_name")

    @property
    def get_leading(self):
        candidates = Candidate.objects.filter(
            position=self).annotate(
                num_votes=Count('votes')).order_by("-num_votes")
        if candidates:
            if(candidates.first().num_votes > 0):
                return candidates.first().user
            else:
                return None
        else:
            return None
        return None


class PartyList(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='candidate_info'
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name='candidate_infos'
    )
    party = models.ForeignKey(
        PartyList,
        on_delete=models.CASCADE,
        related_name='candidate_infos',
        null=True,
        blank=True
    )

    def __str__(self):
        return "{} running for {}".format(
            self.user.get_full_name(), self.position.position_title)

    def save(self, *args, **kwargs):
        if not self.party:
            self.party = None
        super(Candidate, self).save(*args, **kwargs)

    @property
    def no_of_votes(self):
        return self.votes.Count()

    def is_voted(self, voter):
        return self.votes.filter(owner=voter).exists()


class Vote(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='votes'
    )
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name='votes'
    )
    when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Voted for " + self.candidate.user.get_full_name()
