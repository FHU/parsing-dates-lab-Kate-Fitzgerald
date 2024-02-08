#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    if month == "January":
        return "01"
    elif month == "February":
        return "02"
    elif month == "March":
        return "03"
    elif month == "April":
        return "04"
    elif month == "May":
        return "05"
    elif month == "June":
        return "06"
    elif month == "July":
        return "07"
    elif month == "August":
        return "08"
    elif month == "September":
        return "09"
    elif month == "October":
        return "10"
    elif month == "November":
        return "11"
    else:
        return "12"
    

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    user_string = user_string.replace(",", "")
    list = []
    for i in user_string.split(" "):
        list.append(i)
    parsed_month = parse_month(list[0])

    if int(list[1]) >= 10:
        return (f'{parsed_month}/{list[1]}/{list[2]}')
    else: return (f'{parsed_month}/0{list[1]}/{list[2]}')
    
#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    date = input()
    if date != -1:
        print(parse_date(date))
    else:
        print("nope")

#comment