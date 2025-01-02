from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Image(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.category.name} - {self.caption or 'Image'}"



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()    
    
    def __str__(self):
        return f"{self.name}"
    

class Timeline_category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Timeline(models.Model):
    category = models.ForeignKey(Timeline_category, on_delete=models.CASCADE, related_name='timeline_items')
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='timeline_images/')
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.category.name} - {self.title}"
    


class About_description(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()





class About_blog_1(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about_blog_images/')

    def __str__(self):
        return self.title
    




class About_blog_2(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about_blog_images/')

    def __str__(self):
        return self.title
    


class About_title_2(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    


class About_title_1(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title



class About_title_3(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    