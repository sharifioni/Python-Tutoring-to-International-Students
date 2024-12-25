birthday1=int(input("Enter birthdate in 8 digit format for person1 YYYYMMDD: "))
birthday2=int(input("Enter birthdate in 8 digit format for person2 YYYYMMDD: "))

name1=input("Enter name for person 1: ")
name2=input("Enter name for person 2: ")

date1=birthday1%100
month1=(birthday1//100)%100
year1= birthday1//10000


date2=birthday2%100
month2=(birthday2//100)%100
year2= birthday2//10000


#f strings
print(f" {name1}'s date of birth is {month1}/{date1}/{year1}")
print(f" {name2}'s date of birth is {month2}/{date2}/{year2}")


if birthday1 == birthday2:
    print(f"{name1} and {name2} have same age")

elif birthday1<birthday2:
    print(f"{name1} is older than {name2}")

else:
    print(f"{name2} is older than {name1}")