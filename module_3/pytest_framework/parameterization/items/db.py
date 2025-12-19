import tinydb

class DB:
    def __init__(self, db_path, db_file_prefix):
        self._db = tinydb.TinyDB(
            db_path / f"{db_file_prefix}.json", create_dirs = True
        )

    def create(self, item: dict):
        """Create an item
        
        Returns:
            id: The items id.
        """

        return id
    
    def read(self, id: int):
        """Reads an item.
        
        Args:
            id(int): The item id of an item
        Returns:
            item: The item object.
        """
        return 
    
    def update(self, id: int, mods):
        """Update an item in the database.
        
        Args:
            id (int): The item id of an item.
            mods (Item): The modification to be made to this item.
        """
        self._db.update(doc_ids=[id])

    def delete(self, id: int):
        """Deletes an item in the database.
        
        Args:
            id (int): The item id of an item.
        """
        self._db.remove(doc_ids=[id])

    def close(self):
        """Closes the database connection."""
        self._db.close()