import random
import string
from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instancia, new_slug=None):
    """
    This is for a Django project and it assumes your instancia
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        marcado = new_slug
    else:
        marcado = slugify(instancia.nombre)

    Klass = instancia.__class__
    qs_exists = Klass.objects.filter(marcado=marcado).exists()
    if qs_exists:
        new_slug = "{marcado}-{randstr}".format(
                    marcado=marcado,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instancia, new_slug=new_slug)
    return marcado
