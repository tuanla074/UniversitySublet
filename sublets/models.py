from django.db import models


# Create your models here.
class SubletPlace(models.Model):
    sublet_company = models.CharField(max_length=100)
    sublet_address = models.CharField(max_length=800)
    website = models.CharField(max_length=800)

    def __str__(self):
        return self.sublet_company


class SubletOwnerInfo(models.Model):
    sublet_owner_name = models.CharField(max_length=200)
    sublet_owner_email = models.CharField(max_length=200)
    sublet_owner_phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.sublet_owner_name


class SubletGender(models.Model):
    sublet_gender = models.CharField(max_length=100)

    def __str__(self):
        return self.sublet_gender


class LegalFee(models.Model):
    legal_fee = models.FloatField(default=50)

    def __str__(self):
        return str(self.legal_fee)


class SubletListing(models.Model):
    sublet_place = models.ForeignKey(SubletPlace, on_delete=models.CASCADE)
    sublet_owner_info = models.ForeignKey(SubletOwnerInfo, on_delete=models.CASCADE)
    sublist_price = models.FloatField(default=0)
    sublet_start_date = models.DateTimeField()
    sublet_end_date = models.DateTimeField()
    sublet_status = models.IntegerField(default=1)
    parking_cost = models.FloatField(default=0)
    total_room = models.IntegerField(default=1)
    room_number = models.CharField(max_length=100)
    utilities = models.CharField(max_length=5000)
    sublet_gender = models.ForeignKey(SubletGender, on_delete=models.CASCADE)
    sublet_legal_fee = models.ForeignKey(LegalFee, on_delete=models.CASCADE)

    def __str__(self):
        pre_text = self.sublet_place.sublet_address + "-" + self.room_number
        if self.sublet_status == 1:
            return "Status [" + pre_text + "]: showing"
        return "Status [" + pre_text + "]: not showing"


class ImageModel(models.Model):
    main_image = models.ImageField(upload_to='img', null=True)
    image = models.ForeignKey(SubletListing, on_delete=models.CASCADE)


class Subtenant(models.Model):
    legal_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=800)
    photo_id = models.ImageField(upload_to='img')
    date = models.DateTimeField(auto_now=True)
    signature = models.CharField(max_length=200)

    def __str__(self):
        return self.legal_name
