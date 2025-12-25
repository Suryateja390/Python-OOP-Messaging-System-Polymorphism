class Messenger:
    def send_message(self):
        print("I am sending messages")

    def receive_message(self):
        print("I am receiving messages")

class FMessage(Messenger):
    def send_message(self):
        print("I am sending messages in Facebook")

    def receive_message(self):
        print("I am receiving messages in Facebook")

class WMessage(Messenger):
    def send_message(self):
        print("I am sending messages in WhatsApp")

    def receive_message(self):
        print("I am receiving messages in WhatsApp")

class IMessage(Messenger):
    def send_message(self):
        print("I am sending messages in Instagram")

    def receive_message(self):
        print("I am receiving messages in Instagram")

    def live_location(self):
        print("Sharing live location on Instagram")

class Display:
    def show(self, ref):
        ref.send_message()
        ref.receive_message()

        if isinstance(ref, IMessage):
            ref.live_location()


f = FMessage()
w = WMessage()
i = IMessage()

d = Display()

d.show(i)
print()
d.show(f)
print()
d.show(w)
