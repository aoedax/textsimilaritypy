#pip install spacy
#pyhton -m spacy download en_core_web_lg

import spacy
nlp = spacy.load("en_core_web_lg")

w1 = "weather"
w2 = "whether"

w1 = nlp.vocab[w1]
w2 = nlp.vocab[w2]

word_result = w1.similarity(w2)
#print(word_result)

s1 = nlp("I ate breakfast today")
s2 = nlp("We eat rice this morning")
s3 =  nlp("I have ate before lunch")

sentence_result = s1.similarity(s3)
#print(sentence_result)

s1_verbs = " ".join([token.lemma_ for token in s1 if token.pos_ == "VERB"])
s1_adjs = " ".join([token.lemma_ for token in s1 if token.pos_ == "ADJ"])
s1_nouns = " ".join([token.lemma_ for token in s1 if token.pos_ == "NOUN"])

s2_verbs = " ".join([token.lemma_ for token in s2 if token.pos_ == "VERB"])
s2_adjs = " ".join([token.lemma_ for token in s2 if token.pos_ == "ADJ"])
s2_nouns = " ".join([token.lemma_ for token in s2 if token.pos_ == "NOUN"])

s3_verbs = " ".join([token.lemma_ for token in s3 if token.pos_ == "VERB"])
s3_adjs = " ".join([token.lemma_ for token in s3 if token.pos_ == "ADJ"])
s3_nouns = " ".join([token.lemma_ for token in s3 if token.pos_ == "NOUN"])

print(f"{s1} and {s2} VERBS: {nlp(s1_verbs).similarity(nlp(s2_verbs))}")
print(f"{s1} and {s3} VERBS: {nlp(s1_verbs).similarity(nlp(s3_verbs))}")
print(f"{s2} and {s3} VERBS: {nlp(s2_verbs).similarity(nlp(s3_verbs))}")

print(f"{s1} and {s2} ADJ: {nlp(s1_adjs).similarity(nlp(s2_adjs))}")
print(f"{s1} and {s3} ADJ: {nlp(s1_adjs).similarity(nlp(s3_adjs))}")
print(f"{s2} and {s3} ADJ: {nlp(s2_adjs).similarity(nlp(s3_adjs))}")

print(f"{s1} and {s2} NOUN: {nlp(s1_nouns).similarity(nlp(s2_nouns))}")
print(f"{s1} and {s3} NOUN: {nlp(s1_nouns).similarity(nlp(s3_nouns))}")
print(f"{s2} and {s3} NOUN: {nlp(s2_nouns).similarity(nlp(s3_nouns))}")

