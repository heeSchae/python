def all_time_record(opponent):
    
    record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    wins = 0
    losses = 0
    ties = 0
    
    for line in record_file:
        item = line.split(",")
        
        if item[1] == opponent:
            
            if int(item[3]) > int(item[4]):
                wins += 1
                    
            elif int(item[3]) == int(item[4]):
                ties += 1
                    
            else:
                losses += 1
                    
    
    record_file.close()
    return str(wins) + "-" + str(losses) + "-" + str(ties)    
