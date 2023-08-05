from django import template

register = template.Library()


@register.filter
def only_active_comments(comments):
    return comments.filter(active=True)  # comments.exclude(active=False)


@register.filter
def order_by_date_time(comments):
    return comments.order_by('-datetime_modified')
