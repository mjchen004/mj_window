import psycopg2
import data
import os
from dotenv import load_dotenv
load_dotenv()

def main():    
    conn = psycopg2.connect("postgresql://tvdi_ecbm_user:83RAfDagPTvAhdxU5DSz4jtYS94zr4Lt@dpg-cpscsaaj1k6c738l6hhg-a.singapore-postgres.render.com/tvdi_ecbm")
    with conn: #with conn會自動commit(),手動close
        with conn.cursor() as cursor: #自動close()
            sql = '''
                CREATE TABLE IF NOT EXISTS youbike(
                _id Serial Primary Key,
                sna VARCHAR(50) NOT NULL,
                sarea VARCHAR(50),
                ar VARCHAR(100),
                mday timestamp,
                updateTime timestamp,
                total SMALLINT,
                rent_bikes SMALLINT,
                return_bikes SMALLINT,
                lat REAL,
                lng REAL,
                act boolean,
                UNIQUE (sna, updateTime)
            );
            '''
            cursor.execute(sql)

        all_data:list[dict] = data.load_data()

        with conn.cursor() as cursor:            
            insert_sql = '''
            INSERT INTO youbike(sna, sarea, ar, mday, updatetime, total, rent_bikes,return_bikes,lat,lng,act)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT (sna, updateTime) 
			DO NOTHING;
            '''
            for site in all_data:
                cursor.execute(insert_sql,(site['sna'],
                                site['sarea'],
                                site['ar'],
                                site['mday'],
                                site['updateTime'],
                                site['total'],
                                site['rent_bikes'],
                                site['retuen_bikes'],
                                site['lat'],
                                site['lng'],
                                site['act']
                                ))
    conn.close()
        
    

if __name__ == '__main__':
    main()