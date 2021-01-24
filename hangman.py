# step 1
import random
stage_blood =[
    '''♥♥♥♥♥''',
    '''♥♥♥♥ ''',
    '''♥♥♥  ''',
    '''♥♥   ''',
    '''♥    ''',
]
chance_lives = 0
print(stage_blood[chance_lives])
#print(stage_blood)
word_list = ["google", "apple", "tesla","nike"]
select_w = random.choice(word_list)

select_num = len(select_w)

# step 2 : try to replace [] with "__"
blank = []
for _ in range(0, select_num):
    blank += "_"
print(blank)


# step 3 : if have correct number replace "_" with letter
end_game = False
while end_game == False:
    guess_w = input("Guess a letter: ").lower()
    for position in range(select_num):
        x = select_w[position]
        if x == guess_w:
            blank[position] = x
    if guess_w not in select_w:
        chance_lives += 1
        
        if chance_lives == 5:
            end_game == True
            print("You lose!!!")
            quit()
        print(stage_blood[chance_lives])
        
    print(blank)
    if "_" not in blank:
        end_game == True
        print("You win!!!")
        quit()
