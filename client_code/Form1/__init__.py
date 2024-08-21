from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    signups = anvil.server.call('get_user_signups')
    
    # Anvil plots use the Plot.ly API: https://plot.ly/python/#basic-charts
    self.signup_plot.data = go.Scatter(x = [signup_time for (count,signup_time) in signups],
                        y = [count for (count,signup_time) in signups],
                        fill = 'tozeroy')