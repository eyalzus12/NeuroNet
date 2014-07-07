from coplay.models import Feedback, Task, Decision, Vote, Discussion, Viewer, \
    FollowRelation, Segment, UserProfile, UserUpdate
from django.contrib import admin

# Register your models here.

class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')
    
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ( 'feedbabk_type', 'created_at')
    ordering = ['feedbabk_type', 'created_at']
    search_fields = ['feedbabk_type']


class TaskAdmin(admin.ModelAdmin):
    list_display = ( 'responsible', 'goal_description')

class VoteAdmin(admin.ModelAdmin):
    list_display = ( 'voater', 'value')

class DecisionAdmin(admin.ModelAdmin):
    list_display = ( 'content','created_at')

class ViewerAdmin(admin.ModelAdmin):
    list_display = ('user', 'discussion')
    
class FollowRelationAdmin(admin.ModelAdmin):
    list_display = ( 'follower_user', 'following_user')

class SegmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'segment')

    
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'header')
        

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Decision, DecisionAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(Discussion, DiscussionAdmin)

admin.site.register(Viewer, ViewerAdmin)
admin.site.register(FollowRelation, FollowRelationAdmin)
admin.site.register(Segment, SegmentAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserUpdate, UpdateAdmin)


