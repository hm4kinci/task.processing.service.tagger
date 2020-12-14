from flair.data import Sentence
from flair.models import MultiTagger
from collections import defaultdict
import logging

class_mapping = {
    'PERSON' : ['PER','PERSON'],
    'MISC': ['PRODUCT', 'MISC', 'ORG', 'ORGANIZATION', 'WORK_OF_ART', 'FAC'],
    'DATE': ['DATE'],
    'LOCATION': ['LOC', 'LOCATION']
}


class TaggerModel:
    _model = None

    def __init__(self) -> None:
        pass

    @staticmethod
    def load_model():
        if TaggerModel._model is not None:
            return
        logging.info('model loading')
        TaggerModel._model = MultiTagger.load(['ner-ontonotes-fast','ner-fast'])
        logging.info('model loaded')

    @staticmethod
    def predict(query: str):

        if query is None or len(query) == 0:
            return {'success': False, 'message': 'query is required'}

        try:
            sentence = Sentence(query)
            TaggerModel.load_model()
            TaggerModel._model.predict(sentence)

            temp = defaultdict(list)
            for entity in sentence.to_dict(tag_type='ner-fast').get('entities'):
                temp[entity['text']].extend(entity['labels'])
            for entity in sentence.to_dict(tag_type='ner-ontonotes-fast').get('entities'):
                temp[entity['text']].extend(entity['labels'])
            ner_entities = [{'text': text, 'labels': label} for text, label in temp.items()]

            entities = list()
            for item in ner_entities:
                entity = dict()
                entity['text'] = item['text']
                labels = TaggerModel.map_and_merge_labels(
                    [label.to_dict() for label in item['labels']],
                    ['PERSON', 'MISC', 'DATE']
                )
                entity['labels'] = labels
                if len(labels) > 0:
                    entities.append(entity)
            return {'success': True, 'data': entities}
        except RuntimeError as e:
            logging.error(e, exc_info=True)
            return {'success': False, 'message': "Runtime Error: {0}".format(e)}
        except Exception as e:
            logging.error(e, exc_info=True)
            return {'success': False, 'message': 'exception occurred'}

    @staticmethod
    def map_and_merge_labels(labels, ner_classes):
        merged_labels = dict()
        for ner_class in ner_classes:
            confidence_values = [label['confidence'] for label in labels if label['value'] in class_mapping[ner_class]]
            if len(confidence_values) > 0:
                merged_labels[ner_class] = max(confidence_values)
        return merged_labels

