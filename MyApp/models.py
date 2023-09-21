from django.contrib.admin.utils import model_ngettext
from django.db import models

# Create your models here.

from django.db import models
from shortuuid import ShortUUID
from shortuuidfield import ShortUUIDField
from django.utils.html import mark_safe, escape
from userauths.models import User
from django.templatetags.static import static


STATUS_CHOICE = (
    ("process", "Process"),
    ("shipped", "Shipped"),
    ("delivered","Delivered"),
)
STATUS = (
    ("draft","Draft"),
    ("disabled","Disabled"),
    ("rejected", "Rejected"),
    ("in_review","In_review"),
    ("published","Published"),
)

RATTING = (
    (1,"★☆☆☆☆"),
    (2,"★★☆☆☆"),
    (3,"★★★☆☆"),
    (4,"★★★★☆"),
    (5,"★★★★★"),
)


def user_directory_path(instance, filename):

    return 'user_{0}/{1}'.format(instance.user.id, filename)
class Catergory(models.Model):
    cid = ShortUUIDField(unique=True, max_length=30)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category")

    def save(self, *args, **kwargs):
        if not self.cid:
            prefix = "cat"
            cid_prefix = "abcdefgh12345"
            cid = ShortUUID().random(length=22)
            self.cid = f"{prefix}-{cid}"
        super(Catergory, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (escape(static(self.image.url))))

    def __str__(self):
        return self.title

class Vendor(models.Model):
    vid = ShortUUIDField(unique=True,max_length=30)
    def save(self, *args, **kwargs):
        if not self.id:
            prefix = "ven"
            vid = ShortUUID().random(length=22)
            vid_prefix = "abcdefgh12345"
            self.vid = f"{prefix}-{vid}"
        super(Vendor, self).save(*args, **kwargs)

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path)
    description = models.TextField(null=True, blank=True)

    address = models.CharField(max_length=100, default="123 Main street")
    contact = models.CharField(max_length=100, default="+123 (456) 789")
    chat_resp_time = models.CharField(max_length=100, default="100")
    shipping_on_time = models.CharField(max_length=100, default="100")
    days_return = models.CharField(max_length=100, default="100")
    warranty_period = models.CharField(max_length=100, default="100")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):

        return mark_safe('<img src="/media%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

class Tag(models.Model):
    pass
class Product(models.Model):
    pid = ShortUUIDField(unique=True, max_length=20)
    sku = ShortUUIDField(unique=True, max_length=20)

    def save(self, *args, **kwargs):

            if not self.pid:
                pid_prefix = "pid"
                pid_prefix = "abcdefgh12345"
                pid_uuid = ShortUUID().random(length=15)
                self.pid = f"{pid_prefix}-{pid_uuid}"

            if not self.sku:
                sku_prefix = "skuProd"
                sku_prefix = "abcdefgh12345"
                sku_uuid = ShortUUID().random(length=15)
                self.sku = f"{sku_prefix}-{sku_uuid}"

            super(Product, self).save(*args, **kwargs)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Catergory, on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)


    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="product")
    description = models.TextField(null=True, blank=True)

    price = models.DecimalField(max_digits=9999999999999, decimal_places=2, default="1.99")
    old_price = models.DecimalField(max_digits=9999999999999, decimal_places=2, default="2.99")

    specifications = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=100, default="Organic", null=True)
    stock_count = models.CharField(max_length=100, default="10", null=True)

    product_status = models.CharField(choices=STATUS, max_length=10,default="in_review")

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)
    digital = models.CharField(max_length=100, default="100")

    # date = models.DateTimeField(auto_now_add=True)
    # update = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        # return mark_safe('<img src="%s" width="50" height="50" />' % (escape(static(self.image.url))))
        return mark_safe('<img src="/media%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

    def get_percentage(self):

        return((self.price / self.old_price ) * 100)

class ProductImages(models.Model):
    images = models.ImageField(upload_to="product_images", default="product.jpg")
    product = models.ForeignKey(Product, related_name="p_images", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Products Images"


class CartOder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9999999999999, decimal_places=2, default="1.99")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="processing")

    class Meta:
        verbose_name_plural = "Cart Order"


class CartOderItems(models.Model):
    order = models.ForeignKey(CartOder, on_delete=models.CASCADE, null=True)
    product_status = models.CharField(max_length=200)
    invoice_no = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=9999999999999, decimal_places=2, default="1.99")
    total = models.DecimalField(max_digits=9999999999999, decimal_places=2, default="1.99")


class Meta:
    verbose_name_plural = "Cart Order Items"


def order_img(self):
    return mark_safe('<img src="/media%s" width="50" height="50" />' % (self.image.url))