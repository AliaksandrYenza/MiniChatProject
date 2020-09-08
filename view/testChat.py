import time


class Messenger:

    db = []
    req_count = 0

    def send_message(self, name, text):
        timestamp = time.asctime()
        self.db.append({
            'name': name,
            'text': text,
            'timestamp': timestamp
        })

    def get_message(self):
        return self.db

    def get_new_message(self):
        new_messages = self.db[self.req_count:]
        self.req_count += len(new_messages)
        return new_messages


messanger = Messenger()
messanger.send_message('Jack', 'abc')
messanger.send_message('Jack', 'abcd')

print('All:', messanger.get_message())
print('New:', messanger.get_new_message())
print()

messanger.send_message('Black', 'Hello 1 !')
print('All:', messanger.get_message())
print('New:', messanger.get_new_message())
print()

messanger.send_message('Black', 'Hello 2 !')
print('All:', messanger.get_message())
print('New:', messanger.get_new_message())
print()

messanger.send_message('Black', 'Hello 3 !')
print('All:', messanger.get_message())
print('New:', messanger.get_new_message())
print()