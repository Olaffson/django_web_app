from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listings_remove_band_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Listings',
            new_name='Listing',
        ),
    ]
