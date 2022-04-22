#kata: Tennis Score

To try all these tools on the field, I executed the tennis kata. 

It consists of implementing the scoring rules of a tennis set:

- Each player can have either of these points in one game, described as 0-15-30-40. Each time a player scores, it advances of one position in the scale.

- A player at 40 who scores wins the set. Unless...

- If both players are at 40, we are in a *deuce*. 

- If the game is in deuce, the next scoring player will gain an *advantage*. Then if the player in advantage scores he wins, while if the player not in advantage scores they are back at deuce.