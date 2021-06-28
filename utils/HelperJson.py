import json

class HelperJson:
    """HelperJson Class"""

    def __init__(self):
        """
        This method Initialize the class
        """
        self.path = "/Users/juandelgado/PycharmProjects/netflix-testing/suites/test_data/"

    def read(self,nameFile):
        """
        this methd read all the data of the scripts are allocated on a json file
        :param nameFile: dataComputer.json
        :return:
        """
        with open(self.path+nameFile) as json_file:
            return json.load(json_file)