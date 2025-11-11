from src.database.neo4j_driver import Neo4jDriver

neo4j_driver = None
try:
    neo4j_driver = Neo4jDriver()
except ValueError as e:
    print(f"Failed to initialize Neo4jDriver: {e}")
except Exception as e:
    print(f"An unexpected error occurred during Neo4jDriver initialization: {e}")
