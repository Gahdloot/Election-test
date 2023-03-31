from django.shortcuts import render
from .models import PollingUnit, Lga, AnnouncedPuResults, PollingUnit
from django.db.models import Sum
# Create your views here.


def polling_unit(request, id):
    unit = PollingUnit.objects.get(uniqueid=id)
    context = {
        'unit' : unit
    }
    print(unit)
    return render(request, 'index.html', context)

def total_res_lga(request):
   if request.method == 'GET':
        lga = Lga.objects.all()
        for lg in lga:
            lga_id = Lga.objects.get(lga_name=lg.lga_name).lga_id
            #print(lga_id)
            pu = PollingUnit.objects.filter(lga_id=lga_id)
            score = 0
            for i in pu:
                pu = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=i.polling_unit_id)
                party_score = pu.aggregate(Sum('party_score'))['party_score__sum']
                #print(party_score)
                if party_score:
                    score += party_score
            lg.score = score
            print(lg, lg.lga_name, lg.lga_id, lg.score)
        #print(lga.lga_id)
        context = {
            'lga': lga
        }

        return render(request, 'total.html', context)