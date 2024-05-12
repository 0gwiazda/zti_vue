import psycopg2 as pg

con_str = "host=cornelius.db.elephantsql.com dbname=gdufqwah user=gdufqwah password=0w4x7F00Tz-BdT2B1Ab_a4600C1ZCfSL port = 5432"

def view_people() -> list:
    
    res = []
    
    try:
        with pg.connect(con_str) as con:
            with con.cursor() as cur:

                cur.execute("SELECT * FROM \"public\".\"person\"")

                rows = cur.fetchall()

                res_row = []

                for row in rows:
                    res_row = []
                    for r in row:
                        res_row.append(r)
                    res.append(res_row)

    except(Exception, pg.DatabaseError) as err:
        print(err)
        res.append(0)
    finally:
        return res

def add_person(data:list) -> int:

    row_count = 0

    try:
        with pg.connect(con_str) as con:
            with con.cursor() as cur:
                cur.execute("INSERT INTO \"public\".\"person\"(\"fname\", \"lname\", \"city\", \"email\", \"tel\") VALUES (%s, %s, %s, %s, %s)", tuple(data))

                row_count = cur.rowcount

            con.commit()

    except(Exception, pg.DatabaseError) as err:
        print(err)
    finally:
        return row_count

def del_person(params:list) -> int:

    row_count = 0

    try:
        with pg.connect(con_str) as con:
            with con.cursor() as cur:

                cur.execute("DELETE FROM \"public\".\"person\" WHERE fname = %s AND lname = %s", tuple(params))
                
                row_count = cur.rowcount

            con.commit()

    except(Exception, pg.DatabaseError) as err:
        print(err)
    finally:
        return row_count

def edit_person(params:list, data:list) -> int:

    row_count = 0

    try:
        with pg.connect(con_str) as con:
            with con.cursor() as cur:
                data.extend(params)
                print(data)
                cur.execute("UPDATE \"public\".\"person\" SET fname = %s, lname = %s, city = %s, email = %s, tel = %s WHERE fname = %s AND lname = %s", tuple(data))

                row_count = cur.rowcount

            con.commit()

        cur.close()

    except(Exception, pg.DatabaseError) as err:
        print(err)
    finally:
        return row_count