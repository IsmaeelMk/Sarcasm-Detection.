import json

#extracting not sarcastic headlines
with open("sarcastic.json","r", encoding = "utf-8") as file, \
    open("sarcastic_headlines.txt","w",encoding = "utf-8") as sarcastic_headlines:


    for line in file:
        oneline = json.loads(line)
        headline = oneline["headline"]
        sarcastic_headlines.write(headline + "\n")


#extracting non sarcastic headlines
with open("not_sarcastic.json","r", encoding = "utf-8") as file, \
    open("not_sarcastic_headlines.txt","w",encoding = "utf-8") as not_sarcsatic_headlines:


    for line in file:
        oneline = json.loads(line)
        headline = oneline["headline"]
        not_sarcsatic_headlines.write(headline + "\n")