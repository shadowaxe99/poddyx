class Integrations:
    def __init__(self):
        self.ide_integrations = {}
        self.integration_status = {}

    def manage_integrations(self, ide_name, integration_details):
        self.ide_integrations[ide_name] = integration_details

    def update_integration_status(self, ide_name, status):
        self.integration_status[ide_name] = status
