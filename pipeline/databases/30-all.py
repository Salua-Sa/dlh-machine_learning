// Lists all documents in a collection.
def list_all(mongo_collection):
  documents = list(mongo_collection.find())
  if documents == []:
    return []
  return documents
