from array import array
from pyexpat import model
import random
import json
import pickle
from secrets import choice
from unittest import result
import numpy as np
    # Installation de module nécessaire a l'integration du fichier .JSON et des bibliotheques de machine learnning
import nltk
from nltk.stem import WordNetLemmatizer
    # Installation du module "WordNetLemmatizer" permettant de ne pas surchargez le pc
import tensorflow
from tensorflow.keras.models import load model

    # On prépare le lemmatizer et l'ouverture du fichier .JSON 
lemmatizer = WordNetLemmatizer
intents = json.loads(open('intents.json').read())

    # On initialise 3 variables, Words, Classes et Model
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
model = load_model('chatbot_model.model')
    #On intitialise 4 variables pour utilisez de manières a utilisez le fichier "training.py" de la mailleur des manieres possible
    # Actuellement le code reçois des valeurs numérique, mais ici on va chercher a ce que le code renvoie une valeur textuel
    # les 4 fonction sont la pour Nettoyer la phrase, avoir le nombre de mots, prédire la classe a partir de la phrase et enfin une fonction pour la réponse

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmetaize(word) for word in sentence_words] 
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word ==w:
                bag[i] = 1
    returnnp.array(bag)

def predic_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow])[0]
    ERROR_THRESHOLD = 0.25
    result =[[i,r]for i,r in enumerate(res) if r > ERROR_THRESHOLD]

    result.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in result:
        return_list.append({'intents': classes[r[0]],'probability: str(r[1])})
    return return_list    

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intents']
    list_of_intents =intents_json['intents']
    for i in list_of_intents:
        if i ['tag'] ==tag:
            result = random.choice(i['responses'])
            break
    return result

Print("Go Bot is Running")

while True:
    message = input("")
    ints = predict_class(message)
    res = get_response(ints,intents)
    print(res)