from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json

questions = [
    {
        'type': 'list',
        'name': 'location',
        'message': 'Ou voulez vous aller',
        'choices' : ["chateau", "plaine"]
    }
]

answers = prompt(questions)
print(answers)
