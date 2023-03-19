from django import forms
from taskmanager.models import Task

class ParentTaskSelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs={'class': 'form-select'}):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['name'] = value.instance.name
        return option

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            # 'is_active',
            'dead_line',
            'parent_task'
        ]
        widgets = {'parent_task': ParentTaskSelect}


class CreateForm(forms.ModelForm):

    email = forms.EmailField()
    reason = forms.ChoiceField(
        choices=[("COMMENT", "Comment"), ("COMMENT", "Complaint")],
        widget=forms.Select,
        required=False,
    )
    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Task
        fields = [
            'name',
            # 'is_active',
            'dead_line',
            'parent_task'
        ]
        widgets = {
            'dead_line': forms.DateInput(),
            'parent_task': forms.Select(attrs={'class': "form-select"})
        }


class FeedbackModelForm(forms.ModelForm):
    
    class Meta:
        model = Feedback
        fields = ["email", "reason", "comment"]
        widgets = {
            'comment' : forms.Textarea(attrs={'cols': 100, "rows": 40})
        }