from sets import Set
vocab = []
with open('MidtermVocabList.txt') as f:
	for l in f:
		line = l.strip().split("\t")
		for w in line:
			vocab.append(w)
		
#print vocab
outfile = open('MidtermResult.txt', 'w+')
with open('NovakVocab.txt') as f:
	for l in f:
		#get the vocab word (string until :)
		term = l.split(':')[0]
		#print term
		#if this word is in the list, write the entire line into output file
		if term in vocab:
			outfile.write(l)
