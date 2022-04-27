import os

pwm = "pretrained3"
if pwm == "pretrained":
    directory = f".\\output\\{pwm}\\samples"
    with open(f".\data\\train.txt", "r") as testf:
        testpw = set(testf.read().splitlines())
        for filename in os.listdir(directory):
            with open(os.path.join(directory, filename), "r") as genf:
                genpw = set(genf.read().splitlines())
                print(filename, list(genpw.intersection(testpw)))
        with open(f".\\output\\{pwm}\\generated.txt", "r") as genf:
            genpw = set(genf.read().splitlines())
            print(f"generated.txt", list(genpw.intersection(testpw)))
else:
    for i in range(5):
        directory = f".\\output\\{pwm}\\{i}\\samples"
        with open(f".\data\\train_test\\train\\{i}_test.txt", "r") as testf:
            testpw = set(testf.read().splitlines())
            for filename in os.listdir(directory):
                with open(os.path.join(directory, filename), "r") as genf:
                    genpw = set(genf.read().splitlines())
                    print(filename, list(genpw.intersection(testpw)))
            with open(f".\\output\\{pwm}\\{i}_generated.txt", "r") as genf:
                genpw = set(genf.read().splitlines())
                print(f"{len(genpw.intersection(testpw))} {i}_generated.txt", list(genpw.intersection(testpw)))