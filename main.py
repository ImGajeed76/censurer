from data import censurer

if __name__ == '__main__':
    c_words_path = "data/censure_words.txt"
    e_words_path = "data/exceptions.txt"

    c = censurer.Censure()
    c.set_censure_words(c.delete_duplicates(c_words_path))
    c.set_exceptions(c.delete_duplicates(e_words_path))
    print("\n" * 100)

    while True:
        print("To exit type -> :stop:")
        text = input("Some text: ")
        if text == ":stop:":
            break
        c.update(text)
        print("Not Censured: \t" + c.raw_string)
        print("Censured:     \t" + c.censured_string)
        input()
        print("\n"*100)

    c.save_censures(c_words_path)
    c.save_exceptions(e_words_path)
