# IS String made of unique characters.

class Error(Exception):
    pass

class NoStringCreated(Error):
    pass

class ArrayStrings:
    def __init__(self) -> None:
        pass

    def set_string(self, string):
        self.string = string
    
    def get_string(self):
        try:
            if hasattr(self, 'string'):
                return self.string
            else:
                raise  NoStringCreated
        except:
            print(("No string is available, set before proceeding"))

    
    def is_unique(self, method="hash"):
        if method=="hash":
            return self.__is_unique_hash()
        elif method=="bit":
            return self.__is_unique_bit()

    def __is_unique_hash(self):
        """
        """
        hash = {}
        if not self.get_string():
            return

        for char in self.string:
            if char in hash:
                return False
            hash[char] = True
        
        return True

    def __is_unique_bit(self):
        """
        """
        if not self.get_string():
            return
        checker = 0
        for char in self.string:
            pass # TODO

    def __is_permutation(self):
        pass

    @staticmethod
    def is_permutation(string_a, string_b):
        if len(string_a) != len(string_b):
            return False
        hash = {}
        for char in string_a:
            if char in hash:
                hash[char] +=1
            else:
                hash[char] = 1
        
        for char in string_b:
            if char not in hash:
                return False
            elif hash[char] <= 0:
                return False
            else:
                hash[char] -= 1
        return True

def check_is_unique():
    """
    """
    print("############### check_is_unique ##################\n")
    obj = ArrayStrings()
    obj.set_string("xzabcdefghijka")
    print("String ---------------------- ", obj.get_string())
    print("Is Unique hash --------------------------- ",obj.is_unique())
    print("Is Unique bit --------------------------- ",obj.is_unique(method="bit"))


def check_is_permutation():
    print("############### check_is_permutation ##################\n")
    per_obj = ArrayStrings()
    
    per_obj.set_string("abcdef")
    string_a = per_obj.get_string()

    per_obj.set_string("fedcab")
    string_b = per_obj.get_string()

    print(f"string_a = {string_a}, string_b = {string_b}")
    print("is_permutation ------------- ", per_obj.is_permutation(string_a, string_b))

def check_palindrome_permutation():
    print("############### check_is_permutation ##################\n")
    per_obj = ArrayStrings()
    
    per_obj.set_string("abcdef")
    string_a = per_obj.get_string()

    per_obj.set_string("fedcab")
    string_b = per_obj.get_string()

    print(f"string_a = {string_a}, string_b = {string_b}")
    print("is_permutation ------------- ", per_obj.is_permutation(string_a, string_b))


if __name__ == "__main__":
    # check_is_unique()
    # check_is_permutation()
    check_palindrome_permutation()

