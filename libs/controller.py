from libs.uow import UOW


class Controller:
    def __init__(self,page,params,migration=[]) -> None:
        self.page = page
        self.params = params
        self.db = UOW.db
        self.db.create_tables(migration)
    