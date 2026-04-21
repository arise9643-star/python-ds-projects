import groq
import os
import dotenv
from dotenv import load_dotenv
load_dotenv()
client = groq.Groq(api_key = os.getenv("AGENT_KEY"))
def calculator(expression):
    try:
        return str(eval(expression))
    except:
        print("invalid math expression")
def shout(word):
    try:
        return word.upper()
    except:
        return "something went wrong try again"
system_prompt = """You are an agent with access to these tools:

1. calculate(expression) - solves math. Example: calculate(2 + 2)
2. shout(text) - makes text uppercase. Example: shout(hello)

When you need a tool, respond ONLY in this format:
TOOL: tool_name(input)

When you have the final answer, respond ONLY in this format:
ANSWER: your answer here"""
def run_agent(user_goal):
    history = [
        {"role":"system","content": system_prompt},
        {"role":"user","content":user_goal}
    ]
    turns = 0
    max_turns = 5
    while turns < max_turns:
        turns += 1
        response = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages= history
        )
        ai_reply = response.choices[0].message.content
        print(f"Agent: {ai_reply}")
        if ai_reply.startswith("ANSWER:"):
            print(f"\nFinal:{ai_reply.replace('ANSWER','').strip()}")
            break
        elif ai_reply.startswith("TOOL:"):
            tool_call = ai_reply.replace("TOOL:","").strip()
            if tool_call.startswith("calculate"):
                expression = tool_call[10:-1]
                result = calculator(expression)
            elif tool_call.startswith("shout"):
                text = tool_call[6:-1]
                result = shout(text)
            else:
                result = "Unknown tool"
            print(f"Tool result: {result}")

            
            history.append({"role": "assistant", "content": ai_reply})
            history.append({"role": "user", "content": f"Tool result: {result}"})
while True:
    user_input = input("what would your quiestion be: ")
    run_agent(user_input)



