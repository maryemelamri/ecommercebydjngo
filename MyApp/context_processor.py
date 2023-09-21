from MyApp.models import Product,Catergory

def default(request):
    categories = Catergory.objects.all()

    return {
        'categories': categories
    }