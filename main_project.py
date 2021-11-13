def sort_str_list(input: list) -> list:
    # str_list.sort(key=int)
    # return str_list

    #########
    # bubble sort version?

    smallest_value = input[0]
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(input)):
            if len(input[i]) == (len(input[i - 1]) and (input[i]) < (input[i - 1])) or (
                    len(input[i]) < len(input[i - 1])):
                temp = input[i]
                input[i] = input[i - 1]
                input[i - 1] = temp
                sorted = False

            if len(input[i]) < len(input[i - 1]):
                temp = input[i]
                input[i] = input[i - 1]
                input[i - 1] = temp
                sorted = False
    return input

def current_is_less_than_previous(current: str, previous: str):
    if len(current) < len(previous):
        return True
    elif len(current) > len(previous):
        return False
    else:
        return current < previous


        # temp = input[i]
        # input[i] = input[i - 1]
        # input[i - 1] = temp
        # sorted = False


if __name__ == "__main__":
    pass
