import pickle
from pathlib import Path
from typing import Any, Union
from implicit.cpu.als import AlternatingLeastSquares as cpu_ALS_cls
from implicit.gpu.als import AlternatingLeastSquares as gpu_ALS_cls
from scipy.sparse import csc_matrix


class ALS:
    def __init__(self, model_pkl_path: str, interactions_pkl_path: str) -> None:
        self.model = ALS.read_pkl(model_pkl_path)
        assert isinstance(self.model, Union[cpu_ALS_cls, gpu_ALS_cls]), "Expected implicit ALS model instance"
        self.interactions = ALS.read_pkl(interactions_pkl_path)
        assert isinstance(self.interactions, csc_matrix), "Expected scipy csc matrix instance"
        # Save max allowed number of items and users for further checks
        self.max_users = self.interactions.shape[0]
        self.max_items = self.interactions.shape[1]

    def get_user_recommendations(self, user_id: int, num_recs: int) -> list:
        """
        Get N recommendations for specified user id
        """
        assert user_id < self.max_users, f"User ID out of range, max allowed ID is {self.max_users}"
        assert num_recs < self.max_items, f"Too many recommendations requested, max allowed number is {self.max_items}"

        # Create user_items matrix for the user
        user_items = self.interactions[user_id]
        # Get user recommendations in score decreasing orders
        recommendations = self.model.recommend(
            user_id,
            user_items.tocsr(),
            N=num_recs,
            filter_already_liked_items=True)[0].tolist()
        for

        return recommendations

    @staticmethod
    def read_pkl(file_name: str) -> Any:
        """
        Read pickle file in recsys directory
        """
        abs_path = Path(__file__).with_name(file_name)
        try:
            with open(abs_path, 'rb') as f:
                data = pickle.load(f)
        except FileNotFoundError:
            raise "Please put pickle file in the recsys folder"
        return data


ALS_model = ALS('trained_model.pkl', 'interact_matrix.pkl')
