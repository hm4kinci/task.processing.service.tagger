from flask import Flask, request
from models.tagger_model import TaggerModel
import settings

app = Flask(__name__)
app.config.from_object(settings)

TaggerModel.load_model()


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    query = request.args.get('query')
    return TaggerModel.predict(query)


if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=int(app.config['PORT']),
        debug=app.config['DEBUG']
    )
