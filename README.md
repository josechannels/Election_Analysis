# Election_Analysis

## Project Overview
A Colorado Board of Elections employee asked for help in conducting an audit of a recent local congressional elections.
Specifically, he asked for the following tasks to be completed:

1. Calculate the total number of votes cast.
2. Get a complete list of all the counties where a vote was cast.
3. Calculate the total number of votes cast per county.
4. Calculate the percentage of the total votes cast in each county.
5. Get a complete list of candidates who received votes.
6. Calculate the total number of votes each candidate received.
7. Calculate the percentage of votes each candidate won.
8. Determine the winner of the elections based on popular vote.

## Resources
Data Source: election_results.csv
Software: Python 3.7.6, Visual Studio Code 1.53.2

## Summary

The analysis of the election show that:
- There were 369,711 total votes cast in the election:
  - In Jefferson county, a total of 38,855 votes were cast, accounting for 10.5% of the total vote.
  - In Denver county, a total of 306,055 votes were cast, accounting for 82.8% of the total vote.
  - In Arapahoe county, a total of 24,801 votes were cast accounting for 6.7% of the total vote.
- The county where the most votes were cast was Denver.
- The candidates were
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes
  - Diana Gagette received 73.8% of the vote and 272,892 votes
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes.  

## Election Audit Summary

We succeded in conducting the audit and provided all the metrics requested by writting a generalized script that could easily be adapted to audit any another election.

This could be done by first altering the name of the file containing the ballot results (e.g. "election_results.csv") in the following line of code: 
`file_to_load = os.path.join("Resources", "election_results.csv")`. 

Secondly the code could be adapted to analyze election results from files that contained the "county" and the "candidate name" on different columns than those observed in this file: column #1 for county, column#2 for candidate name.  This could be done by changing the numbers in the square brackets to match the column number where the candidate name and county names are found the following lines of code:

` # Get the candidate name from each row.`
  `candidate_name = row[2]`

  `# 3: Extract the county name from each row.`
  `county_name = row[1]`      







