from .models import Category
import random
from .models import Adv
def categories_processor(request):
    categories = Category.objects.all()
    return {
        'categories': categories
    }

def ad_rotator(request):
    ads = Adv.objects.filter(is_active=True)
    # Выбираем случайный баннер из базы
    random_ad = random.choice(ads) if ads.exists() else None
    return {'global_ad': random_ad}