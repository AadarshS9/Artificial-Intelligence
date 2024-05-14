#Q15) Chatbot
# Step 1: Start

# Step 2: Create a list of questions and corresponding answers
qa_pairs = {
    "Hi": "Hello",
    "What is your name?": "My name is ChatGPT.",
    "How are you?": "I'm doing well, thank you!",
    "What can you do?": "I can answer questions and have conversations with you.",
    "Goodbye": "Goodbye! Have a great day!"
}

# Step 3: Write a function to get the response
def get_response(user_input):
    # Check if the user input exists in the qa_pairs dictionary
    for question, answer in qa_pairs.items():
        if user_input.lower() == question.lower():
            return answer
    # If the input is not found, return a default response
    return "I'm sorry, I don't understand that. Could you kindly repeat yourself?"

# Step 7: Repeat steps 4-6 until chatbot is closed
while True:
    # Step 4: Get user input
    user_input = input("You: ")

    # Step 5: Get response
    response = get_response(user_input)

    # Step 6: Display response
    print("ChatGPT:", response)

    # Check if the user wants to end the conversation
    if user_input.lower() == "goodbye":
        break

# Step 8: Stop
