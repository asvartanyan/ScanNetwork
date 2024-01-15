import os
import sqlite3 as sq

class ScanNetLocalDataBase:
    con = None
    cur = None
    dbname = "scannet.db"
    last_packet_id = 0
    def __init__(self):
        pass
    #проверка существования базы данных
    # создание новой базы данных с необходимой структурой

    def insertPacket(self,time,smac,dmac,ip_src,ip_dst,ttl,len, year, microsecond, sport, dport, proto):
        with sq.connect(self.dbname) as con:
            cur = con.cursor()
            #вычисление текущего id пакета
           # currows = cur.execute("""SELECT id FROM packets ORDER BY id DESC LIMIT 1""")
            #current_id = currows.fetchall()[0][0] + 1

            cur.execute(f"INSERT INTO packets (timestamp,s_mac_address,d_mac_address,s_ip_address,d_ip_address,ttl,len,sport,dport, proto_id) VALUES ('{time}','{smac}','{dmac}','{ip_src}','{ip_dst}','{ttl}','{len}','{sport}','{dport}','{proto}')")
            #cur.execute(f"INSERT INTO timestamps (packet_id,year, millisec) VALUES ('{current_id}','{int(year)}','{int(microsecond)}')")

    def createDataBase(self, dbname):
        self.dbname = str(dbname)
        with sq.connect(str(dbname)) as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS protocols (
                        id integer PRIMARY KEY,
                        protocol_name TEXT,
                        description TEXT
                         )""")
            cur.execute("""INSERT OR REPLACE INTO protocols (id, protocol_name, description) VALUES 
            (1, 'TCP', 'Transmission Control Protocol'), 
            (2, 'UDP', 'User Datagram Protocol')""")

            cur.execute("""CREATE TABLE IF NOT EXISTS packets (
                            "id" integer PRIMARY KEY,
                             "timestamp" TEXT,
                               "s_mac_address" TEXT,
                                  "d_mac_address" TEXT,
                                 "s_ip_address" TEXT,
                                  "d_ip_address" TEXT,
                                    `sport` TEXT,
                                    `dport` TEXT,
                                 "proto_id" TEXT,
                                  "ttl" integer,
                                  "len" integer,
                                  FOREIGN KEY (proto_id) REFERENCES protocols (id)
                                  )""")


            cur.execute("""CREATE TABLE IF NOT EXISTS timestamps (
                        id integer PRIMARY KEY,
                        packet_id integer,
                        year integer,
                        month integer,
                        day integer,
                        hour integer,
                        minute integer,
                        second integer,
                        millisec integer,
                        FOREIGN KEY (packet_id) REFERENCES packets(id)
                         )""")
            cur.execute("""CREATE TABLE IF NOT EXISTS payloads (
                        id integer PRIMARY KEY,
                        packet_id integer,
                        len integer,
                        data TEXT,
                        FOREIGN KEY (packet_id) REFERENCES packets(id)
                         )""")
    def getIPcounts(self):
        ips = []
        count = []
        with sq.connect(self.dbname) as con:
           con.row_factory = sq.Row
           cur = con.cursor()

           cur.execute("""SELECT all_ips, COUNT(*) as count FROM(
             SELECT  s_ip_address as all_ips  FROM packets
             UNION ALL
             SELECT  d_ip_address as all_ips FROM packets)
             GROUP BY all_ips
             ORDER BY count DESC;
             """)
           result = cur.fetchmany(25)
           for res in result:
               ips.append(res['all_ips'])
               count.append(res['count'])
           return ips,count
    def getFlows(self):
        flows = []
        with sq.connect(self.dbname) as con:
           con.row_factory = sq.Row
           cur = con.cursor()
           cur.execute("""SELECT s_ip_address, d_ip_address, sport, dport, proto_id, COUNT(*) as count_packets FROM packets
                          GROUP BY s_ip_address, d_ip_address, sport, dport, proto_id
                          ORDER BY count_packets DESC;
                        """)
        result = cur.fetchall()
        #for res in result:
            #flows.append([res['s_ip_address'],res['d_ip_address'],res['sport'],res['dport'],res['proto_id'],res['count_packets']])
        return result
    def getPortsCount(self):
        ports = []
        count = []
        with sq.connect(self.dbname) as con:
           con.row_factory = sq.Row
           cur = con.cursor()

           cur.execute("""SELECT all_ports, COUNT(*) as count FROM(
                          SELECT  sport as all_ports FROM packets
                          UNION ALL
                          SELECT  dport as all_ports FROM packets)
                          GROUP BY all_ports
                          ORDER BY count DESC;
             """)
           result = cur.fetchmany(30)
           for res in result:
               ports.append(res['all_ports'])
               count.append(res['count'])
           return ports,count

    def getProtosCount(self):
        protos = []
        count = []
        with sq.connect(self.dbname) as con:
           con.row_factory = sq.Row
           cur = con.cursor()

           cur.execute("""SELECT proto_id, COUNT(*) as count FROM packets
                          GROUP BY proto_id;
             """)
           result = cur.fetchall()
           for res in result:
               protos.append(res['proto_id'])
               count.append(res['count'])
           return protos,count

    def clearDB(self):
        with sq.connect(self.dbname) as con:
            cur = con.cursor()
            cur.execute("""DELETE FROM packets""")

    def removeDataBase(self, dbname = ""):
        if dbname != "":
            dbrm = dbname
        else:
            dbrm = self.dbname

        os.remove(dbrm)



