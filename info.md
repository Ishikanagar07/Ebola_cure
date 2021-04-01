# Ebola_cure

An antidote has been developed for the ebola crisis. This antidote is conjuctive, i.e. If it is given to a person, then the person who is connected to this person will also be cured. Two people X and Y are connected if X and Y are adjacent or if there exists a person Z such that X and Z are connected and Z and Y are connected.

So, for every connected group of people we need one antidote. This antidotes strength must be equal to the highest infected person in the group.

Your task is to calculate the number of antidotes of different strengths needed.

Input
First line contains the size of the grid N.
Next contains the NxN grid.

Output
Print 4 integers, the number of antidotes required of strength 2, 3, 4 and 5.

Sample Input 0
5
0 0 0 1 5
1 1 0 1 1
3 1 0 0 0
1 1 0 1 1
4 4 0 3 1


Sample Output 0
0 1 1 1 
