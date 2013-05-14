import sys
import json

def hw(tweet_file):
	wc = 0
	freq_table={}
	for tweet in tweet_file:
		entry = json.loads(tweet)
		if 'text' in entry:
			msg = (entry['text']).encode('utf-8')
			words = msg.split()
			for word in words:
				wc += 1
				if word in freq_table:
					freq_table[word] += 1
				else:
					freq_table[word] = 0
	for word in sorted(freq_table, key=freq_table.get, reverse=True):
		print word, '%.4f' %(float(freq_table[word])/wc)

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)
    tweet_file.close()

if __name__ == '__main__':
    main()
