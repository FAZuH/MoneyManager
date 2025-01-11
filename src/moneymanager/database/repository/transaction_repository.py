from dataclasses import asdict

from moneymanager.database.base_csv_repository import BaseCsvRepository
from moneymanager.database.model.transaction import Transaction
from moneymanager.database.repository.repository import Repository


class TransactionRepository(BaseCsvRepository, Repository[Transaction, str]):
    def select(self, identifier: str) -> Transaction:
        with self.enter_reader() as reader:
            for row in reader:
                if row["uuid"] == identifier:
                    return self.model(**row)  # type: ignore
        raise ValueError(f"Transaction with id {identifier} not found")

    def insert(self, entity: Transaction) -> None:
        with self.enter_reader() as reader:
            rows = list(reader) # Turns into a list
            for i in range(len(rows)):
                if rows[i]["uuid"] == entity.uuid: # If account name is already exist
                    raise ValueError(f"Transaction with id {entity.uuid} is already exist!")
        # If the account hasn't been created 
        new = asdict(entity) # Turn into dictionary
        with self.enter_writer() as writer:
            writer.writerow(new)
            return

    def update(self, identifier: str, entity: Transaction) -> None:
        available = False
        with self.enter_reader() as reader:
            rows = list(reader)
            for i in range(len(rows)):
                if rows[i]["uuid"] == identifier:
                    rows[i]["date"] = entity.date
                    rows[i]["account"] = entity.account
                    rows[i]["amount"] = entity.amount
                    rows[i]["type_"] = entity.type_
                    rows[i]["category"] = entity.category
                    rows[i]["comment"] = entity.comment
                    available = True
        
        if available:
            with self.enter_writer('w') as writer:
                writer.writeheader()
                writer.writerows(rows)
        else:
            raise ValueError(f"The transaction with id {identifier} is not exist!")

    def delete(self, identifier: str) -> None:
        available = False # for checking availablity
        with self.enter_reader() as reader:
            with self.enter_writer('w') as writer:
                for row in reader:
                    if row["uuid"] != identifier: # If not the same uuid as identifier, write it
                        writer.writerow(row)
                    else: # Else don't write
                        available = True
    
        if available:
            return
        else:  # If the transaction doesn't exists
            raise ValueError(f"Transaction with id {identifier} is not exist!")

    def select_all(self) -> list[Transaction]:
        with self.enter_reader() as reader:
            return [self.model(**row) for row in reader]  # type: ignore

    @property
    def filename(self) -> str:
        return "transaction_history.csv"

    @property
    def model(self) -> type[Transaction]:
        return Transaction
