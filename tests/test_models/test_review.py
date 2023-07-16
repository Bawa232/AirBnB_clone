#!/usr/bin/python3
"""unittest for the Review class"""

from models.review import Review
import unittest


class TestBaseModel(unittest.TestCase):
    """Test the Review class"""

    def test_instantiation(self):
        """Test for correct instantiation"""
        b = Review()
        self.assertEqual(type(b.id), str)
        self.assertEqual(type(b.place_id), str)
        self.assertEqual(type(b.user_id), str)
        self.assertNotEqual(b.created_at, None)
        self.assertNotEqual(b.updated_at, None)

    def test_unique_id(self):
        """Simple test to show id are different"""
        b1 = Review()
        b2 = Review()
        b3 = Review()
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b2.id, b3.id)
        self.assertNotEqual(b1.id, b3.id)

    def test_save(self):
        """Test to check instance is upated at each time save() called"""
        b = Review()
        update0 = b.updated_at
        b.save()
        update1 = b.updated_at
        b.save()
        update2 = b.updated_at
        self.assertTrue(update0 < update1)
        self.assertTrue(update1 < update2)
        self.assertTrue(update0 < update2)

    def test_str(self):
        """check for right string representation"""
        b = Review()
        b.text = "My First Model"
        string = "[{}] ({}) {}".format(b.__class__.__name__, b.id, b.__dict__)
        self.assertEqual(str(b), string)

    def test_to_dict(self):
        """tests that dict represntation is correct"""
        b = Review()
        b.text = "My First Model"
        b.save()
        json_dict = b.to_dict()
        self.assertEqual(len(json_dict), (len(b.__dict__) + 1))
        self.assertEqual(json_dict["id"], b.id)
        self.assertEqual(json_dict["updated_at"], b.updated_at.isoformat())
        self.assertEqual(json_dict["created_at"], b.created_at.isoformat())
        self.assertEqual(json_dict["__class__"], b.__class__.__name__)

    def test_from_dict(self):
        """Create a Review class from a dictionary gotten from to_dict"""
        b = Review()
        b.text = "Love the location and little details"
        b.save()
        json_dict = b.to_dict()
        new_b = Review(**json_dict)
        self.assertEqual(b.id, new_b.id)
        self.assertEqual(b.text, new_b.text)
        self.assertEqual(str(b), str(new_b))
        self.assertTrue(b.created_at == new_b.created_at)
        self.assertTrue(b.updated_at == new_b.updated_at)

    def test_instantiation_with_args(self):
        """Test to ensure args passed on instatntiation are not used"""
        b = Review()
        c = Review(b.id, b.created_at, b.updated_at)
        self.assertNotEqual(b.id, c.id)
        self.assertTrue(b.created_at < c.created_at)
        self.assertTrue(b.updated_at < c.updated_at)
