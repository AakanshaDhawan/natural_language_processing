from nltk.tokenize import sent_tokenize,word_tokenize

text="Hi there how are you today ? I am fine thankyou."

print(sent_tokenize(text))

#output-['Hi there how are you today ?','I am fine thankyou.']


print(word_tokenize(text))

#output-['Hi','there','how','are','you','today','?','I','am','fine','thankyou','.']