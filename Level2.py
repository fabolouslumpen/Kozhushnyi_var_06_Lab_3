def swap_case(text):
    result = ""
    i = 0
    while i < len(text):
        char = text[i]
        if 'a' <= char <= 'z':
            result += chr(ord(char) - ord('a') + ord('A'))
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) - ord('A') + ord('a'))
        else:
            result += char
        i += 1
    return result

def main():
    text = input("Enter a string: ")
    swapped = swap_case(text)
    print(swapped)

if __name__ == "__main__":
    main()