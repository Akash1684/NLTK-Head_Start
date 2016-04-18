from nltk.tokenize import  sent_tokenize, word_tokenize

article = "Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics concerned with the interactions between computers and human (natural) languages. As such, NLP is related to the area of human–computer interaction. Many challenges in NLP involve: natural language understanding, enabling computers to derive meaning from human or natural language input; and others involve natural language generation."


print("Tokenizing by sentence:\n")
for i in sent_tokenize(article):
    print(i)


print("\n\nTokenizing by word:\n")
for i in word_tokenize(article):
    print(i)
