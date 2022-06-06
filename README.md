# Mathematical Research into Optimizing the Number of U-Bikes (City Bikes)
<p align="center">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/103551562/172152615-688734c6-d7f2-42cd-b1c0-6d087462c9f2.png">
</p>
  
## Introduction & Rationale
In Taiwan, specifically Taipei, U-Bike is a public city bicycle sharing service released in 2016 that offers a convenient way of travelling and is incredibly easy to use with the EasyCard. To me, it is the most cost-efficient, healthy, and enjoyable way to travel around the city without the hassle of carrying your bike around: simply park it and move on. As a declaration of its clear success, the government is introducing U-Bike 2.0, which inspired me to start to think about the numbers regarding how many people arrive or leave a U-Bike Station in a certain area. From this, I pondered how the government decides the number of U-Bikes to place at a certain area and the possible optimisation of the number of U-Bikes at U-Bike Stations. Apart from my interest in optimising, the rationale behind this is to attempt to reduce the amount of unnecessary spendings by the government and help direct resources to sectors that require it – an attempt to steer away from the concept of squandering. In order to execute this, I will be focusing on two discrete variables, how many of the U-Bikes leave and how many of the U-Bikes arrive. Through these discrete variables, I intend to then predict the probability discrete random variables occurring in a set time period through Poisson distribution and from there, attempt to optimise the initial number of U-Bikes and the number of available U-Bike slots that should be present at a U-Bike Station.

## Aim & Approach
In this investigation, I will be using Poisson distribution to estimate the probability of two discrete random variables the number of U-Bikes that arrive is A, while the number of U-Bikes that leave is L. The type of statistics will fall under discrete distribution as all of the data have discrete values. As mentioned in the previous section, we must address also address the conditions required to use Poisson distribution. Condition 2 may be assumed to be constant, but this will be addressed later in the Evaluation section. Condition 3 is met as the longer one spends recording the number of bikes that leave and arrive, the higher both of these numbers will be. Conditions 1 and 4 are different as the number of times both of these events can actually occur is limited by the number of bikes that are currently in the U-Bike Station, meaning that this investigation may not be independent. For example, let’s assume that a U-Bike Station has 10 slots and all of them are filled up with U-Bikes. The discrete variable, A, is limited and cannot increase as you cannot override the slots that are available in the U-Bike station. Therefore, I have decided that for the data collection (where I set out to a U-Bike station to record the number of bikes that leave and the number of bikes that arrive), even if the U-Bike station is full or empty, if someone is believed to be looking to park their U-Bike or is in need of one, I will record it down. This is because the question is surrounding the optimal number of U-Bikes and U-Bike slots at a U-Bike station and should therefore be able to extend beyond the number that is currently there. The type of sampling that will be used is Convenience Sampling. The reason for this is due to COVID-19, which prevents me from gaining a sample of U- Bike stations that covers a variety of spaces in Taipei. Furthermore, I realise that U-Bike does have an online U-Bike tracker, but as of when I recorded this data and performed my investigation, the online tracker was not accurate, which motivated me to collect the data on my own. Apart from the variables, A and L, we will also need two other discrete variables that will be optimised throughout this investigation: S = The number of available slots in the U-Bike station, which defines the maximum number of U-Bikes that can be placed in the station; B = The number of U-Bikes initially at the U-Bike station.
