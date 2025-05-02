from usl import EpidemicView
if __name__ == '__main__':
    view = EpidemicView()
    while True:
        view.display_menu()
        view.select_menu()