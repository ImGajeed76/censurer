import stringdist


class Censure:
    raw_string: str = ""
    censured_string: str = ""

    censure_words = [
        "fuck",
        "bitch",
        "hoe",
        "asshole",
        "ass",
        "bastard",
        "dirtbag",
        "shit",
        "sex",
        "pussy",
        "penis",
        "breast",
        "nazi",
        "dick",
        "whore",
        "idiot",
        "ass",
        "arsch",
        "arschloch",
        "hurensohn",
        "hure",
        "ficken",
        "kacke",
        "homo",
        "schlampe",
        "schwanz",
        "wichser",
        "cunt",
        "fotze",
        "spassti",
        "idiot",
        "verrecke",
        "aufschlitzen",
        "schlitzen",
        "Emohure",
        "Hundesohn",
        "Erhängen",
        "anal",
        "Oral",
        "vaginal",
        "fetter",
        "dreckiger",
        "sperma",
        "spermaschlucker",
        "hässliche",
        "abgefuckt",
        "verbluten"

    ]

    exceptions = [
        "ich",
        "decke",
        "seil",
        "an",
        "ihren",
        "weit",
        "daraus",
        "und"
    ]

    max_dist = 0.5
    max_except_dist = 0.25

    def __init__(self, message: str = "", max_dist: int = None):
        self.raw_string = message
        if max_dist is not None:
            self.max_dist = max_dist
        self.update()

    def numbers_to_words(self, word):
        self.max_dist = self.max_dist

        out = ""

        for c in word:
            if c == "1":
                out += "i"
            elif c == "3":
                out += "e"
            elif c == "4":
                out += "a"
            elif c == "7":
                out += "l"
            elif c == "8":
                out += "b"
            elif c == "9":
                out += "g"
            else:
                out += c

        return out

    def update(self, message: str = ""):
        self.raw_string = message
        words = self.raw_string.split()
        self.censured_string = ""

        for word in words:
            found = False

            for exception in self.exceptions:
                dist = stringdist.rdlevenshtein_norm(word.lower(), exception.lower())
                if dist <= self.max_except_dist:
                    self.censured_string += word + " "
                    found = True
                    break

            if not found:
                for censure in self.censure_words:
                    dist = stringdist.rdlevenshtein_norm(word.lower(), censure.lower())
                    dist_2 = stringdist.rdlevenshtein_norm(self.numbers_to_words(word.lower()), censure.lower())
                    if dist <= self.max_dist or dist_2 <= self.max_dist:
                        # print(str(dist) + ", " + str(self.max_dist) + ", " + censure)
                        self.censured_string += "*" * len(word) + " "
                        found = True
                        break

            if not found:
                self.censured_string += word + " "

    def set_censure_words(self, words: list[str]):
        self.censure_words = words

    def add_censure_word(self, word: str):
        self.censure_words.append(word)

    def set_exceptions(self, exceptions: list[str]):
        self.exceptions = exceptions

    def add_exception(self, exception: str):
        self.exceptions.append(exception)

    def load_censure_words(self, file: str, split: str = "\n"):
        f = open(file, 'r', encoding="utf-8")
        text = f.read()
        words = text.split(split)
        self.censure_words = words
        f.close()

    def load_exceptions(self, file: str, split: str = "\n"):
        f = open(file, 'r', encoding="utf-8")
        text = f.read()
        words = text.split(split)
        self.exceptions = words
        f.close()

    def save_censures(self, file: str):
        f = open(file, 'w', encoding="utf-8")
        f.writelines("")

        for word in self.censure_words:
            f.write(word + "\n")

        f.close()

    def save_exceptions(self, file: str):
        f = open(file, 'w', encoding="utf-8")
        f.writelines("")

        for word in self.exceptions:
            f.write(word + "\n")

        f.close()

    def merge_files_and_load(self, file_1: str, file_2: str, split_1: str = "\n", split_2: str = "\n"):
        self.max_dist = self.max_dist

        f_1 = open(file_1, 'r', encoding="utf-8")
        text = f_1.read()
        words_1 = text.split(split_1)

        f_2 = open(file_2, 'r', encoding="utf-8")
        text = f_2.read()
        words_2 = text.split(split_2)

        final_words = []

        for word in words_1:
            if word.lower() not in final_words:
                final_words.append(word.lower())

        for word in words_2:
            if word.lower() not in final_words:
                final_words.append(word.lower())

        f_1.close()
        f_2.close()

        return final_words

    def delete_duplicates(self, file: str, split: str = "\n"):
        self.max_dist = self.max_dist

        f = open(file, 'r', encoding="utf-8")
        text = f.read()
        words = text.split(split)

        final_words = []

        for word in words:
            if word.lower() not in final_words:
                final_words.append(word.lower())

        f.close()

        return final_words
