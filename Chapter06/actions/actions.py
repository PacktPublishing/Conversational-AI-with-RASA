import os
from typing import Text

from rasa_sdk import utils
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase

USE_NEO4J = bool(os.getenv("USE_NEO4J", False))

if USE_NEO4J:
    from neo4j_knowledge_base import Neo4jKnowledgeBase


class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def name(self) -> Text:
        return "action_response_query"

    def __init__(self):
        if USE_NEO4J:
            print("using Neo4jKnowledgeBase")
            knowledge_base = Neo4jKnowledgeBase(
                "bolt://localhost:7687", "neo4j", "43215678"
            )
        else:
            print("using InMemoryKnowledgeBase")
            knowledge_base = InMemoryKnowledgeBase("data.json")

        super().__init__(knowledge_base)

    async def utter_objects(
        self,
        dispatcher,
        object_type,
        objects,
    ) -> None:
        """
        Utters a response to the user that lists all found objects.
        Args:
            dispatcher: the dispatcher
            object_type: the object type
            objects: the list of objects
        """
        if objects:
            dispatcher.utter_message(text=f"找到下列{object_type}:")

            repr_function = await utils.call_potential_coroutine(
                self.knowledge_base.get_representation_function_of_object(object_type)
            )

            for i, obj in enumerate(objects, 1):
                dispatcher.utter_message(text=f"{i}: {repr_function(obj)}")
        else:
            dispatcher.utter_message(text=f"我没找到任何{object_type}.")

    def utter_attribute_value(
        self,
        dispatcher,
        object_name,
        attribute_name,
        attribute_value,
    ) -> None:
        """
        Utters a response that informs the user about the attribute value of the
        attribute of interest.
        Args:
            dispatcher: the dispatcher
            object_name: the name of the object
            attribute_name: the name of the attribute
            attribute_value: the value of the attribute
        """
        if attribute_value:
            dispatcher.utter_message(
                text=f"{object_name}的{attribute_name}是{attribute_value}。"
            )
        else:
            dispatcher.utter_message(
                text="没有找到{}的{}。".format(object_name, attribute_name)
            )
