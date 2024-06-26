from goods.models import Products
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    vector = SearchVector("name", "brief_description", "full_description")
    query = SearchQuery(query)
    return Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
    
    
    #return Products.objects.annotate(search=SearchVector("name", "brief_description", "full_description")).filter(search=query)

    #keywords = [word for word in query.split() if len(word) > 2]

    #q_objects = Q()

    #for token in keywords:
        #q_objects |= Q(name__icontains=token)
        #q_objects |= Q(brief_description__icontains=token)
        #q_objects |= Q(full_description__icontains=token)

    #return Products.objects.filter(q_objects)