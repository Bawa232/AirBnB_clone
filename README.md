This is a project on the implementation of the back-end console of the airbnb clone.

Classes: AirBnB Clone utilizes the following classes:

BaseModel FileStorage User State City Amenity Place Review

PUBLIC INSTANCE ATTRIBUTES id created_at updated_at

PUBLIC INSTANCE METHODS save to_dict all new save reload

PUBLIC CLASS ATTRIBUTES email password first_name last_name name state_id city_id user_id description number_of_rooms number_of_bathrooms max_guest price_by_night latitude longitude amenity_ids place_id user_id text

PRIVATE CLASS ATTRIBUTES file_path objects

Storage: The above classes are handled by the abstracted storage engine defined in the FileStorage class.

Every time the backend is initialized, AirBnB instantiates an instance of FileStorage called storage. The storage object is loaded/re-loaded from any class instances stored in the JSON file file.json. As class instances are created, updated, or deleted, the storage object is used to register corresponding changes in the file.json.

Console: The console is a command line interpreter that permits management of the backend of AirBnB. It can be used to handle and manipulate all classes utilized by the application (achieved by calls on the storage object defined above).
