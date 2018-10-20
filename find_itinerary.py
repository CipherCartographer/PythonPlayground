'''
Given a list of tickets, find itinerary in order using the given list.

Example:

Input:
"Chennai" -> "Banglore"
"Bombay" -> "Delhi"
"Goa"    -> "Chennai"
"Delhi"  -> "Goa"

Output: 
Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Banglore,
It may be assumed that the input list of tickets is not cyclic and there is one ticket from every city except final destination.
'''

def findItinerary(ticket_map):
    if ticket_map is None:
        return None
    
    reverse_map = {}
    # Reverse the ticket map
    for key in ticket_map:
        reverse_map[ticket_map[key]] = key

    start = None
    for key in ticket_map.keys():
        if key not in reverse_map.keys():
            start = key
    to = ticket_map[start]
    print "Final Itinerary: "
    print start,
    while to is not None:
        print "->" + to,
        start = to
        if to in ticket_map:
            to = ticket_map[to]
        else: 
            to = None
    

if __name__ == "__main__":
    ticket_map = {}
    ticket_map["Chennai"] = "Banglore"
    ticket_map["Bombay"] = "Delhi"
    ticket_map["Goa"] = "Chennai"
    ticket_map["Delhi"] = "Goa"

    print "Ticket map : ",
    print ticket_map

    findItinerary(ticket_map)
