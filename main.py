sarcastic_wordlist = {}
with open("sarcastic_headlines.txt", "r",encoding = "utf-8") as file:
    for line in file:
        words = line.lower().split()

        for word in words:
            if word in sarcastic_wordlist:
                sarcastic_wordlist[word] += 1
            else:
                sarcastic_wordlist[word] = 1


not_sarcastic_wordlist = {}
with open("not_sarcastic_headlines.txt","r",encoding = "utf-8") as file:
    for line in file:
        words = line.lower().split()

        for word in words:
            if word in not_sarcastic_wordlist:
                not_sarcastic_wordlist[word] += 1
            else:
                not_sarcastic_wordlist[word] = 1

#actual logic
def guess(sentence):
    sarcasticscore = 0
    nonsarcasticscore = 0
    overallscore = 0
    sentencewords = sentence.lower().split()
    for word in sentencewords:
        sarcasticscore = sarcastic_wordlist[word]
        nonsarcasticscore = not_sarcastic_wordlist[word]
        thiswordscore = sarcasticscore - nonsarcasticscore
        overallscore += thiswordscore
    if overallscore > 0:
        return "this is a sarcastic headline"
    else:
        return "this is a non sarcastic headline"


print(guess("two cars destroyed the entire planet"))