import unittest

from src.rookline.domain_review import DomainReview, review_lane, review_score


class DomainReviewTests(unittest.TestCase):
    def test_review_lane(self) -> None:
        item = DomainReview(58, 47, 22, 87)
        self.assertEqual(review_score(item), 184)
        self.assertEqual(review_lane(item), "ship")


if __name__ == "__main__":
    unittest.main()
