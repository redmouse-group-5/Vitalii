from django.contrib import admin

# Register your models here.
from comment.models import Comments

class CommentsAdmin(admin.ModelAdmin):
    pass
    # inlines = [
    #     UserInline,
    # ]
admin.site.register(Comments)