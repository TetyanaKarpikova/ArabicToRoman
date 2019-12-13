from importlib import resources

from webfirst.models import Reservation


class DateResource(resources.ModelResource):
    class Meta:
        model = Reservation
        fields = ('id', 'input_date_model', 'output_date_model',)