choice =int(input("Grasz w [0]kamien [1]papier [2]nozyce\n"))
import random
r1 = random.randint(0, 2)
if r1==0:
     r2='''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)'''
elif r1==1:
    r2 = '''
            _______
    ---'   _________)
          (__________)
          (_________)
          (________)
    ---.__(_______)'''
elif r1==2:
    r2 = '''
             _______
    ---'   __________)
          (__________)
          (_____)
          (____)
    ---.__(___)'''

if choice == 0:
     ch2='''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)'''
elif choice == 1:
    ch2 = '''
           _______
    ---'   __________)
          (__________)
          (_________)
          (________)
    ---.__(_______)'''
elif choice == 2:
    ch2 = '''
           _______
    ---'   __________)
          (__________)
          (_____)
          (____)
    ---.__(___)'''


if  choice==r1:
    print(f"{ch2} {r2} + remis")
elif (choice==0 and r1==1) or (choice==1 and r1==2) or (choice==2 and r1==0):
    print(f"{ch2}\n Computer choice \n{r2}\n You loose")
elif (r1==0 and choice==1) or (r1==1 and choice==2) or (r1==2 and choice==0):
    print(f"{ch2}\n Computer choice \n{r2}\n You win")
elif choice>2:
    print("podales zly numer")

