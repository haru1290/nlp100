from ex60 import get_option


def main():
    args = get_option()

    with open(args.test1_add, 'r') as f:
        sem_cnt = 0
        sem_cor = 0
        syn_cnt = 0
        syn_cor = 0
        for r in f:
            r = r.split()
            if not r[0].startswith('gram'):
                sem_cnt += 1
                if r[4] == r[5]:
                    sem_cor += 1
            else:
                syn_cnt += 1
                if r[4] == r[5]:
                    syn_cor += 1

        print(f"意味的アナロジーの正解率：{sem_cor/sem_cnt:.3f}")
        print(f"文法的アナロジーの正解率：{syn_cor/syn_cnt:.3f}")


if __name__ == '__main__':
    main()
