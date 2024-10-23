#it is used to able to assign a meaning to a particular element in the program such as abbreviations
month = { #a dictionary for the abbreviations of the months of the year
	"Jan" and "jan": "January",
	"Feb" and "feb": "February",
	"Mar" and "mar": "March",
	"Apr" and "apr": "April",
	"May" and "may": "May",
	"Jun" and "jun": "June",
	"Jul" and "jul": "July",
	"Aug" and "aug": "August",
	"Sep" and "sep": "September",
	"Oct" and "oct": "October",
	"Nov" and "nov": "November",
	"Dec" and "dec": "December",
}

print("This is a program to change the abbreviation of a month to the full name of the month.")
abbr = input("Enter the abbreviation: ")
if abbr in month: #to make the program cross-check the dictionary for the month
    print(month[abbr]) #to get the exact name assigned to Jan
else: #if the abbr provided by the user is not among the assigned
    print(abbr + " is not a month abbreviation.")