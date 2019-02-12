
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])
print(monthConversions.get("Nov"))
print(monthConversions.get("Nom","Not a Valid Key"))
print(monthConversions.keys())

# temp = monthConversions.pop("Non")

print(monthConversions.pop("Nov"))

