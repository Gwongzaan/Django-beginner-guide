from ecomm.models import Type1, Type2, Type3, Type4, Category

def create_types():
    return {
        'type1': Type1.objects.create(name='type1-1'),
        'type2': Type1.objects.create(name='type1-2'),
        'type3': Type1.objects.create(name='type1-3'),
        'type4': Type2.objects.create(name='type2-1', parent=Type1.objects.get(name='type1-1')),
    }

def create_categories():
    return {
        'cat1': Category.objects.create(name='cate-1', level=1, description='cat 1 of level 1', code='cat 1 code'), 
        'cat2': Category.objects.create(name='cat2', level=2, parent_cat=Category.objects.get(id=1), code='cat 2 code'),
    }