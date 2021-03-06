# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from mlagents.envs.communicator_objects.agent_action_pb2 import (
    AgentActionProto as mlagents___envs___communicator_objects___agent_action_pb2___AgentActionProto,
)

from mlagents.envs.communicator_objects.command_pb2 import (
    CommandProto as mlagents___envs___communicator_objects___command_pb2___CommandProto,
)

from mlagents.envs.communicator_objects.environment_parameters_pb2 import (
    EnvironmentParametersProto as mlagents___envs___communicator_objects___environment_parameters_pb2___EnvironmentParametersProto,
)

from typing import (
    Iterable as typing___Iterable,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


class UnityRLInputProto(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ListAgentActionProto(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def value(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[mlagents___envs___communicator_objects___agent_action_pb2___AgentActionProto]: ...

        def __init__(self,
            *,
            value : typing___Optional[typing___Iterable[mlagents___envs___communicator_objects___agent_action_pb2___AgentActionProto]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UnityRLInputProto.ListAgentActionProto: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> None: ...

    class AgentActionsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> UnityRLInputProto.ListAgentActionProto: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[UnityRLInputProto.ListAgentActionProto] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UnityRLInputProto.AgentActionsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"value"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    is_training = ... # type: builtin___bool
    command = ... # type: mlagents___envs___communicator_objects___command_pb2___CommandProto

    @property
    def agent_actions(self) -> typing___MutableMapping[typing___Text, UnityRLInputProto.ListAgentActionProto]: ...

    @property
    def environment_parameters(self) -> mlagents___envs___communicator_objects___environment_parameters_pb2___EnvironmentParametersProto: ...

    def __init__(self,
        *,
        agent_actions : typing___Optional[typing___Mapping[typing___Text, UnityRLInputProto.ListAgentActionProto]] = None,
        environment_parameters : typing___Optional[mlagents___envs___communicator_objects___environment_parameters_pb2___EnvironmentParametersProto] = None,
        is_training : typing___Optional[builtin___bool] = None,
        command : typing___Optional[mlagents___envs___communicator_objects___command_pb2___CommandProto] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> UnityRLInputProto: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"environment_parameters"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"agent_actions",u"command",u"environment_parameters",u"is_training"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"environment_parameters",b"environment_parameters"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"agent_actions",b"agent_actions",u"command",b"command",u"environment_parameters",b"environment_parameters",u"is_training",b"is_training"]) -> None: ...
