import gptscript
def detect_hate_speech(text):
    gptscript.intialize(compile_slurs())
    toReturn = gptscript.response(text)
    return toReturn

def compile_slurs():
    return ["retard", "chink", "basketball americans"]