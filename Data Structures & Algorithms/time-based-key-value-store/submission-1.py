class TimeMap:

    def __init__(self):
        self.keyStore = defaultdict(list) # key : list of [val, timestamp]


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append([value, timestamp]) # remains sorted as timestamps are stricly increasing

    def get(self, key: str, timestamp: int) -> str:
        
        key_list = self.keyStore.get(key, [])
        
        result = ""
            
        lower_bound, upper_bound = 0, len(key_list) - 1

        while lower_bound <= upper_bound:

            m = (lower_bound + upper_bound) // 2

            if key_list[m][1] <= timestamp:
                result = key_list[m][0]
                lower_bound = m + 1
            
            else:
                upper_bound = m - 1
        
        return result
                

