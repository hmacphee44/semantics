import spacy
nlp = spacy.load('en_core_web_md')

import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

"""
Cat and monkey are most similar because they are both animals, 
but monkey and banana are very similar too, compared to cat and banana. 
They probably come up a lot together in text.
"""

tokens = nlp('cat apple monkey banana fish ladybird')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

"""
banana and apple are the most similar because they are both fruits.
cat and monkey are the most similar animals maybe because they are both mammals
"""

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I've lost my car in my car",
"I'd like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

"""
I would have expected where did my dog go to be the most similar to why is my cat on the car
Hello there is my car is actually the most similar. 
Maybe it's because these two sentences would go together and make sense
"""