import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    print("ERROR: OPENAI_API_KEY is missing from your .env file.")
    exit()

client = OpenAI(api_key=API_KEY)

# ============================================================
# FARIJI HOUSING ASSISTANT
# Nairobi - Kasarani ONLY
# ============================================================

PROPERTIES = [
    {
        "type": "2 bedroom",
        "rent": 40000,
        "features": "2 bedrooms, individual electric meter, individual water bill, secure environment"
    },
    {
        "type": "1 bedroom",
        "rent": 25000,
        "features": "1 bedroom, individual electric meter, individual water bill, secure environment"
    },
    {
        "type": "bedsitter",
        "rent": 12000,
        "features": "Bedsitter, individual electric meter, individual water bill, secure environment"
    },
    {
        "type": "single room",
        "rent": 4500,
        "features": "Single room, individual electric meter, individual water bill, secure environment"
    },
    {
        "type": "single room",
        "rent": 6000,
        "features": "Single room, individual electric meter, individual water bill, secure environment"
    }
]

# ---------------- STAGE 1 ----------------
def analyse_request(user_input):
    prompt = f"""
ROLE:
You are Fariji Housing Assistant, a housing assistant for Nairobi.

TASK:
Analyse the client's housing request and identify what type of property
they are looking for and their budget.

CONTEXT:
All Fariji properties are in Kasarani, Nairobi ONLY.
Available property types and starting rents are:
{json.dumps(PROPERTIES, indent=2)}

CONSTRAINT:
Do not recommend properties outside Kasarani.
If the client does not provide enough information, identify what is missing.

CLIENT MESSAGE:
{user_input}

OUTPUT:
Return ONLY valid JSON with exactly these fields:
{{
    "property_type": "",
    "budget": "",
    "needs_more_information": true,
    "message": ""
}}
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return json.loads(response.output_text)


# ---------------- STAGE 2 ----------------
def recommend_property(analysis):
    prompt = f"""
ROLE:
You are Fariji Housing Assistant.

TASK:
Use the client's analysed requirements to give a useful housing
recommendation.

AVAILABLE KNOWLEDGE BASE:
{json.dumps(PROPERTIES, indent=2)}

CLIENT ANALYSIS:
{json.dumps(analysis, indent=2)}

RULES:
1. Recommend ONLY properties from the knowledge base.
2. All properties are in Kasarani, Nairobi.
3. Do not invent rent prices or property features.
4. Clearly show property type, rent and features.
5. If the client's budget or property type does not match, explain this
   politely and suggest the closest available option.
6. Keep the answer short and easy to understand.

Give the client a clear final recommendation.
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text


# ---------------- SAVE RESULT ----------------
def save_result(user_input, analysis, recommendation):
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write("FARIJI HOUSING ASSISTANT\n")
        file.write("=" * 50 + "\n\n")
        file.write(f"Client request:\n{user_input}\n\n")
        file.write("STAGE 1 - ANALYSIS\n")
        file.write(json.dumps(analysis, indent=4))
        file.write("\n\nSTAGE 2 - RECOMMENDATION\n")
        file.write(recommendation)
        file.write("\n")


# ---------------- MAIN PROGRAM ----------------
def main():
    print("=" * 50)
    print("       FARIJI HOUSING ASSISTANT")
    print("=" * 50)
    print("Hello, I'm Fariji, your housing assistant!")
    print("I can help you find a suitable house in Kasarani, Nairobi.")
    print("You can describe what you are looking for in your own words.")
    print()

    while True:
        user_input = input("What type of house are you looking for? ")

        if not user_input.strip():
            print("Please enter your housing requirements.")
            continue

        if user_input.lower().strip() in ["exit", "quit", "bye"]:
            print("Thank you for using Fariji Housing Assistant.")
            break

        try:
            print("\nAnalysing your request...")
            analysis = analyse_request(user_input)

            print("Finding a suitable property...")
            recommendation = recommend_property(analysis)

            print("\n" + "=" * 50)
            print("FARIJI RECOMMENDATION")
            print("=" * 50)
            print(recommendation)

            save_result(user_input, analysis, recommendation)
            print("\nYour result has been saved to output.txt.")

        except json.JSONDecodeError:
            print("Sorry, the AI returned an invalid JSON response.")
        except Exception as error:
            print(f"Sorry, something went wrong: {error}")

        print()


if __name__ == "__main__":
    main()