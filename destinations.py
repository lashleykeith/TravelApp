from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Destinations, Base, Item, User

engine = create_engine('sqlite:///Destinations.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create Destinations
africa_map = Destinations(name="Africa")
europe_map = Destinations(name="Europe")
asia_map = Destinations(name="Asia")
australia_map = Destinations(name="Oceania")
north_america_map = Destinations(name="North America")
south_america_map = Destinations(name="South America")



# Add Destinations
session.add(africa_map)
session.add(europe_map)
session.add(asia_map)
session.add(australia_map)
session.add(north_america_map)
session.add(south_america_map)

# Create user
user1 = User(username="InitalSetup")

# Create Items
item1 = Item(title="Kenya",
             description="East Africa", video="https://www.youtube.com/watch?v=CYhZSx9TKvQ",
             photo_image="https://www.google.co.kr/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=0ahUKEwinxLDQgfvYAhWHoZQKHRx_B9EQjBwIBA&url=https%3A%2F%2Fwww.africaendeavours.com%2Fwp-content%2Fuploads%2F2015%2F04%2FD184-hero-seychelles-constance-ephelia-resort-beach-hero-2000x837.jpg&psig=AOvVaw299tmZRS4lD86hNkNayPiy&ust=1517241080630096",
             category=africa_map, user=user1)
item2 = Item(title="Nigeria",
             description="West Africa",video="https://www.youtube.com/watch?v=hr729vSl0us",
             photo_image="http://www.africapropertyinvest.com/wp-content/uploads/2015/11/Lagos-Nigeria-Honeymoon.jpg",
             category=africa_map, user=user1)
item3 = Item(title="Spain",
             description="Southern Europe", video="https://www.youtube.com/watch?v=jimXRJCz8bI",
             photo_image="https://www.zicasso.com/sites/default/files/styles/original_scaled_down/public/photos/tour/spain_park_guell_in_barcelona_spain4.jpg",
             category=europe_map, user=user1)
item4 = Item(title="Hong Kong",
             description="East Asia",video="https://www.youtube.com/watch?v=w1uoP9ZBDO8",
             photo_image="https://gotravelly.com/assets/img/tinymce/84b9b47e3683472a65a2fdd7260caf71.jpg",
             category=asia_map, user=user1)
item5 = Item(title="Israel",
             description="Middle East",video="https://www.youtube.com/watch?v=VSPyiqK8ac8",
             photo_image="https://www.globusjourneys.ca/user/images/gl_religious_israel_jordan.jpg",
             category=asia_map, user=user1)
item6 = Item(title="New Zealand",
             description="Oceania",video="https://www.youtube.com/watch?v=QdEsM7-_DLI",
             photo_image="https://data.whicdn.com/images/8820274/large.jpg",
             category=australia_map, user=user1)


# Add items
session.add(item1)
session.add(item2)
session.add(item3)
session.add(item4)
session.add(item5)
session.add(item6)


# Commit the additions to the database
session.commit()
