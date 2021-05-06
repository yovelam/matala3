# -*- coding: utf-8 -*-
"""
Created on Mon May  3 09:57:16 2021

@author: user
"""
myfile=open('whatsapp.txt', 'r', encoding='utf-8')
id=0
list_of_dics=[]
dic_of_data={}
counter=0
for line in myfile:
    if "נוצרה על ידי" in line:
        metadata={"chat_name": line[line.find(' "')+2:line.find('" ')], "creation_date": line[ :line.find('-')-1], "num_of_participants": 0, "creator": line[line.find('" ')+15: ].strip()}
    if ":" in line[line.find('-')+2: ]:
        if line[line.find('-')+2:line.find(': ')] not in dic_of_data:
            id+=1
            dic_of_data[line[line.find('-')+2:line.find(': ')]]=id
        list_of_dics.append({"datetime":line[ :line.find('-')-1], "id":dic_of_data[line[line.find('-')+2:line.find(': ')]], "text":line[line.find(': ')+1: ].strip()})
        counter+=1
    if ":" and "-" not in line:
        list_of_dics[counter-1]['text']=list_of_dics[counter-1]['text']+" "+line.strip()
metadata['num_of_participants']=id
metadata['creator']=dic_of_data[metadata['creator']]
all_data={"messages":list_of_dics, "metadata":metadata}

import json
my_jason=json.dumps(all_data, ensure_ascii=False, indent=5)
print(my_jason)
with open (metadata['chat_name']+'.txt', 'w', encoding='utf-8') as j:
    j.write(my_jason)
    
    