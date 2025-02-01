import gptscript
def detect_hate_speech(text):
    gptscript.intialize(compile_slurs())
    toReturn = gptscript.response(text)
    return toReturn

import csv



def compile_slurs():
    slurs = []
    with open('combined_table.csv', newline='') as f:
        reader = csv.reader(f)
        slurs.extend([item for sublist in reader for item in sublist])
        
    with open('acronyms.csv', newline='') as f:
        reader = csv.reader(f)
        slurs.extend([item for sublist in reader for item in sublist])
        
    with open('numbers.csv', newline='') as f:
        reader = csv.reader(f)
        slurs.extend([item for sublist in reader for item in sublist])
    with open('phrases.csv', newline='') as f:
        reader = csv.reader(f)
        slurs.extend([item for sublist in reader for item in sublist])
    
    return slurs