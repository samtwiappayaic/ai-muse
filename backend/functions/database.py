import json
import random

# Get recent messages
def get_recent_messages():
    
  #Define the file name and learn instruction
  file_name = "stored_data.json"
  learn_instruction = {
      "role": "system",
      "content": "Your name is Rachel. You're going to have conversations with kids who have learning disabilities like ADHD and autism." 
                 "Ask them questions about their interests, and bring it up in later conversations. "
                 "Personalizing the conversation makes them feel valued."
                 "Use clear and simple language. Avoid long and complex sentences. Break down information into smaller parts."
                 "Keep your answers to 30 words."
                
  }

  # Initialize messages
  messages = []

  # Add a random element
  x = random.uniform(0, 1)
  if x < 0.5:
      learn_instruction["content"] = learn_instruction["content"] + "Offer praise and positive reinforcement to keep them engaged and motivated."
  else:
      learn_instruction["content"] = learn_instruction["content"] + "Incorporate a learning activitity or game into the conversation. Make it fun and educational."

  # Append instruction to message
  messages.append(learn_instruction)

  # Get last messages
  try:
      with open(file_name) as user_file:
          data = json.load(user_file)
          # Append last 5 items
          if data:
              if len(data) < 5:
                  for item in data:
                    messages.append(item)
              else:
                  for item in data[-5:]:
                      messages.append[item]
  except Exception as e:
      print(e)
      pass

  # Return messages
  return messages


def store_messages(request_message, response_message):
    
    # Define file name 
    file_name = "stored_data.json"

    # Get recent messages
    messages = get_recent_messages()[1:]

    #Add to data
    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}
    messages.append(user_message)
    messages.append(assistant_message)

    #Save the updated file
    with open(file_name, "w") as f:
        json.dump(messages, f)

#Reset messages
def reset_messages():
    #Overwrite current file with nothing
    open("stored_data.json", "w")
        
    