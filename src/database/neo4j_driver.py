import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

class Neo4jDriver:
    def __init__(self):
        if not NEO4J_URI or not NEO4J_USER or not NEO4J_PASSWORD:
            raise ValueError("Neo4j credentials not configured in .env file.")
        self._driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        self._driver.verify_connectivity()
        print("Connected to Neo4j successfully.")

    def close(self):
        self._driver.close()

    def store_triplet(self, head: str, relation: str, tail: str):
        query = """
        MERGE (h:Concept {name: $head})
        MERGE (t:Concept {name: $tail})
        MERGE (h)-[r:RELATION {type: $relation}]->(t)
        RETURN h, r, t
        """
        with self._driver.session() as session:
            session.run(query, head=head, relation=relation, tail=tail)

    def store_triplets(self, triplets: list[dict]):
        for triplet in triplets:
            if isinstance(triplet, dict) and "head" in triplet and "relation" in triplet and "tail" in triplet:
                head = triplet["head"]
                relation = triplet["relation"]
                tail = triplet["tail"]
                self.store_triplet(head, relation, tail)
            else:
                print(f"Skipping invalid triplet: {triplet}")
        print(f"Stored {len(triplets)} triplets in Neo4j.")
