
from Tkinter import *
from ttk import *
import sf_health_inspection_manager

root_widget = Tk()                          # creates a widget window which will hold all other widgets.
cmb_box_years = Combobox()
lst_box_results = Listbox(width=40)


def cmb_box_select(event):
    selected_business = cmb_box_business.get()     # returns the text that is selected in the combobox
    inspection_info_list = sf_health_inspection_manager.get_inspection_by_business(selected_business)
    business_names = []
    global lst_box_results

    lst_box_results.delete(0, END)          # clears the combobox each time

    for info in inspection_info_list:
        if not business_names:
            business_names.append(info.business_name)
            lst_box_results.insert(END, info.business_address, info.inspection_date, info.inspection_score, info.violation_description, info.risk_category)   # fills in the combobox entries with data

        else:
            if info.business_name not in business__names:
                business_names.append(info.business_name)
                lst_box_results.insert(END, info.business_address, info.inspection_date, info.inspection_score, info.violation_description, info.risk_category)


def main():
    root_widget.geometry("500x500")                 # sets the size of the window
    root_widget.title("Search Health Inspection Information by Business")   # sets the title of the window
    root_widget.configure(background = "teal")

    lbl_hello = Label(root_widget, text="Choose a business.")
    lbl_hello.pack()                                # shows the label

    sf_health_inspection_manager.load_inspection_data()            # get data from movie_info_manager

    global cmb_box_years
    cmb_box_business_name = Combobox(values=sf_health_inspection_manager.get_business_name_list())
    cmb_box_business_name.bind("<<ComboboxSelected>>", cmb_box_select)  # event that calls cmb_box_select when triggered
    cmb_box_business_name.current(0)
    cmb_box_business_name.pack()                            # shows the combobox

    lst_box_results.configure(background = "light grey")
    lst_box_results.pack()                          # shows the listbox

    root_widget.mainloop()                          # runs the widget window


if __name__ == '__main__':
    main()