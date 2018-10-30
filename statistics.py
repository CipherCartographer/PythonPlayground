class Statistics:
    def __init__(self, array):
        self.array = array

    def mean(self):
        sum  = 0.0
        for n in self.array:
            sum += n
        return float(sum/len(self.array))

    def median(self):
        self.array = sorted(self.array)
        length = len(self.array)
        if length % 2 == 0:
           return float((self.array[length/2] + self.array[(length/2) - 1])/2.0)
        else:
            return self.array[length/2]
    
    def mode(self):
        self.array = sorted(self.array)
        return self.array[len(self.array) - 1]

def main():
    array = [ 1, 3, 4, 2, 7, 5, 8, 6 ]
    print array
    s = Statistics(array)

    print "Mean : " + str(s.mean())
    print "Median : " + str(s.median())
    print  "Mode : " + str(s.mode())



if __name__ == "__main__":
    main()
