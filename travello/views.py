from django.shortcuts import render

from .models import Destination

# Create your views here.
def index(request):

    # dest1=Destination()
    # dest1.name="Delhi"
    # dest1.desc='Yeh hai dilwalon ki Dilli'
    # dest1.price=1150
    # dest1.img='destination_1.jpg'
    # dest1.offer=True

    # dest2=Destination()
    # dest2.name="Hydrabad"
    # dest2.desc='First Biryani, Next Sherwani'
    # dest2.price=1000
    # dest2.img='destination_2.jpg'
    # dest2.offer=True

    # dest3=Destination()
    # dest3.name="San Francisco"
    # dest3.desc='If you’re not alive, San Francisco will bring you to life.'
    # dest3.price=1750
    # dest3.img='destination_3.jpg'
    # dest3.offer=False
    # dests=[dest1,dest2,dest3]
    dests=Destination.objects.all()
    return render(request,'index.html',{'dests':dests})
