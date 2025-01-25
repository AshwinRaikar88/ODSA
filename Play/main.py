



if __name__ == "__main__":
    s = "pwwkew"
    count = 1
    best_count = 1

    prev_char = ""
    substring = ""
    for char in s:
        substring += char
        print(substring)

        if (len(substring) > 1 and substring[0] == substring[-1]) or (char == prev_char):
            substring = char
            count = 1
        else:
            count += 1

        if count > best_count:
            best_count = count
        prev_char = char

    print(best_count)

