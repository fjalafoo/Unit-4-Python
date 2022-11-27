1. Retrieve All Cats:
    - Cat.objects.all()

    Retrieve first row of query:
        - Cat.objects.first()

2. Create a new Cat:
    - catInstance = Cat(name='', .. .. .)

3. Save changes to an exisitng queryset
    - catInstance.save()

4. Filter Cats from DB:
    - Cat.objects.filter(name='.. ...)
    - Cat.objects.filter(name__contains=' .... ..')
    - Cat.objects.filter(age__lte= .. .. .. ) (Less than or equal to)

5. Retrieve Cat by property:
    - Cat.objects.get(id=1) (or any property)

6. Retrieve Cats and order:
    - Cat.objects.order_by('-age')
