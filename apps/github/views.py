from django.http import HttpResponse
from django.conf import settings

import commands
import os


# hace git pull y copia los archivos estaticos a public_html
def update(solicitud):
    os.chdir(os.path.dirname(os.path.dirname(__file__)))

    gitpull = commands.getstatusoutput('git pull origin master')[1]

    return HttpResponse("<pre>"+gitpull+"</pre>")
