import numpy as np

class Henon( object ):
    """
    Single implemention of Henon. No coupling. 'Typical' parameters.
    """
    def __init__( self, a=1.4, b=0.3, x0=0., y0=0. ):

        self.a = 1.4
        self.b = 0.3
        self.x = [ float( x0 ) ]
        self.y = [ float( y0 ) ]

    def iterate( self ):
        """
        Map forward
        """
        self.x.append( self.y - self.a * self.x**2 + 1 )
        self.y.append( self.b * self.x )
