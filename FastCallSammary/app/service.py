from msilib.schema import File
from app.user import User
from app.model import MLModel

class PredictionTask:
    def __init__(self, user: User, ml_model: MLModel): # добавить валидацию файла для проекта
        self.user = user
        self.ml_model = ml_model
        self.valid_data = None
        self.errors = []

    def execute_task(self, get_file):
        validation_results = self.ml_model.validate_data(get_file)
        if validation_results is True:
            pass
        else:
            pass

    def delete_result_of_task(self, get_files):
        if get_files is not delete:
            pass
        else:
            pass

    def get_download_ulr(args):
        pass



