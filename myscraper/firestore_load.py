import firebase_admin
import json
from firebase_admin import firestore

cred = firebase_admin.credentials.Certificate('../firebase.json')
firebase_app = firebase_admin.initialize_app(cred)

input_file_path = 'output.json'

with open(input_file_path) as file:
    json_data = json.load(file)

    db = firestore.client()

    collection_ref = db.collection('properties')

    for document in json_data:
        print(".")
        doc_ref = collection_ref.document()  # Generate a new document reference
        doc_ref.set(document)  # Set the data for the document