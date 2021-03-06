from django.contrib import admin

# Register your models here.
from WebApp.models import Team,Player,Matches
class TeamAdmin(admin.ModelAdmin):
    list_display = ["tname","logourl","state"]
admin.site.register(Team,TeamAdmin)

class PlayerAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","player_image","jersy_number","team","country",
                    "matches","runs","heightruns","half_centuries","centuries"]
admin.site.register(Player,PlayerAdmin)

class MatchesAdmin(admin.ModelAdmin):
    list_display = ["match_id","date","time","team1","team2","team1_score","team1_score",
                    "team2_score","team1_overs","team2_overs","result"]
admin.site.register(Matches,MatchesAdmin)