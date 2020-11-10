The reason it was going so slow before is because you were checking if a neighbor had been visited before adding it to the queue. If that node was already in the queue but hadn't been hit yet there would be repeats. Instead check if it's already been visited as soon as you dequeue so it will immidiately deal with repeat nodes. 

