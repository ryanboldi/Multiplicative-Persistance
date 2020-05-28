# Multiplicative Persistence
 A genetic algorithm to find a number with very large multiplicative persistence: (how long it takes to boil down to a single digit)
 * 123 -> 1x2x3 = 6 (so this has MP of 1)
 *  6788 -> 6x7x8x8 = 2688 -> 2x6x8x8 = 768 -> 7x6x8 = 336 -> 3x3x6 = 54 -> 5x4 = 20 -> 2x0 = 0 (that's 6) 

the official record for the smallest number with mulptiplicative persistence of 11 is:
**277777788888899**


I let my genetic algorithm search through all possible 15 digit numbers to see how close I could get to the real record.

This is the log after training for 50 generations. The Algorithm discorvers a solution with MP of 10 within one generation. 
~~~
gen: 0 -> best: 4 || answer: 111122344688889
gen: 1 -> best: 10 || answer: 122333344666778
gen: 2 -> best: 9 || answer: 223344467778888
gen: 3 -> best: 10 || answer: 113333344667788
gen: 4 -> best: 10 || answer: 113333444666778
gen: 5 -> best: 10 || answer: 122333344666778
gen: 6 -> best: 10 || answer: 113333444666778
gen: 7 -> best: 10 || answer: 112333446666778
gen: 8 -> best: 8 || answer: 111122234677789
gen: 9 -> best: 9 || answer: 111222233446669
gen: 10 -> best: 10 || answer: 111234444778999
gen: 11 -> best: 9 || answer: 111233477777899
gen: 12 -> best: 10 || answer: 112223346778899
gen: 13 -> best: 10 || answer: 112222446778999
gen: 14 -> best: 10 || answer: 112223346778899
gen: 15 -> best: 10 || answer: 112223337788899
gen: 16 -> best: 10 || answer: 112223346778899
gen: 17 -> best: 10 || answer: 112233336778889
gen: 18 -> best: 10 || answer: 112223346778899
gen: 19 -> best: 10 || answer: 112223346778899
gen: 20 -> best: 10 || answer: 112233336778889
gen: 21 -> best: 10 || answer: 112223446677899
gen: 22 -> best: 10 || answer: 112223346778899
gen: 23 -> best: 10 || answer: 112223346778899
gen: 24 -> best: 10 || answer: 111223466778899
gen: 25 -> best: 10 || answer: 112223446677899
gen: 26 -> best: 10 || answer: 112223446677899
gen: 27 -> best: 10 || answer: 111223367788899
gen: 28 -> best: 10 || answer: 112233444677899
gen: 29 -> best: 10 || answer: 111223466778899
gen: 30 -> best: 10 || answer: 122333334477889
gen: 31 -> best: 10 || answer: 111223466778899
gen: 32 -> best: 10 || answer: 111223466778899
gen: 33 -> best: 10 || answer: 111233347788899
gen: 34 -> best: 10 || answer: 112223346778899
gen: 35 -> best: 10 || answer: 111233347788899
gen: 36 -> best: 10 || answer: 111223466778899
gen: 37 -> best: 10 || answer: 112233346677889
gen: 38 -> best: 10 || answer: 111223466778899
gen: 39 -> best: 10 || answer: 112233346677889
gen: 40 -> best: 10 || answer: 112233336778889
gen: 41 -> best: 9 || answer: 111112233468899
gen: 42 -> best: 10 || answer: 111233446778899
gen: 43 -> best: 9 || answer: 111122333446689
gen: 44 -> best: 10 || answer: 112223346778899
gen: 45 -> best: 10 || answer: 112223346778899
gen: 46 -> best: 10 || answer: 111233446778899
gen: 47 -> best: 10 || answer: 222333333467788
gen: 48 -> best: 9 || answer: 111122333466668
gen: 49 -> best: 10 || answer: 112223337788899
122333344666778
10
~~~

As we can see, the algorithm quickly learns not to have 5s and 2s together, as they multiply to make 10, (which has a 0 and thus -> instant loss)