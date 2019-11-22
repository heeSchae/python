from datetime import date


#Write your code here!
def binary_search_year(searchList, year):
    searchList.sort()
    if 1 <= len(searchList) -1:
        mid = len(searchList)//2
        if searchList[mid].year == year:
            return True
        elif searchList[mid].year > year:
            return binary_search_year(searchList[:mid], year)
        else:
            return binary_search_year(searchList[mid:], year)
    else:
        return False
            
    
   


#If your function works correctly, this will originally
#print: True, then False
listOfDates = [date(2016, 11, 26), date(2014, 11, 29), 
               date(2008, 11, 29), date(2000, 11, 25), 
               date(1999, 11, 27), date(1998, 11, 28), 
               date(1990, 12, 1), date(1989, 12, 2), 
               date(1985, 11, 30)]

print(binary_search_year(listOfDates, 2016))
print(binary_search_year(listOfDates, 2007))
