from modules import application

window = application.open_ui()

application.bind_events(window)

window.mainloop()
