# Generated by Django 4.2.3 on 2023-08-20 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/product_cover/', verbose_name='Product Image'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='Comment Text'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='stars',
            field=models.CharField(choices=[('1', 'Very Bad'), ('2', 'Bad'), ('3', 'Normal'), ('4', 'Good'), ('5', 'Perfect')], max_length=10, verbose_name='Your score for this product'),
        ),
    ]
