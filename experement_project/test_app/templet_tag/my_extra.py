from django import template

register = template.Library()

def cut(value,arg):
    """
        This Cuts out all Value of "arg" from the Strging
    """

    return value.replace(arg,'')

register.filter('cut',cut)
