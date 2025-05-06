from database.DB_connect import DBConnect
from model.arco import Arco
from model.country import Country


class DAO():

    @staticmethod
    def getAllNodes(year):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        result = []

        query = """  select c2.StateAbb ,c2.CCode ,c2.StateNme 
                    from contiguity c, country c2 
                    where c.conttype = %s
                    and `year` <= %s
                    group by c2.stateAbb
                    """

        cursor.execute(query, (1,year))

        for row in cursor:
            result.append(Country(**row))

        cnx.close()
        cursor.close()
        return result

    @staticmethod
    def getAllEdges(idMap, year):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        result = []

        query = """  select c.state1no , c.state2no
                        from contiguity c
                        where c.conttype =%s
                        and year< %s
                        and c.state1no < c.state2no 
                        """

        cursor.execute(query, (1, year))

        for row in cursor:
            result.append(Arco(**row))

        cnx.close()
        cursor.close()
        return result


if __name__== "__main__":
    print(DAO().getAllNodes(1900))
   # print(DAO().getAllEdges(1900))
