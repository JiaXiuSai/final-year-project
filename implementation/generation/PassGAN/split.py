# Split 
import os
import random

input_dir = '.\data'
output_dir = '.\data\\train_test'
random.seed(1)
pwms = ['firefox']

for pwm in pwms:
    with open(os.path.join(input_dir, pwm+'.txt')) as f:
        lines = f.readlines()
        random.shuffle(lines)
        lines = lines[:100000]
        if not os.path.exists(os.path.join(output_dir, pwm)):
            os.makedirs(os.path.join(output_dir, pwm))
        for x in range(5):
            with open(os.path.join(output_dir, pwm, str(x)+'_train.txt'), 'w+') as trainf, open(os.path.join(output_dir, pwm, str(x)+'_test.txt'), 'w+') as testf:
                for i, line in enumerate(lines):
                    if i >= x*20000 and i < (x+1)*20000:
                        testf.write(line)
                    else:
                        trainf.write(line)
                    

