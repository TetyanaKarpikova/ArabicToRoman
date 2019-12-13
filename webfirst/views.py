import json
from django.shortcuts import render
from django.http import HttpResponse
from .forms import IntForm
from .utils import num_to_roman
from .utils import roman_to_num
from .raising import InvalidRomanError


def index(request):
    save_json = {}
    if request.method == "POST":
        user_form = IntForm(request.POST)
        if user_form.is_valid():
            input_date = user_form.cleaned_data["input_date"]

            try:
                output_date = num_to_roman(input_date)
            except Exception as e:
                try:
                    output_date = roman_to_num(input_date)
                except InvalidRomanError as er:
                    output_date = 'Invalid enter letters'

            save_json["writing"] = input_date
            save_json["reading"] = output_date
            json.dump(save_json, open("j_file.json", "w"))

            return render(request, "index.html", {"form": user_form, "answer": save_json["reading"]})
        else:
            return HttpResponse("Invalid data")
    else:
        user_form = IntForm()
        return render(request, "index.html", {"form": user_form})
