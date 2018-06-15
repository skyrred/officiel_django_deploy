from django import template
from blog.models import *
from django.shortcuts import get_object_or_404
register = template.Library()

@register.assignment_tag
def define(val=None):
    return val

@register.simple_tag
def get_flag(country = None):
	flag_link = get_object_or_404(flags,country_name = country)
	#print(vars(flag_link))
	#print(vars(flag_link))
	return flag_link.flag_url

@register.simple_tag
def get_teams(rank=None):
	teams = get_object_or_404(group , rank = rank).team_set.all().order_by("-Points")
	return teams

@register.simple_tag
def get_matches(date=None):
	matches = get_object_or_404(match_dates , date = date).all_matches_set.all()
	return matches

