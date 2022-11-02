class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        """
        Given a pattern and a string s, find if s follows the same pattern.

        :param self: Instance of the class
        :param pattern: String with a defined pattern of alphabets
        :param s: Sentence of words which is then compared for the word pattern similarity                    with letters in 'pattern'
        :return: Output as True or False depending on whether the pattern matches
        """

        # Creating a string of words from the string parameter in order to check its pattern           as a whole
        
        words_in_string = s.split(" ")

        
        # Firstly we need to check whether length of both the parameter pattern and s are the          same in order to compare the pattern and return False if length is not the same
        
        if len(pattern) != len(words_in_string):
            return False
        
        
        # Create Two Has Maps which stores mapping of the pattern character to each word in s          in the Pat_Wor variable in sequential order and also each word from the s string              mapped to each word in the pattern parameter in sequential order
        
        Pat_Wor = {}
        Wor_Pat = {}

        
        # Iterate through each character and word from pattern and s using the zip command
        
        for c, w in zip(pattern, words_in_string):
            
            
            # Check whether c exists in the map Pat_Wor and if it does exist check whether it               maps the same word, in Wor_Pat, if not return false
            
            if c in Pat_Wor and Pat_Wor[c] != w:
                return False
            
            # Check whether w exists in the map Wor_Pat and if it does exist check whether it               maps the same character, in Pat_Wor, if not return false
            
            if w in Wor_Pat and Wor_Pat[w] != c:
                return False

            # If the above two conditions are not met then map the character to the word and              vice versa
            
            Pat_Wor[c] = w
            Wor_Pat[w] = c

        # Once the for loop is complete and there are no mismatch found between the mappings,           return True
        return True

