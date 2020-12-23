numbers = [0, 3, 6]
numbers = [1, 3, 2]
numbers = [11, 18, 0, 20, 1, 7, 16]
spoken_numbers = []
turn = 1
last_num = 0
while True:
    if turn <= len(numbers):
        num = numbers[turn - 1]
        spoken_numbers.append(num)
    else:
        # done all start nums
        if spoken_numbers.count(last_num) == 1:
            num = 0
            spoken_numbers.append(num)
        else:
            last_spoken_turn = None
            last_last_spoken_turn = None
            for index, spoken_number in enumerate(reversed(spoken_numbers)):
                if spoken_number == last_num and not last_spoken_turn:
                    last_spoken_turn = turn - (index + 1)
                    continue
                if last_spoken_turn and spoken_number == last_num:
                    last_last_spoken_turn = turn - (index + 1)
                    break
            num = last_spoken_turn - last_last_spoken_turn
            spoken_numbers.append(num)

    print(f"turn: {turn}: {num}")
    last_num = num
    if turn >= 2020:
        break
    turn += 1