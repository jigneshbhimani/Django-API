from django.db import models

# Create your models here

# Category
class Category(models.Model):
    category = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.category}"

    class Meta:
        verbose_name_plural = 'Category'


# Available on which Devices 
class Available_on(models.Model):
    available_on_which_device = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.available_on_which_device}"

    class Meta:
        verbose_name_plural = 'Available_on'


# System requirements
class System_requirements(models.Model):
    os = models.CharField(max_length=255, null=False)
    architecture = models.CharField(max_length=255, null=False)
    notes = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.os}-{self.architecture}-{self.notes}"

    class Meta:
        verbose_name_plural = 'System_requirements'


# Publishers
class Publishers(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Publishers'


# Language Supported
class Language_supported(models.Model):
    language = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.language}"

    class Meta:
        verbose_name_plural = 'Language_supported'


# Capabilities
class Capabilities(models.Model):
    capabilities = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.capabilities}"

    class Meta:
        verbose_name_plural = 'Capabilities'


# Games
class Games(models.Model):
    name = models.CharField(max_length=255, null=False)
    game_profile_pic = models.ImageField(null=False)
    size = models.CharField(max_length=255, null=False)
    category = models.ManyToManyField(Category)
    publishers = models.ForeignKey(Publishers, on_delete=models.CASCADE)
    available_on = models.ManyToManyField(Available_on)
    description = models.CharField(max_length=10000, null=False)
    language_supported = models.ManyToManyField(Language_supported)
    system_requirements = models.ManyToManyField(System_requirements)
    capabilities = models.ManyToManyField(Capabilities)
    best_of_all_time = models.BooleanField()
    trending = models.BooleanField()
    release_date = models.DateField(auto_now_add=False, null=False)
    age_rating = models.IntegerField(null=False, default=5)
    
    PRICES = (
        ('PAID', 'Paid'),
        ('FREE', 'Free'),
    )

    price = models.CharField(max_length=255,choices=PRICES)
    game_price_if_paid = models.IntegerField(null=True, blank=True)    

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['-release_date']
        verbose_name_plural = 'Games'
    
