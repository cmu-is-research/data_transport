from challenge2_json import *

#Note: The nth attacker requested in not 0 indexed. Hence 1 means the first
#attacker in the list or the 0th element in the list.
test1 = JSON("trials.json")
test1.getCSV("attackers", 1, "attacker1_info.csv")
test1.getCSV("attackers", 2, "attacker2_info.csv")
test1.getCSV("attackers", 3, "attacker3_info.csv")

#Raises an error if calling for an attacker that doesn't exist
#test1.getCSV("attackers", 51, "attacker51_info.csv")



