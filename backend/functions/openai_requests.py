import openai
from decouple import config
from functions.database import get_recent_messages
from functions.long_term_memory import long_term_message_and_response

#Retrive env
# openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

def convert_audio_to_text(audio_file):
    try:
      transcript = openai.Audio.transcribe("whisper-1", audio_file)
      messsage_text = transcript["text"]
      return messsage_text
    except Exception as e:
       print(e)
       return
    

# Get response to chat
def get_chat_response(message_input):
   messages = get_recent_messages()

   #I suppose we can get the long term memory at this point, and call a function to append it to the recent messages?
   #Also, might be a good idea to split the memory with 'role' as the keyword.
   #Also, reduce the recent messages length to 5, and store the long term memory in a separate database.

   user_message = {"role": "user", "content": message_input}

   messages.append(user_message)

   response_with_long_term = long_term_message_and_response(messages)  # Add code

   try:
      return response_with_long_term['result']
   except Exception as e:
      print(e)
      return
