from owlready2 import get_ontology
import random

class KnowledgeBase:
    def __init__(self, owl_file):
        self.ontology = get_ontology(owl_file).load()

    def get_formula(self, shape_name):
        for individual in self.ontology.individuals():
            if shape_name.lower() in individual.name.lower():
                if hasattr(individual, "area"):
                    return individual.area[0]
        return None

    def list_shapes(self):
        return list({ind.name.replace("1", "") for ind in self.ontology.individuals()})

    def generate_quiz_questions(self, num_questions=10):
        shapes = self.list_shapes()
        questions = []

        for _ in range(num_questions):
            shape = random.choice(shapes)
            dimensions = {}
            answer = None

            if shape.lower() == "circle":
                dimensions["radius"] = random.randint(1, 10)
                answer = 3.14 * dimensions["radius"] ** 2
            elif shape.lower() == "square":
                dimensions["side"] = random.randint(1, 10)
                answer = dimensions["side"] ** 2
            elif shape.lower() == "rectangle":
                dimensions["length"] = random.randint(1, 10)
                dimensions["width"] = random.randint(1, 10)
                answer = dimensions["length"] * dimensions["width"]
            elif shape.lower() == "triangle":
                dimensions["base"] = random.randint(1, 10)
                dimensions["height"] = random.randint(1, 10)
                answer = 0.5 * dimensions["base"] * dimensions["height"]
            else:
                continue

            questions.append({
                "shape": shape,
                "dimensions": dimensions,
                "answer": round(answer, 2)
            })

        return questions
