from django.contrib import admin
from .models import Dog, Breed

# Register your models here.
class DogAdmin(admin.ModelAdmin):
    # Fields to display in admin interface
    list_display = ("name", "age", "breed", "favoritetoy", "favoritefood")

    # Available search fields
    search_fields = ("name", "breed", "favoritetoy", "favoritefood")

    # Available filters
    list_filter = ("age", "favoritetoy", "favoritefood")

    # Clickable links for more details
    list_display_links = ("name",)

    # Fields displayed for editing dogs
    fields = ("name", "age", "breed", "gender", "color", "favoritetoy", "favoritefood")

class BreedAdmin(admin.ModelAdmin):
    # Fields to display in admin interface
    list_display = ("name", "size", "friendliness")

    # Available search fields
    search_fields = ("name", "size", "friendliness", "trainability", "sheddingamount", "exerciseneeds")

    # Available filters
    list_filter = ("size", "friendliness", "trainability", "sheddingamount", "exerciseneeds")

    # Clickable links for more details
    list_display_links = ("name",)

    # Fields displayed for editing dogs
    fields = ("name", "size", "friendliness", "trainability", "sheddingamount", "exerciseneeds")

# Initialize them.
admin.site.register(Dog, DogAdmin)
admin.site.register(Breed, BreedAdmin)
