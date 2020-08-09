# This file views the GUI based output after an action has been done.
from tkinter import *
import tkinter as tk
import re
import tkinter.messagebox
from Backend import Block
import webbrowser
class Methods:
    def __init__(self,link_value):
        self.link_value = link_value
        self.pattern = "www.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

    def add_site(self):
        if len(re.findall(self.pattern, self.link_value.get())) != 1:
            tkinter.messagebox.showerror("Error","Please put valid link in the box.\nFormat : www.examplewebsite.com")
        else:
            ch = tkinter.messagebox.askyesnocancel("Website Blocker",f"Confirm to block { self.link_value.get() }")
            if ch:
                b = Block()
                b.block_website(self.link_value.get())
                tkinter.messagebox._show(title="Website Blocker",message = f"{self.link_value.get()} has been blocked.")
            else:
                pass

    def remove_sites(self):
        if tkinter.messagebox.askyesnocancel("Website Blocker",f"Confirm to unblock { self.link_value }"):
            b = Block()
            b.unblock_website(self.link_value)
            tkinter.messagebox._show(title = "Website Blocker", message= f"{self.link_value} has been unblocked.")       


    @staticmethod
    def show_sites():
        b = Block()
        web_list = b.website_list
        return web_list
   
    @staticmethod
    def github_callback(event):
                webbrowser.open_new("https://Github.com/sriprakhar2")
    @staticmethod
    def facebook_callback(event):
        webbrowser.open_new("https://www.facebook.com/prakhar.srivastava.37017794/")
    @staticmethod
    def linkedin_callback(event):
        webbrowser.open_new("https://www.linkedin.com/in/prakhar-srivastava-155565148/")
