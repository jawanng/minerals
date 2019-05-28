from django.db import models
import re


# Create your models here.
class Gem(models.Model):
    name = models.CharField(max_length=120)
    image_filename = models.CharField(max_length=120)
    image_caption = models.CharField(blank=True, max_length=120)
    category = models.CharField(max_length=120)
    formula = models.CharField(max_length=120)
    strunz_classification = models.CharField(max_length=120)
    color = models.CharField(null=True, max_length=120)
    crystal_system = models.CharField(null=True, max_length=120)
    unit_cell = models.CharField(null=True, max_length=120)
    crystal_symmetry = models.CharField(null=True, max_length=120)
    cleavage = models.CharField(null=True, max_length=120)
    mohs_scale_hardness = models.CharField(null=True, max_length=120)
    luster = models.CharField(null=True, max_length=120)
    streak = models.CharField(null=True, max_length=120)
    diaphaneity = models.CharField(null=True, max_length=120)
    optical_properties = models.CharField(null=True, max_length=120)
    refractive_index = models.CharField(null=True, max_length=120)
    crystal_habit = models.CharField(null=True, max_length=120)
    specific_gravity = models.CharField(null=True, max_length=120)
    group = models.CharField(null=True, max_length=120)

    def __str__(self):
        """There was a few Gems that had a hyphen in the name and this catches
        them. """
        match = re.match(r'^\w+(-\w+ite)?', self.name)
        if match:
            return match.group(0)

