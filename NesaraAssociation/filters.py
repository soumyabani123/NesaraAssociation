from .models import member
from .models import meeting
import django_filters

class memberfilter(django_filters.FilterSet):
    class Meta:
        model = member
        fields = '__all__'
        exclude = 'member_id','address'
