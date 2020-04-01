# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flunkyprotocol.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='flunkyprotocol.proto',
  package='endpoints.flunky.simulator',
  syntax='proto3',
  serialized_options=b'\n\'com.google.endpoints.examples.bookstoreB\016BookstoreProtoP\001',
  serialized_pb=b'\n\x14\x66lunkyprotocol.proto\x12\x1a\x65ndpoints.flunky.simulator\"\x1a\n\x07LogResp\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\"\x08\n\x06LogReq\"D\n\x10StreamEventsResp\x12\x30\n\x05\x65vent\x18\x01 \x01(\x0b\x32!.endpoints.flunky.simulator.Event\"\x11\n\x0fStreamEventsReq\"G\n\x0fStreamStateResp\x12\x34\n\x05state\x18\x01 \x01(\x0b\x32%.endpoints.flunky.simulator.GameState\"\x10\n\x0eStreamStateReq\"\x1a\n\x18SelectThrowingPlayerResp\"@\n\x17SelectThrowingPlayerReq\x12\x12\n\nplayerName\x18\x01 \x01(\t\x12\x11\n\ttargeName\x18\x02 \x01(\t\"\x11\n\x0fSendMessageResp\"5\n\x0eSendMessageReq\x12\x12\n\nplayerName\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"\x0f\n\rResetGameResp\"\"\n\x0cResetGameReq\x12\x12\n\nplayerName\x18\x01 \x01(\t\"\x10\n\x0eKickPlayerResp\"6\n\rKickPlayerReq\x12\x12\n\nplayerName\x18\x01 \x01(\t\x12\x11\n\ttargeName\x18\x02 \x01(\t\"\x14\n\x12RegisterPlayerResp\"\'\n\x11RegisterPlayerReq\x12\x12\n\nplayerName\x18\x01 \x01(\t\"_\n\x08ThrowReq\x12\x12\n\nplayerName\x18\x01 \x01(\t\x12?\n\x08strength\x18\x02 \x01(\x0e\x32-.endpoints.flunky.simulator.EnumThrowStrength\"\x1c\n\tThrowResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\xa0\x01\n\x05\x45vent\x12\x45\n\x0cprepareVideo\x18\x01 \x01(\x0b\x32-.endpoints.flunky.simulator.PrepareVideoEventH\x00\x12\x41\n\nplayVideos\x18\x02 \x01(\x0b\x32+.endpoints.flunky.simulator.PlayVideosEventH\x00\x42\r\n\x0b\x65vent_oneof\" \n\x11PrepareVideoEvent\x12\x0b\n\x03url\x18\x01 \x03(\t\"I\n\x0fPlayVideosEvent\x12\x36\n\x06videos\x18\x01 \x03(\x0b\x32&.endpoints.flunky.simulator.TimedVideo\":\n\nTimedVideo\x12\r\n\x05\x64\x65lay\x18\x01 \x01(\x03\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x10\n\x08mirrored\x18\x03 \x01(\x08\"\xc5\x01\n\tGameState\x12\x37\n\x0bplayerTeamA\x18\x01 \x03(\x0b\x32\".endpoints.flunky.simulator.Player\x12\x37\n\x0bplayerTeamB\x18\x02 \x03(\x0b\x32\".endpoints.flunky.simulator.Player\x12\x16\n\x0ethrowingPlayer\x18\x03 \x01(\t\x12\x16\n\x0estrafbierTeamA\x18\x04 \x01(\x03\x12\x16\n\x0estrafbierTeamB\x18\x05 \x01(\x03\"<\n\x06Player\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tabgegeben\x18\x02 \x01(\x08\x12\x11\n\tspectator\x18\x03 \x01(\x08*@\n\x11\x45numThrowStrength\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04SOFT\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\x08\n\x04HARD\x10\x03\x32\xb4\x07\n\tSimulator\x12T\n\x05Throw\x12$.endpoints.flunky.simulator.ThrowReq\x1a%.endpoints.flunky.simulator.ThrowResp\x12o\n\x0eRegisterPlayer\x12-.endpoints.flunky.simulator.RegisterPlayerReq\x1a..endpoints.flunky.simulator.RegisterPlayerResp\x12\x63\n\nKickPlayer\x12).endpoints.flunky.simulator.KickPlayerReq\x1a*.endpoints.flunky.simulator.KickPlayerResp\x12`\n\tResetGame\x12(.endpoints.flunky.simulator.ResetGameReq\x1a).endpoints.flunky.simulator.ResetGameResp\x12\x81\x01\n\x14SelectThrowingPlayer\x12\x33.endpoints.flunky.simulator.SelectThrowingPlayerReq\x1a\x34.endpoints.flunky.simulator.SelectThrowingPlayerResp\x12\x66\n\x0bSendMessage\x12*.endpoints.flunky.simulator.SendMessageReq\x1a+.endpoints.flunky.simulator.SendMessageResp\x12h\n\x0bStreamState\x12*.endpoints.flunky.simulator.StreamStateReq\x1a+.endpoints.flunky.simulator.StreamStateResp0\x01\x12k\n\x0cStreamEvents\x12+.endpoints.flunky.simulator.StreamEventsReq\x1a,.endpoints.flunky.simulator.StreamEventsResp0\x01\x12V\n\tStreamLog\x12\".endpoints.flunky.simulator.LogReq\x1a#.endpoints.flunky.simulator.LogResp0\x01\x42;\n\'com.google.endpoints.examples.bookstoreB\x0e\x42ookstoreProtoP\x01\x62\x06proto3'
)

_ENUMTHROWSTRENGTH = _descriptor.EnumDescriptor(
  name='EnumThrowStrength',
  full_name='endpoints.flunky.simulator.EnumThrowStrength',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOFT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEDIUM', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HARD', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1349,
  serialized_end=1413,
)
_sym_db.RegisterEnumDescriptor(_ENUMTHROWSTRENGTH)

EnumThrowStrength = enum_type_wrapper.EnumTypeWrapper(_ENUMTHROWSTRENGTH)
UNKNOWN = 0
SOFT = 1
MEDIUM = 2
HARD = 3



_LOGRESP = _descriptor.Descriptor(
  name='LogResp',
  full_name='endpoints.flunky.simulator.LogResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='endpoints.flunky.simulator.LogResp.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=78,
)


_LOGREQ = _descriptor.Descriptor(
  name='LogReq',
  full_name='endpoints.flunky.simulator.LogReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=88,
)


_STREAMEVENTSRESP = _descriptor.Descriptor(
  name='StreamEventsResp',
  full_name='endpoints.flunky.simulator.StreamEventsResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='endpoints.flunky.simulator.StreamEventsResp.event', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=158,
)


_STREAMEVENTSREQ = _descriptor.Descriptor(
  name='StreamEventsReq',
  full_name='endpoints.flunky.simulator.StreamEventsReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=160,
  serialized_end=177,
)


_STREAMSTATERESP = _descriptor.Descriptor(
  name='StreamStateResp',
  full_name='endpoints.flunky.simulator.StreamStateResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='endpoints.flunky.simulator.StreamStateResp.state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=250,
)


_STREAMSTATEREQ = _descriptor.Descriptor(
  name='StreamStateReq',
  full_name='endpoints.flunky.simulator.StreamStateReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=268,
)


_SELECTTHROWINGPLAYERRESP = _descriptor.Descriptor(
  name='SelectThrowingPlayerResp',
  full_name='endpoints.flunky.simulator.SelectThrowingPlayerResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=270,
  serialized_end=296,
)


_SELECTTHROWINGPLAYERREQ = _descriptor.Descriptor(
  name='SelectThrowingPlayerReq',
  full_name='endpoints.flunky.simulator.SelectThrowingPlayerReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerName', full_name='endpoints.flunky.simulator.SelectThrowingPlayerReq.playerName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targeName', full_name='endpoints.flunky.simulator.SelectThrowingPlayerReq.targeName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=298,
  serialized_end=362,
)


_SENDMESSAGERESP = _descriptor.Descriptor(
  name='SendMessageResp',
  full_name='endpoints.flunky.simulator.SendMessageResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=364,
  serialized_end=381,
)


_SENDMESSAGEREQ = _descriptor.Descriptor(
  name='SendMessageReq',
  full_name='endpoints.flunky.simulator.SendMessageReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerName', full_name='endpoints.flunky.simulator.SendMessageReq.playerName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='endpoints.flunky.simulator.SendMessageReq.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=383,
  serialized_end=436,
)


_RESETGAMERESP = _descriptor.Descriptor(
  name='ResetGameResp',
  full_name='endpoints.flunky.simulator.ResetGameResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=438,
  serialized_end=453,
)


_RESETGAMEREQ = _descriptor.Descriptor(
  name='ResetGameReq',
  full_name='endpoints.flunky.simulator.ResetGameReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerName', full_name='endpoints.flunky.simulator.ResetGameReq.playerName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=455,
  serialized_end=489,
)


_KICKPLAYERRESP = _descriptor.Descriptor(
  name='KickPlayerResp',
  full_name='endpoints.flunky.simulator.KickPlayerResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=491,
  serialized_end=507,
)


_KICKPLAYERREQ = _descriptor.Descriptor(
  name='KickPlayerReq',
  full_name='endpoints.flunky.simulator.KickPlayerReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerName', full_name='endpoints.flunky.simulator.KickPlayerReq.playerName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targeName', full_name='endpoints.flunky.simulator.KickPlayerReq.targeName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=509,
  serialized_end=563,
)


_REGISTERPLAYERRESP = _descriptor.Descriptor(
  name='RegisterPlayerResp',
  full_name='endpoints.flunky.simulator.RegisterPlayerResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=565,
  serialized_end=585,
)


_REGISTERPLAYERREQ = _descriptor.Descriptor(
  name='RegisterPlayerReq',
  full_name='endpoints.flunky.simulator.RegisterPlayerReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerName', full_name='endpoints.flunky.simulator.RegisterPlayerReq.playerName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=587,
  serialized_end=626,
)


_THROWREQ = _descriptor.Descriptor(
  name='ThrowReq',
  full_name='endpoints.flunky.simulator.ThrowReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerName', full_name='endpoints.flunky.simulator.ThrowReq.playerName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strength', full_name='endpoints.flunky.simulator.ThrowReq.strength', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=628,
  serialized_end=723,
)


_THROWRESP = _descriptor.Descriptor(
  name='ThrowResp',
  full_name='endpoints.flunky.simulator.ThrowResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='endpoints.flunky.simulator.ThrowResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=725,
  serialized_end=753,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='endpoints.flunky.simulator.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prepareVideo', full_name='endpoints.flunky.simulator.Event.prepareVideo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='playVideos', full_name='endpoints.flunky.simulator.Event.playVideos', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='event_oneof', full_name='endpoints.flunky.simulator.Event.event_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=756,
  serialized_end=916,
)


_PREPAREVIDEOEVENT = _descriptor.Descriptor(
  name='PrepareVideoEvent',
  full_name='endpoints.flunky.simulator.PrepareVideoEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='endpoints.flunky.simulator.PrepareVideoEvent.url', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=918,
  serialized_end=950,
)


_PLAYVIDEOSEVENT = _descriptor.Descriptor(
  name='PlayVideosEvent',
  full_name='endpoints.flunky.simulator.PlayVideosEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='videos', full_name='endpoints.flunky.simulator.PlayVideosEvent.videos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=952,
  serialized_end=1025,
)


_TIMEDVIDEO = _descriptor.Descriptor(
  name='TimedVideo',
  full_name='endpoints.flunky.simulator.TimedVideo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='delay', full_name='endpoints.flunky.simulator.TimedVideo.delay', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='endpoints.flunky.simulator.TimedVideo.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mirrored', full_name='endpoints.flunky.simulator.TimedVideo.mirrored', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1027,
  serialized_end=1085,
)


_GAMESTATE = _descriptor.Descriptor(
  name='GameState',
  full_name='endpoints.flunky.simulator.GameState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerTeamA', full_name='endpoints.flunky.simulator.GameState.playerTeamA', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='playerTeamB', full_name='endpoints.flunky.simulator.GameState.playerTeamB', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='throwingPlayer', full_name='endpoints.flunky.simulator.GameState.throwingPlayer', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strafbierTeamA', full_name='endpoints.flunky.simulator.GameState.strafbierTeamA', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strafbierTeamB', full_name='endpoints.flunky.simulator.GameState.strafbierTeamB', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1088,
  serialized_end=1285,
)


_PLAYER = _descriptor.Descriptor(
  name='Player',
  full_name='endpoints.flunky.simulator.Player',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='endpoints.flunky.simulator.Player.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abgegeben', full_name='endpoints.flunky.simulator.Player.abgegeben', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spectator', full_name='endpoints.flunky.simulator.Player.spectator', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1287,
  serialized_end=1347,
)

_STREAMEVENTSRESP.fields_by_name['event'].message_type = _EVENT
_STREAMSTATERESP.fields_by_name['state'].message_type = _GAMESTATE
_THROWREQ.fields_by_name['strength'].enum_type = _ENUMTHROWSTRENGTH
_EVENT.fields_by_name['prepareVideo'].message_type = _PREPAREVIDEOEVENT
_EVENT.fields_by_name['playVideos'].message_type = _PLAYVIDEOSEVENT
_EVENT.oneofs_by_name['event_oneof'].fields.append(
  _EVENT.fields_by_name['prepareVideo'])
_EVENT.fields_by_name['prepareVideo'].containing_oneof = _EVENT.oneofs_by_name['event_oneof']
_EVENT.oneofs_by_name['event_oneof'].fields.append(
  _EVENT.fields_by_name['playVideos'])
_EVENT.fields_by_name['playVideos'].containing_oneof = _EVENT.oneofs_by_name['event_oneof']
_PLAYVIDEOSEVENT.fields_by_name['videos'].message_type = _TIMEDVIDEO
_GAMESTATE.fields_by_name['playerTeamA'].message_type = _PLAYER
_GAMESTATE.fields_by_name['playerTeamB'].message_type = _PLAYER
DESCRIPTOR.message_types_by_name['LogResp'] = _LOGRESP
DESCRIPTOR.message_types_by_name['LogReq'] = _LOGREQ
DESCRIPTOR.message_types_by_name['StreamEventsResp'] = _STREAMEVENTSRESP
DESCRIPTOR.message_types_by_name['StreamEventsReq'] = _STREAMEVENTSREQ
DESCRIPTOR.message_types_by_name['StreamStateResp'] = _STREAMSTATERESP
DESCRIPTOR.message_types_by_name['StreamStateReq'] = _STREAMSTATEREQ
DESCRIPTOR.message_types_by_name['SelectThrowingPlayerResp'] = _SELECTTHROWINGPLAYERRESP
DESCRIPTOR.message_types_by_name['SelectThrowingPlayerReq'] = _SELECTTHROWINGPLAYERREQ
DESCRIPTOR.message_types_by_name['SendMessageResp'] = _SENDMESSAGERESP
DESCRIPTOR.message_types_by_name['SendMessageReq'] = _SENDMESSAGEREQ
DESCRIPTOR.message_types_by_name['ResetGameResp'] = _RESETGAMERESP
DESCRIPTOR.message_types_by_name['ResetGameReq'] = _RESETGAMEREQ
DESCRIPTOR.message_types_by_name['KickPlayerResp'] = _KICKPLAYERRESP
DESCRIPTOR.message_types_by_name['KickPlayerReq'] = _KICKPLAYERREQ
DESCRIPTOR.message_types_by_name['RegisterPlayerResp'] = _REGISTERPLAYERRESP
DESCRIPTOR.message_types_by_name['RegisterPlayerReq'] = _REGISTERPLAYERREQ
DESCRIPTOR.message_types_by_name['ThrowReq'] = _THROWREQ
DESCRIPTOR.message_types_by_name['ThrowResp'] = _THROWRESP
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['PrepareVideoEvent'] = _PREPAREVIDEOEVENT
DESCRIPTOR.message_types_by_name['PlayVideosEvent'] = _PLAYVIDEOSEVENT
DESCRIPTOR.message_types_by_name['TimedVideo'] = _TIMEDVIDEO
DESCRIPTOR.message_types_by_name['GameState'] = _GAMESTATE
DESCRIPTOR.message_types_by_name['Player'] = _PLAYER
DESCRIPTOR.enum_types_by_name['EnumThrowStrength'] = _ENUMTHROWSTRENGTH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogResp = _reflection.GeneratedProtocolMessageType('LogResp', (_message.Message,), {
  'DESCRIPTOR' : _LOGRESP,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.LogResp)
  })
_sym_db.RegisterMessage(LogResp)

LogReq = _reflection.GeneratedProtocolMessageType('LogReq', (_message.Message,), {
  'DESCRIPTOR' : _LOGREQ,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.LogReq)
  })
_sym_db.RegisterMessage(LogReq)

StreamEventsResp = _reflection.GeneratedProtocolMessageType('StreamEventsResp', (_message.Message,), {
  'DESCRIPTOR' : _STREAMEVENTSRESP,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.StreamEventsResp)
  })
_sym_db.RegisterMessage(StreamEventsResp)

StreamEventsReq = _reflection.GeneratedProtocolMessageType('StreamEventsReq', (_message.Message,), {
  'DESCRIPTOR' : _STREAMEVENTSREQ,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.StreamEventsReq)
  })
_sym_db.RegisterMessage(StreamEventsReq)

StreamStateResp = _reflection.GeneratedProtocolMessageType('StreamStateResp', (_message.Message,), {
  'DESCRIPTOR' : _STREAMSTATERESP,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.StreamStateResp)
  })
_sym_db.RegisterMessage(StreamStateResp)

StreamStateReq = _reflection.GeneratedProtocolMessageType('StreamStateReq', (_message.Message,), {
  'DESCRIPTOR' : _STREAMSTATEREQ,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.StreamStateReq)
  })
_sym_db.RegisterMessage(StreamStateReq)

SelectThrowingPlayerResp = _reflection.GeneratedProtocolMessageType('SelectThrowingPlayerResp', (_message.Message,), {
  'DESCRIPTOR' : _SELECTTHROWINGPLAYERRESP,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.SelectThrowingPlayerResp)
  })
_sym_db.RegisterMessage(SelectThrowingPlayerResp)

SelectThrowingPlayerReq = _reflection.GeneratedProtocolMessageType('SelectThrowingPlayerReq', (_message.Message,), {
  'DESCRIPTOR' : _SELECTTHROWINGPLAYERREQ,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.SelectThrowingPlayerReq)
  })
_sym_db.RegisterMessage(SelectThrowingPlayerReq)

SendMessageResp = _reflection.GeneratedProtocolMessageType('SendMessageResp', (_message.Message,), {
  'DESCRIPTOR' : _SENDMESSAGERESP,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.SendMessageResp)
  })
_sym_db.RegisterMessage(SendMessageResp)

SendMessageReq = _reflection.GeneratedProtocolMessageType('SendMessageReq', (_message.Message,), {
  'DESCRIPTOR' : _SENDMESSAGEREQ,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.SendMessageReq)
  })
_sym_db.RegisterMessage(SendMessageReq)

ResetGameResp = _reflection.GeneratedProtocolMessageType('ResetGameResp', (_message.Message,), {
  'DESCRIPTOR' : _RESETGAMERESP,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.ResetGameResp)
  })
_sym_db.RegisterMessage(ResetGameResp)

ResetGameReq = _reflection.GeneratedProtocolMessageType('ResetGameReq', (_message.Message,), {
  'DESCRIPTOR' : _RESETGAMEREQ,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.ResetGameReq)
  })
_sym_db.RegisterMessage(ResetGameReq)

KickPlayerResp = _reflection.GeneratedProtocolMessageType('KickPlayerResp', (_message.Message,), {
  'DESCRIPTOR' : _KICKPLAYERRESP,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.KickPlayerResp)
  })
_sym_db.RegisterMessage(KickPlayerResp)

KickPlayerReq = _reflection.GeneratedProtocolMessageType('KickPlayerReq', (_message.Message,), {
  'DESCRIPTOR' : _KICKPLAYERREQ,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.KickPlayerReq)
  })
_sym_db.RegisterMessage(KickPlayerReq)

RegisterPlayerResp = _reflection.GeneratedProtocolMessageType('RegisterPlayerResp', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERPLAYERRESP,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.RegisterPlayerResp)
  })
_sym_db.RegisterMessage(RegisterPlayerResp)

RegisterPlayerReq = _reflection.GeneratedProtocolMessageType('RegisterPlayerReq', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERPLAYERREQ,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.RegisterPlayerReq)
  })
_sym_db.RegisterMessage(RegisterPlayerReq)

ThrowReq = _reflection.GeneratedProtocolMessageType('ThrowReq', (_message.Message,), {
  'DESCRIPTOR' : _THROWREQ,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.ThrowReq)
  })
_sym_db.RegisterMessage(ThrowReq)

ThrowResp = _reflection.GeneratedProtocolMessageType('ThrowResp', (_message.Message,), {
  'DESCRIPTOR' : _THROWRESP,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.ThrowResp)
  })
_sym_db.RegisterMessage(ThrowResp)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.Event)
  })
_sym_db.RegisterMessage(Event)

PrepareVideoEvent = _reflection.GeneratedProtocolMessageType('PrepareVideoEvent', (_message.Message,), {
  'DESCRIPTOR' : _PREPAREVIDEOEVENT,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.PrepareVideoEvent)
  })
_sym_db.RegisterMessage(PrepareVideoEvent)

PlayVideosEvent = _reflection.GeneratedProtocolMessageType('PlayVideosEvent', (_message.Message,), {
  'DESCRIPTOR' : _PLAYVIDEOSEVENT,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.PlayVideosEvent)
  })
_sym_db.RegisterMessage(PlayVideosEvent)

TimedVideo = _reflection.GeneratedProtocolMessageType('TimedVideo', (_message.Message,), {
  'DESCRIPTOR' : _TIMEDVIDEO,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.TimedVideo)
  })
_sym_db.RegisterMessage(TimedVideo)

GameState = _reflection.GeneratedProtocolMessageType('GameState', (_message.Message,), {
  'DESCRIPTOR' : _GAMESTATE,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.GameState)
  })
_sym_db.RegisterMessage(GameState)

Player = _reflection.GeneratedProtocolMessageType('Player', (_message.Message,), {
  'DESCRIPTOR' : _PLAYER,
  '__module__' : 'flunkyprotocol_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.Player)
  })
_sym_db.RegisterMessage(Player)


DESCRIPTOR._options = None

_SIMULATOR = _descriptor.ServiceDescriptor(
  name='Simulator',
  full_name='endpoints.flunky.simulator.Simulator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1416,
  serialized_end=2364,
  methods=[
  _descriptor.MethodDescriptor(
    name='Throw',
    full_name='endpoints.flunky.simulator.Simulator.Throw',
    index=0,
    containing_service=None,
    input_type=_THROWREQ,
    output_type=_THROWRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RegisterPlayer',
    full_name='endpoints.flunky.simulator.Simulator.RegisterPlayer',
    index=1,
    containing_service=None,
    input_type=_REGISTERPLAYERREQ,
    output_type=_REGISTERPLAYERRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='KickPlayer',
    full_name='endpoints.flunky.simulator.Simulator.KickPlayer',
    index=2,
    containing_service=None,
    input_type=_KICKPLAYERREQ,
    output_type=_KICKPLAYERRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ResetGame',
    full_name='endpoints.flunky.simulator.Simulator.ResetGame',
    index=3,
    containing_service=None,
    input_type=_RESETGAMEREQ,
    output_type=_RESETGAMERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SelectThrowingPlayer',
    full_name='endpoints.flunky.simulator.Simulator.SelectThrowingPlayer',
    index=4,
    containing_service=None,
    input_type=_SELECTTHROWINGPLAYERREQ,
    output_type=_SELECTTHROWINGPLAYERRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendMessage',
    full_name='endpoints.flunky.simulator.Simulator.SendMessage',
    index=5,
    containing_service=None,
    input_type=_SENDMESSAGEREQ,
    output_type=_SENDMESSAGERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamState',
    full_name='endpoints.flunky.simulator.Simulator.StreamState',
    index=6,
    containing_service=None,
    input_type=_STREAMSTATEREQ,
    output_type=_STREAMSTATERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamEvents',
    full_name='endpoints.flunky.simulator.Simulator.StreamEvents',
    index=7,
    containing_service=None,
    input_type=_STREAMEVENTSREQ,
    output_type=_STREAMEVENTSRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamLog',
    full_name='endpoints.flunky.simulator.Simulator.StreamLog',
    index=8,
    containing_service=None,
    input_type=_LOGREQ,
    output_type=_LOGRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SIMULATOR)

DESCRIPTOR.services_by_name['Simulator'] = _SIMULATOR

# @@protoc_insertion_point(module_scope)
