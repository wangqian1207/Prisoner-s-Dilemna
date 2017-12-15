team_name = 'Hamster Peteman' # Only 10 chars displayed.
strategy_name = 'Cheesy Torto :)'
strategy_description = 'Artificial Intelligence'
last_result = bool(false)
    
def move(my_history, their_history, my_score, their_score):
    agent1 = test_score(my_score, their_score)
    agent2 = test_history(my_history, their_history)
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    if agent1 and agent2:
        return 'c'    
    else:
        return 'b'    
def test_score(my, op):
    if my >= (op+250):
        return bool('true')
        last_result = true
    elif my < op:
        return false
        last_result = false
    else:
        return last_result
        
def test_history(my, op):
    length = len(op)
    
    