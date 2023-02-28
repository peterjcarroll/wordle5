# wordle5
Five words to reveal most or all of the letters in Wordle, Quordle, and similar games.

## TL;DR
Type in the five words from one of the lines below into Wordle, Quordle, and similar games:
```
waltz bench fjord skimp gusty
stack whelp fjord vying thumb
angst whelp fjord mucky blitz
```

## What is this?
It occurred to me it might be possible to find five words with no overlapping letters between them to enter into a Wordle-style game, which would attempt 25 out of the 26 letters of the alphabet. This means that for your final guess, you probably have all the letters in the answers revealed, you just need to put them in order.

I started with the list of possible Wordle answers, and got rid of words with duplicated letters and multiple vowels. That list is in wordle_answers_reduced.txt. 

Next I attempted to find the five words that combined have no letters duplicated. No such luck, but I found many sets of 4 words.

So I took those sets of 4 words, and tried to find a fifth with only one letter duplicated. No luck. But with 2 letters duplicated, I had the 3 sets of words that fit.

The reduce.py script is the script I wrote to find these results.
