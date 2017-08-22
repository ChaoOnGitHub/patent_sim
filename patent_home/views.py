from django.shortcuts import render
from models import ClaimText
import datetime
from django.conf import settings
from pytz import timezone
from management.commands import modelcom
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def predict(request):
    content_data = {}
    if request.method=="GET":
        content_data.update({ "submit": True})
    elif request.method=="POST":
        patent_id      =request.POST.get("patent_id")
        claim          =request.POST.get("claim")
        run_date       = datetime.datetime.now(tz=timezone(settings.TIME_ZONE))

        if request.POST.get("submit"):
            dictionary, index, model= modelcom.modelcommand()
            query_bow = dictionary.doc2bow(claim.lower().split())
            query_lsi = model[query_bow]
            sims      = index[query_lsi]
            sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
            if sort_sims:
                content_data.update({"result": True, "prediction": sort_sims[:5],"claim":claim})
                claim_data = ClaimText.objects.create(Event_id     =datetime.datetime.now(tz=timezone(settings.TIME_ZONE)),
                                       patent_Num   =patent_id,
                                          claim     =claim,
                                          sim_patent=str(sort_sims[:5]),
                                          run_date  =run_date)


    return render(request,"Home.html",context=content_data)


