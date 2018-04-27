from django.contrib import admin
from .models import Position, Candidate, PartyList, Vote
# Register your models here.

admin.site.register(Position)
admin.site.register(PartyList)
admin.site.register(Candidate)
admin.site.register(Vote)
