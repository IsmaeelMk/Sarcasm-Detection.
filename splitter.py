import json

sarcastic_file = "sarcastic.txt"
not_sarcastic_file = "not_sarcastic.txt"

with open("Sarcasm_Headlines_Dataset.json", "r", encoding="utf-8") as infile, \
     open(sarcastic_file, "w", encoding="utf-8") as sarcastic_out, \
     open(not_sarcastic_file, "w", encoding="utf-8") as not_sarcastic_out:

    for line in infile:
        line = line.strip()
        if not line:
            continue
        record = json.loads(line)

        if record["is_sarcastic"] == 1:
            sarcastic_out.write(json.dumps(record) + "\n")
        else:
            not_sarcastic_out.write(json.dumps(record) + "\n")

with open("not_sarcastic.json","r",ecoding = "utf-8") as file:
    record = json.loads(line)

    for i in range(1):
        print(record)
