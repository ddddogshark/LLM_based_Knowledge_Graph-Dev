import os
from neo4j import GraphDatabase
from dotenv import load_dotenv
from src.config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, NEO4J_DATABASE

load_dotenv()

class Neo4jDriver:
    def __init__(self, database: str = None):
        if not NEO4J_URI or not NEO4J_USER or not NEO4J_PASSWORD:
            raise ValueError("Neo4j credentials not configured in .env file.")
        self.database = database if database else NEO4J_DATABASE
        self._driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        self._driver.verify_connectivity()
        print(f"Connected to Neo4j successfully. Using database: '{self.database}'")

    def close(self):
        self._driver.close()

    def store_triplet(self, head: str, relation: str, tail: str):
        query = """
        MERGE (h:Concept {name: $head})
        MERGE (t:Concept {name: $tail})
        MERGE (h)-[r:RELATION {type: $relation}]->(t)
        RETURN h, r, t
        """
        with self._driver.session(database=self.database) as session:
            session.run(query, head=head, relation=relation, tail=tail)

    def store_triplets(self, triplets: list[dict]):
        with self._driver.session(database=self.database) as session:
            for triplet in triplets:
                if isinstance(triplet, dict) and "head" in triplet and "relation" in triplet and "tail" in triplet:
                    head = triplet["head"]
                    relation = triplet["relation"]
                    tail = triplet["tail"]
                    session.run(
                        """
                        MERGE (h:Concept {name: $head})
                        MERGE (t:Concept {name: $tail})
                        MERGE (h)-[r:RELATION {type: $relation}]->(t)
                        """,
                        head=head, relation=relation, tail=tail
                    )
                else:
                    print(f"Skipping invalid triplet: {triplet}")
        print(f"Stored {len(triplets)} triplets in Neo4j database '{self.database}'.")
