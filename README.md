### TAGGER

This service gets a string value as an input and tries to recognize named entities. 

Class Names: PERSON, MISC, DATE, LOCATION

It uses Flair Sequence Tagging combining 2 different model by maximizing merged/combined predictions. 
- ner-fast: 4-class NER 
- ner-ontonotes-fast: 18-class NER  

### TRAINING ###

There has no further training made on this models, using pretrained weights
Future plans: 
- Instead of combining 2 heavy models, a custom model might be trained if enough training data is obtained.
- If there is not enough labelled data, transfer learning using a small learning rate and batch size can be tried.
    
### PREDICTION ###

Prediction method is served as an api endpoint `/predict`

### RUNNING ###

- uses Python >= 3.8

`Development/Virtual Environment`: 
- $pip install -r requirements.txt
- refer settings.py file if configuration is needed
- $python app.py
 
`Docker`
- $docker-compose build
- $docker-compose up
- refer docker-compose.yaml if configuration needed. 
- requires **task-network** docker network to communicate with other services. 
- to create: $docker network create task-network
- to remove: $docker network rm my-net