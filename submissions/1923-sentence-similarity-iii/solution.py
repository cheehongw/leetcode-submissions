class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # tokenize the words
        # shorter sentence require words to be inserted
        
        # tokens = {}

        words_1 = sentence1.split()
        words_2 = sentence2.split()

        # token_count = 0
        # for w in words_1:
        #     if (w in tokens):
        #         continue
        #     tokens[w] = token_count
        #     token_count += 1

        # for w in words_2:
        #     if (w in tokens):
        #         continue
        #     tokens[w] = token_count
        #     token_count += 1

        # tokenized_s1 = [tokens[w] for w in words_1]
        # tokenized_s2 = [tokens[w] for w in words_2]

        shorter = words_1 if len(words_1) < len(words_2) else words_2
        longer = words_2 if len(words_1) < len(words_2) else words_1

        l_ptr, r_ptr = 0, len(shorter)
        longer_r_ptr = len(longer)
        while (l_ptr != r_ptr):
            if (shorter[l_ptr] == longer[l_ptr]):
                l_ptr += 1
            elif (shorter[r_ptr - 1] == longer[longer_r_ptr - 1]):
                r_ptr -= 1
                longer_r_ptr -= 1
            else:
                return False

        return True
            
        
