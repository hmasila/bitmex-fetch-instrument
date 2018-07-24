# bitmex-fetch-instrument

To get started:

1) Edit settings.py to add your interval preferences (For instrument, API key and SECRET are not necessary)
2) `pip install -r requirements.txt` to install the requirements
3) Run it: 
     - for the response, using https

      `python bitmex_instrument.py` 
     
    - for the response, using websocket 
      
    `python bitmex_ws_instrument.py`

For more details about the API connector, go [here](https://github.com/BitMEX/api-connectors/tree/master/official-http/python-swaggerpy)
