line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()
letter = position[0].lower()
number = int(position[1])-1
abc = ["a", "b", "c"]
num = [1,2,3]
letter_index = abc.index(letter)
num_index = num.index(number)
map[letter_index][num_index]= "X"

print(f"{line1}\n{line2}\n{line3}")