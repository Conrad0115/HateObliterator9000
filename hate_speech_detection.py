import gptscript
def detect_hate_speech(text):
    gptscript.intialize(compile_slurs())
    toReturn = gptscript.response(text)
    return toReturn

import csv



def compile_slurs():
    with open('combine_table.csv', newline='') as f:
        reader = csv.reader(f)
        slurs = list(map(lambda x: str(x), list(reader)))
        return slurs