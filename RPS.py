# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


def player(prev_play, opponent_history=[], my_history=[], play_order={}, results=[]):
    #first move---------
    if prev_play=='': 
  
      play_order["RR"]=0
      play_order["RP"]=0
      play_order["RS"]=0
      play_order["PR"]=0
      play_order["PP"]=0
      play_order["PS"]=0
      play_order["SR"]=0
      play_order["SP"]=0
      play_order["SS"]=0
      
      results.append(0)
      results.append(1)
      my_history.append("R")
      return "R"  # start with R (win or tie)
    #----------first move 

    opponent_history.append(prev_play)

    #who wins last
    win_dict={"R":"S", "P":"R", "S":"P"}
    if win_dict[my_history[-1]]==prev_play:
      results[0]+=1
    elif win_dict[prev_play]==my_history[-1]:
      results[1]+=1

    
    #----------------------------------
    #kris strategy beat? enought to mrugesh
    response = "A"
    best_response={"R":["S","P"], "P":["R","S"], "S":["P","R"]}
    response=best_response[my_history[-1]][0] 

    #--------------------------- last pair check
    if len(my_history)<2:
      my_history.append(response)
      return response
    elif len(my_history)==2:
      play_order["".join([my_history[0], my_history[1]])]+=1

    potential_pairs = [
        "".join([my_history[-1], "R"]),
        "".join([my_history[-1], "P"]),
        "".join([my_history[-1], "S"])
    ]
    sub_order = {}
    for p in potential_pairs:
      sub_order[p]=play_order[p]
    
    prediction = max(sub_order, key=sub_order.get)[-1:]
    #print("my pred",prediction)  # very good predict what abbey predict 
    
    # abbey 
    if prediction==response:
      response=best_response[my_history[-1]][1]
    
    #---------------------------quincy
    if float(results[0])/(results[0]+results[1])<0.7:
      choices = ["R", "R", "P", "P", "S"]
      his_move = choices[(len(my_history)+1) % len(choices)]
      response = [k for k in win_dict if win_dict[k]==his_move][0]

    # ------------------------------- RETURN
    play_order["".join([my_history[-1], response])]+=1
    my_history.append(response)
    return response




'''# GOOD STRATEGY WITH HUMAN--------------------------------
    ideal_response = {'P': 'R', 'S': 'P', 'R': 'S'}
    response="A"
    if ideal_response[my_history[-1]]==prev_play:  # player win
      response=prev_play 
    elif ideal_response[prev_play]==my_history[-1]:  # opponent win
      response=ideal_response[prev_play]
    else:
      response=my_history[-1]
    '''