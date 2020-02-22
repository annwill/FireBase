# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 11:50:02 2020

@author: ASUS
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred=credentials.Certificate('fire200108-firebase-adminsdk-y5j3t-af4ba798f7.json')
 #初始化firebase，注意不能重複初始化
#firebase_admin.initialize_app(cred)
# 初始化firestore
db=firestore.client()

doc={
     'name':'測試哥',
     'no':4
     }
doc_ref=db.collection("Students")
doc_ref.add(doc)