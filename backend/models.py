from flask_login import UserMixin
from dataclasses import dataclass
from slplayer import db

@dataclass
class Albums(db.Model):
    """Artist class"""

    __tablename__ = "album"
    album_id:str = db.Column(db.Integer,primary_key=True)
    name:str = db.Column(db.String(50))
    cover:str = db.Column(db.String(50))
    artist:str = db.Column(db.String(50))

    def __init__(self,id:int,name:str,cover:str):
        """initialize Albums class

        Args:
            id (int): Albums id
            name (str): Albums name

        Returns:
            _type_: _description_
        """
        self.album_id:str = id
        self.name:str = name
        self.cover = cover

    def __repr__(self):
        """return official representation

        Returns:
            string : id
        """
        return self.album_id

    def __str__(self):
        """return unofficial rpresentation

        Returns:
            string : name+id
        """

        return self.name+"with id: "+self.album_id


@dataclass
class Track():
    """track class"""

    def __init__(self,id:int,name:str,artist:str,cover:str,album:str,duration:int):
        """initialize track class

        Args:
            id (int): track id
            artist (string): track artist
            cover (string): track cover
            album (string): track's album
            duration (int): track duration

        Returns:
            None: _description_
        """

        self.id:int = id
        self.name:str = name
        self.artist:str = artist
        self.cover:str = cover
        self.album:str = album
        self.duration:str = self.convert_time(duration)

    def convert_time(self,ms):

        """convert milli seconds to min:second

        Args:
            ms (int): milliseconds

        Returns:
            string: min:sec converted
        """

        min = ms//60000
        sec = (ms%60000)//1000
        return str(min) +':'+ (str(sec) if (sec > 9) else "0"+ str(sec))

    def __repr__(self) -> str:

        """return formal string representation of class

        Returns:
            str: string representation
        """

        return 'Track '+ self.named + "(+" +self.id +"+)"

    def __str__(self) -> str:

        """returns informal string representation of class

        Returns:
            str: string representation
        """

        return self.id


@dataclass
class User(UserMixin,db.Model):
    __tablename__ = "user"
    user_id: int = db.Column(db.Integer,primary_key=True)
    name: str = db.Column(db.String(50))
    username: str = db.Column(db.String(45))
    email: str = db.Column(db.String(45))
    password: str = db.Column(db.String(45))
    fav_artist: str = db.Column(db.String(45),)
    fav_style: str = db.Column(db.String(45))

    def get_id(self):
        """return id

        Returns:
            self: object
        """
        return self.user_id

    def __init__(self,name,username,email,password,fav_artist) -> None:
        """initialize user class

        Args:
            name (_type_): name of user
            username (_type_): user's username
            email (_type_): user's email
            password (_type_): user's password_
            fav_artist (_type_): user favorite artist
            fav_style (_type_): user favorite music style
        """
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.fav_artist = fav_artist

    def __repr__(self) -> str:
        """return formal string representation of class

        Returns:
            str: string representation
        """

        return 'User '+ self.username + "(+" +self.user_id +"+)"

    def __str__(self) -> str:
        """returns informal string representation of class

        Returns:
            str: string representation
        """

        return self.user_id

if __name__ == "__main__":
    db.create_all()
