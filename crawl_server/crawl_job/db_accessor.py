import psycopg2

def add_pokemon_to_db(encounter_id, expire, pokemon_id, latitude, longitude):
    # 1. open connection
    conn = psycopg2.connect(host = "pokemon1.cozbedhsxp0j.us-west-2.rds.amazonaws.com",
                            port = 5432,
                            database="pokemon1", 
                            user="pokemon1", 
                            password="pokemon1")

    # 2. Execute SQL
    with conn.cursor() as cur:
        cur.execute("INSERT INTO pokemon_map (encounter_id, expire, pokemon_id, latitude, longitude)" +
                    " VALUES (%s, %s, %s, %s, %s)" +
                    " ON CONFLICT (encounter_id) DO NOTHING",
                    (encounter_id, expire, pokemon_id, latitude, longitude))

    # 3. connection commit
    conn.commit()
    conn.close()
    return

if __name__ == "__main__":
    add_pokemon_to_db(1,1,1,1,1)
