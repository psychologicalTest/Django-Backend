import json
from fb.models import Main_question,Sub_question,Answer,Option
import codecs

j = 0
k = 0
b = 0
file = 0
while file < 5:
	j = 0
	if file == 0:
		json_data=json.load(codecs.open('love.json', 'r', 'utf-8-sig'))
	elif file == 1:
		json_data=json.load(codecs.open('money.json', 'r', 'utf-8-sig'))
	elif file == 2:
		json_data=json.load(codecs.open('interest.json', 'r', 'utf-8-sig'))
	elif file == 3:
		json_data=json.load(codecs.open('future.json', 'r', 'utf-8-sig'))
	else :
		json_data=json.load(codecs.open('characteristic.json', 'r', 'utf-8-sig'))
	while j < len(json_data):
		k=0
		while k < len(json_data[j]['questions']):
			sub_question = Sub_question(main_quest=json_data[j]['questions'][k]['Qtitle'],main_question_id=b+j+1)
			sub_question.save()
			k = k+1
		j = j+1
	b = b+j
	file = file+1




print()
