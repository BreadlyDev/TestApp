from django.contrib import admin

from . import models as m

admin.site.register(m.User)
admin.site.register(m.Profile)
admin.site.register(m.Question)
admin.site.register(m.Answer)
admin.site.register(m.Test)
admin.site.register(m.Course)
admin.site.register(m.Video)
admin.site.register(m.News)
admin.site.register(m.UserAnswer)
admin.site.register(m.UserTest)
