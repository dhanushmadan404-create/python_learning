class theater:
    def __init__(self):
        self.movies=[]

    def add_movie(self,title,price,total_ticket):
        add={"title":title,"price":price,"total_ticket":total_ticket}
        self.movies.append(add)
        print(self.movies)


    def book_ticket(self,title,seat):
        for el in self.movies:
            if title==el["title"]:
                if el["total_ticket"]>seat:
                    el["total_ticket"]-=seat
                    print("ticket booked successfully")
                else:
                    print("not enough seats available")
            else:
                print("movie not fount")
    
    def cancel(self,name,seats):
        for el in self.movies:
            if name==el["title"]:
                if seats<=el["total_ticket"]:
                    el["total_ticket"]-=seats
                else:
                    print("false number")
            else:
                print("not found")


    def check(self,title):
       for el in self.movies:
           if title==el["title"]:
               return el       
           else:
               return "not found"
        
movie=theater()

movie.add_movie("master",180,100)
movie.book_ticket("master",5)
movie.cancel("master",3)
print(movie.check("master"))





