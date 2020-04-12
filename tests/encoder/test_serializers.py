import unittest
import datetime

import sergeant.encoder.serializer


class SerializersTestCase(
    unittest.TestCase,
):
    def test_msgpack(
        self,
    ):
        obj_to_serialize = {
            'a': 1.3,
            'b': [
                1,
            ],
            'c': {
                '1': {
                    'a': True,
                    'b': False,
                    'c': -1,
                },
                '2': None,
            },
            'd': 'unicode string \u00AE',
            'e': {
                1: 1,
                2: 2,
            },
        }

        serialized_object = sergeant.encoder.serializer.msgpack.Serializer.serialize(
            data=obj_to_serialize,
        )
        unserialized_object = sergeant.encoder.serializer.msgpack.Serializer.unserialize(
            data=serialized_object,
        )

        self.assertEqual(
            first=unserialized_object,
            second=obj_to_serialize,
        )

    def test_json(
        self,
    ):
        obj_to_serialize = {
            'a': 1.3,
            'b': [
                1,
            ],
            'c': {
                '1': {
                    'a': True,
                    'b': False,
                    'c': -1,
                },
                '2': None,
            },
            'd': 'unicode string \u00AE',
            'e': {
                '1': 1,
                '2': 2,
            },
        }

        serialized_object = sergeant.encoder.serializer.json.Serializer.serialize(
            data=obj_to_serialize,
        )
        unserialized_object = sergeant.encoder.serializer.json.Serializer.unserialize(
            data=serialized_object,
        )

        self.assertEqual(
            first=unserialized_object,
            second=obj_to_serialize,
        )

    def test_pickle(
        self,
    ):
        obj_to_serialize = {
            'a': 1.3,
            'b': [
                1,
            ],
            'c': {
                '1': {
                    'a': True,
                    'b': False,
                    'c': -1,
                },
                '2': None,
            },
            'd': 'unicode string \u00AE',
            'e': {
                1: 1,
                2: 2,
            },
            'f': datetime.datetime.utcnow(),
            'g': (
                1,
                2,
            ),
        }

        serialized_object = sergeant.encoder.serializer.pickle.Serializer.serialize(
            data=obj_to_serialize,
        )
        unserialized_object = sergeant.encoder.serializer.pickle.Serializer.unserialize(
            data=serialized_object,
        )

        self.assertEqual(
            first=unserialized_object,
            second=obj_to_serialize,
        )
