import spacy

nlp = spacy.load("en_core_web_sm")

def anonymize_text(sentences):
    answer = ""
    words = nlp(sentences)

    for word in words:
        answer += word.pos_ + " "

    return answer 
anonymize_text("John is so sweet")