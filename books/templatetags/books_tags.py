from django.template.defaulttags import register


@register.filter
def translated_pages(func, user):
    return func.filter(translator=user).filter(is_translated=True).count()


@register.filter
def remain_pages(func, user):
    return func.filter(translator=user).filter(is_translated=False).count()
