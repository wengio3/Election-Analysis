counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties")    
if "Arapahoe" in counties or "EL Paso" in counties:
    print ("Arapahoe and El paso in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
for county in counties:
    print(county)
numbers = [0, 1, 2, 3, 4, 5]
for num in numbers:
    print(num)
counties_dict = {}
counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432437}
for county in counties_dict:
    print(county)
    for county in counties_dict.keys():
        print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county, voters in counties_dict.items():
    print(county, voters)
voting_data = {}
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
for county_dict in voting_data:
    print(county_dict['county'])

