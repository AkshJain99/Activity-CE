#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.contrib.auth.models import Group

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False


@register.filter
@stringfilter
def template_exists(template_name="links.html"):
    try:
        template.loader.get_template(template_name)
        return True
    except template.TemplateDoesNotExist:
        return False
