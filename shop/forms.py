
from django import forms
from django.utils import timezone


class OrderForm(forms.Form):

    name = forms.CharField(label='Имя')
    last_name = forms.CharField(required=False, label='Фамилия')
    phone = forms.CharField(required=False)
    buying_type = forms.ChoiceField(widget=forms.Select(), required=False, choices=([("self", "Самовывоз"), ("delivery", "Доставка")]))
    date = forms.DateField(widget=forms.SelectDateWidget(), initial=timezone.now(), required=False)
    address = forms.CharField(required=False)
    comments = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        # self.fields['name'].label = 'Имя'
        # # self.fields['last_name'].label = 'Фамилия'
        self.fields['phone'].label = 'Телефон'
        self.fields['phone'].help_text = 'Номер телефона в формате +79011234567'
        # self.fields['buying_type'].label = 'Способ получения'
        self.fields['address'].label = 'Адрес доставки'
        self.fields['address'].help_text = '*Обязательно указывайте город'
        # self.fields['comments'].label = 'Комментарий'
        self.fields['date'].label = 'Дата доставки'
        self.fields['date'].help_text = 'Доставка осуществляется на следующий день после оформления заказа'
