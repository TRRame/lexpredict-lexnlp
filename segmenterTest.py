import lexnlp.nlp.en.segments.sentences

case1 = open("/home/tristan/Stage/TextesJuridiques/AmericansForProsperityFoundationvBontaRoberts.txt", 'r')
text = case1.read()

processed_test = lexnlp.nlp.en.segments.sentences.get_sentence_list(text)

for item in processed_test:
    print(item)