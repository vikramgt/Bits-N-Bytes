from django.contrib import admin
from .models import user_id, personal_details, QuizResponse

class usertable (admin.ModelAdmin):
    list_display = ("user_name","password","gender","dob","email")
    list_filter = ("gender","dob",)

class PersonalDetailsAdmin(admin.ModelAdmin):
    list_display = ("user_id", "family_history", "treatment", "mental_health_condition", "phy_health_condition", "comments")

class QuizResponseAdmin(admin.ModelAdmin):
    list_display = ("user_id", "answers")

# Register your models with their respective admin classes
admin.site.register(user_id, usertable)
admin.site.register(personal_details, PersonalDetailsAdmin)
admin.site.register(QuizResponse, QuizResponseAdmin)
