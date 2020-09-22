import string
import random

from .models import order

def id_generatorOrder(size=6, chars   = string.ascii_uppercase + string.digits):
    the_id = ''.join(random.choice(chars) for x in range(size))
    try:
        Order = order.objects.get(order_id=the_id)
        id_generatorOrder()
    except order.DoesNotExist:
        return the_id