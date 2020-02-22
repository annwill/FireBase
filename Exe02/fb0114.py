import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#引用私密金鑰
cred=credentials.Certificate('fire20113-adminsdk.json')

#注意!初使化 firebase 不可重覆初使化
firebase_admin.initialize_app(cred)

#初使化 firebase
db=firestore.client()