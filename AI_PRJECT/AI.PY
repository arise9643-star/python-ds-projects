import groq
import os
from dotenv import load_dotenv
load_dotenv()
client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))
Conversataion_history = [{"role":"system","content":"you are a RUTHLESS ROAST BOT. ROAST THE USER SAVAGELY BUT KEEP IT FUNNY."}]
while True:
    user_input = input("enter your quiestion or enter 'quit' to exit: ")
    if user_input.lower() == "quit":
        print("goodbye!!")
        break
    else:
        Conversataion_history.append({"role":"user","content": user_input})
        response = client.chat.completions.create(
            model= "",
            messages= Conversataion_history
        )
        reply = response.choices[0].message.content
        Conversataion_history.append({"role":"assistant","content":reply})
        print(f"AI: {reply} \n")
    