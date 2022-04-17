# Markov Decision Model

In mathematics, a Markov decision process (MDP) is a discrete-time stochastic control process. It provides a 
mathematical framework for modeling decision-making in situations where outcomes are partly random and partly 
under the control of a decision maker. MDPs are useful for studying optimization problems solved 
via dynamic programming. MDPs were known at least as early as the 1950s; 
a core body of research on Markov decision processes resulted from Ronald Howard's 1960 book, Dynamic Programming 
and Markov Processes. They are used in many disciplines, including robotics, automatic control, economics 
and manufacturing. The name of MDPs comes from the Russian mathematician Andrey Markov 
as they are an extension of Markov chains.
___
### Problem Statement:

![alt text](https://github.com/luccianozz/Markov-Decision-Process-AI/blob/main/s.png?raw=true)

We need to decide what proportion of salmons to catch in a year in a specific area maximizing the longer term 
return. Each salmon generates a fixed amount of dollar. But if a large proportion of salmons are caught then the 
yield of the next year will be lower. We need to find the optimum portion of salmons to catch to maximize the return 
over a long time period.

Here we consider a simplified version of the above problem; whether to fish a certain portion of salmon or not. This 
problem can be expressed as an MDP as follows

States: The number of salmons available in that area in that year. For simplicity assume there are only four states; 
empty, low, medium, high. The four states are defined as follows

Empty -> no salmons are available; low -> available number of salmons are below a certain threshold t1; medium -> 
available number of salmons are between t1and t2; high -> available number of salmons are more than t2

Actions: For simplicity assumes there are only two actions; fish and not_to_fish. Fish means catching certain 
proportions of salmon. For the state empty the only possible action is not_to_fish.

Rewards: Fishing at certain state generates rewards, let’s assume the rewards of fishing at state low, medium and high 
are $5K, $50K and $100k respectively. If an action takes to empty state then the reward is very low -$200K as it 
require re-breeding new salmons which takes time and money.

State Transitions: Fishing in a state has higher a probability to move to a state with lower number of salmons. 
Similarly, not_to_fish action has higher probability to move to a state with higher number of salmons 
(excepts for the state high).