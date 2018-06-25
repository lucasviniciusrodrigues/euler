
import time


runs = 10000

# Even Fibonacci numbers

def main():
    value = 0
    firstAux = 1
    secondAux = 2
    limit = 4000000

    while True:
        if firstAux < secondAux:
            if firstAux % 2 == 0:
                value += firstAux
            firstAux += secondAux
        else:
            if secondAux % 2 == 0:
                value += secondAux
            secondAux += firstAux

        if firstAux > limit and secondAux > limit:
            break

    return value;


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

