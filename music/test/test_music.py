try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '../'
            )
        )
    )
except:
    raise

from unittest import TestCase, main
import music

class TestMusic(TestCase):
    def setUp(self):
        self.music = Music()
        
    def test_levanta_erro_
    

if __name__ == "__main__":
    main(verbosity=2)