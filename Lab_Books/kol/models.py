from django.db import models


class HousePublish(models.Model):
    name = models.CharField(max_length=57)
    country = models.CharField(max_length=57)
    city = models.CharField(max_length=57)
    date_founded = models.DateField()
    website = models.URLField()
    def __str__(self):
        return self.name


class Book(models.Model):

    material_book = [
        ("WEAK","WEAK"),
        ("STRONG", "STRONG")
    ]

    category_ch = [
        ("History", "History"),
        ("Drama", "Drama"),
        ("Classic", "Classic"),
        ("Biography", "Biography"),
        ("Thriller", "Thriller"),
        ("Romance", "Romance")
    ]
    category = models.CharField(max_length=20, choices=category_ch)
    material = models.CharField(max_length=10, choices=material_book)
    title = models.CharField(max_length=57)
    image = models.ImageField(upload_to='admin/',blank=True,null=True)
    isbn = models.CharField(max_length=57)
    year_published = models.IntegerField()
    house_publish = models.ForeignKey(HousePublish,on_delete=models.CASCADE)
    num_pages = models.IntegerField()
    dimensions = models.CharField(max_length=57)
    price = models.IntegerField()
    def __str__(self):
        return self.title