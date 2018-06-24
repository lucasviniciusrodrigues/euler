
import time


runs = 10000

# Largest prime factor

primeList = [2]

def main():
    value = 600851475143

    while(value != 1):
        for prime in primeList:
           if value % prime == 0:
                value //= prime
                break
           elif(prime == primeList[len(primeList) - 1]):
               nextPrimeValue(value)

    return primeList[len(primeList) - 1];


def nextPrimeValue(max):
    for x in range(primeList[len(primeList) - 1], max + 1):
        aux = 1
        if x % 2 != 0:
            for prime in primeList:
                if x % prime == 0:
                    aux = 0
                    break
            if aux != 0:
                primeList.append(x)
                if(max % x == 0):
                    break


if __name__ == "__main__":
    answer = 0
    total_time = 0

    for run in range(0, runs):
        start_time = time.time()
        answer = main()
        run_time = time.time() - start_time
        total_time += run_time

    print("answer  --- {} ---".format(answer))
    print("runtime --- {:.4f} ms ---".format((total_time * 1000) / runs))

