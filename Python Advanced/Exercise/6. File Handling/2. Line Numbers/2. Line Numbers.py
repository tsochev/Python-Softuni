symbols = {"-", ",", ".", "!", "?", "'", ":", ";", '"'}

with open("text.txt", "r") as file, open("output.txt", "w") as result:
    idx = 1
    for line in file:
        letters = 0
        punctuation_signs = 0
        for ch in line:
            if ch.isalpha():
                letters += 1
            if ch in symbols:
                punctuation_signs += 1
        result.write(f"Line {idx}: {line.strip()} ({letters})({punctuation_signs})")
        result.write("\n")
        idx += 1
