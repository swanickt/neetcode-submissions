class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        products.sort()

        out = []

        R = len(products) - 1
        L = 0

        for i in range(len(searchWord)):
            
            char = searchWord[i]

            while (len(products[R]) <= i or products[R][i] != char) and L <= R:
                R -= 1

            while (len(products[L]) <= i or products[L][i] != char) and L <= R:
                L += 1
            
            matches = []
            
            if L <= R:
                match_count = min(3, R-L+1)
                for j in range(match_count):
                    matches.append(products[L+j])

            out.append(matches)
        
        return out
            
            



        
