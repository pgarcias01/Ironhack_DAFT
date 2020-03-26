from pandas import DataFrame

class Params:
    """
    Parameters class.

    This file centralizes anything that can be
    parametrized in the code.
    """

    raw_data = '../data/raw/'
    external_data = '../data/external/'
    processed_data = '../data/processed/'
    intermediate_data = '../data/intermediate/'

    log_name = '../log/dump.log'

    # if this is set to True, then all the nodes will be automatically
    # considered not up-to-date and will be rerun.
    rerun = True

    ## Database connection params
    user = 'postgres'
    password = 'xxx'
    host = 'localhost'
    database = 'xxx'

    def get_url_moedas(self, currency : str, start_date : str, end_date : str):
        """
        Function to return a end point for get data's for currency from BCB
        Args:
            currency: currency of user want the data's ex: dólar ('USD')
            start_date: date of start the search in format: mm-dd-yyyy
            end_date:date of end the search in format: mm-dd-yyyy
        Returns:
        a end point with the params of user inputs
        """
        return f'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/' \
               f'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?' \
               f'@moeda=\'{currency}\'&@dataInicial=\'{start_date}\'&@dataFinalCotacao=\'{end_date}\'&' \
               f'$format=json&$select=cotacaoCompra,dataHoraCotacao,tipoBoletim'

