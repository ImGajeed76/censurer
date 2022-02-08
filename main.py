import censurer

c_words_path = "censure_words.txt"
e_words_path = "exceptions.txt"

c = censurer.Censure()
c.set_censure_words(c.delete_duplicates(c_words_path))
c.set_exceptions(c.delete_duplicates(e_words_path))

c.update("")
print(c.raw_string)
print(c.censured_string)

c.save_censures(c_words_path)
c.save_exceptions(e_words_path)
