# generated from rosidl_generator_py/resource/_idl.py.em
# with input from my_interfaces:msg/SensorStatus.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SensorStatus(type):
    """Metaclass of message 'SensorStatus'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('my_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'my_interfaces.msg.SensorStatus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__sensor_status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__sensor_status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__sensor_status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__sensor_status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__sensor_status

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SensorStatus(metaclass=Metaclass_SensorStatus):
    """Message class 'SensorStatus'."""

    __slots__ = [
        '_temerature',
        '_is_motor_ready',
        '_debug_messages',
    ]

    _fields_and_field_types = {
        'temerature': 'int64',
        'is_motor_ready': 'boolean',
        'debug_messages': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.temerature = kwargs.get('temerature', int())
        self.is_motor_ready = kwargs.get('is_motor_ready', bool())
        self.debug_messages = kwargs.get('debug_messages', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.temerature != other.temerature:
            return False
        if self.is_motor_ready != other.is_motor_ready:
            return False
        if self.debug_messages != other.debug_messages:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def temerature(self):
        """Message field 'temerature'."""
        return self._temerature

    @temerature.setter
    def temerature(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'temerature' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'temerature' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._temerature = value

    @builtins.property
    def is_motor_ready(self):
        """Message field 'is_motor_ready'."""
        return self._is_motor_ready

    @is_motor_ready.setter
    def is_motor_ready(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'is_motor_ready' field must be of type 'bool'"
        self._is_motor_ready = value

    @builtins.property
    def debug_messages(self):
        """Message field 'debug_messages'."""
        return self._debug_messages

    @debug_messages.setter
    def debug_messages(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'debug_messages' field must be of type 'str'"
        self._debug_messages = value
