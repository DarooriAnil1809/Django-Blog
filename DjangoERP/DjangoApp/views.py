from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
# def Jan(request):
#     return HttpResponse("THIS IS MY FIRST DJANGO")

# def Feb(request):
#     return HttpResponse("THIS IS MY 2nd DJANGO")

# More Dynamic Logic - using dictionary
allmonths_challenges = {
    "january": "Rathnamachary",
    "Febuary": "Sirisha",
    "March": "Smrithika",
    "April": "Virat",
    "May": "Meena",
    "June": "Divya",
    "July": "Charishma",
    "August": "Geetha",
    "September": "Daroori",
    "October": "Kalyan",
    "November": "Pinky",
    "December": None,
}


def allmonths_challenge(request, month):
    try:
        challenge_text = allmonths_challenges[month]

        #response_htmldata = f"<h1>{challenge_text}</h1>"
        return render(request, "challanges/challenge.html", {
            "text": challenge_text,
            "monthname": month.capitalize()
        })
        # response_htmldata = render_to_string("challanges/challenge.html")
        # return HttpResponse(response_htmldata)
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)


def allmonths_challenge_by_number(request, month):

    months = list(allmonths_challenges.keys())
    if month > len(months):
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404
    Redirect_month = months[month-1]
    # Path for DjangoApp/january - Reverse function
    redirect_path = reverse("month-challenge", args=[Redirect_month])
    return HttpResponseRedirect(redirect_path)
    # HardCode
   # return HttpResponseRedirect("/DjangoApp/" + Redirect_month)

# This Function mainly display the list of all months


def index(request):
    #list_items = ""
    months = list(allmonths_challenges.keys())
    return render(request, "challanges/index.html", {
        "months": months

    })
    # for month in months:
    #     capitalized_month = month.capitalize()  # Capitalize the 1st Letter
    #     # get the all months list
    #     month_path = reverse("month-challenge", args=[month])
    #     # list of all months in variable list_items
    #     list_items += f"<li><a href =\"{month_path}\">{capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
