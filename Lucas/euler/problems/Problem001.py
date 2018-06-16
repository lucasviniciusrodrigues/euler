
import time


runs = 10000


def main():
    limit = 10000;
    sum = 0;
    multipleFive = 5;
    multipleThree = 3;

    while multipleThree < limit:
        if multipleFive < limit:
            sum += multipleFive;
            multipleFive += 5;
        if multipleThree % 5 != 0:
            sum += multipleThree;
        multipleThree += 3;

    return sum;


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

