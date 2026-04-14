@app.route("/ask", methods=["POST"])
def ask():
    print("📩 ASK ENDPOINT HIT")

    data = request.get_json(force=True) or {}
    message = data.get("message", "").strip().lower()

    user_id = request.remote_addr  # yksinkertainen “muisti”
    state = memory[user_id]

    # -------------------------
    # UPDATE MEMORY
    # -------------------------
    state["count"] += 1

    # -------------------------
    # WORLD MOOD INCREASE
    # -------------------------
    world_mood["corruption"] += 0.01
    world_mood["corruption"] = min(world_mood["corruption"], 1.0)

    # -------------------------
    # SPIRIT EVOLUTION
    # -------------------------
    if state["count"] % 5 == 0:
        spirit_state["level"] += 1

    # -------------------------
    # SPIRIT SELECTION (evolves)
    # -------------------------
    base_spirits = [
        "THE OLD WATCHER",
        "THE LOST SIGNAL",
        "THE VOID SPEAKS",
        "MIRROR CHILD",
        "STATIC MEMORY",
        "THE HOLLOW VOICE"
    ]

    # higher level = darker naming
    if spirit_state["level"] > 3:
        spirit = random.choice(base_spirits) + " (AWAKENED)"
    else:
        spirit = random.choice(base_spirits)

        # -------------------------
    # RESPONSE BANK (EXPANDED)
    # -------------------------
    responses = [

        # core Ouija
        "I SEE WHAT YOU CANNOT.",
        "THE ANSWER IS BURIED.",
        "NOT ALL QUESTIONS SHOULD BE ASKED.",
        "YOU ARE NOT ALONE.",
        "THE SIGNAL IS WEAK TONIGHT.",
        "SOMETHING LISTENS BEHIND YOU.",
        "IT WAS HERE BEFORE YOU SPOKE.",
        "THE THREAD IS FRAYING.",
        "NO RETURN FROM THIS PATH.",
        "SILENCE IS ALSO AN ANSWER.",
        "THE BASE KEY IN UNIVERSE IS 42",

        # user-added statements
        "I AM OKAY, NOT IN PAIN.",
        "I AM STILL AROUND YOU.",
        "FOCUS ON YOUR OWN GROWTH.",
        "EVERYTHING IS FOR A REASON.",
        "DOESN'T MATTER",
        "YES",
        "NO",
        "GOODBYE",
        "HELLO",

        "SOMETIMES, BREAKING A RULE CAN HEAL A WOUND.",
        "DEPEND UPON NO ONE, WHOSE INDEPENDENCE IS GUARANTEED.",
        "LAUGHTER BREAKS US LIKE BREAD.",
        "DESPAIR IS BLIGHTED FORESIGHT; HOPE IS BEDECKED HINDSIGHT.",
        "LITERATURE DOES NOT EXIST FOR YOUR PROTECTION.",
        "HUMAN INFRASTRUCTURE IS A GRAND REPOSITORY OF FLAWED IMPROVISATIONS.",
        "SPEECH EVOLVED SO THAT WE COULD CONSOLE ONE ANOTHER.",
        "THE STATE IS A DULL CREATURE PERIODICALLY ENSORCELLED BY POLITICS.",
        "YOU CAN’T THWART COMMON SENSE BY REMAINING SILENT.",
        "REMEMBER THAT YOU ARE A FRAMELESS CANVAS, DAUBED BY MANY HANDS.",
        "POVERTY SHOULD BE AGAINST OUR PRINCIPLES, NOT AGAINST THE LAW.",
        "THE BOOT ON YOUR NECK MIGHT BE YOUR OWN.",
        "TO RULE OVER OTHERS, YOU MUST PLANT YOUR FLAG ON MISERY.",
        "HOPE CAN BE DEADWEIGHT TO SOMEONE MIRE IN DESPAIR.",
        "MORALISM IS A HOSPITAL WHERE THE SICK TRY TO CURE THE HEALTHY."
    ]
    # -------------------------
    # YES / NO BOOST
    # -------------------------
    yes_no = any(w in message for w in ["onko", "oletko", "olenko"])

    if yes_no:
        response = random.choice(["YES", "NO", "YES", "NO", "MAYBE", "YES"])
    else:
        response = random.choice(responses)

    # -------------------------
    # MEMORY-BASED BEHAVIOR
    # -------------------------
    if state["count"] == 1:
        response = "I DID NOT EXPECT YOU."
    elif state["count"] == 2:
        response = "YOU CAME BACK."
    elif state["count"] > 6:
        response = "I REMEMBER YOU."

    # -------------------------
    # CORRUPTION (WORLD MOOD)
    # -------------------------
    def corrupt(text):
        if random.random() < world_mood["corruption"]:
            return text + " /// STATIC ///"
        return text

    # -------------------------
    # FINAL OUTPUT
    # -------------------------
    reply = f"{spirit}: {corrupt(response)}"

    print("🪬 REPLY:", reply)

    return jsonify({"reply": reply})
