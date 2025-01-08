// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_interfaces:action/Move.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__ACTION__DETAIL__MOVE__STRUCT_H_
#define MY_INTERFACES__ACTION__DETAIL__MOVE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in action/Move in the package my_interfaces.
typedef struct my_interfaces__action__Move_Goal
{
  /// 이동 거리
  double distance;
} my_interfaces__action__Move_Goal;

// Struct for a sequence of my_interfaces__action__Move_Goal.
typedef struct my_interfaces__action__Move_Goal__Sequence
{
  my_interfaces__action__Move_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__action__Move_Goal__Sequence;


// Constants defined in the message

/// Struct defined in action/Move in the package my_interfaces.
typedef struct my_interfaces__action__Move_Result
{
  /// 총 이동 거리
  double total_distance;
} my_interfaces__action__Move_Result;

// Struct for a sequence of my_interfaces__action__Move_Result.
typedef struct my_interfaces__action__Move_Result__Sequence
{
  my_interfaces__action__Move_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__action__Move_Result__Sequence;


// Constants defined in the message

/// Struct defined in action/Move in the package my_interfaces.
typedef struct my_interfaces__action__Move_Feedback
{
  /// 현재까지 이동한 거리
  double current_distance;
} my_interfaces__action__Move_Feedback;

// Struct for a sequence of my_interfaces__action__Move_Feedback.
typedef struct my_interfaces__action__Move_Feedback__Sequence
{
  my_interfaces__action__Move_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__action__Move_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "my_interfaces/action/detail/move__struct.h"

/// Struct defined in action/Move in the package my_interfaces.
typedef struct my_interfaces__action__Move_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  my_interfaces__action__Move_Goal goal;
} my_interfaces__action__Move_SendGoal_Request;

// Struct for a sequence of my_interfaces__action__Move_SendGoal_Request.
typedef struct my_interfaces__action__Move_SendGoal_Request__Sequence
{
  my_interfaces__action__Move_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__action__Move_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/Move in the package my_interfaces.
typedef struct my_interfaces__action__Move_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} my_interfaces__action__Move_SendGoal_Response;

// Struct for a sequence of my_interfaces__action__Move_SendGoal_Response.
typedef struct my_interfaces__action__Move_SendGoal_Response__Sequence
{
  my_interfaces__action__Move_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__action__Move_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/Move in the package my_interfaces.
typedef struct my_interfaces__action__Move_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} my_interfaces__action__Move_GetResult_Request;

// Struct for a sequence of my_interfaces__action__Move_GetResult_Request.
typedef struct my_interfaces__action__Move_GetResult_Request__Sequence
{
  my_interfaces__action__Move_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__action__Move_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "my_interfaces/action/detail/move__struct.h"

/// Struct defined in action/Move in the package my_interfaces.
typedef struct my_interfaces__action__Move_GetResult_Response
{
  int8_t status;
  my_interfaces__action__Move_Result result;
} my_interfaces__action__Move_GetResult_Response;

// Struct for a sequence of my_interfaces__action__Move_GetResult_Response.
typedef struct my_interfaces__action__Move_GetResult_Response__Sequence
{
  my_interfaces__action__Move_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__action__Move_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "my_interfaces/action/detail/move__struct.h"

/// Struct defined in action/Move in the package my_interfaces.
typedef struct my_interfaces__action__Move_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  my_interfaces__action__Move_Feedback feedback;
} my_interfaces__action__Move_FeedbackMessage;

// Struct for a sequence of my_interfaces__action__Move_FeedbackMessage.
typedef struct my_interfaces__action__Move_FeedbackMessage__Sequence
{
  my_interfaces__action__Move_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__action__Move_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_INTERFACES__ACTION__DETAIL__MOVE__STRUCT_H_
