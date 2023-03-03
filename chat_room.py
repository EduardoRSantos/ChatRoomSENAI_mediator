from person import Person

class ChatRoom:
    def __init__(self) -> None:
        self.name = "room"
        self.peoples: list[Person] = []

    def join(self, person: Person):
        
        person.chat_room = self
        self.broadcast(self.name,person.name + " joins the chat")
        self.peoples.append(person)

    def broadcast(self, source: str, message: str) -> None:
            
            for pessoa in self.peoples:
                if pessoa.name != source:
                    pessoa.receive(source, message)

    def message(self, source, destination: str, message: str) -> None:
            
            for pessoa in self.peoples:
                 if pessoa.name == destination:
                      pessoa.receive(source, message)