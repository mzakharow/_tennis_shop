from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.text import slugify
from transliterate import translit


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     # return reverse('category_detail', args=self.slug)
    #     return reverse('category_detail', kwargs={'category_slug': self.slug})


def pre_save_category_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug


pre_save.connect(pre_save_category_slug, sender=Category)


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]    # filename.split('.')[1]- расширение файла
    # return "{0}/{1}".format(instance.slug, filename)
    return f'{instance.slug}/{filename}'    #   попробовать такой формат


# Переопределения менеджера модели
# сейчас переделали выборку запроса all, додбавив фильтр
# class ProductManager(models.Manager):
#
#     def all(self, *args, **kwargs):
#         return super(ProductManager, self).get_queryset().filter(available=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=140)
    slug = models.SlugField(unique=True, default='')
    description = models.TextField()
    image = models.ImageField(upload_to=image_folder)
    price = models.DecimalField(max_digits=9, decimal_places=2)   # max_digits количество знаков ;  decimal_places после запятой
    available = models.BooleanField(default=True)
    # objects = ProductManager()   # Переопределения менеджера модели

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('product_detail', kwargs={'product_slug': self.slug})


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return f'Cart item for product {self.product.title}'


class Cart(models.Model):
    # item = models.ForeignKey(CartItem, blank=True, null=True, on_delete=models.DO_NOTHING)
    # cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    item = models.ManyToManyField(CartItem, blank=True)
    cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)

    def add_to_cart(self, product_slug):
        cart = self
        product = Product.objects.get(slug=product_slug)
        new_item, _ = CartItem.objects.get_or_create(product=product, item_total=product.price)
        if new_item not in cart.item.all():
            cart.item.add(new_item)
            cart.save()

    def remove_from_cart(self, product_slug):
        cart = self
        product = Product.objects.get(slug=product_slug)
        for cart_item in cart.item.all():
            if cart_item.product == product:
                cart.item.remove(cart_item)
                cart.save()
