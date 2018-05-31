from jsonstreamer import JSONStreamer

class Parser:
    
    def __init__(self):
        self._streamer = JSONStreamer() #same for JSONStreamer
        
        # this automatically finds listeners in this class and attaches them if they are named
        # using the following convention '_on_eventname'. Note method names in this class
        self._streamer.auto_listen(self)
    
    def _on_doc_start(self):
        print ('Root Object Started')
        
    def _on_key(self, key):
        print('Key: {}'.format(key))
        
    def parse(self, data):
        self._streamer.consume(data)
        self._streamer.close()
        
        
if __name__ == "__main__":
    m = Parser()
    m.parse("""
    {
        "fruits":["apple","banana", "cherry"],
        "calories":[100,200,50]
    }
""")
