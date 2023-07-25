import random

def shuffle(N):
    """
    The shuffle function creates a list with elements 1..N and uses the efficient Fisher-Yates algorithm to shuffle the list.
    :param N: size of the list
    :return: a list containing elements 1..N in shuffled order
    """
    shuffleList = list(range(1, N + 1)) #create a list from 1..N [O(N) in all cases]
    for i in range(N - 1, 0, -1): #a loop starting from the end of the last index of the list and decrementing to the first index [O(n) in all cases]
        j = random.randint(0, i) #creates a random integer between 0 and i, where i is the last indice that has not been struck out [O(1) in all cases]
        shuffleList[i], shuffleList[j] = shuffleList[j], shuffleList[i] #the elements in position i and j are swapped [O(1) in all cases]

    return shuffleList

def main():
    N = int(input("Enter the value of N: "))
    print("The random order of integers given the input N={} is {}".format(N, shuffle(N)))

if __name__ == '__main__':
    main()

