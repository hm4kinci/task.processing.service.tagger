import pytest
from models.tagger_model import TaggerModel, class_mapping


@pytest.mark.integration
def test_predict_model():
    query = 'I called Benjamin for Project Alpha'
    result = TaggerModel.predict(query=query)
    assert result is not None
    assert result.get('success')
    assert result.get('data') is not None
    data = result.get('data')
    assert isinstance(data, list)
    entities = data

    for entity in entities:
        assert entity.get('text') is not None
        assert entity.get('labels') is not None
        labels = entity.get('labels')
        assert labels is not None
        assert isinstance(labels, dict)
        keys = labels.keys()
        for key in keys:
            assert key in class_mapping.keys()
            confidence = labels[key]
            assert confidence >= 0
            assert confidence <= 1

@pytest.mark.integration
def test_predict_model_empty_input():
    query = None
    result = TaggerModel.predict(query)
    assert result is not None
    assert result.get('success') is not True
    query = ''
    result = TaggerModel.predict(query)
    assert result is not None
    assert result.get('success') is not True

