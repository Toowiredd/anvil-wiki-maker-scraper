from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

anvil.server.connect("client_IQDD4DTLD3NWNH6WVP3VFTL3-JGPJFCSRQRYQCWRU")

class Form1(Form1Template):

    def __init__(self, **properties):
        # Initialize form components
        self.init_components(**properties)
        # Set the event handler for the Enter key press event
        self.url_textbox.set_event_handler('pressed_enter', self.url_textbox_pressed_enter)
        # Check if the server is running
        if 
       
      
      85awaqqqaqanvil.server.call('test_server') == "Server is running":
            self.output_label.text = "Server is running"
        else:
            self.output_label.text = "Server is not running"

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
