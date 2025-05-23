# admin.py for Food Management App

from django.contrib import admin
from .models import FoodCategoryTable, FoodTable

@admin.register(FoodCategoryTable)
class FoodCategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for Food Categories
    """
    list_display = ('name', 'is_active', 'get_food_count', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('is_active',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at', 'get_food_count')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Statistics', {
            'fields': ('get_food_count',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_food_count(self, obj):
        """Display food count in admin"""
        return obj.get_food_count()
    get_food_count.short_description = 'Number of Foods'
    get_food_count.admin_order_field = 'foods__count'


@admin.register(FoodTable)
class FoodAdmin(admin.ModelAdmin):
    """
    Admin configuration for Food Items
    """
    list_display = ('name', 'category', 'is_active', 'is_organic', 'created_at')
    list_filter = ('category', 'is_active', 'is_organic', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'category__name')
    list_editable = ('is_active', 'is_organic')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    
    # Filter by category in the right sidebar
    list_select_related = ('category',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'description')
        }),
        ('Status', {
            'fields': ('is_active', 'is_organic')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    # Add actions for bulk operations
    actions = ['make_active', 'make_inactive', 'mark_as_organic', 'mark_as_non_organic']

    def make_active(self, request, queryset):
        """Bulk action to activate selected food items"""
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} food items were successfully marked as active.')
    make_active.short_description = "Mark selected foods as active"

    def make_inactive(self, request, queryset):
        """Bulk action to deactivate selected food items"""
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} food items were successfully marked as inactive.')
    make_inactive.short_description = "Mark selected foods as inactive"

    def mark_as_organic(self, request, queryset):
        """Bulk action to mark selected food items as organic"""
        updated = queryset.update(is_organic=True)
        self.message_user(request, f'{updated} food items were successfully marked as organic.')
    mark_as_organic.short_description = "Mark selected foods as organic"

    def mark_as_non_organic(self, request, queryset):
        """Bulk action to mark selected food items as non-organic"""
        updated = queryset.update(is_organic=False)
        self.message_user(request, f'{updated} food items were successfully marked as non-organic.')
    mark_as_non_organic.short_description = "Mark selected foods as non-organic"


# Optional: Customize admin site header and title
admin.site.site_header = "Nutrition App Administration"
admin.site.site_title = "Nutrition Admin"
admin.site.index_title = "Welcome to Nutrition Management"