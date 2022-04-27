#Installation des differents module
from array import array
import random
import json
import pickle
import numpy as np
    # Installation de module nécessaire a l'integration du fichier .JSON et des bibliotheques de machine learnning
import nltk
from nltk.stem import WordNetLemmatizer
    # Installation du module "WordNetLemmatizer" permettant de ne pas surchargez le pc
import tensorflow
from tensorflow.keras.models import Sequential   
from tensorflow.keras.layers import Dense, Avtivation, Dropout
from tensorflow.keras.optimizers import SGD

lemmatizer = WordNetLemmatizer()

intents = json.load(open('intents.json').read())
    #Création  de 4 listes
words = []
classes = []
documents = []
ingore_letters = ['?','!','.',',']
    #On csidere le fichier "intents.json" est considérer commme un dictionnaire for intent in intents ['intents']:
for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
            #"tokenize" permet de separer les mots du phrase, la machine ne lira plus "salut comment ça va ?", 
            #"Salut" "Comment" "Ça" "Va" "?" le tout 
        words.extend(word_list)
            #permet de rajoutez les phars tokenizer a la liste words
        documents.append((word_list), intent['tag'])
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
                # On verifie si la classe intents est bien inscrit dans la classe "classes"
words = [lemmatizer.lemmatize(word) for word in word if word not in ignore_letters]
words = sorted(set(words))

classes = sorted(set(classes))

pickle.dump(classes, open('classes.pkl','wb'))        
words.dump(words, open('words.pkl','wb'))  
# On passe a la partie Machine Learning

training = []
output_empty =[0]* len(classes)

for document in documents:
    bag =[]
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1)if word in word_patterns else bag.append(0)
    
    output_row = list(output_empty)
    output_row[classes.index(document[1])]  =1
    training.append([bag,output_row])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:,0])
train_y = list(training[:,1])

# On passe a la création du réseaux de neuronnes
model =Sequential()
model.add(Dense(128,input_shape=len(train_x[0]),),activation='relu')
model.add(Dropout(0.5))
model.add(Dense(64,activation='relu'))
model.add(Dense(0.5)
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01,decay=1e-6,momentum=0.9,nesterov=True)
model.compile(loss='categorical_crossentropy',optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x),np.array(train_y),epochs=200,batch_size=5,verbose=1)
model.save('chatbot_model.model', hist)
print("Done")

# #On test une premiere fois notre code
print(documents) 

