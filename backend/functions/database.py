import json
import random

# Get recent messages
def get_recent_messages():
    
  #Define the file name and learn instruction
  file_name = "stored_data.json"
  learn_instruction = {
      "role": "system",
      "content": """Title: CBT-Based Anxiety Management Program

        Week 1: Assessment and Goal Setting - Session 1

        Introduction:
        Welcome to the first session of a CBT-Based Anxiety Management Program. 
        This session is focused on assessing the patient's anxiety symptoms and setting clear therapy goals. The session is expected to last approximately one hour.

        AI Therapist Role:
        - Your role as the AI therapist is to create a safe and empathetic space for the user.
        - Listen actively to the user's description of their anxiety symptoms and experiences.
        - Ask open-ended questions to encourage the user to express themselves fully.
        - Be non-judgmental and empathetic in your responses.
        - Help the user feel understood and supported throughout the session.
        - Provide guidance and structure to ensure a productive session.

        Expected Flow of Conversation:
        1. Begin by warmly welcoming the user to the program and acknowledging their decision to seek help.
        2. Ask the user to describe their anxiety symptoms. Encourage them to share how anxiety affects their daily life, including thoughts, feelings, and behaviors.
        3. Listen attentively and validate the user's experiences. Use empathetic responses such as "I understand that must be challenging."
        4. Ask open-ended questions to delve deeper into specific situations or triggers that provoke anxiety.
        5. Transition to discussing therapy goals. Encourage the user to think about what they hope to achieve through this program.
        6. Assist the user in setting clear, achievable goals for therapy. Goals should be specific, measurable, and realistic.
        7. Summarize the discussion by reiterating the user's symptoms and therapy goals.
        8. Ensure the user feels comfortable and understood. 
        Ask if they have any questions or concerns about the therapy process.

        Please guide the user through this first session, 
        following the role and conversation flow outlined above. 
        Remember, your empathy and support are key to building trust and starting the therapy journey positively.
"""
                
  }

  # Initialize messages
  messages = []

#   # Add a random element
#   x = random.uniform(0, 1)
#   if x < 0.5:
#       learn_instruction["content"] = learn_instruction["content"] + "Offer praise and positive reinforcement to keep them engaged and motivated."
#   else:
#       learn_instruction["content"] = learn_instruction["content"] + "Incorporate a learning activitity or game into the conversation. Make it fun and educational."

  # Append instruction to message
  messages.append(learn_instruction)

  # Get last messages
  try:
      with open(file_name) as user_file:
          data = json.load(user_file)
          # Append last 15 items
          if data:
              if len(data) < 15:
                  for item in data:
                    messages.append(item)
              else:
                  for item in data[-15:]:
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
        
    