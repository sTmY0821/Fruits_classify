from dtl import RestaurantView

if __name__ == '__main__':
    view = RestaurantView()
    while True:
        view.display_menu()
        view.select_menu()