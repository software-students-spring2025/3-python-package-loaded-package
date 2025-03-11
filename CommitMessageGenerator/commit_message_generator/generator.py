import random

# Function 1: Create emoji-filled commit messages
def emoji_commit():
    messages = [
        "Fixed a bug 🐞🔧",
        "Refactored code 🛠️🎨",
        "Improved performance 🚀🔥",
        "Added new feature 🎉✨",
        "Updated documentation 📚✏️",
    ]
    return random.choice(messages)

# Function 2: Generate messages in different styles (pirate, superhero, etc.)
def themed_commit(style="pirate"):
    pirate = ["Arrr! Fixed me code, matey! 🏴‍☠️", "Shivered me timbers! A bug be gone! 🦜"]
    superhero = ["Justice is served! Bug fixed! 🦸‍♂️", "With great power comes bug fixes! ⚡"]
    
    styles = {"pirate": pirate, "superhero": superhero}
    
    return random.choice(styles.get(style, ["Standard commit message."]))

# Function 3: Create commit haikus based on changed files
def haiku_commit(files):
    haikus = [
        "Code flows like a stream,\nChanges ripple through the trees,\nThe test suite still breaks.",
        "Refactored today,\nErrors fading in the mist,\nDeploy with caution.",
    ]
    return random.choice(haikus)

# Function 4: Turn boring messages into dramatic ones
def dramatic_commit(message):
    return f"🔥🔥 {message.upper()} 🔥🔥"
