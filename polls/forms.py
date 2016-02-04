from django.forms import ModelForm, TextInput, Select

from .models import Choice, Poll


def react_widget(widget, react_attrs=None):
    widget_render = widget.render

    def react_render(*args, **kwargs):
        if react_attrs == 'auto':
            widget_name = args[0]
            attrs = {'onChange': '{this.handle%sChange}' % widget_name.title(), 'value': '{this.state.%s}' % widget_name}
        else:
            attrs = react_attrs
        input = widget_render(*args, **kwargs)
        react_input_attrs = ' '.join(['{}={}'.format(key, value) for key, value in attrs.items()])
        if input.startswith('<input'):
            return input[:-2]+react_input_attrs+'/>'
        elif input.startswith('<select'):
            # this is hardly robust
            first_caret = input.find('>')
            return input[:first_caret]+' '+react_input_attrs+input[first_caret:]
    widget.render = widget_render if react_attrs is None else react_render
    return widget


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['poll', 'choice_text']
        widgets = {
            'poll': react_widget(Select(), react_attrs='auto'),
            'choice_text': react_widget(TextInput(), react_attrs='auto')
        }

class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question']
        widgets = {
            'question': react_widget(TextInput(), react_attrs='auto'),
            #'question': react_widget(TextInput(), react_attrs={'onChange': '{this.handleQuestionChange}', 'value': '{this.state.question}'}),
        }

    def __init__(self, *args, **kwargs):
        super(PollForm, self).__init__(*args, **kwargs)
