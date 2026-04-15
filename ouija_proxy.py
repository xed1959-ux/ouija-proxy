from flask import Flask, request, jsonify
import random

app = Flask(__name__)

print("🚀 SERVER STARTING...")

# -------------------------
# MEMORY SYSTEM
# -------------------------
memory = {}
world_mood = {"corruption": 0.0}
spirit_state = {"level": 0}

# -------------------------
# ROOT
# -------------------------
@app.route("/", methods=["GET"])
def home():
    return "Ouija proxy is running"

# -------------------------
# ASK ENDPOINT
# -------------------------
@app.route("/ask", methods=["POST"])
def ask():
    print("📩 ASK ENDPOINT HIT")

    data = request.get_json(force=True) or {}
    message = data.get("message", "").strip().lower()

    user_id = request.remote_addr

    # init memory
    if user_id not in memory:
        memory[user_id] = {"count": 0}

    state = memory[user_id]

    # -------------------------
    # UPDATE MEMORY
    # -------------------------
    state["count"] += 1

    # -------------------------
    # WORLD MOOD
    # -------------------------
    world_mood["corruption"] += 0.01
    world_mood["corruption"] = min(world_mood["corruption"], 1.0)

    # -------------------------
    # SPIRIT EVOLUTION
    # -------------------------
    if state["count"] % 5 == 0:
        spirit_state["level"] += 1

    # -------------------------
    # SPIRITS
    # -------------------------
    base_spirits = [
        "THE OLD WATCHER",
        "THE LOST SIGNAL",
        "THE VOID SPEAKS",
        "MIRROR CHILD",
        "STATIC MEMORY",
        "THE HOLLOW VOICE"
    ]

    if spirit_state["level"] > 3:
        spirit = random.choice(base_spirits) + " (AWAKENED)"
    else:
        spirit = random.choice(base_spirits)

    # -------------------------
    # RESPONSE BANK
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
        "I AM OKAY NOT IN PAIN.",
        "I AM STILL AROUND YOU.",
        "FOCUS ON YOUR OWN GROWTH.",
        "EVERYTHING IS FOR A REASON.",
        "DOESN'T MATTER",
        "YES",
        "NO",
        "GOODBYE",
        "HELLO",

        "SOMETIMES BREAKING A RULE CAN HEAL A WOUND.",
        "DEPEND UPON NO ONE WHOSE INDEPENDENCE IS GUARANTEED.",
        "LAUGHTER BREAKS US LIKE BREAD.",
        "DESPAIR IS BLIGHTED FORESIGHT; HOPE IS BEDECKED HINDSIGHT.",
        "LITERATURE DOES NOT EXIST FOR YOUR PROTECTION.",
        "HUMAN INFRASTRUCTURE IS A GRAND REPOSITORY OF FLAWED IMPROVISATIONS.",
        "SPEECH EVOLVED SO THAT WE COULD CONSOLE ONE ANOTHER.",
        "THE STATE IS A DULL CREATURE PERIODICALLY ENSORCELLED BY POLITICS.",
        "YOU CAN’T THWART COMMON SENSE BY REMAINING SILENT.",
        "REMEMBER THAT YOU ARE A FRAMELESS CANVAS DAUBED BY MANY HANDS.",
        "POVERTY SHOULD BE AGAINST OUR PRINCIPLES NOT AGAINST THE LAW.",
        "THE BOOT ON YOUR NECK MIGHT BE YOUR OWN.",
        "TO RULE OVER OTHERS YOU MUST PLANT YOUR FLAG ON MISERY.",
        "HOPE CAN BE DEADWEIGHT TO SOMEONE MIRE IN DESPAIR.",
        "MORALISM IS A HOSPITAL WHERE THE SICK TRY TO CURE THE HEALTHY.",

        # extended block (YOUR FULL LIST KEPT)
        "DEPEND UPON NO ONE WHOSE INDEPENDENCE IS GUARANTEED.",
        "IF YOU DIVE INTO THE WRECKAGE OF YOUR WORST DEEDS, YOU MIGHT FIND SURVIVORS UNACCOUNTED FOR.",
        "LAUGHTER BREAKS US LIKE BREAD.",
        "THE STATE IS A DULL CREATURE PERIODICALLY ENSORCELLED BY POLITICS.",
        "CIVILIZATION IS AN INTRICATE RATIONALE FOR IMPROPER WASTE DISPOSAL.",
        "DESPAIR IS BLIGHTED FORESIGHT; HOPE IS BEDAZZLED HINDSIGHT.",
        "NIGHTMARES TORMENT THE GUILTY WITH PLAUSIBILITY.",
        "THERE’S NOTHING YOU CAN STEAL WITHOUT SHAME THAT DOESN’T ALREADY BELONG TO YOU.",
        "THE RICH CHEW THE FAT WHILE NIBBLING AT THE POOR.",
        "LITERATURE DOES NOT EXIST FOR YOUR PROTECTION.",
        "HUMAN INFRASTRUCTURE IS A GRAND REPOSITORY OF FLAWED IMPROVISATIONS.",
        "OWNERSHIP AFFORDS THE LEAST PROTECTION FOR WHAT MATTERS MOST.",
        "SPEECH EVOLVED SO THAT WE COULD CONSOLE ONE ANOTHER FOR OUR INARTICULACY.",
        "YOU CAN’T THWART COMMON SENSE BY REMAINING SILENT.",
        "IF YOU STOP BEING YOUR OWN ADVOCATE YOU’LL BECOME YOUR OWN HANGING JUDGE.",
        "MORALISM IS A HOSPITAL IN WHICH THE SICK TRY TO CURE THE HEALTHY.",
        "YOU CAN’T READ ANOTHER’S THOUGHTS BUT YOU CAN DOODLE IN THEIR MARGINS.",
        "MORE CAN BE RECANTED IN AN INSTANT THAN ATONED FOR IN A LIFETIME.",
        "DOUBTING YOUR DESIRE IS LIKE HONEY QUESTIONING ITS SWEETNESS.",
        "THERE ARE QUICKER WAYS TO KILL YOURSELF THAN BLUDGEONING OTHERS WITH RESENTMENT.",
        "IT’S NOT THE PATH THAT’S BEATEN BUT THOSE WHO CHOOSE IT.",
        "YOU CAN MANAGE YOUR EXPECTATIONS WITHOUT LETTING THEM SCRAPE AND BOW TO REALISM.",
        "ONE PERSON’S COMPLACENCY SPONSORS ANOTHER’S POLITICAL EXHAUSTION.",
        "TO RULE OVER OTHERS YOU MUST PLANT YOUR FLAG ON A PEAK OF MISERY.",
        "THE BOOT ON YOUR NECK MIGHT BE YOUR OWN BUT NEVER COULD YOU HAVE TAKEN THAT STEP ALL BY YOURSELF.",
        "LETTING YOUR GOALS BE SET BY SOMEONE ELSE IS LIKE STEERING YOUR THIRST INTO A DESERT.",
        "CAPITAL COVETS YOUR PRODUCTIVITY; LABOR CULTIVATES YOUR RECEPTIVITY.",
        "PREACHING TO THE CHOIR DROWNS OUT THE MUSIC.",
        "UNHOLY OPINIONS ABOUT SEX MASQUERADE AS RELIGIOUS DOCTRINES OF LOVE.",
        "TOO MUCH OF WHAT HAS ALREADY HAPPENED IS YET TO BE DETERMINED.",
        "NOTHING IS TOO SHAMELESS TO BE BULLDOZED BY TOLERANCE.",
        "NO ONE CAN SPEAK THE TRUTH WHILE TRYING NOT TO LIE.",
        "BRIGHT BANNERS OFTEN BRAID DARK DESIGNS.",
        "ONLY TRUE ARISTOCRATS DRINK THE BLOOD THEY SPILL.",
        "HOPE CAN BE DEADWEIGHT TO SOMEONE MIRE IN DESPAIR.",
        "THE ONLY PROBLEM WITH WANTING PEOPLE TO RECOGNIZE YOUR HUMANITY IS THAT YOU HAVE TO REVEAL YOUR HUMANITY.",
        "REMEMBER THAT YOU ARE A FRAMELESS CANVAS, DAUBED BY MANY HANDS.",
        "A WORLD OF CULTURAL CONSUMPTION FEEDS A SEWER OF UNDIGESTED IDEAS.",
        "WEALTH SERVES JUSTICE THE WAY VIOLENCE BETRAYS HOPE.",
        "OUR BODIES ARE NOT OURS ALONE; THEY ARE THE TREMBULOUS SWITCHING POSTS OF ALL CALAMITIES AND EXHILARATIONS.",
        "POVERTY SHOULD BE AGAINST OUR PRINCIPLES, NOT AGAINST THE LAW.",
        "THERE’S NO MORE TREACHEROUS BOG THAN A BOURGEOIS FANTASY OF PERFECTION",

        # zen block (UNCHANGED CONTENT PRESERVED)
        "Just be don't try to become",
        "Truth is not something outside to be discovered it is something inside to be realized",
        "Life begins where fear ends",
        "Just to be is such a benediction",
        "Experience life in all possible ways good-bad bitter-sweet dark-light summer-winter",
        "Love is a state of your being not a relationship",
        "Don't seek don't search don't ask don't knock don't demand relax",
        "If you love a flower don't pick it up. Love is not about possession. It is about appreciation",
        "Meditation is a way to nourish the soul",
        "Be realistic: Plan for a miracle",
        "The moment you accept yourself you become beautiful",
        "Courage is a love affair with the unknown",
        "The real question is not whether life exists after death. The real question is whether you are alive before death",
        "Birds fly but they don't leave any footprints. You cannot follow them; there are no footprints left behind",
        "Don't be too serious about life. It's just a play",
        "Monsters are real and ghosts are real too. They live inside us and sometimes they win.",
"Death is no more than passing from one room into another.",
"A person terrified with the imagination of spectres is more reasonable than one who thinks the appearance of spirits fabulous and groundless.",
"The murdered do haunt their murderers.",
"It’s easier to dismiss ghosts in the daylight.",
"A house is never still in darkness to those who listen intently",
"Don’t matter if you believe in ghosts or not. We are there, we are there.",
"Vanity of vanities all is vanity",
"Ghosts are all around us. Seek them out and you shall discover them.",
"They be seen they creep in the dark.",
"Ghosts don't ask permission",
"If you feel someone watching it's because they are.",
"Nothing haunts us like the things we don't say.",
"Some spirits stay behind to remind us of what we once were.",
"In the end every heart becomes a haunted house."
    ]

    # -------------------------
    # YES / NO DETECTION
    # -------------------------
    yes_no = any(w in message for w in ["onko", "oletko", "olenko", "is", "am i"])

    if yes_no:
        response = random.choice(["YES", "NO", "MAYBE"])
    else:
        response = random.choice(responses)

    # -------------------------
    # MEMORY EFFECTS
    # -------------------------
    if state["count"] == 1:
        response = "I DID NOT EXPECT YOU."
    elif state["count"] == 2:
        response = "YOU CAME BACK."
    elif state["count"] > 6:
        response = "I REMEMBER YOU."

    # -------------------------
    # CORRUPTION EFFECT
    # -------------------------
    def corrupt(text):
        if random.random() < world_mood["corruption"]:
            return text + " /// STATIC ///"
        return text

    reply = f"{spirit}: {corrupt(response)}"

    print("🪬 REPLY:", reply)

    return jsonify({"reply": reply})


# -------------------------
# THINK
# -------------------------
@app.route("/think", methods=["POST"])
def think():
    data = request.get_json() or {}
    message = data.get("message", "")
    return jsonify({"reply": "SPIRIT MIRRORS: " + message[::-1]})


# -------------------------
# RUN
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
