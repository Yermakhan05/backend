from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Medics,
    ChatGroup,
    Message,
    FirebaseUser,
    Sessions,
    Consultation,
    Document,
    Notification,
)

@admin.register(Medics)
class MedicsAdmin(admin.ModelAdmin):
    list_display = ('medic_name', 'speciality', 'city', 'price', 'doctor_firebase_id')
    search_fields = ('medic_name', 'speciality', 'city', 'doctor_firebase_id')
    list_filter = ('city', 'speciality')

@admin.register(ChatGroup)
class ChatGroupAdmin(admin.ModelAdmin):
    list_display = ('firebase_user_id', 'doctor', 'token_group', 'created_at')
    search_fields = ('firebase_user_id', 'doctor__medic_name', 'token_group')
    readonly_fields = ('created_at',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('group', 'sender_id', 'short_content', 'timestamp')
    search_fields = ('sender_id', 'content')
    list_filter = ('timestamp',)

    def short_content(self, obj):
        return obj.content[:50]
    short_content.short_description = 'Content'

@admin.register(FirebaseUser)
class FirebaseUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'uid', 'created_at')
    search_fields = ('full_name', 'email', 'uid')
    readonly_fields = ('created_at',)

@admin.register(Sessions)
class SessionsAdmin(admin.ModelAdmin):
    list_display = ('medics', 'client', 'appointment', 'fid')
    search_fields = ('medics__medic_name', 'client__full_name', 'fid')
    list_filter = ('appointment',)

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'diagnosis', 'follow_up_date')
    search_fields = ('appointment__client__full_name', 'diagnosis')
    list_filter = ('follow_up_date',)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'patient', 'uploaded_at', 'download_link')
    search_fields = ('title', 'patient__full_name')
    readonly_fields = ('uploaded_at',)

    def download_link(self, obj):
        if obj.file:
            return format_html('<a href="{}">Download</a>', obj.file.url)
        return '-'
    download_link.short_description = 'File'

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'title', 'is_read', 'created_at')
    search_fields = ('doctor__medic_name', 'title')
    list_filter = ('is_read', 'created_at')
    readonly_fields = ('created_at',)
