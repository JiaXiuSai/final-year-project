# https://github.com/dropbox/zxcvbn
from zxcvbn import zxcvbn
import os
password_corpus = ".\\Password Corpus"
pwms = os.listdir(password_corpus)

for current_pwm in pwms:
    with open(password_corpus + current_pwm) as input_f, open(
        "zxcvbn_" + current_pwm.replace(".txt", "") + ".csv", "w", newline=""
    ) as output_f:
        for line in input_f:
            if line:
                result = zxcvbn(line[:-1])
                output_f.write(
                    f"\"{result['password']}\", {result['score']}, {result['guesses']}, {result['guesses_log10']}, {result['sequence'][0]['pattern']}, {result['sequence'][0]['i']}, {result['sequence'][0]['j']}, {result['sequence'][0]['guesses']}, {result['sequence'][0]['guesses_log10']}, {result['crack_times_seconds']['online_throttling_100_per_hour']}, {result['crack_times_seconds']['online_no_throttling_10_per_second']}, {result['crack_times_seconds']['offline_slow_hashing_1e4_per_second']}, {result['crack_times_seconds']['offline_fast_hashing_1e10_per_second']}, {result['crack_times_display']['online_throttling_100_per_hour']}, {result['crack_times_display']['online_no_throttling_10_per_second']}, {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}, {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}, {result['feedback']['warning']}, {'; '.join(str(x) for x in result['feedback']['suggestions'])}\n"
                )
    print(current_pwm, "done")
