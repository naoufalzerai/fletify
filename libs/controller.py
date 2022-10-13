from libs.uow import UOW


class Controller:
    def __init__(self,page,params,migration=[]) -> None:
        self.page = page
        self.params = params
        try:
            UOW.db.create_tables(migration)
        except Exception as e:
            print(e)
    