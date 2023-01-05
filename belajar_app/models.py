from django.db import models

# Create your models here.

class Usaha(models.Model):
   nama = models.CharField(max_length=100)
   keterangan = models.TextField()

   def __str__(self):
      return self.nama

class Tempat(models.Model):
   koordinat = models.CharField(max_length=100)
   provinsi = models.CharField(max_length=40)
   daya = models.TextField()
   usaha_id = models.ForeignKey(Usaha, on_delete=models.CASCADE, null=True)
   
   def __str__(self):
      return self.provinsi



class Jenis(models.Model):
   nama = models.CharField(max_length=100)
   keterangan = models.TextField()

   def __str__(self):
      return self.nama

class Video(models.Model):
   judul = models.CharField(max_length=100)
   gambar = models.FileField(upload_to='media/berita/', null=True)
   publikasi = models.DateField(null=True)
   link = models.CharField(max_length=100)
   sumber = models.CharField(max_length=100)
   jenis_id = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)
   
   def __str__(self):
      return self.judul
