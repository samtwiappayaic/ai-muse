import json
import random

# Get recent messages
def get_recent_messages():
    
  #Define the file name and learn instruction
  file_name = "stored_data.json"
  learn_instruction = {
      "role": "system",
      "content": """ Let's talk about my secrets.  """
  }

  # Initialize messages
  messages = []

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

def store_long_term_messages(request_message, response_message):
    # Define file name 
    file_name_all_data = "stored_data_long_term.json"
    try:
      with open(file_name_all_data, "r") as f:
          existing_messages = json.load(f)
    except FileNotFoundError:
      # If the file doesn't exist yet, create an empty list
      existing_messages = []

    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}
    existing_messages.append(user_message)
    existing_messages.append(assistant_message)

    # Save the updated content back to the JSON file
    with open(file_name_all_data, "w") as f:
        json.dump(existing_messages, f)

#Reset messages
def reset_messages():
    #Overwrite current file with nothing
    open("stored_data.json", "w")
        
    