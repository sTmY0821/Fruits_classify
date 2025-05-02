from usl import EpidemicView
if __name__ == '__main__':
    epidemic = EpidemicView()
    while True:
        epidemic.display_menu()
        epidemic.select_menu()