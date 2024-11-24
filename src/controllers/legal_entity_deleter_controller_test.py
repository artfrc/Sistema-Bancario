from .legal_entity_deleter_controller import LegalEntityDeleterController

def test_delete(mocker):
   mock_repository = mocker.Mock()
   controller = LegalEntityDeleterController(mock_repository)
   controller.delete(1)
   mock_repository.delete_by_id.assert_called_once_with(1)
   