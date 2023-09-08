import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x500")

        self.contacts = {}
        self.selected_contact = None

        self.create_widgets()
        self.update_contact_list()

    def create_widgets(self):
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="w")

        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(self.root, text="Phone:")
        self.phone_label.grid(row=1, column=0, sticky="w")

        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.grid(row=2, column=0, sticky="w")

        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = tk.Label(self.root, text="Address:")
        self.address_label.grid(row=3, column=0, sticky="w")

        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(self.root, text="View Contact", command=self.view_contact)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.search_label = tk.Label(self.root, text="Search:")
        self.search_label.grid(row=6, column=0, sticky="w")

        self.search_entry = tk.Entry(self.root)
        self.search_entry.grid(row=6, column=1, padx=10, pady=5)

        self.search_button = tk.Button(self.root, text="Search", command=self.search_contact)
        self.search_button.grid(row=7, column=0, columnspan=2, pady=5)

        self.contact_listbox = tk.Listbox(self.root, width=40, height=10)
        self.contact_listbox.grid(row=0, column=2, rowspan=8, padx=10, pady=5)

        self.contact_listbox.bind('<<ListboxSelect>>', self.on_select)

        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=8, column=0, columnspan=2, pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=9, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            self.clear_entries()
            self.update_contact_list()
        else:
            messagebox.showerror("Error", "Name and Phone are required.")

    def update_contact(self):
        if self.selected_contact:
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            if name and phone:
                self.contacts[self.selected_contact] = {"Phone": phone, "Email": email, "Address": address}
                self.clear_entries()
                self.update_contact_list()
                self.selected_contact = None
            else:
                messagebox.showerror("Error", "Name and Phone are required.")

    def view_contact(self):
        if self.selected_contact:
            contact = self.contacts.get(self.selected_contact, {})
            messagebox.showinfo("Contact Details", f"Name: {self.selected_contact}\nPhone: {contact.get('Phone', '')}\nEmail: {contact.get('Email', '')}\nAddress: {contact.get('Address', '')}")
        else:
            messagebox.showerror("Error", "Please select a contact from the list.")

    def search_contact(self):
        search_term = self.search_entry.get()
        self.contact_listbox.delete(0, tk.END)
        for name, data in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in data['Phone']:
                self.contact_listbox.insert(tk.END, name)

    def delete_contact(self):
        if self.selected_contact:
            if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {self.selected_contact}'s contact?"):
                del self.contacts[self.selected_contact]
                self.clear_entries()
                self.update_contact_list()
                self.selected_contact = None
        else:
            messagebox.showerror("Error", "Please select a contact from the list.")

    def update_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        for name in self.contacts.keys():
            self.contact_listbox.insert(tk.END, name)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def on_select(self, event):
        if self.contact_listbox.curselection():
            selected_index = self.contact_listbox.curselection()[0]
            self.selected_contact = self.contact_listbox.get(selected_index)
            contact = self.contacts.get(self.selected_contact, {})
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
            self.name_entry.insert(0, self.selected_contact)
            self.phone_entry.insert(0, contact.get("Phone", ""))
            self.email_entry.insert(0, contact.get("Email", ""))
            self.address_entry.insert(0, contact.get("Address", ""))

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
