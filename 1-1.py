import numpy as np

# targets = [1e6, 6e7, 3.6e9, 8.64e10, 2.59e12, 3.15576e13, 3.15576e15]
targets = [3.15576e15]

x = 798160978351
# x = 71870856404
# x = 798160978351
for target in targets:
    while True:
        print(f"x = {x}, x*log2(x) = {x*np.log2(x)}, Y/target = {x*np.log2(x)/target}")
        if x * np.log2(x) - target > 0:
            if (x - 1) * np.log2(x - 1) - target <= 0:
                x = x - 1
                break
            else:
                x = int(x * 0.99)
        elif x * np.log2(x) / target < 0.99:
            x = int(x * target / x * np.log2(x) * 20)
        elif x * np.log2(x) / target < 0.999:
            x = int(x + target / x * np.log2(x) * 15)
        elif x * np.log2(x) / target < 0.9999:
            x = int(x + target / x * np.log2(x) * 10)
        elif x * np.log2(x) / target < 0.999999:
            x = int(x + target / x * np.log2(x) * 10)
        elif x * np.log2(x) / target < 0.99999999999:
            x = int(x + target / x * np.log2(x))
        else:
            x = x + 1
        # print(f"x = {x}, f(x) = {x*np.log2(x)}")

    print(f"last valid for {target} is {x}")
