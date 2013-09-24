# -*- coding: utf-8 -*-
from django.conf import settings

from moocng.externalapps.base import ExternalApp


class Wordpress(ExternalApp):

    class Meta:
        model = 'externalapps.ExternalApp'
        instance_type = 'wordpress'
        instances = settings.MOOCNG_EXTERNALAPPS['wordpress']['instances']
