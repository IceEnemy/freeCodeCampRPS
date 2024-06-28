def player(prev_play, opponent_history=[], orderOfMoves={}):
    # Append the opponent's last move to their history
    if prev_play in ['R', 'P', 'S']:
        opponent_history.append(prev_play)
    else:
        opponent_history.append('S')
    
    # Initialize the orderOfMoves dictionary for sequences of length 5
    if not orderOfMoves:
        for i in ['R', 'P', 'S']:
            for j in ['R', 'P', 'S']:
                for k in ['R', 'P', 'S']:
                    for l in ['R', 'P', 'S']:
                        for m in ['R', 'P', 'S']:
                            orderOfMoves[i + j + k + l + m] = 0
    
    # If history is too short, return 'S'
    if len(opponent_history) < 5:
        return 'S'
    
    # Increment the frequency of the last five moves
    markovAdd = ''.join(opponent_history[-5:])
    orderOfMoves[markovAdd] += 1
    
    # Determine the most likely next move
    beforeMove = ''.join(opponent_history[-4:])
    possibilities = {beforeMove + 'R': orderOfMoves[beforeMove + 'R'],
                     beforeMove + 'P': orderOfMoves[beforeMove + 'P'],
                     beforeMove + 'S': orderOfMoves[beforeMove + 'S']}
    
    # Extract the maximum value from possibilities
    prediction = max(possibilities, key=lambda k: possibilities[k])[-1]
    
    # Map the prediction to the move that beats it
    counter_move = {'R': 'P', 'P': 'S', 'S': 'R'}
    
    return counter_move[prediction]
