import sae

from dblog import wsgi

application = sae.create_wsgi_app(wsgi.application)
