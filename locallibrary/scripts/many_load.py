import csv  # https://docs.python.org/3/library/csv.html

from unesco.models import Category, Region, States, Iso, Site

def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)

    # This skips the first row of the CSV file.
    # csvreader.next() also works in Python 2.
    next(reader)

    Category.objects.all().delete()
    Region.objects.all().delete()
    States.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:
        print(row)


        c, created = Category.objects.get_or_create(name=row[7])
        s, created = States.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        site = Site(name=row[0], description=row[1], justification=row[2], year=row[3], longitude=row[4],
                    latitude=row[5],area_hectares=row[6],category=c, states=s, region=r, iso=i)
        site.save()
