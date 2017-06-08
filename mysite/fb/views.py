from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import psycopg2
import random
import json

def fn(request):

    conn = psycopg2.connect("dbname='' host='' port='' user='' password=''")
    cursor = conn.cursor()
    classification = str(request.GET.get('q',''))

    if classification =='love':
        id = random.randrange(1,253)
    elif classification =='money':
        id = random.randrange(254,310)
    elif classification =='interest':
        id = random.randrange(311,345)
    elif classification =='future':
        id = random.randrange(346,389)
    elif classification =='kidney':
        id = random.randrange(390,521)

    articleContent = {}
    title = {}
    title['type'] = classification

    query = """select m.main_quest
               from   psychological_test_all.fb_main_question as m
               where classification = '%s' and m.id = '%d'
            """ % (classification,id)
    cursor.execute(query)

    main = {}
    main['title'] = cursor.fetchall()[0]

    query = """select a.answer
               from   psy.fb_main_question as m , psy.fb_answer as a
               where classification = '%s' and m.id = '%d' and a.main_question_id = m.id
            """ % (classification,id)

    cursor.execute(query)
    get = cursor.fetchall()
    i = 0

    col = []
    for x in get:
        attr = {}
        attr.clear()
        attr['context'] = x[0]
        col.append(attr)
    ans = {}
    ans['answer'] = col

    query = """select  s.id
               from   psy.fb_main_question as m ,psy.fb_sub_question as s
               where classification = '%s' and m.id = '%d' and s.main_question_id = m.id
            """ % (classification,id)

    cursor.execute(query)
    a=[]
    for x in cursor.fetchall():
        k=str(x)[2:len(str(x))-2]
        a.append(int(str(k)))
    j = 0
    col2=[]

    question={}
    while j < len(a):
        q={}
        q.clear()
        query = """select  s.main_quest
                   from   psy.fb_sub_question as s
                   where s.id = '%d'
                """ % (int(a[j]))

        cursor.execute(query)
        c = cursor.fetchall()

        q['Qtitle']=c[0][0]
        query = """select  o.option
                   from   psy.fb_sub_question as s,psy.fb_option as o
                   where o.sub_question_id = s.id and s.id = '%d'
                """ % (int(a[j]))
        cursor.execute(query)
        b = cursor.fetchall()
        i=0
        col3=[]

        while i < len(b):
            con={}
            con.clear()
            con['context']=b[i][0]
            col3.append(con)
            i=i+1
        q['Qoption']=col3
        col2.append(q)
        j=j+1
    question['question']=col2
    data={}
    data['title']=main['title'][0]
    data['answer']=ans['answer']
    data['question']=question['question']
    send=json.dumps(data,indent=4)

    return HttpResponse(send)
