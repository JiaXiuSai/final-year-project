import os

password_corpus = ".\\Password Corpus"
pwms = os.listdir(password_corpus)
allAlpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
allNum = "1243567890"

with open("stats_result.txt", "w+", newline="") as output_f:
    for current_pwm in pwms:
        char_dict = {}
        with open(".\\password_corpus\\" + current_pwm) as input_f:
            for line in input_f:
                for c in line:
                    if c != "\n":
                        if c in char_dict:  # check if character is in dictionary
                            char_dict[
                                c
                            ] += 1  # if it's been seen before, increment counter
                        else:
                            char_dict[c] = 1
            sorted_keys = sorted(char_dict, key=char_dict.get, reverse=True)
            letters, numbers, symbols = [], [], []
            for k in sorted_keys:
                if k.isalpha():
                    letters.append(k)
                elif k.isdigit():
                    numbers.append(k)
                else:
                    symbols.append(k)
            output_f.write(f"{current_pwm}\nFrequency sorted char list (Highest to lowest):\n{''.join(sorted_keys)}\n")
            output_f.write(f"Total number of characters: {len(sorted_keys)}\n")
            output_f.write(f"Alphabet set: {''.join(sorted(letters, key = lambda s: sum(map(ord, s))))}\n")
            excAlpha = [x for x in allAlpha if x not in letters]
            if len(excAlpha):
                output_f.write(f"Excluded alphabets: {','.join(sorted(excAlpha))}\n")
            output_f.write(f"Number set: {''.join(sorted(numbers, key = lambda s: sum(map(ord, s))))}\n")
            excNum = [x for x in allNum if x not in numbers]
            if len(excNum):
                output_f.write(f"Excluded numbers: {','.join(sorted(excNum))}\n")
            output_f.write(f"Symbol set: {''.join(sorted(symbols, key = lambda s: sum(map(ord, s))))}\n\n")
        print(current_pwm, "done")
