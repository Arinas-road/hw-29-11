from django.shortcuts import render

# Create your views here.
def main(req):
   kek = {
      'date': "29/11/22",
      'title': "Промышленное программирование",
      'lesson': "Занятие 12",
      'theme': "Знакомство с Django",
   }
   return render(request=req, template_name='main/index.html', context=kek)

def quest(req):
   question = {
      'question': "Simple question",
   }
   return render(request=req, template_name='main/question.html', context=question)

def answ(req):
   answer = {
      'answer': "Its number 8!",
   }
   return render(request=req, template_name='main/answer.html', context=answer)
   
def tbl(req):
   table = {}
   table['values'] = []
   for i in range(1, 11):
      table['values'].append({'value1': 7, 'value2': i, 'result': i*7})
   return render(request=req, template_name='main/table.html', context=table)