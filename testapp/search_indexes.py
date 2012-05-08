from testapp.models import *
from haystack import indexes
import datetime

class DataIndex(indexes.RealTimeSearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='name')

    def get_model(self):
        return Data