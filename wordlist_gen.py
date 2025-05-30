#/usr/bin/env python3
import itertools

LEET_DICT = {
    'a': ['a', '@', '4'],
    'e': ['e', '3'],
    'i': ['i', '1', '!'],
    'o': ['o', '0'],
    's': ['s', '$', '5'],
    't': ['t', '7'],
    'l': ['l', '1']
}

def leet_variants(pwd):
        chars = [LEET_DICT.get(c.lower(),[c]) for c in pwd]
        variants = map(''.join, itertools.product(*chars))
        return list(set(variants))

def generate_passwords(info_dict):
        base_parts = [info_dict['name'], info_dict['age'], info_dict['pet'], info_dict['color']]
        base_parts = [part for part in base_parts if part]

        combos = []

        for r in range(1,len(base_parts) + 1):
                for combo in itertools.permutations(base_parts,r):
                        joined = ''.join(combo)
                        combos.append(joined)
                        combos.append(joined.capitalize())

        leet_passwords = set()

        for pwd in combos:
                leet_passwords.update(leet_variants(pwd))
        return leet_passwords

def write_to_file(password,filename):
        filename = filename + ".txt"
        with open(filename, "w", encoding = "utf-8") as f:
                for pwd in sorted(password):
                        f.write(pwd + "\n")
        print("passwords written to " + filename)


def main():
        print("password generator program....")
        name = input("enter your name: ")
        age = input("enter your age: ")
        pet = input("enter your pet's name: ")
        color = input("enter your favorite color: ")
        file = input("enter the name of the file to store the passwords: ")

        info_dict = {

        'name': name,
        'age': age,
        'pet': pet,
        'color': color

        }

        passwords = generate_passwords(info_dict)

        for pwd in sorted(passwords):
                print(pwd)

        write_to_file(passwords,file)


if __name__ == "__main__":
        main()
