def main():
    file_path = "books/frankenstein.txt"
    text = get_text_from_file(file_path)
    total_words = len(text)
    characters = count_characters(text)
    report = get_book_report(characters, file_path)

def get_book_report(characters, path):
    sorted_list = []
    dictionary = {}
    print(f"--- Begin report of {path} ---")
    
    for c in characters:
        
        sorted_list.append({"char": c, "num": characters[c]})
    sorted_list.sort(reverse=True, key=sort_on)

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
        
def sort_on(d):
    return d["num"]
        
    

def get_text_from_file(path):
    with open(path) as f:
        file_contents = f.read() 
    return file_contents

def count_characters(text):
    chars = {}

    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()  

