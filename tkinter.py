import tkinter as tk
import requests


class Id:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('600x500')
        self.window.title('search')

        self.input = tk.Entry(self.window)
        self.input.pack(pady=10)

        self.button = tk.Button(
            self.window,
            text='Search',
            command=self.on_submit
        )
        self.button.pack(pady=5)

        self.label = tk.Label(self.window, text='', wraplength=560, justify='left')
        self.label.pack(pady=10)

    def on_submit(self):
        user_input = self.input.get().strip()
        if not user_input.isdigit():
            self.label['text'] = 'Please enter numbers only.'
            return
        self.id_requests(user_input)

    def id_requests(self, user_input):
        url = f'https://jsonplaceholder.typicode.com/users/{user_input}'
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            self.label['text'] = (
                f"Name: {data.get('name')}\n"
                f"Email: {data.get('email')}\n"
                f"City: {data.get('address', {}).get('city')}"
            )
        else:
            self.label['text'] = f'User {user_input} not found.'

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    ids = Id()
    ids.run()


 
