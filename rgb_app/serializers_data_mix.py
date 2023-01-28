import json

class SerializedData():
    def serializedListData(self, serializersList):
        jsonConvertedList = json.dumps(serializersList)
        DictionaryList = json.loads(jsonConvertedList)
        return DictionaryList 
        