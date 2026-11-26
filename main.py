import os

ENTRY = "The User agrees to water the office ficus every third Tuesday, in silence, wearing the Company lanyard, or forfeit one (1) left shoe as liquidated damages."


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
