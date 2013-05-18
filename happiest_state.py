import sys
import json

def hw(tweet_file, scores, state_score):
	for tweet in tweet_file:
		entry = json.loads(tweet)
		if 'lang' in entry and entry['lang'] == "en" and entry['text'] != None:
				if entry['place'] != None and entry['place']['country_code'] == "US":
					city, state = entry['place']['full_name'].split(", ")
					if state == "US" or state == "Nashville":
						state = entry['place']['name']
					tweet_str = entry['text'].encode ('utf-8')
					words = tweet_str.split()
					senti_score = 0
					for word in words:
						if word in scores:
							senti_score+= scores[word]
					if state in state_score:
						state_score[state]+=senti_score
					else:
						state_score[state]=senti_score
	res = list(sorted (state_score, key=state_score.__getitem__, reverse=True));
	if res != None:
		print res
def lines(fp):
    print str(len(fp.readlines()))

def build_affin_dict (fp,scores):	
	for line in fp:
		term, score = line.split("\t")
		scores[term] = int(score)

def main():
    scores = {}
    state_score = {}
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    build_affin_dict (sent_file,scores)
    hw(tweet_file, scores, state_score)
    tweet_file.close()
    sent_file.close()

if __name__ == '__main__':
    main()
