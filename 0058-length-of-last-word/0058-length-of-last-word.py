class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """ 
        In a sentence of words with multiple spaces,the user wants to find out the length of           the last word in the sentence without counting the unnecessary spaces nect to the last         word.
        """
        
        # Step 1: To split the words from the spaces in the sentence and make them individual             elements of a list using the split()
        word_list = s.split()
        
        
        #Step 2: After creating a list of words from the input sentence call the list inndexing          methods and input [-1] as the last element/word in the list/sentence
        return len(word_list[-1])
        