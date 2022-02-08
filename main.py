import censurer

if __name__ == '__main__':
    c_words_path = "censure_words.txt"
    e_words_path = "exceptions.txt"

    c = censurer.Censure()
    c.set_censure_words(c.delete_duplicates(c_words_path))
    c.set_exceptions(c.delete_duplicates(e_words_path))

    while True:
        print("To exit type :stop:")
        text = input("Some text: ")
        if text == ":stop:":
            break
        c.update(text)
        print("Not Censured: " + c.raw_string)
        print("Censured" + c.censured_string)

    c.save_censures(c_words_path)
    c.save_exceptions(e_words_path)
