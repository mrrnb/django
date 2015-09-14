#!/root/github/django/mysite/manage.py shell
from django.template import Template, Context
from django.conf import settings

raw_template = """Hi {{person.u.upper}}, My name is {{person.my.upper}}, Welcome to here {{ person.age.isdigit }}"""
t = Template(raw_template)
person = {'u':'Obama','my':'Ezreal','age':'22'}
c = Context({'person':person})
print t.render(c)
