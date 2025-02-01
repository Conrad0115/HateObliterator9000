from openai import OpenAI
import os as os
import dotenv
dotenv.load_dotenv()

# Get the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)


message_history = []        # list of strings
slurs = ["\"retard\"", "\"chink\"", "\"basketball americans\""]

def intialize(slurs):
    info = (slurs , "provided above is a list of hate speech terms and dogwhistles. If a slur is multiple words, all of the words need to be present to be considered a slur, and in order. You are to return all instances" +
            "in the following texts of hate speech. You should only respond with the specific word you think might be hate speech."+
            "it doesn't have to be an exact match, often times hate will be concealed through altering spelling. please return"+
            "a comma seperated list of all words. Write the words as they are spelled in following texts, not how they slur is actually spelled."+
            "if a word is similar to one of the slurs or dogwhistles, use context to decide if it is hateful or not." +
            "If you can't find any instances, simply reply \"none\"")
    
    message_history.append({"role": "user", "content": f"{info}"})
    message_history.append({"role": "assistant", "content": f"ok"})

def response(input):
    message_history.append({"role": "user", "content": f"{input}"})
    completion = client.chat.completions.create(
      model="gpt-4o",
      messages=message_history
    )
    reply_content = completion.choices[0].message.content
    print(reply_content)
    return reply_content

intialize(slurs)
response("poopity scoop")
