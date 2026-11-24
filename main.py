import os

WORD = "snickersnee"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f_out:
    f_out.write(WORD)
