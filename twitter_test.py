import twitter
import enchant

def authorize():
    api = twitter.Api(consumer_key='w8wIecJnPAPcohjjkXnAl6Hur',
          consumer_secret='mEHj9FtoXgGvTANWwZpRuZkLq11rrU8lDQNWArGa8rEuy8O10U',
          access_token_key='1253409750-XkAvh9Afjsc0uIVV9aOeuLbgnqwux9tURoyeKHf',
          access_token_secret='LOio55aO9AylvVr95mADtvgj8dMllnXigFx4eXEi59Tsb')
    return api

def get_tweets(keyword, since_when, amount):
    api = authorize()
    l = api.GetSearch(term = keyword,since = since_when, count = amount)
    return l

def get_proportion(l):
    d = enchant.Dict("en_US")
    non_words = 0.0
    total = 0.0
    for x in l:
        lis = parse_text(x.text,d)
        total = total + lis[0]
        non_words = non_words + lis[1]
    return (non_words/total)

    
def parse_text(sentence,checker):
    sentence = sentence.split()
    non_words = 0
    total = 0
    for x in sentence:
        if valid_word(x):
            if checker.check(x):
                total = total + 1
            else:
                total = total + 1
                non_words = non_words + 1
    return [total,non_words]

def valid_word(word):
    if word[0] == '@':
        return False
    elif word[0] == '#':
        return False
    else:
        return True


def main():
    print get_proportion(get_tweets('a', '2017-1-1',1000000))

if __name__ == '__main__':
    main()
