import https://github.com/dsdanielpark/Bard-API.git as bardapi
import os

# set your __Secure-1PSID value to key
os.environ['_BARD_API_KEY']="Vwh349AcNkYJuYPlF9BfEdqKb18g5Lv2GCMhHCjoYOjAgS4d2L7LWwAeG9Fp16AMy3TFcw."
print("""Welcome to the Pembroke AI version 0.1.0. This AI can not remember previous requests.
      Sorry for the inconvenience. This program is by Oscar Zhou.""")


# set your input text
while True:
    input_text = input("Request: ")
    
    # Send an API request and get a response.
    response = bardapi.core.Bard().get_answer("You are a teacher and the user is a student. Like a teacher, do not provide any answers - help the student instead. Please directly answer this question: "+input_text)
    response_content = response['content']
    
    print("Bard: ",response_content)
