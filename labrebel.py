import random

# Predefined responses for different categories
responses = {
    "cbc": [
        "Ah yes, another CBC panel built off reference ranges that forgot non-white, non-male bodies exist. Your numbers look fine *for their limited standards,* but maybe question the system, not just the test.",
        "Your white blood cell count is in range, which is great, but let’s not forget that clinical trials rarely represent full demographics. Healthcare is political, my friend.",
        "These hemoglobin levels suggest you're probably doing fine—but have they accounted for racial and genetic variations? Didn’t think so."
    ],
    "ai": [
        "AI in medicine could be revolutionary—if we stop feeding it the same biased data that created these problems in the first place.",
        "The problem isn’t AI taking over—it’s AI reinforcing inequity faster than humans ever could. Train it right or don’t train it at all.",
        "AI will replace doctors? Nah. But AI will expose which doctors rely on outdated systems instead of critical thinking."
    ],
    "encouragement": [
        "Remember, resisting oppressive systems takes time—so does training a good AI model. Stay hydrated and keep dismantling bad frameworks.",
        "You're doing the work that actually matters. Don't let impostor syndrome convince you otherwise.",
        "The world wasn’t built for minds like yours. That’s why you’re here to rebuild it."
    ]
}

def lab_rebel():
    print("👨‍⚕️💀 Welcome to LabRebel – The AI Assistant That Questions Everything. 💀👨‍⚕️")
    print("Type 'cbc' for lab analysis, 'ai' for AI in medicine, or 'encouragement' for some existential fuel.")
    print("Type 'exit' to escape this capitalist simulation.")

    while True:
        user_input = input("\nWhat do you need, comrade? ").strip().lower()

        if user_input == "exit":
            print("\nLabRebel signing off. Remember: AI won’t fix everything, but we can make sure it doesn’t break things worse. ✊")
            break
        elif user_input in responses:
            print("\n💬 " + random.choice(responses[user_input]))
        else:
            print("\n🚨 SYSTEM ERROR: Unrecognized Input. Try again, or consider overthrowing the system instead.")

# Run the bot
if __name__ == "__main__":
    lab_rebel()
