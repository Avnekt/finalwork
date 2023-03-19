from django_filters import rest_framework as dj_filters
from .models import Task


class TodoFilterSet(dj_filters.FilterSet):
    """Набор фильтров для представления для модели todoList."""
    
    task = dj_filters.CharFilter(field_name="name", lookup_expr="icontains")
    # is_active = dj_filters.BooleanFilter(field_name="is_active", exclude=False)

    order_by_field = "ordering"

    class Meta:
        model = Task
        fields = [
            "id",
            "name",
        ]
    
    def invert_value(self, obj, *argvs):
        try:
            eval(obj.lookup_expr)
            return eval(obj.lookup_expr)
        except:
             return obj.lookup_expr
