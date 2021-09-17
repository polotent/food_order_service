# Generated by Django 3.2.7 on 2021-09-17 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('order_user_addr', models.CharField(max_length=200)),
                ('order_user_phone', models.CharField(max_length=200)),
                ('order_status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=200)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.menu')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_item_price', models.IntegerField(default=0)),
                ('order_item_quantity', models.IntegerField(default=0)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.restaurant'),
        ),
        migrations.AddField(
            model_name='item',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.menu'),
        ),
    ]
