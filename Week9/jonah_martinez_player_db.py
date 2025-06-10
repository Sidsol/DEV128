# Assignment: Player DB 
# Class: DEV 128
# Date: 06/09/2025
# Author: Jonah Martinez
# Description: Database tier for the Players' data manager program

import sqlite3
from contextlib import closing

from player_objects import Player

conn = None


def connect():
    global conn
    if not conn:
        DB_FILE = "player_db.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row


def close():
    if conn:
        conn.close()


def get_players():
    """Method to executes a query to get the list of all players ordered
        by wins - player with the most wins first.
    It returns a list of Player class objects
    """
    with closing(conn.cursor()) as c:
        # SQL statement to select all players ordered by wins
        sql = """SELECT playerID, name, wins, losses, ties
                 FROM Player ORDER BY wins DESC"""
        c.execute(sql)
        # Fetch all rows that match the query
        rows = c.fetchall()

        # If rows are found, create Player objects and return them
        players = []

        # Loop through the rows and create Player objects
        for row in rows:
            player = Player(
                name=row["name"],
                wins=row["wins"],
                losses=row["losses"],
                ties=row["ties"],
                id=row["playerID"],
            )
            players.append(player)
        return players
    return []


def get_player(name):
    """Method to execute a query to get all the data for the player with the given
    name. It returns a Player class object with that data.
    """
    with closing(conn.cursor()) as c:
        # SQL statement to select a player by name
        sql = """SELECT playerID, name, wins, losses, ties
                 FROM Player WHERE name = ?"""
        c.execute(sql, (name,))
        # Fetch the first row that matches the name
        row = c.fetchone()

        # If a player is found, create and return a Player object
        if row:
            player = Player(
                name=row["name"],
                wins=row["wins"],
                losses=row["losses"],
                ties=row["ties"],
                id=row["playerID"],
            )
            return player
    # If no player found, return None
    return None


def add_player(player):
    """Method to execute a query to add a new row in the database with the data
    of the player
    """
    with closing(conn.cursor()) as c:
        # SQL statement to insert a new player
        # Note: player.id is not used here as it is auto-incremented by the database
        # I had to modify the db to auto-increment the playerID
        sql = """INSERT INTO Player (name, wins, losses, ties)
               VALUES (?, ?, ?, ?)"""
        c.execute(sql, (player.name, player.wins, player.losses, player.ties))
    conn.commit()


def delete_player(name):
    """Method to execute a query to delete the data in the database for the
    player with given name.
    """
    with closing(conn.cursor()) as c:
        # SQL statement to delete a player by name
        # This will not delete any player if the name is not found
        sql = """DELETE FROM Player WHERE name = ?"""
        c.execute(sql, (name,))
    conn.commit()
    # If no player found, do nothing
    pass


def main():
    connect()
    players = get_players()
    for player in players:
        print(
            player.name,
            player.id,
            player.wins,
            player.losses,
            player.ties,
            player.games,
        )
    print()

    player = get_player("Mike")
    if player:
        print(
            player.name,
            player.id,
            player.wins,
            player.losses,
            player.ties,
            player.games,
        )


if __name__ == "__main__":
    main()
