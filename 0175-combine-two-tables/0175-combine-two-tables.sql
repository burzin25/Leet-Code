# Write your MySQL query statement below

# Explanation :
# As only a Left join will satisfy the requirement of delivering all values from the left table   and considering null as values for the missing data when used in conjunction with another       table, its use is crucial here.

SELECT Person.firstName, Person.lastName, Address.city, Address.state
FROM Person
LEFT JOIN Address ON Person.personId = Address.personId

