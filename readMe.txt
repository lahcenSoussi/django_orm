1- Models & queries
    a- create one Model Course(label,price,avialable,create_at, create_update)
    b- queries functions
        - save() : create
        - read 
            + all()
            + one:
                + get(param1,param2): for one // [use param2 if param1 not unique] 
                + all()[index]
            + __str__()
        - update
            + by one: save after get
        - delete()
            + one
            + all
        - filter
            + (,) : AND
            + (Q()|Q()): OR // must import Q from django.db.models
            (<= : __lte; >=: gte; __contains="char" ...)
        - create methods and handle  them
            + read
            + decorator @proprity
            + save()
                exemple:
                    redux()
                    slug() // from django.utils.text import slugify
2- Relationships
    a- many-to-one: forigne key (exemple user from django.contrib.auth.models import User) / param2: on_delete=models.(cascade,set_null...)
    b- many-to-many: 
        + (): add new line, 
        + set(): update (ecrase)
        + all(): //without objects
        + remove()//after get it 
        + clear(): all
        + inverse// how can i get with inverst: get one id and syntaxe ctg.course_set.all()
    c- one-to-one
3- Views
    a- functions
    b- render(request,html page,any paramtre)
    c- template
    a- jinja2
3- Administration
4- Forms
5- CRUD 