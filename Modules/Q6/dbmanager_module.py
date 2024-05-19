from contextmanager_module import ContextManager

class DataBaseManager:

    config={
         'dbname':'b_bank',
         'host':'localhost',
         'port':5648,
         'user':'postgres',
         'password':'1380ACreZA46'
        }

    def __init__(self , table_name:str) -> None:
        pass

    @classmethod
    def delete(cls, table_name:str, **kwargs):
        """
            kwargs: contain where clause {column:value}
        """
        base_query =f"DELETE FROM {table_name} WHERE"
        where_condition="and".join([f"{key} = %s" for key in kwargs['where'].keys()])
        query= base_query + where_condition
        with ContextManager as db:
            db.cursor.execute(query)

    @classmethod
    def select(cls, table_name:str, where_clause:dict=None):
        basic_query=f"Select * from {table_name}"
        if where_clause:
            where_condition=' and '.join([f"{key} = %s" for key in where_clause.keys()])
            params = tuple([val for val in where_clause.values()])
            query=basic_query+' WHERE '+where_condition   
        else:
            query=basic_query 
        with ContextManager(cls.config) as db:
            db.cursor.execute(query,params)
            return db.cursor.fetchone()
                

    @classmethod
    def update(cls, table_name:str, **kwargs):
        """
            kwarg: contain set clause and where clause {set:{column:value},where:{column:value}}"
        """
        base_query=f"UPDATE {table_name}"
        set_condition=",".join([f"{key} = %s" for key in kwargs['set'].keys()])
        param_set=tuple([val for val in kwargs['set'].values()])
        where_condition=" and ".join([f"{key} = %s" for key in kwargs['where'].keys()])
        param_where=tuple([val for val in kwargs['where'].values()])
        query=base_query + ' SET ' + set_condition + ' WHERE ' + where_condition
        'update account set balance=balance-%s where acc_id=%s'
        print(param_set+param_where)
        with ContextManager(cls.config) as db:
            db.cursor.execute(query,param_set+param_where)

############################# how to merge to tuples solved by majid           
# t1=(1,)
# t2=(2,)

# print(t1+t2)