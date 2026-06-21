import os
from neo4j import GraphDatabase
from src.config import get_logger

logger = get_logger(__name__)


class Neo4jDriver:
    """Driver for Neo4j graph database operations.

    Manages connections and provides methods for storing knowledge graph
    triplets as nodes and relationships.
    """

    def __init__(self):
        uri = os.getenv("NEO4J_URI")
        user = os.getenv("NEO4J_USER")
        password = os.getenv("NEO4J_PASSWORD")
        if not uri or not user or not password:
            raise ValueError("Neo4j credentials not configured in .env file.")
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
        self._driver.verify_connectivity()
        logger.info("Connected to Neo4j successfully.")

    def close(self):
        """Close the Neo4j driver connection."""
        self._driver.close()
        logger.debug("Neo4j connection closed.")

    def store_triplet(self, head: str, relation: str, tail: str):
        """Store a single (head, relation, tail) triplet in Neo4j."""
        query = """
        MERGE (h:Concept {name: $head})
        MERGE (t:Concept {name: $tail})
        MERGE (h)-[r:RELATION {type: $relation}]->(t)
        RETURN h, r, t
        """
        with self._driver.session() as session:
            session.run(query, head=head, relation=relation, tail=tail)

    def store_triplets(self, triplets: list[dict]):
        """Store multiple triplets in Neo4j."""
        for triplet in triplets:
            self.store_triplet(triplet["head"], triplet["relation"], triplet["tail"])
        logger.info("Stored %d triplets in Neo4j.", len(triplets))
