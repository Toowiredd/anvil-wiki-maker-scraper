from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form1(Form1Template):

    def __init__(self, **properties):
        # Initialize form components
        self.init_components(**properties)
        # Set the event handler for the Enter key press event
        self.url_textbox.set_event_handler('pressed_enter', self.url_textbox_pressed_enter)

    def scrape_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        url = self.url_textbox.text
        if url:
            result = anvil.server.call('start_scraping', url)
            if result:
                self.output_label.text = "Scraping completed successfully!"
            else:
                self.output_label.text = "Scraping failed."
        else:
            self.output_label.text = "Please enter a URL."

    def url_textbox_pressed_enter(self, **event_args):
        """This method is called when the Enter key is pressed in the URL text box"""
        self.scrape_button_click()