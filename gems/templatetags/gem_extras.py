from django import template

register = template.Library()


@register.filter(name='underscore')
def underscore(title):
    # Remove the underscores from the key names
    return " ".join(title.split('_'))
