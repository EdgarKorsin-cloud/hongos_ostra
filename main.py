import tkinter as tk
from tkinter import messagebox
from inventory_manager import Inventory_Manager, Siembra
from schedule_manager import Scheduler

manager = Inventory_Manager()
scheduler = Scheduler()

def calculate_all_dates(siembra_id, start_date, label_to_update):
    colonized = scheduler.incubation_end(start_date)
    harvest = scheduler.fructification(colonized)

    manager.update_dates(siembra_id, colonized, harvest)
    label_to_update.config(text=f"Fin incubación: {colonized} | Fructificación: {harvest}")

    messagebox.showinfo("Éxito",
                        f"Fechas calculadas y guardadas:\n"
                        f"Incubación fin: {colonized}\nFructificación: {harvest}")

def open_window2():
    window2 = tk.Tk()
    window2.grid_rowconfigure(0, weight=1)
    window2.grid_columnconfigure(0, weight=1)
    window2.title("Lista de siembras")

    siembras = manager.session.query(Siembra).all()

    if not siembras:
        tk.Label(window2, text="No hay siembras registradas.").grid(row=0, column=0)

    for index, item in enumerate(siembras, start=1):
        cultivo = item.product_name
        fecha = item.incubation_start_date
        tipo = item.product_type
        fin_inc = item.incubation_end_date or "Pendiente"
        fruct = item.fructification_start or "Pendiente"
        item_id = item.id

        info_text = f"{index}. {cultivo} | Inicio: {fecha} | Tipo: {tipo}"
        info_label = tk.Label(window2, text=info_text)
        info_label.grid(row=index, column=0, padx=10, pady=5, sticky="w")
        dates_text = f"Fin incubación: {fin_inc} | Fructificación: {fruct}"
        dates_label = tk.Label(window2, text=dates_text, fg="green")
        dates_label.grid(row=index, column=1, padx=10, pady=5, sticky="w")

        if not item.incubation_end_date or not item.fructification_start:
            calculate_all_dates(item_id, fecha, dates_label)



    window2.mainloop()

def show_supplies():
    inventory = manager.get_supplies()
    antiplagas_label.config(text=f"Anti-plagas: {inventory['Anti-plagas']}")
    antihongos_label.config(text=f"Anti-hongos: {inventory['Anti-hongos']}")
    booster_label.config(text=f"Booster: {inventory['Booster']}")
    atrapamoscas_label.config(text=f"Atrapa-moscas: {inventory['Atrapa-moscas']}")
    sustratos_label.config(text=f"Sustrato: {inventory['Sustrato']}")
    micelio_label.config(text=f"Micelio: {inventory['Micelio']}")

def update_inventory():
    current_inventory = manager.get_supplies()

    new_value_antiplagas_entry = tk.Entry(window)
    new_value_antiplagas_entry.grid(row=6, column=1)
    new_value_antiplagas_entry.insert(0, current_inventory["Anti-plagas"])

    new_value_antihongos_entry = tk.Entry(window)
    new_value_antihongos_entry.grid(row=6, column=4)
    new_value_antihongos_entry.insert(0, current_inventory["Anti-hongos"])

    new_value_booster_entry = tk.Entry(window)
    new_value_booster_entry.grid(row=7, column=1)
    new_value_booster_entry.insert(0, current_inventory["Booster"])

    new_value_atrapamoscas_entry = tk.Entry(window)
    new_value_atrapamoscas_entry.grid(row=7, column=4)
    new_value_atrapamoscas_entry.insert(0, current_inventory["Atrapa-moscas"])

    new_value_sustratos_entry = tk.Entry(window)
    new_value_sustratos_entry.grid(row=8, column=1)
    new_value_sustratos_entry.insert(0, current_inventory["Sustrato"])

    new_value_micelio_entry = tk.Entry(window)
    new_value_micelio_entry.grid(row=8, column=4)
    new_value_micelio_entry.insert(0, current_inventory["Micelio"])

    def confirm_and_save():
        confirm = messagebox.askokcancel("Confirmar", "¿Guardar los cambios en el inventario?")
        if confirm:
            try:
                manager.update_supplies(
                    antiplagas=int(new_value_antiplagas_entry.get()),
                    antihongos=int(new_value_antihongos_entry.get()),
                    booster=int(new_value_booster_entry.get()),
                    atrapamos=int(new_value_atrapamoscas_entry.get()),
                    sustrato=int(new_value_sustratos_entry.get()),
                    micelio=int(new_value_micelio_entry.get()),
                )
                new_value_sustratos_entry.destroy()
                new_value_antiplagas_entry.destroy()
                new_value_antihongos_entry.destroy()
                new_value_micelio_entry.destroy()
                new_value_atrapamoscas_entry.destroy()
                new_value_booster_entry.destroy()
                save_changes_button.destroy()
                show_supplies()
            except ValueError:
                messagebox.showerror("Error", "Por favor ingresa solo números")

    save_changes_button = tk.Button(text="Guardar nuevo inventario", padx=5, pady=5, command=confirm_and_save)
    save_changes_button.grid(row=5, column=3)



window = tk.Tk()
window.title("Granja de hongos")

product_name_label = tk.Label(window, text="Nombre para la siembra:", padx=20, pady=20)
product_name_label.grid(row=0, column=0)
product_name_entry = tk.Entry(window)
product_name_entry.config(highlightbackground="black")
product_name_entry.grid(row=0, column=1)

product_type_label = tk.Label(window, text="Tipo de hongo:", padx=20, pady=20)
product_type_label.grid(row=1, column=0)
product_type_entry = tk.Entry(window)
product_type_entry.config(highlightbackground="black")
product_type_entry.grid(row=1, column=1)

incubacion_date_label = tk.Label(window, text="Fecha de inico de Incubacion(YYYY-MM-DD):", padx=20, pady=20)
incubacion_date_label.grid(row=2, column=0)
incubacion_date_entry = tk.Entry(window)
incubacion_date_entry.config(highlightbackground="black")
incubacion_date_entry.grid(row=2, column=1)


def save_ui_action():
    manager.anadir_siembra(
        product=product_name_entry.get(),
        incubacion=incubacion_date_entry.get(),
        product_type=product_type_entry.get()
    )
    product_name_entry.delete(0, tk.END)
    product_type_entry.delete(0, tk.END)
    incubacion_date_entry.delete(0, tk.END)
    messagebox.showinfo("Éxito", "Siembra guardada correctamente")


save_button = tk.Button(window, text="Grabar", command=save_ui_action, padx=5, pady=5)
save_button.grid(row=3, column=0, columnspan=2)

list_of_products = tk.Button(window, text="Lista de siembras", command=open_window2)
list_of_products.grid(row=3, column=2, columnspan=2)

supply_label = tk.Label(window, text="SUPPLIES", width=30, font=("Arial", 18))
supply_label.grid(row=4, column=0, columnspan=2)

update_supplies_btn = tk.Button(text="Actualizar inventario", command=update_inventory, padx=5, pady=5)
update_supplies_btn.grid(row=5, column=0)

antiplagas_label = tk.Label(window, text="Anti-plagas:", fg="Green", padx=10, pady=10)
antiplagas_label.grid(row=6, column=0)
antihongos_label = tk.Label(window, text="Anti-hongos:", fg="Green", padx=10, pady=10)
antihongos_label.grid(row=6, column=3)
booster_label = tk.Label(window, text="Booster:", fg="Green", padx=10, pady=10)
booster_label.grid(row=7, column=0)
atrapamoscas_label = tk.Label(window, text="Atrapa-moscas:", fg="Green", padx=10, pady=10)
atrapamoscas_label.grid(row=7, column=3)
sustratos_label = tk.Label(window, text="Sustratos:", fg="Green", padx=10, pady=10)
sustratos_label.grid(row=8, column=0)
micelio_label = tk.Label(window, text="Micelio:", fg="Green", padx=10, pady=10)
micelio_label.grid(row=8, column=3)

show_supplies()

window.mainloop()