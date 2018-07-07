
import time

runs = 10000

# Smallest multiple

def main():
    value = 2520
    aux_end = 0
    max_range = 20

    while True:
        if value % max_range == 0:
            for divisor in range(3, max_range):
                if value % divisor != 0:
                    value += 10
                    break;
                elif divisor + 1 == max_range:
                    aux_end = 1
        else:
            value += 1

        if aux_end == 1:
            break

    return value

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

