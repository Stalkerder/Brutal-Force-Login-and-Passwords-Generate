import itertools
import random
import string
import time
from tqdm import tqdm

def generate_rand_pw(char_length):
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*()'
    out_str = ""
    while len(out_str) < char_length:
        out_str += random.choice(alphabet)
    return out_str

def brute_force(password):
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*()'
    estimated_time = int((len(alphabet) ** len(password)) / len(alphabet))
    password_tuple = tuple(password)
    char_list = [[x for x in alphabet]] * len(password)
    for combination in tqdm(itertools.product(*char_list), total=estimated_time):
        if combination == password_tuple:
            return "".join(combination)

if __name__ == "__main__":
    start_time = int(time.time())
    rand_pw = generate_rand_pw(6)
    print(f"Attempting to brute force {rand_pw}")
    result = brute_force(rand_pw)
    end_time = int(time.time())
    print(f"Brute forced password {result} in {end_time - start_time} seconds")
