from django.contrib import admin
from .models import Course, Tag, Scope, University, TagToApprove


class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'scope_name')


admin.site.register(Course)
admin.site.register(TagToApprove)
admin.site.register(Tag)
admin.site.register(Scope, MyModelAdmin)
admin.site.register(University)
