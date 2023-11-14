import tkinter as tk
from tkinter import ttk


# Создаём базовый класс, из которого будем запускать другие окна
class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Название основного окна
        self.wm_title('БАНК')
        # Создание фрейма-контейнера
        container = tk.Frame(self, height=400, width=600)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # Создание словаря фреймов
        self.frames = {}
        # Добавление компонентов в словарь
        for F in (MainPage, SidePage, CompletionScreen):
            frame = F(container, self)
            # Класс windows действует как корневое окно для фреймов
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        # Метод переключения фреймов
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # Поднимаем фрейм вверх
        frame.tkraise()


# Создание классов для фреймов
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Главное меню')
        label.pack(padx=10, pady=10)
        switch_window_button = tk.Button(self, text='Go SidePage',
                                         command=lambda: controller.show_frame(SidePage))
        switch_window_button.pack(side='bottom', fill=tk.X)


class SidePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the Side Page")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Completion Screen",
            command=lambda: controller.show_frame(CompletionScreen),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class CompletionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Completion Screen, we did it!")
        label.pack(padx=10, pady=10)
        switch_window_button = ttk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(MainPage)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


if __name__ == '__main__':
    testObj = windows()
    testObj.mainloop()
