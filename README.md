# round-robin-pairings

The RoundRobin class will return a list of tuples (pairs of names) to represent distinct and unique teams when given a list of names. 

The parameter for the constructor will be a list of names. 

This class is perfect for these purposes:
 - Say you are organizing an academic conference, and you want to schedule each attendee to have a one-on-one meeting with each other attendee.
 - Or you are organizing a sports tournament, and you need to schedule games such that each participant plays each other participant exactly once.
 - Or you are teaching a writing class, and you'd like each student to review each other student's draft exactly once during the semester.
 
If you have N items in your list, this means there will be N - 1 rounds, and each round will have N / 2 matches.

The method, generate_round, will produce a distinct and unique list of tuples for each time the generate_round method is called. This method will return a message letting you know when you have exhausted the maximum number of unique team pairings.

Please note: if there is an odd number of names in your list, then the program will append 'bye' as a placeholder to achieve an even number of names in the list.
