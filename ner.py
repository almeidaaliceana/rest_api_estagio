import spacy

class NER:
    def __init__(self) -> None:
        self.nlp = spacy.load('pt_core_news_lg')
    
    
    def process_text(self, text):
        doc = self.nlp(text)
        entities = []
        for entity in doc.ents:
            entities.append({
                'text': entity.text,
                'label': entity.label_
            })
        return entities
       

