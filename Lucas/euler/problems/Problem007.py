
import time


runs = 10000

# 10001st prime

def main():

    global prime_list
    prime_list = list()
    prime_list.append(2)
    aux_value = 3

    while len(prime_list) != 10001:
        checkPrimeValue(aux_value)
        aux_value += 1

    return prime_list[-1];


def checkPrimeValue(x):
        if x % 2 == 0:
            return

        for prime in prime_list:
            if x % prime == 0:
                return

        prime_list.append(x)


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

