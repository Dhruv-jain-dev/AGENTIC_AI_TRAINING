"""
    Problem Statement:-Another Brick in the Wall

    customer - 13 bricks
    iteration 1     3
    john  1         
    jack  2
    iteration 2     6+3 = 9
    john  2
    jack  4
    iteration 3     9 + 3 + 1 => 13 
    john  3
    jack  6 -> 1

    Answer: Who placed the last brick and how many
    jack placed the last brick. qty: 1

"""

#CODE SPNIPPET:-

requirement=int(input('Enter Bricks:'))
brick_required=requirement
total_bricks=0
i=1
while(True):
    john=i
    jack=john*2

    if(john>brick_required):
        total_bricks+=brick_required
        # print('Total_bricks after Jack placed:',total_bricks)
        # brick_required-=john
        if(total_bricks==requirement):
            print('john cemented last brick. Qty: ',brick_required)
            break
    else:
        total_bricks+=john
        # print('Total_bricks after Jack placed:',total_bricks)
        brick_left=brick_required
        brick_required-=john
        if(brick_required==0):
            print('john cemented last brick. Qty: ',brick_left)
            break

    if(jack>brick_required):
        total_bricks+=brick_required
        # print('Total_bricks after Jack placed:',total_bricks)
        # brick_required-=jack
        if(total_bricks==requirement):
            print('jack cemented last brick. Qty: ',brick_required)
            break
    else:
        total_bricks+=jack
        # print('Total_bricks after Jack placed:',total_bricks)
        brick_left=brick_required
        brick_required-=jack
        if(brick_required==0):
            print('jack cemented last brick. Qty: ',brick_left)
            break 
    i+=1   
