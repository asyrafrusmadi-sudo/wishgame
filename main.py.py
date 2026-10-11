import tkinter as tk

def wish():
    text = box.get().lower().strip()

    if text in ["all", "semua"]:
        result.config(text="BOOM! YOU HAVE EVERYTHING!\n- Money + All Heroes + All Animals!")

    # MONEY
    elif text in ["rich", "kaya"]:
        result.config(text="BOOM! $1,000,000! You are RICH!")
    elif text in ["billionaire"]:
        result.config(text="BOOM! $1 BILLION! BILLIONAIRE!")
    elif text in ["trillionaire"]:
        result.config(text="BOOM! $1 TRILLION! TRILLIONAIRE!")
    elif text in ["infinity money", "infinite money", "unlimited money", "infinity", "infinite", "unlimited", "infiniti"]:
        result.config(text="INFINITE MONEY!\n- Unlimited! You own the universe!")

    # HEROES
    elif text in ["superman", "super"]:
        result.config(text="You are SUPERMAN! Fly & super strong!")
    elif text in ["batman"]:
        result.config(text="You are BATMAN! Rich + smart!")
    elif text in ["spiderman", "spider"]:
        result.config(text="You are SPIDERMAN!\n- Danger Sense!\n- Climb Walls!\n- Swing!")
    elif text in ["ironman", "iron man"]:
        result.config(text="You are IRONMAN! Suit up!")
    elif text in ["hulk"]:
        result.config(text="You are HULK! SMASH!")
    elif text in ["thor"]:
        result.config(text="You are THOR! God of Thunder!")
    elif text in ["flash"]:
        result.config(text="You are FLASH! Super fast!")

    # ANIMALS - 2 OPTION
    elif "cat" in text or "kucing" in text:
        if "jadi" in text or "become" in text or "turn" in text:
            result.config(text="You ARE a cat! Meow! 🐱")
        else:
            result.config(text="You get a cat")

    elif "dog" in text or "anjing" in text:
        if "jadi" in text or "become" in text:
            result.config(text="You ARE a dog! Woof! 🐶")
        else:
            result.config(text="You get a dog")

    elif "hamster" in text:
        if "jadi" in text or "become" in text:
            result.config(text="You ARE a hamster! 🐹")
        else:
            result.config(text="You get a hamster")

    elif "rabbit" in text or "bunny" in text or "arnab" in text:
        if "jadi" in text or "become" in text:
            result.config(text="You ARE a rabbit! Hop hop! 🐰")
        else:
            result.config(text="You get a rabbit")

    elif "fish" in text or "ikan" in text:
        if "jadi" in text or "become" in text:
            result.config(text="You ARE a fish! 🐠")
        else:
            result.config(text="You get a fish")

    elif "bird" in text or "burung" in text:
        if "jadi" in text or "become" in text:
            result.config(text="You ARE a bird! You can fly! 🦜")
        else:
            result.config(text="You get a bird")

    elif "turtle" in text or "kura" in text:
        if "jadi" in text or "become" in text:
            result.config(text="You ARE a turtle! Slow but strong! 🐢")
        else:
            result.config(text="You get a turtle")

    else:
        result.config(text="Try: infinity money, billionaire, superman, batman, spiderman, cat, jadi cat, all")

window = tk.Tk()
window.title("INFINITE WISH - FINAL")
window.geometry("450x420")

tk.Label(window, text="What do you wanna be or what do you want?", font=("Arial", 11)).pack(pady=10)
box = tk.Entry(window, width=35, font=("Arial", 12))
box.pack()
tk.Button(window, text="WISH! ✨", command=wish, font=("Arial", 14, "bold"), bg="gold").pack(pady=15)
result = tk.Label(window, text="", font=("Arial", 13, "bold"), wraplength=400, justify="center")
result.pack(pady=10)

window.mainloop()