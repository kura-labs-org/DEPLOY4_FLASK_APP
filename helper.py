import sqlite3
DB='./teams.db'
def start():
    try:
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.executescript("""
                    pragma foreign_keys=on;
                    create table if not exists teams(
                    team_id INTEGER PRIMARY KEY,
                    team_name TEXT NOT NULL,
                    total_score INTEGER DEFAULT 0
                );
                create table if not exists users(
                    user_id INTEGER PRIMARY KEY,
                    user_name TEXT NOT NULL,
                    team_id INTEGER DEFAULT 1,
                    is_active BOOLEAN DEFAULT 0,
                    total_score INTEGER DEFAULT 0,
                FOREIGN KEY (team_id) REFERENCES teams(team_id)ON UPDATE CASCADE 
                );
                create table if not exists round(
                    round_id INTEGER NOT NULL,
                    total_score INTEGER DEFAULT 0,
                    total_time Integer,
                    score_sheet BLOB NOT NULL,
                    user_id Integer not NULL,
                    team_id Integer NOT NULL,
                    FOREIGN KEY (round_id) REFERENCES round(round_id) ON UPDATE CASCADE
                );
                                            """)
        conn.commit()
        return ("Finished")
    except Exception as e:
        print(f"Err:{e}")
        return None
def get_all_teams():
    try:
        conn  = sqlite3.connect(DB)
        con = conn.cursor()
        con.execute('select * from teams')
        r = con.fetchall()
        return{'count': len(r),'teams':r}
    except Exception as error:
        print(f"Err:{error}")
        return None
def get_all_users():
    try:
        conn  = sqlite3.connect(DB)
        con = conn.cursor()
        con.execute('select * from users')
        r = con.fetchall()
        return{'count': len(r),'users':r}
    except Exception as error:
        print(f"Err:{error}")
        return None
def get_user_byname(user_name):
    try:
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute('select * from users where user_name=?',(user_name,))
        a = c.fetchone()[0]
        return(a)
    except Exception as err:
        print(f"err:{err}")
        return None
def add_user_to_team(user_name,team_id):
    try:
        conn = sqlite3.connect(DB)
        con = conn.cursor()
        con.execute('update users set team_id=? where user_name=?',(team_id,user_name,))
        conn.commit()
        return(user_name,team_id)
    except Exception as error:
        print(f"Err:{error}")
        return None
def create_user(user_name):
    try:
        conn  = sqlite3.connect(DB)
        con = conn.cursor()
        con.execute("insert into users(user_name,is_active) values (?,1)",(user_name,))
        conn.commit()
        return(user_name)
    except Exception as error:
        print(f"Err:{error}")
        print(user_name)
        return None
def create_team(team_name):
    try:
        conn  = sqlite3.connect(DB)
        con = conn.cursor()
        con.execute('insert into teams(team_name) values (?)',(team_name,))
        conn.commit()
        return(team_name)
    except Exception as error:
        print(f"Err:{error}")
        return None
def delete_user(user_name):
    try:
        conn  = sqlite3.connect(DB)
        con = conn.cursor()
        con.execute('delete from users where user_name=?',(user_name,))
        conn.commit()
        return(user_name)
    except Exception as error:
        print(f"Err:{error}")
        return None
def delete_team(team_name):
    try:
        conn  = sqlite3.connect(DB)
        con = conn.cursor()
        con.execute('delete from teams where team_name=?',(team_name,))
        conn.commit()
        return(team_name)
    except Exception as error:
        print(f"Err:{error}")
        return None