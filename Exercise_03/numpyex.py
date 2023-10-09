import numpy as np

random_floats = np.random.random(10)
mean = np.mean(random_floats)
median = np.median(random_floats)
std_dev = np.std(random_floats)

print("Random Numbers:", random_floats)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
