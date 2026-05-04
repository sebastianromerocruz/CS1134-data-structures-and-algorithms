from ChainingHashTableMap import ChainingHashTableMap


class InvertedFile:
    def __init__(self, file_name):
        self.index = ChainingHashTableMap()

        file_obj = open(file_name)
        words = file_obj.read().split()
        file_obj.close()

        i = 0
        for raw_word in words:
            word = ''.join([c for c in raw_word if c.isalpha()]).lower()
            if word != '':
                if word not in self.index:
                    self.index[word] = []
                self.index[word].append(i)
            i += 1

    def indices(self, word):
        letters = [char for char in word if char.isalpha()]
        word = ''.join(letters).lower()
        
        if word not in self.index:
            return []
        return self.index[word]
