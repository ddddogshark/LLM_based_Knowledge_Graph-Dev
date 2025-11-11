def plan_course_kg_construction(course_name: str) -> list[str]:
    """
    Generates a plan for constructing the knowledge graph for a given course.
    """
    if course_name == "DSAA2011 Machine Learning":
        return [
            f"Generate core concepts for {course_name}",
            f"Generate detailed definitions and examples for each concept in {course_name}",
            f"Identify relationships between concepts in {course_name}",
            f"Structure knowledge into triplets (entity-relation-entity) for {course_name}",
            f"Store triplets in the Neo4j knowledge graph for {course_name}",
            f"Perform quality assessment and refinement for {course_name} knowledge graph",
        ]
    else:
        return [f"No specific plan for {course_name}. Defaulting to generic steps.",
                f"Generate core concepts for {course_name}",
                f"Generate detailed definitions and examples for each concept in {course_name}",
                f"Identify relationships between concepts in {course_name}",
                f"Structure knowledge into triplets (entity-relation-entity) for {course_name}",
                f"Store triplets in the Neo4j knowledge graph for {course_name}",
                f"Perform quality assessment and refinement for {course_name} knowledge graph",
                ]
