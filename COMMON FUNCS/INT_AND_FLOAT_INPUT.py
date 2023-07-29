def intinput(prompt: str):
    usr_in = "wrong"

    while True:
        usr_in = input(prompt + " ")
        try:
            int(usr_in)
            break

        except ValueError:
            print("NaN error")


def float_input(prompt: str):
    usr_in = "wrong"

    while True:
        usr_in = input(prompt + " ")
        try:
            return float(usr_in)

        except ValueError:
            print("NaN error")

