 def find_xth_negative():
        count = 0
        for v in range(0, 50):  # only negative numbers (-50 to -1)
            count += freq[v]
            if count >= x:
                return v - 50
        return 0 def find_xth_negative():
        count = 0
        for v in range(0, 50):  # only negative numbers (-50 to -1)
            count += freq[v]
            if count >= x:
                return v - 50
        return 0