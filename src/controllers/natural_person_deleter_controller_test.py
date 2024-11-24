from .natural_person_deleter_controller import NaturalPersonDeleterController

def test_delete(mocker):
   mock_repository = mocker.Mock()
   controller = NaturalPersonDeleterController(mock_repository)
   controller.delete(1)
   mock_repository.delete_by_id.assert_called_once_with(1)
   