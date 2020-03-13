#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for i in range(len(tickets)):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    for i in range(len(route)):
        if i != 0:
            route[i] = hash_table_retrieve(hashtable, route[i-1])
        else:
            route[i] = hash_table_retrieve(hashtable, "NONE")

    route.pop()

    return route



    ## HT = [{source: destination}, {source: destination} ...]
    ## loop through destinations, find the source
    ## source is one left of destination
    ## the destination NONE is at the end


