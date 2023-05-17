import unittest


class ModelTestCase(unittest.TestCase):
    def setUp(self) -> None:
        from recsys.model import ALS_model
        self.model = ALS_model

    def test_recommendations_number(self) -> None:
        user_id = 1
        num_rec = 7

        recs = self.model.get_user_recommendations(user_id, num_rec)
        self.assertEqual(len(recs), num_rec)