from flask import Flask, jsonify, request
from ner import NER


app = Flask(__name__)
ner = NER()

@app.route('/ner', methods=['POST', 'GET'])
def ner_classification():
        data = request.get_json()
        text = data.get('extracted_text', '') 
    
        entities = ner.process_text(text)
        response_data = {
                'extracted text': text,
                'status code': '200',
                'message': 'Ner processed successfully',
                'entities': entities
            
            }
        return jsonify(response_data)




  
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 



