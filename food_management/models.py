# Create your models here.
# models.py for Food Management App

from django.db import models
from django.utils import timezone

class FoodCategoryTable(models.Model):
    """
    Model to manage food categories for nutrition calculation app
    """
    name = models.CharField(
        max_length=100, 
        unique=True,
        help_text="Name of the food category (e.g., Fruits, Vegetables, Grains)"
    )
    description = models.TextField(
        blank=True, 
        null=True,
        help_text="Brief description of the food category"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this category is currently active"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'food_category'
        verbose_name = 'Food Category'
        verbose_name_plural = 'Food Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_food_count(self):
        """Return the number of food items in this category"""
        return self.foods.count()


class FoodTable(models.Model):
    """
    Model to manage individual food items with nutritional information
    """
    # Basic Food Information
    name = models.CharField(
        max_length=200,
        help_text="Name of the food item (e.g., Apple, Brown Rice)"
    )
    category = models.ForeignKey(
        FoodCategoryTable,
        on_delete=models.CASCADE,
        related_name='foods',
        help_text="Category this food belongs to"
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Additional description or notes about the food item"
    )
    
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this food item is currently active"
    )
    is_organic = models.BooleanField(
        default=False,
        help_text="Whether this is an organic food item"
    )
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'food_item'
        verbose_name = 'Food Item'
        verbose_name_plural = 'Food Items'
        ordering = ['name']
        unique_together = [['name', 'category']]  # Prevent duplicate food names in same category

    def __str__(self):
        return f"{self.name} ({self.category.name})"