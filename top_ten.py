import sys
import json

def hw(tweet_file):
	freq_table={}
	for tweet in tweet_file:
		entry = json.loads(tweet)
		if 'entities' in entry:
			tags = entry['entities']['hashtags']
			for i in range (len(tags)):
				if tags[i]["text"] in freq_table:
					freq_table[tags[i]["text"]] += 1
				else:
					freq_table[tags[i]["text"]] = 0 
	lc=0
	for word in sorted(freq_table, key=freq_table.get, reverse=True):
		if lc <10:
			print word, '%.1f' %(float(freq_table[word]))
		else:
			break
		lc+=1

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)
    tweet_file.close()

if __name__ == '__main__':
    main()
