from django.contrib.gis.geos import Point, MultiPoint
from django.http import JsonResponse

from peak.models import Peak


# Create your views here.
def peak(request, peak_id=None):
    if request.method == "GET":
        if peak_id:
            p = list(Peak.objects.filter(id=peak_id).values())[0]

            p["lat"] = p["coordinates"][1]
            p["long"] = p["coordinates"][0]
            del p["coordinates"]

            return JsonResponse(p, safe=False)

        elif not peak_id and not request.GET:
            peaks = list(Peak.objects.all().values())
            for key, p in enumerate(peaks):
                p["lat"] = p["coordinates"][1]
                p["long"] = p["coordinates"][0]
                del p["coordinates"]

            return JsonResponse(peaks, safe=False)

        else:
            box = MultiPoint(
                Point(
                    float(request.GET.get("min_long")),
                    float(request.GET.get("min_lat"))
                ),
                Point(
                    float(request.GET.get("max_long")),
                    float(request.GET.get("max_lat"))
                ), srid=4326).envelope

            peaks = list(Peak.objects.filter(
                coordinates__intersects=box
            ).values())

            for key, p in enumerate(peaks):
                p["lat"] = p["coordinates"][1]
                p["long"] = p["coordinates"][0]
                del p["coordinates"]

            return JsonResponse(peaks, safe=False)

    elif request.method == "POST":
        lat, long = request.GET.get("lat"), request.GET.get("long")

        p = Peak(
            coordinates=Point(x=float(long), y=float(lat)),
            altitude=request.GET.get("alt"),
            name=request.GET.get("name"))
        p.save()

        return JsonResponse("OK", safe=False)

    elif request.method == "DELETE":
        p = Peak.objects.get(pk=peak_id)
        p.delete()

        return JsonResponse("OK", safe=False)

    elif request.method == "PUT":
        p = Peak.objects.get(pk=peak_id)
        for param, val in request.GET.items():
            setattr(p, param, val)

        p.save()

        return JsonResponse("OK", safe=False)
