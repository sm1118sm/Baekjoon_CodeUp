p, m = map(int, input().split())

rooms = []  

for _ in range(p):
    lv, name = input().split()
    if len(rooms) == 0:     
        rooms.append([[int(lv), name]])    
        
    else:    
        for room in rooms:      
            first_lv = room[0][0]     
            if len(room) < m and first_lv - 10 <= int(lv) <= first_lv + 10:
                room.append([lv, name])  
                break     
                
        else:     
            rooms.append([[int(lv), name]])     
    
for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    room.sort(key=lambda x:x[1]) 
    
    for player in room:
        print(player[0], player[1])