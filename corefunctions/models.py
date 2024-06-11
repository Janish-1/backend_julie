from django.db import models
from django.contrib.auth.models import User as DjangoUser

class User(models.Model):
    email = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=10)
    address = models.TextField(null=True, blank=True)
    street_area = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    otp = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    aadhar_number = models.CharField(max_length=12, null=True, blank=True)
    base_salary = models.IntegerField(null=True, blank=True)
    actual_salary = models.IntegerField(null=True, blank=True)
    leaves_taken = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.email or "N/A"

    @property
    def remaining_leaves(self):
        return self.leave_set.filter(start_date__year=now().year).count()

    def take_leave(self, start_date, end_date, is_half_day=False):
        leave = Leave.objects.create(user=self, start_date=start_date, end_date=end_date, is_half_day=is_half_day)
        leave.save()

    def calculate_salary(self, month):
        leaves_taken = self.leave_set.filter(start_date__month=month).count()
        salary = Salary.objects.create(user=self, month=month, base_salary=self.base_salary, leaves_taken=leaves_taken)
        salary.save()
        return salary.actual_salary

class Order(models.Model):
    product = models.IntegerField()
    title = models.CharField(max_length=255)
    mobile_no = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    shirt_measurement_chest = models.IntegerField(null=True, blank=True, default=0)
    shirt_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    pant_measurement_waist = models.IntegerField(null=True, blank=True, default=0)
    pant_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    coat_measurement_chest = models.IntegerField(null=True, blank=True, default=0)
    coat_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    jacket_measurement_chest = models.IntegerField(null=True, blank=True, default=0)
    jacket_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    nehrujacket_measurement_chest = models.IntegerField(null=True, blank=True, default=0)
    nehrujacket_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    kurta_measurement_chest = models.IntegerField(null=True, blank=True, default=0)
    kurta_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    kameej_measurement_chest = models.IntegerField(null=True, blank=True, default=0)
    kameej_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    pathani_measurement_chest = models.IntegerField(null=True, blank=True, default=0)
    pathani_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    pajama_measurement_waist = models.IntegerField(null=True, blank=True, default=0)
    pajama_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    chudidar_measurement_waist = models.IntegerField(null=True, blank=True, default=0)
    chudidar_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    style = models.CharField(null=True, blank=True, max_length=50)
    estimate_price = models.IntegerField(null=True, blank=True)
    color = models.CharField(null=True, blank=True, max_length=20)
    shipping_address = models.CharField(null=True, blank=True, max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or "N/A"

class CartItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    mobile_no = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    shirt_measurement_chest = models.IntegerField(null=True, blank=True, default=0)
    shirt_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    pant_measurement_waist = models.IntegerField(null=True, blank=True, default=0)
    pant_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    coat_measurement_chest = models.IntegerField(null=True, blank=True, default=0)
    coat_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    jacket_measurement_chest = models.IntegerField(null=True, blank=True, default=0)
    jacket_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    nehrujacket_measurement_chest = models.IntegerField(null=True, blank=True, default=0)
    nehrujacket_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    kurta_measurement_chest = models.IntegerField(null=True, blank=True, default=0)
    kurta_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    kameej_measurement_chest = models.IntegerField(null=True, blank=True, default=0)
    kameej_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    pathani_measurement_chest = models.IntegerField(null=True, blank=True, default=0)
    pathani_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    pajama_measurement_waist = models.IntegerField(null=True, blank=True, default=0)
    pajama_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    chudidar_measurement_waist = models.IntegerField(null=True, blank=True, default=0)
    chudidar_measurement_length = models.IntegerField(null=True, blank=True, default=0)
    style = models.CharField(null=True, blank=True, max_length=50)
    estimate_price = models.IntegerField(null=True, blank=True)
    color = models.CharField(null=True, blank=True, max_length=20)
    shipping_address = models.CharField(null=True, blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} x {self.title or 'N/A'} in cart"

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Shirt', 'Shirt'),
        ('Pant', 'Pant'),
        ('Coat', 'Coat'),
        ('Jacket', 'Jacket'),
        ('NehruJacket', 'NehruJacket'),
        ('Kurta', 'Kurta'),
        ('Kameej', 'Kameej'),
        ('Pathani', 'Pathani'),
        ('Pajama', 'Pajama'),
        ('Chudidar', 'Chudidar'),
    ]
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=255, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/')
    categories = models.CharField(max_length=255, choices=CATEGORY_CHOICES, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title or "N/A"

class Task(models.Model):
    status = models.CharField(max_length=50)
    start_date_time = models.DateTimeField()
    site_address = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)
    site_contact = models.CharField(max_length=15)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name or "N/A"

class Leave(models.Model):
    STATUS_CHOICES = [
        (None, 'Pending'),
        (True, 'Approved'),
        (False, 'Declined'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_half_day = models.BooleanField(default=False)
    reason = models.CharField(max_length=100)
    status = models.BooleanField(choices=STATUS_CHOICES, default=None, null=True)

    def __str__(self):
        return f"Leave for {self.user.email or 'N/A'} from {self.start_date} to {self.end_date}"

class Salary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.DateField()
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    leaves_taken = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    @property
    def actual_salary(self):
        full_day_salary = self.base_salary / 30  # Assuming monthly salary
        return self.base_salary - (self.leaves_taken * full_day_salary)

    def __str__(self):
        return f"Salary for {self.user.email or 'N/A'} for {self.month}"

class DeliveryPerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assigned_orders = models.ManyToManyField(Order, related_name='delivery_persons')

    def __str__(self):
        return self.user.email or "N/A"

class DeliveryStatus(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Status for {self.order.title or 'N/A'}: {self.status}"

class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    last_restocked = models.DateTimeField()

    def __str__(self):
        return f"Stock for {self.product.title or 'N/A'}: {self.quantity}"

class ManagerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    team_size = models.PositiveIntegerField()

    def __str__(self):
        return f"Manager {self.user.email or 'N/A'} in {self.department}"

class EmployeeDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, related_name='employees', on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.user.email or 'N/A'} in {self.department} as {self.designation}"

class Interview(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or "N/A"
