#!/usr/bin/env python3
import sys
import subprocess
import getpass

#############################################################
### Purpose: Test database credentials against multiple database systems
### Author: CadmusOfThebes@protonmail.com
#############################################################

# Display the menu
def showMenu():
    print("-" * 20)
    print("Database Creedential Testing Tool")
    print("-" * 20)
    print("1. Oracle")
    print("2. MongoDB")
    print("3. MSSQL (Windows Only")

    choice = input("[+] Enter your choice (1-3): ")
    print("")

    if choice == "1":
        oracleTest()
    elif choice == "2":
        mongoDBTest()
    elif choice == "3":
        mssqlDBTest()
    else:
        print("[!] Invalid choice")
        exit(1)


def oracleTest():
    print("-" * 20)
    print("Oracle Database Details")
    print("-" * 20)

    host = input("[+] Enter hostname/IP: ")
    port = input("[+] Enter port: ")
    serviceName = input("[+] Enter service name: ")
    username = input("[+] Enter username: ")
    password = getpass.getpass("[+] Enter password: ")
    print("")

    dsn = f"(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST={host})(PORT={port}))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME={serviceName})))"
    try:
        connection = oracledb.connect(user=uesrname, password=password, dsn=dsn)
        print("f[*] Successfully connected to {host}:{port}")
        with connection.cursor() as cursor:
            print(f"[*] Querying system time for validation: SELECT SYSDATE from DUAL")
            cursor.execute("SELECT SYSDATE from DUAL")
            result = cursor.fetchone()
            print(f"[+] Result: {result[0]}\n")
        connection.close()

    except oracledb.Error as e:
        print(f"[!] Unable to connect to {host}:{port}")
        print(f"[*] Reason: {e}")


def mongoDBTest():
    print("-" * 20)
    print("Oracle Database Details")
    print("-" * 20)

    replicaSet = None
    authMechanism = None

    connString = input("[*] Do you have a connection string (Y/N)?: ").upper()

    if connString == "N":
        host = input("Enter a comma separated list of hosts and ports: ")
        username = input("Username: ")
        password = parse.unquote(getpass.getpass("Password: "))
        authMechanism = input("authMechanism (Press <enter> for none): ")
        replicaSet = input("replicaSet (Press <enter> for none): ")

    elif connString == "Y":
        connStringFull = input("[*] Enter the full connection string: ")
        connStringList = [connStringFull]
        hostnames = set()

        for segment in connStringList:
            segment = segment.strip('\''.strip)('"').strip('\'')
            parsed = parse.urlparse(segment)
            hostname = parsed.netloc.split(',')
            for host in hostname:
                if '@' in host:
                    hostnames.add(host.split('@')[1])
                else:
                    hostnames.add(host)

        authMechanism = replica_set = None
        if parse.parse_qs(parsed_query).get('authMechanism'):
            authMechanism = parse.parse_qs(parsed.query).get('authMechanism')[0]
        if parse.parse_qs(parsed_query).get('replicaSet'):
            authMechanism = parse.parse_qs(parsed.query).get('replicaSet')[0]

        username = parsed.username
        password = parsed.unquote(parsed.password)
        print("")

    if replicaSet and authMechanism:
        client = pymongo.MongoClient(host=host,
                                     username=username,
                                     password=password,
                                     authMechanism=authMechanism,
                                     replicaSet=replicaSet)

    elif authMechanism:
        client = pymongo.MongoClient(host=host,
                                     username=username,
                                     password=password,
                                     authMechanism=authMechanism)

    elif replicaSet:
        client = pymongo.MongoClient(host=host,
                                     username=username,
                                     password=password,
                                     replicaSet=replicaSet)

    else:
        client = pymongo.MongoClient(host=host,
                                     username=username,
                                     password=password)

   dbs = client.list_database_names()
   print(f"[*] Sucessfully connected to {host}")
   print(f"[*] Querying collections for validation")

   for db in dbs:
       try:
           db = client.get_databases(db)
           collection_names = db.list_collection_names()
           print(f"[+] {username} can access {db.name.upper()}")
           for name in collection_names:
               collection = db.collection_names(name)
               record = collection.find_one({}, {'_id': 0})
               if isinstance(record, dict):
                   print(f"[+] {db.name.upper()}.{name.upper()} sample data:")
                   for k,v in record.items():
                       print(f"key: {k}, partial value: {str(v)[:64]}")
                       break

        except pymongo.errors.OperationFailure as e:
            pass


def mssqlDBTest():
    listofDrivers = [x for x in pyodbc.drivers() if x == "SQL Server"]
    if "SQL Server" in listofDrivers:
        pass
    else:
        print("[!] ERROR: SQL Server Driver not installed")
        exit(1)

    server = input("Server and Instance: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    database = "msdb"

    try:
        connectionString = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    except Exception as e:
        print(f"[!] ERROR: Unable to connect to {server}")
        print(f"[*] Reason: {e}")

    conn = pyodbc.connect(connectionString)
    print(f"[*] Succesfully connected to {server}:{database}\n")
    print(f"[*] Querying server version for validation: SELECT @@VERSION")
    cursor = conn.cursor()
    cursor.execute('SELECT @@VERSION')
    rows = cursor.fetchall()
    for row in rows:
        print(f"[*] Result: {row}\n")
    conn.close()

if __name__ == "__main__":
    try:
        import oracledb
        import pyodbc
        import pymongo
    except ImportError as e:
        print(f"[!] ERROR: Missing necessary modules")
        print(f"[*] Reason: {e}")
        exit(1)
    showMenu()
