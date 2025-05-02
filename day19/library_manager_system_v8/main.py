from day19.library_manager_system_v8.usl import LibraryView

if __name__ == '__main__':
    view = LibraryView()
    while True:
        view.display_menu()
        view.select_menu()